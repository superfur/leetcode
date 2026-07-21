#!/usr/bin/env python3
"""
对单题一次性按多种语言提交到 LeetCode。

用法:
    python scripts/submit_all.py 75                       # 提交第 75 题的全部 5 种语言
    python scripts/submit_all.py 75 --langs python,go     # 只提交指定语言
    python scripts/submit_all.py 75 --site leetcode.com   # 切到 .com 站点
    python scripts/submit_all.py 75 --yes                 # 跳过确认 (脚本/CI 使用)
    python scripts/submit_all.py 75 --wait 30             # 自定义每题等待秒数

设计目标:
    一条命令搞定“校验登录 → 拉英文 slug → 读代码 → 提交 → 等待 → 汇总”全链路，
    不再依赖 sync_and_test.py 的交互 input()。

返回:
    0 = 全部 Accepted
    1 = 任意一题未 Accepted (含 WA / TLE / RE 等)
    2 = 配置/登录/找不到代码等前置失败
"""
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Windows 控制台编码兼容
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))

from config import load_config, is_configured  # noqa: E402
from api import LeetCodeAPI, wait_for_result  # noqa: E402
from new_solution import find_problem  # noqa: E402

ROOT_DIR = Path(__file__).parent.parent

# 通用语言名 → 文件扩展名
_LANG_EXT = {"python": "py", "typescript": "ts", "go": "go", "rust": "rs", "java": "java"}

# LeetCode 状态码 → 中文说明 (与 sync_and_test.py 中保持一致)
_STATUS_TEXT = {
    10: "Accepted",
    11: "Wrong Answer",
    12: "Memory Limit Exceeded",
    13: "Time Limit Exceeded",
    14: "Runtime Error",
    15: "Compile Error",
    20: "Unknown Error",
}


def _find_code_file(problem: Dict, lang: str) -> Optional[Path]:
    """根据 problem 与 lang 找代码文件，兼容多种命名变体。"""
    ext = _LANG_EXT.get(lang)
    if not ext:
        return None
    folder = ROOT_DIR / "solutions" / lang
    if not folder.exists():
        return None
    pid = f"{problem['id']:04d}"
    candidates = [
        folder / f"{pid}.{ext}",
        folder / f"{pid}_{problem.get('title_slug', '')}.{ext}",
    ]
    for c in candidates:
        if c.exists():
            return c
    matches = sorted(folder.glob(f"{pid}*.{ext}"))
    return matches[0] if matches else None


def _ensure_login(api: LeetCodeAPI) -> bool:
    """检查 cookie 配置 + 服务端登录态，缺一不可。"""
    if not is_configured(api.site):
        print(f"[!] {api.site} 未配置 csrftoken / LEETCODE_SESSION，请先运行 login")
        return False
    if not api.is_logged_in():
        print(f"[!] {api.site} 已配置但服务端判定未登录 (cookie 可能失效)")
        return False
    info = api.get_user_info()
    if info:
        print(f"[OK] {api.site} 已登录：用户={info.get('username', '?')}, "
              f"已解决={info.get('totalSolved', '?')}/{info.get('totalQuestions', '?')}")
    return True


def _submit_one(api: LeetCodeAPI, slug: str, lang: str, code: str, wait: int) -> Dict:
    """提交一种语言并等结果，返回规范化结果 dict。"""
    result = api.submit_solution(slug, lang, code)
    if not result:
        return {"lang": lang, "ok": False, "error": "提交失败 (无 submission_id)"}
    submission_id = result.get("submission_id") or result.get("submissionId")
    print(f"  -> submission_id={submission_id}, 等待判题 (最长 {wait}s)...")
    final = wait_for_result(submission_id, api, max_wait=wait)
    if not final:
        return {"lang": lang, "ok": False, "submission_id": submission_id,
                "error": "等待结果超时"}

    code_n = final.get("status_code")
    ok = code_n == 10
    return {
        "lang": lang,
        "ok": ok,
        "status_code": code_n,
        "status": _STATUS_TEXT.get(code_n, f"状态码 {code_n}"),
        "submission_id": submission_id,
        "total_correct": final.get("total_correct"),
        "total_testcase": final.get("total_testcase"),
        "runtime": final.get("status_runtime"),
        "memory": final.get("status_memory"),
        "error": final.get("error") if not ok else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="对单题按多种语言一次性提交 LeetCode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("query", help="题目查询 (编号 / slug / 中文名)")
    parser.add_argument("--site", choices=["leetcode.com", "leetcode.cn"],
                        default=load_config().get("default_site", "leetcode.cn"))
    parser.add_argument("--langs", default="python,typescript,go,rust,java",
                        help="要提交的语言列表，逗号分隔 (默认 5 种)")
    parser.add_argument("--yes", "-y", action="store_true", help="跳过确认")
    parser.add_argument("--wait", type=int, default=60, help="每次提交等判题的最大秒数")
    args = parser.parse_args()

    # 1. 找题目
    problem = find_problem(args.query)
    if not problem:
        print(f"[!] 找不到题目: {args.query}")
        return 2
    print(f"题目: #{problem['id']} - {problem['title']}")

    # 2. 登录态
    api = LeetCodeAPI(args.site)
    if not _ensure_login(api):
        return 2

    # 3. 拿英文 slug (本地可能是中文目录名)
    slug = api.get_slug_by_id(problem["id"]) if not problem.get("title_slug", "").isascii() \
        else problem.get("title_slug")
    if not slug:
        print(f"[!] 无法获取英文 slug")
        return 2
    print(f"slug: {slug}")
    print(f"语言: {args.langs}")
    print()

    # 4. 确认
    if not args.yes:
        confirm = input("确认提交以上题目到 LeetCode? (y/n): ")
        if confirm.strip().lower() != "y":
            print("已取消")
            return 0

    # 5. 遍历语言提交
    langs = [s.strip() for s in args.langs.split(",") if s.strip()]
    results: List[Dict] = []
    for lang in langs:
        code_file = _find_code_file(problem, lang)
        if not code_file or not code_file.exists():
            print(f"[跳过] {lang}: 代码文件不存在")
            results.append({"lang": lang, "ok": False, "error": "代码文件不存在"})
            continue
        try:
            code = code_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"[跳过] {lang}: 代码不是 utf-8 ({code_file})")
            results.append({"lang": lang, "ok": False, "error": "编码不是 utf-8"})
            continue

        print(f"[{lang}] {code_file.name} ({len(code)} chars) -> submit")
        try:
            r = _submit_one(api, slug, lang, code, args.wait)
        except Exception as e:  # 网络/JSON 解析异常不中断后续提交
            r = {"lang": lang, "ok": False, "error": f"异常: {e}"}
        results.append(r)
        if r.get("ok"):
            print(f"  ✓ {lang}: Accepted "
                  f"({r.get('total_correct')}/{r.get('total_testcase')}, "
                  f"{r.get('runtime')}, {r.get('memory')})")
        else:
            print(f"  ✗ {lang}: {r.get('status') or r.get('error')}")
            if r.get("error"):
                print(f"      {r['error']}")
        print()

    # 6. 汇总
    print("=" * 56)
    print("汇总")
    print("=" * 56)
    width = max((len(r["lang"]) for r in results), default=8)
    for r in results:
        mark = "✓" if r.get("ok") else "✗"
        detail = (r.get("status")
                  or r.get("error")
                  or "")
        line = f"  {mark} {r['lang']:<{width}}  {detail}"
        if r.get("ok"):
            line += f"  ({r.get('total_correct')}/{r.get('total_testcase')}, {r.get('runtime')}, {r.get('memory')})"
        print(line)

    ac_count = sum(1 for r in results if r.get("ok"))
    print(f"\n{ac_count}/{len(results)} Accepted")
    return 0 if ac_count == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
