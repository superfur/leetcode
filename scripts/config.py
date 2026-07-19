"""
LeetCode 配置文件管理
"""
import os
import json
from pathlib import Path
from typing import Optional, Dict

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent

# 配置文件路径
CONFIG_FILE = ROOT_DIR / ".leetcode_config.json"


def get_default_config() -> Dict:
    """获取默认配置"""
    return {
        "leetcode.com": {
            "base_url": "https://leetcode.com",
            "graphql_url": "https://leetcode.com/graphql",
            "api_url": "https://leetcode.com/api/problems/all/",
            "submit_url": "https://leetcode.com/problems/{slug}/submit/",
            "check_url": "https://leetcode.com/submissions/detail/{submission_id}/check/",
            "cookies": {
                "csrftoken": "",
                "LEETCODE_SESSION": "",
                "browser_cookies": {}
            }
        },
        "leetcode.cn": {
            "base_url": "https://leetcode.cn",
            "graphql_url": "https://leetcode.cn/graphql",
            "api_url": "https://leetcode.cn/api/problems/all/",
            "submit_url": "https://leetcode.cn/problems/{slug}/submit/",
            "check_url": "https://leetcode.cn/submissions/detail/{submission_id}/check/",
            "cookies": {
                "csrftoken": "",
                "LEETCODE_SESSION": "",
                "browser_cookies": {}
            }
        },
        "default_site": "leetcode.cn"
    }


def load_config() -> Dict:
    """加载配置文件"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            # 合并默认配置，确保新字段存在
            default = get_default_config()
            for site in default:
                if site not in config:
                    config[site] = default[site]
                else:
                    for key in default[site]:
                        if key not in config[site]:
                            config[site][key] = default[site][key]
            return config
    return get_default_config()


def save_config(config: Dict) -> None:
    """保存配置文件"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def get_site_config(site: str = None) -> Dict:
    """获取指定站点的配置"""
    config = load_config()
    site = site or config.get("default_site", "leetcode.cn")
    return config.get(site, config.get("leetcode.cn"))


def set_cookies(site: str, csrftoken: str, session: str) -> None:
    """设置站点 Cookie"""
    config = load_config()
    site_config = config.get(site, get_default_config()[site])
    site_config["cookies"]["csrftoken"] = csrftoken
    site_config["cookies"]["LEETCODE_SESSION"] = session
    config[site] = site_config
    save_config(config)
    print(f"已更新 {site} 的 Cookie 配置")


def set_default_site(site: str) -> None:
    """设置默认站点"""
    config = load_config()
    config["default_site"] = site
    save_config(config)
    print(f"已将默认站点设置为 {site}")


def get_cookies(site: str = None) -> Dict:
    """获取 Cookie"""
    site_config = get_site_config(site)
    return site_config.get("cookies", {})


def set_browser_cookies(site: str, cookies_dict: Dict) -> None:
    """保存浏览器抓取的全部 cookie（含 WAF 验证 cookie，如 aliyungf_tc 等）。

    leetcode.cn 的阿里云 WAF 会拦截非浏览器请求；必须带上浏览器执行 JS 后
    种下的验证 cookie 才能访问 API。这里把 Playwright 抓取的所有 cookie
    存入 browser_cookies，同时同步提取 csrftoken/LEETCODE_SESSION 到顶层
    字段，保持与旧逻辑兼容。
    """
    config = load_config()
    site_config = config.get(site, get_default_config()[site])
    site_config["cookies"]["browser_cookies"] = cookies_dict
    if cookies_dict.get("csrftoken"):
        site_config["cookies"]["csrftoken"] = cookies_dict["csrftoken"]
    if cookies_dict.get("LEETCODE_SESSION"):
        site_config["cookies"]["LEETCODE_SESSION"] = cookies_dict["LEETCODE_SESSION"]
    config[site] = site_config
    save_config(config)
    print(f"已更新 {site} 的 Cookie 配置（含 {len(cookies_dict)} 个浏览器 cookie）")


def get_all_cookies(site: str = None) -> Dict:
    """获取用于发请求的全部 cookie（合并 browser_cookies + 顶层 csrftoken/session）。

    顶层 csrftoken/LEETCODE_SESSION 优先（保证 cookie 方式登录的值不被覆盖）。
    """
    cookies = get_cookies(site)
    merged = {}
    # 先放 browser_cookies（验证 cookie）
    extra = cookies.get("browser_cookies") or {}
    merged.update(extra)
    # 顶层 csrftoken/session 覆盖
    if cookies.get("csrftoken"):
        merged["csrftoken"] = cookies["csrftoken"]
    if cookies.get("LEETCODE_SESSION"):
        merged["LEETCODE_SESSION"] = cookies["LEETCODE_SESSION"]
    return merged


def is_configured(site: str = None) -> bool:
    """检查是否已配置"""
    cookies = get_cookies(site)
    return bool(cookies.get("csrftoken") and cookies.get("LEETCODE_SESSION"))
