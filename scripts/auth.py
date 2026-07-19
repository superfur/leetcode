#!/usr/bin/env python3
"""
LeetCode 登录模块

基于 Playwright 浏览器自动化：脚本启动一个可见的浏览器窗口，
用户在其中用任意方式（扫码 / 短信 / 账号密码 / 第三方）完成登录，
脚本检测到登录成功后自动捕获 cookie 并保存到本地配置。

不依赖 leetcode 内部登录 graphql 字段（这些字段未公开且会变动），因此最稳定。

依赖:
    pip install playwright
    playwright install chromium
"""
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Tuple

sys.path.insert(0, str(Path(__file__).parent))

from config import get_site_config, set_cookies, set_browser_cookies, load_config

# Windows 控制台编码兼容
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# 优先用 curl_cffi 验证登录态（不依赖 page 状态，比 page.evaluate 更可靠）
try:
    from curl_cffi import requests as _crequests
    _HAS_CURL_CFFI = True
except ImportError:
    _HAS_CURL_CFFI = False


# 通过页面内 fetch 调用 graphql 验证登录状态的脚本
# 复用浏览器自身的 cookie，无需手动构造请求头
_VERIFY_JS_TEMPLATE = """
async () => {
    const m = document.cookie.match(/(?:^|;\\s*)csrftoken=([^;]+)/);
    const csrftoken = m ? m[1] : '';
    try {
        const r = await fetch('/graphql', {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 'x-csrftoken': csrftoken},
            credentials: 'include',
            body: JSON.stringify({query: '%s'})
        });
        if (!r.ok) return {ok: false, status: r.status};
        const j = await r.json();
        const us = (j && j.data && j.data.userStatus) || {};
        return {ok: true, signedIn: !!us.isSignedIn, username: us.username || ''};
    } catch (e) {
        return {ok: false, error: String(e)};
    }
}
"""

_USER_STATUS_QUERY = "query{userStatus{isSignedIn username}}"


# 反自动化检测脚本：在每个页面加载前注入，隐藏 Playwright/webdriver 特征。
# 不做这步的话，leetcode.cn 的极验滑块/图形验证会识别出自动化浏览器并报错。
_STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
Object.defineProperty(navigator, 'languages', {get: () => ['zh-CN', 'zh', 'en']});
Object.defineProperty(navigator, 'plugins', {get: () => [{name:'Chrome PDF Plugin'},{name:'Chrome PDF Viewer'},{name:'Native Client'}]});
window.chrome = window.chrome || {runtime: {}, app: {}, csi: function(){}, loadTimes: function(){}};
const _origQuery = (window.navigator.permissions || {}).query;
if (_origQuery) {
    window.navigator.permissions.query = (p) => p && p.name === 'notifications'
        ? Promise.resolve({state: Notification.permission})
        : _origQuery(p);
}
"""


def _check_login_in_page(page) -> Dict[str, object]:
    """在浏览器页面内调用 graphql 检查登录状态（fallback 方案，依赖 page 在 leetcode 域）。"""
    js = _VERIFY_JS_TEMPLATE % _USER_STATUS_QUERY
    try:
        result = page.evaluate(js)
        if isinstance(result, dict):
            return result
    except Exception as e:
        return {"ok": False, "error": str(e)}
    return {"ok": False, "error": "unknown"}


def _verify_login_curlcffi(base_url: str, cookies_dict: Dict) -> Tuple[bool, str]:
    """用 curl_cffi 带 cookie 调 graphql 验证登录态。

    比 page.evaluate 更可靠：不依赖 page 当前 URL/状态，
    登录跳转/popup 等场景下也能正确识别。
    """
    if not _HAS_CURL_CFFI:
        return False, ""
    try:
        s = _crequests.Session(impersonate="chrome")
        s.cookies.update(cookies_dict)
        r = s.post(
            f"{base_url}/graphql",
            json={"query": "query{userStatus{isSignedIn username}}"},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if r.status_code == 200 and "application/json" in r.headers.get("Content-Type", ""):
            us = r.json().get("data", {}).get("userStatus", {})
            return bool(us.get("isSignedIn")), us.get("username", "")
    except Exception:
        pass
    return False, ""


def login_with_browser(site: Optional[str] = None, timeout: int = 300) -> Optional[Dict[str, str]]:
    """
    启动浏览器让用户登录，登录成功后捕获 cookie。

    Args:
        site: 站点 key (如 "leetcode.cn")，None 时用默认站点
        timeout: 最长等待秒数

    Returns:
        {"csrftoken": ..., "LEETCODE_SESSION": ...} 或 None
    """
    cfg = load_config()
    site_key = site or cfg.get("default_site", "leetcode.cn")
    site_config = get_site_config(site_key)
    base_url = site_config.get("base_url", f"https://{site_key}")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print()
        print("[!] 未安装 playwright，无法使用浏览器登录。")
        print("    请先安装:")
        print("        pip install playwright")
        print("        python -m playwright install chromium")
        print()
        print("    或者改用 cookie 方式登录:")
        print("        python sync_and_test.py login --method cookie")
        return None

    print("=" * 56)
    print(f"  LeetCode 浏览器登录  ({site_key})")
    print("=" * 56)
    print(f"  即将打开浏览器到 {base_url}")
    print(f"  请在浏览器中用任意方式完成登录：")
    print(f"    - 扫码 (力扣 App)")
    print(f"    - 手机号 + 短信验证码")
    print(f"    - 账号密码")
    print(f"    - 微信 / GitHub / QQ 等第三方")
    print(f"  登录成功后，脚本会自动捕获 cookie（无需手动操作）。")
    print(f"  最多等待 {timeout} 秒。")
    print("-" * 56)

    with sync_playwright() as p:
        browser = None
        try:
            # --disable-blink-features=AutomationControlled 从 Chrome 层面去掉
            # navigator.webdriver 标志，配合下面的 stealth 脚本进一步隐藏
            browser = p.chromium.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],
            )
        except Exception as e:
            # 可能是 chromium 未安装
            msg = str(e)
            print(f"[!] 启动浏览器失败: {msg}")
            if "Executable doesn't appear" in msg or "playwright install" in msg.lower():
                print("    看起来 chromium 还未安装，请运行:")
                print("        python -m playwright install chromium")
            return None

        try:
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1100, "height": 800},
            )
            # 注入反检测脚本（必须在 new_page/goto 之前）
            context.add_init_script(_STEALTH_JS)
            page = context.new_page()

            # 优先打开登录页，失败则打开首页
            opened = False
            for url in (f"{base_url}/accounts/login/", base_url):
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    opened = True
                    break
                except Exception:
                    continue
            if not opened:
                print("[!] 无法打开 LeetCode 页面，请检查网络。")
                return None

            print("[i] 浏览器已打开，等待你完成登录...")
            cookies = None
            start = time.time()
            last_hint = 0
            while time.time() - start < timeout:
                time.sleep(3)
                try:
                    cd = {c["name"]: c["value"] for c in context.cookies()}
                    if not cd:
                        continue
                    # 用 curl_cffi 验证登录态（不依赖 page 当前 URL/状态），
                    # 解决手机号登录等场景下 page 跳转/popup 导致 page.evaluate 失败的问题；
                    # curl_cffi 不可用时 fallback 到 page.evaluate
                    if _HAS_CURL_CFFI:
                        signed_in, username = _verify_login_curlcffi(base_url, cd)
                    else:
                        info = _check_login_in_page(page)
                        signed_in = info.get("signedIn")
                        username = info.get("username", "")
                    if signed_in:
                        # 登录已识别，多等 2 秒让所有 cookie（含 WAF 验证 cookie）落地
                        time.sleep(2)
                        cookies = {c["name"]: c["value"] for c in context.cookies()}
                        print()
                        print(f"[OK] 检测到登录成功! 用户: {username or '(未知)'}")
                        print(f"     已捕获 {len(cookies)} 个浏览器 cookie (含 WAF 验证 cookie)")
                        if not cookies.get("csrftoken"):
                            print("[!] 警告: 未获取到 csrftoken，提交/测试可能失败。")
                        break
                    # 周期性提示进度 + 诊断信息（cookie 数量、session 有无）
                    elapsed = int(time.time() - start)
                    if elapsed - last_hint >= 15:
                        has_session = "LEETCODE_SESSION" in cd
                        print(f"     等待登录... ({elapsed}/{timeout}s) "
                              f"cookies={len(cd)} session={'有' if has_session else '无'}")
                        last_hint = elapsed
                except Exception:
                    continue

            if not cookies:
                print()
                print("[!] 登录超时或未检测到登录成功。")
                print("    如果已经登录但仍未捕获，可能是 leetcode 页面结构变化，")
                print("    可改用: python sync_and_test.py login --method cookie")
                return None

            return cookies
        finally:
            try:
                browser.close()
            except Exception:
                pass


def login_and_save(site: Optional[str] = None, timeout: int = 300) -> bool:
    """启动浏览器登录并把全部 cookie 写入配置文件。成功返回 True。"""
    cfg = load_config()
    site_key = site or cfg.get("default_site", "leetcode.cn")

    cookies = login_with_browser(site_key, timeout=timeout)
    if not cookies:
        return False

    set_browser_cookies(site_key, cookies)
    print(f"[OK] cookie 已保存到本地配置 (站点: {site_key})")
    return True


def cookie_login_and_save(site: Optional[str] = None) -> bool:
    """交互式让用户从浏览器粘贴 cookie 并保存（fallback 方案）。"""
    cfg = load_config()
    site_key = site or cfg.get("default_site", "leetcode.cn")
    base_url = get_site_config(site_key).get("base_url", f"https://{site_key}")

    print("=" * 56)
    print(f"  手动粘贴 Cookie  ({site_key})")
    print("=" * 56)
    print(f"  1. 在浏览器登录 {base_url}")
    print(f"  2. 打开开发者工具 (F12) -> Application (应用) -> Cookies")
    print(f"  3. 复制 csrftoken 和 LEETCODE_SESSION 的值")
    print("-" * 56)

    csrftoken = input("请输入 csrftoken: ").strip()
    session = input("请输入 LEETCODE_SESSION: ").strip()

    if not csrftoken or not session:
        print("[!] 两者都不能为空")
        return False

    set_cookies(site_key, csrftoken, session)
    print(f"[OK] cookie 已保存 (站点: {site_key})")
    if site_key == "leetcode.cn":
        print("[!] 注意: 手动 cookie 方式缺少 WAF 验证 cookie，leetcode.cn 的 API 调用可能失败。")
        print("    推荐改用浏览器登录: python sync_and_test.py login")
    return True


if __name__ == "__main__":
    # 直接运行此文件即触发浏览器登录
    ok = login_and_save()
    sys.exit(0 if ok else 1)
