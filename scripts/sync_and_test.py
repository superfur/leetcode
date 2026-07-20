#!/usr/bin/env python3
"""
LeetCode 同步和测试脚本

功能:
1. 配置 LeetCode 登录信息
2. 同步题目和提交状态
3. 本地测试
4. 远程测试和提交
"""
import argparse
import os
import sys
import json
import time
from pathlib import Path

# Windows 控制台默认 GBK 编码，输出 ✓/✗ 等 Unicode 符号会崩溃，强制 utf-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from typing import Dict, List, Optional

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    load_config, save_config, set_cookies, set_default_site,
    is_configured, get_site_config, CONFIG_FILE
)
from api import LeetCodeAPI, wait_for_result


ROOT_DIR = Path(__file__).parent.parent


# 语言 -> 扩展名
_LANG_EXT = {"python": "py", "typescript": "ts", "go": "go", "rust": "rs", "java": "java"}


def find_code_file(problem: Dict, lang: str):
    """查找题目对应的代码文件。

    solutions 目录下文件命名不统一（0001.py / 0001_two-sum.py / 0074_搜索二维矩阵.java），
    这里用精确 + glob 兜底的方式匹配，兼容所有变体。
    返回 Path 或 None。
    """
    ext = _LANG_EXT.get(lang)
    if not ext:
        return None
    folder = ROOT_DIR / "solutions" / lang
    pid = f"{problem['id']:04d}"
    # 1) 精确 {id}.ext  2) {id}_{slug}.ext  3) glob {id}*.ext 兜底
    for name in (f"{pid}.{ext}", f"{pid}_{problem.get('title_slug', '')}.{ext}"):
        p = folder / name
        if p.exists():
            return p
    matches = sorted(folder.glob(f"{pid}*.{ext}"))
    return matches[0] if matches else None


def add_lang_args(parser, default="python"):
    """为子命令注册语言参数：--language python，以及 --python/--typescript 等简写。"""
    parser.add_argument("--language", default=default,
                        choices=["python", "typescript", "go", "rust", "java"],
                        help="编程语言")
    for short, val in (("--python", "python"), ("--typescript", "typescript"),
                       ("--go", "go"), ("--rust", "rust"), ("--java", "java")):
        parser.add_argument(short, dest="language", action="store_const", const=val)


def _ensure_english_slug(api, problem):
    """本地 title_slug 可能是中文目录名；leetcode API 需要英文 slug，按题号查并更新。"""
    slug = problem.get("title_slug", "")
    if slug and not slug.isascii():
        en = api.get_slug_by_id(problem["id"])
        if en:
            problem["title_slug"] = en
        else:
            print(f"[!] 无法获取题目 #{problem['id']} 的英文 slug (仍用 '{slug}')")
    return problem.get("title_slug")


def cmd_login(args):
    """登录配置命令"""
    site = args.site or None
    method = getattr(args, "method", None) or "browser"

    print("=" * 56)
    print("LeetCode 登录")
    print("=" * 56)

    if method == "cookie":
        from auth import cookie_login_and_save
        ok = cookie_login_and_save(site)
    else:
        from auth import login_and_save
        ok = login_and_save(site)

    if not ok:
        return False

    # 验证登录状态
    print("\n正在验证登录状态...")
    api = LeetCodeAPI(site)
    if api.is_logged_in():
        user_info = api.get_user_info()
        username = user_info.get("username", "Unknown")
        print(f"[OK] 登录有效! 用户: {username}")
        return True
    else:
        print("[!] cookie 已保存，但服务器验证未通过。")
        print("    可能原因: cookie 失效 / 网络问题 / 站点接口变化。")
        return False


def cmd_status(args):
    """查看状态命令"""
    site = args.site or None

    print("=" * 50)
    print("LeetCode 状态")
    print("=" * 50)

    if not is_configured(site):
        print("尚未配置 LeetCode 登录信息")
        print("请先运行: python sync_and_test.py login")
        return False

    api = LeetCodeAPI(site)
    if not api.is_logged_in():
        print("登录状态已失效，请重新配置")
        return False

    user_info = api.get_user_info()
    if user_info:
        print(f"用户: {user_info.get('username', 'N/A')}")
        print(f"总解决: {user_info.get('totalSolved', 0)} / {user_info.get('totalQuestions', 0)}")
        print(f"  - 简单: {user_info.get('easySolved', 0)}")
        print(f"  - 中等: {user_info.get('mediumSolved', 0)}")
        print(f"  - 困难: {user_info.get('hardSolved', 0)}")
    else:
        print("无法获取用户信息")


def cmd_sync(args):
    """同步命令"""
    site = args.site or None
    force = args.force

    print("=" * 50)
    print("同步 LeetCode 数据")
    print("=" * 50)

    if not is_configured(site):
        print("尚未配置 LeetCode 登录信息")
        return False

    api = LeetCodeAPI(site)

    # 同步题目列表
    print("\n正在同步题目列表...")
    problems = api.fetch_problem_list()
    print(f"获取到 {len(problems)} 道题目")

    # 同步已解决题目
    print("\n正在同步解决状态...")
    solved_count = 0
    total_count = len(problems)

    # 更新 problems.json
    problems_file = ROOT_DIR / "problems.json"
    local_problems = {}

    if problems_file.exists():
        with open(problems_file, "r") as f:
            local_problems = json.load(f)

    for problem in problems:
        stat = problem.get("stat", {})
        question_id = stat.get("frontend_question_id", 0)
        title_slug = stat.get("question__title_slug", "")
        status = problem.get("status", "")

        is_solved = status == "ac"
        if is_solved:
            solved_count += 1

        # 更新本地
        local_problems[str(question_id)] = {
            "title_slug": title_slug,
            "solved": is_solved,
            "status": status
        }

    with open(problems_file, "w") as f:
        json.dump(local_problems, f, indent=2)

    print(f"已解决: {solved_count} / {total_count}")

    # 同步提交历史
    print("\n正在同步提交历史...")
    submissions = api.fetch_user_submissions(limit=50)
    print(f"获取到 {len(submissions)} 条提交记录")

    # 保存提交历史
    submissions_file = ROOT_DIR / "submissions.json"
    submissions_data = []
    if submissions_file.exists():
        with open(submissions_file, "r") as f:
            submissions_data = json.load(f)

    # 合并新提交
    existing_ids = {s.get("id") for s in submissions_data}
    for sub in submissions:
        if sub.get("id") not in existing_ids:
            submissions_data.insert(0, sub)

    # 只保留最近100条
    submissions_data = submissions_data[:100]

    with open(submissions_file, "w") as f:
        json.dump(submissions_data, f, indent=2)

    print("\n同步完成!")


def cmd_test(args):
    """本地测试命令"""
    query = args.query
    lang = args.language

    # 查找题目
    from new_solution import find_problem
    problem = find_problem(query)

    if not problem:
        print(f"未找到题目: {query}")
        return False

    print(f"题目: #{problem['id']} - {problem['title']}")

    # 获取代码文件
    code_file = find_code_file(problem, lang)
    if not code_file:
        print(f"不支持的语言或代码文件不存在: {lang} / #{problem['id']}")
        print("请先生成代码文件: python new_solution.py \"题目名称\"")
        return False

    if not code_file.exists():
        print(f"代码文件不存在: {code_file}")
        print("请先生成代码文件: python new_solution.py \"题目名称\"")
        return False

    # 读取测试用例
    test_cases_file = ROOT_DIR / "problems" / problem["folder_name"] / "test_cases.json"
    if not test_cases_file.exists():
        print(f"测试用例文件不存在: {test_cases_file}")
        return False

    with open(test_cases_file, "r") as f:
        test_cases = json.load(f).get("test_cases", [])

    if not test_cases:
        print("没有测试用例")
        return False

    print(f"\n运行 {len(test_cases)} 个测试用例:")
    print("-" * 50)

    # 运行测试
    if lang == "python":
        import subprocess
        for i, tc in enumerate(test_cases, 1):
            input_data = tc.get("input", "")
            expected = tc.get("expected", "")
            print(f"\n��试用例 {i}:")
            print(f"输入: {input_data}")
            print(f"预期: {expected}")
            # 简单运行测试
            result = subprocess.run(
                ["python3", str(code_file)],
                capture_output=True,
                text=True
            )
            print(f"输出: {result.stdout.strip() if result.stdout else '(无输出)'}")
            if result.stderr:
                print(f"错误: {result.stderr.strip()}")

    print("\n" + "-" * 50)
    print("测试完成（本地测试仅供参考，请以远程测试为准）")


def cmd_remote_test(args):
    """远程测试命令"""
    query = args.query
    lang = args.language
    site = args.site or None

    if not is_configured(site):
        print("尚未配置 LeetCode 登录信息")
        return False

    api = LeetCodeAPI(site)

    if not api.is_logged_in():
        print("登录状态已失效，请重新配置")
        return False

    # 查找题目
    from new_solution import find_problem
    problem = find_problem(query)

    if not problem:
        print(f"未找到题目: {query}")
        return False

    print(f"题目: #{problem['id']} - {problem['title']}")
    print()

    # 获取代码
    code_file = find_code_file(problem, lang)
    if not code_file or not code_file.exists():
        print(f"代码文件不存在: solutions/{lang}/#{problem['id']}")
        return False
    lang_slug = lang  # 通用语言名，api 层会做站点映射 (python->python3 等)

    with open(code_file, "r", encoding="utf-8") as f:
        code = f.read()

    print(f"语言: {lang}")
    print(f"代码长度: {len(code)} 字符")
    print()

    # 获取示例测试用例
    problem_dir = ROOT_DIR / "problems" / problem["folder_name"]
    test_cases_file = problem_dir / "test_cases.json"

    test_case = ""
    if test_cases_file.exists():
        with open(test_cases_file, "r") as f:
            test_cases = json.load(f).get("test_cases", [])
            if test_cases:
                test_case = test_cases[0].get("input", "")

    if not test_case:
        # 从题目详情获取
        detail = api.fetch_problem_detail(problem["title_slug"])
        if detail:
            test_case = detail.get("sampleTestCase", "") or detail.get("exampleTestcases", "")

    print("正在提交远程测试...")
    _ensure_english_slug(api, problem)
    result = api.run_test(problem["title_slug"], lang_slug, code, test_case)

    if not result:
        print("提交失败")
        return False

    submission_id = result.get("submission_id") or result.get("submissionId")
    print(f"提交ID: {submission_id}")
    print("正在等待结果...")

    final_result = wait_for_result(submission_id, api)

    if final_result:
        status = final_result.get("status_code", 0)
        if status == 10:  # Accepted
            print("\n✓ 测试通过!")
        else:
            print(f"\n✗ 测试失败 (状态码: {status})")

        # 显示运行信息
        total_correct = final_result.get("total_correct", 0)
        total_testcase = final_result.get("total_testcase", 0)
        status_runtime = final_result.get("status_runtime", "")
        status_memory = final_result.get("status_memory", "")

        print(f"正确/总计: {total_correct}/{total_testcase}")
        if status_runtime:
            print(f"运行时间: {status_runtime}")
        if status_memory:
            print(f"内存使用: {status_memory}")

        # 显示错误信息
        if status != 10 and final_result.get("error"):
            print(f"\n错误信息: {final_result['error']}")
    else:
        print("等待结果超时")
        print("[!] leetcode.cn 的「运行测试」(test_mode) 提交后通常不会判题，")
        print("    建议改用正式提交: python sync_and_test.py submit \"" + args.query + "\" --" + args.language)


def cmd_submit(args):
    """提交命令"""
    query = args.query
    lang = args.language
    site = args.site or None

    if not is_configured(site):
        print("尚未配置 LeetCode 登录信息")
        return False

    api = LeetCodeAPI(site)

    if not api.is_logged_in():
        print("登录状态已失效，请重新配置")
        return False

    # 查找题目
    from new_solution import find_problem
    problem = find_problem(query)

    if not problem:
        print(f"未找到题目: {query}")
        return False

    print(f"题目: #{problem['id']} - {problem['title']}")
    print()

    # 获取代码
    code_file = find_code_file(problem, lang)
    if not code_file or not code_file.exists():
        print(f"代码文件不存在: solutions/{lang}/#{problem['id']}")
        return False
    lang_slug = lang  # 通用语言名，api 层会做站点映射 (python->python3 等)

    with open(code_file, "r", encoding="utf-8") as f:
        code = f.read()

    print(f"语言: {lang}")
    print(f"代码长度: {len(code)} 字符")
    print()
    print("警告: 此操作将提交代码到 LeetCode")
    confirm = input("是否继续? (y/n): ")

    if confirm.lower() != "y":
        print("已取消")
        return True

    print("\n正在提交...")
    _ensure_english_slug(api, problem)
    result = api.submit_solution(problem["title_slug"], lang_slug, code)

    if not result:
        print("提交失败")
        return False

    submission_id = result.get("submission_id") or result.get("submissionId")
    print(f"提交ID: {submission_id}")
    print("正在等待结果...")

    final_result = wait_for_result(submission_id, api)

    if final_result:
        status = final_result.get("status_code", 0)
        if status == 10:  # Accepted
            print("\n✓ 恭喜! Accepted!")
        elif status == 11:  # Wrong Answer
            print("\n✗ Wrong Answer")
        elif status == 12:  # Memory Limit Exceeded
            print("\n✗ Memory Limit Exceeded")
        elif status == 13:  # Time Limit Exceeded
            print("\n✗ Time Limit Exceeded")
        elif status == 14:  # Runtime Error
            print("\n✗ Runtime Error")
        else:
            print(f"\n? 未知状态 (状态码: {status})")

        # 显示运行信息
        total_correct = final_result.get("total_correct", 0)
        total_testcase = final_result.get("total_testcase", 0)
        status_runtime = final_result.get("status_runtime", "")
        status_memory = final_result.get("status_memory", "")

        print(f"正确/总计: {total_correct}/{total_testcase}")
        if status_runtime:
            print(f"运行时间: {status_runtime}")
        if status_memory:
            print(f"内存使用: {status_memory}")

        # 显示错误信息
        if status != 10 and final_result.get("error"):
            print(f"\n错误信息: {final_result['error']}")
    else:
        print("等待结果超时，请稍后到 LeetCode 网站查看结果")


def cmd_submissions(args):
    """查看提交历史命令"""
    site = args.site or None
    limit = args.limit

    if not is_configured(site):
        print("尚未配置 LeetCode 登录信息")
        return False

    api = LeetCodeAPI(site)

    if not api.is_logged_in():
        print("登录状态已失效，请重新配置")
        return False

    submissions = api.fetch_user_submissions(limit=limit)

    print("=" * 80)
    print("最近提交记录")
    print("=" * 80)
    print(f"{'状态':<10} {'题目':<30} {'语言':<12} {'时间'}")
    print("-" * 80)

    for sub in submissions:
        status = sub.get("status", "")
        title = sub.get("title", "")[:28]
        lang = sub.get("lang", "")
        timestamp = sub.get("timestamp", 0)

        # 格式化时间
        from datetime import datetime
        dt = datetime.fromtimestamp(timestamp)
        time_str = dt.strftime("%Y-%m-%d %H:%M")

        # 状态图标
        if status == "AC":
            status_icon = "✓"
        elif status == "WA":
            status_icon = "✗"
        elif status == "TLE":
            status_icon = "⏱"
        elif status == "MLE":
            status_icon = "💾"
        else:
            status_icon = "?"

        print(f"{status_icon} {status:<8} {title:<30} {lang:<12} {time_str}")


def main():
    parser = argparse.ArgumentParser(
        description="LeetCode 同步和测试工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    # 浏览器登录 (默认, 弹出浏览器，扫码/短信/账密均可)
    python sync_and_test.py login

    # 手动粘贴 cookie 登录
    python sync_and_test.py login --method cookie

    # 指定 leetcode.com 站点登录
    python sync_and_test.py login --site leetcode.com

    # 查看状态
    python sync_and_test.py status

    # 同步数据
    python sync_and_test.py sync

    # 本地测试
    python sync_and_test.py test "两数之和" --python

    # 远程测试
    python sync_and_test.py remote-test "两数之和" --python

    # 提交代码
    python sync_and_test.py submit "两数之和" --python

    # 查看提交历史
    python sync_and_test.py submissions
        """
    )

    parser.add_argument("--site", choices=["leetcode.com", "leetcode.cn"],
                        help="指定 LeetCode 站点")

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # login 命令
    login_parser = subparsers.add_parser("login", help="登录 LeetCode")
    login_parser.add_argument("--site", choices=["leetcode.com", "leetcode.cn"],
                              help="指定站点 (默认 leetcode.cn)")
    login_parser.add_argument("--method", choices=["browser", "cookie"],
                              default="browser",
                              help="登录方式: browser=浏览器自动化(默认) / cookie=手动粘贴")

    # status 命令
    status_parser = subparsers.add_parser("status", help="查看登录状态")

    # sync 命令
    sync_parser = subparsers.add_parser("sync", help="同步题目和提交状态")
    sync_parser.add_argument("--force", action="store_true", help="强制重新同步")

    # test 命令
    test_parser = subparsers.add_parser("test", help="本地测试代码")
    test_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    add_lang_args(test_parser)

    # remote-test 命令
    remote_parser = subparsers.add_parser("remote-test", help="远程测试代码")
    remote_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    add_lang_args(remote_parser)

    # submit 命令
    submit_parser = subparsers.add_parser("submit", help="提交代码到 LeetCode")
    submit_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    add_lang_args(submit_parser)

    # submissions 命令
    submissions_parser = subparsers.add_parser("submissions", help="查看提交历史")
    submissions_parser.add_argument("--limit", type=int, default=20, help="显示数量")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # 根据命令执行
    commands = {
        "login": cmd_login,
        "status": cmd_status,
        "sync": cmd_sync,
        "test": cmd_test,
        "remote-test": cmd_remote_test,
        "submit": cmd_submit,
        "submissions": cmd_submissions,
    }

    func = commands.get(args.command)
    if func:
        func(args)


if __name__ == "__main__":
    main()
