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
from typing import Dict, List, Optional

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    load_config, save_config, set_cookies, set_default_site,
    is_configured, get_site_config, CONFIG_FILE
)
from api import LeetCodeAPI, wait_for_result


ROOT_DIR = Path(__file__).parent.parent


def cmd_login(args):
    """登录配置命令"""
    print("=" * 50)
    print("LeetCode 登录配置")
    print("=" * 50)
    print()
    print("请按照以下步骤获取 Cookie:")
    print("1. 在浏览器中登录 LeetCode (leetcode.com)")
    print("2. 打开开发者工具 (F12)")
    print("3. 切换到 Application/存储 标签")
    print("4. 在 Cookies 中找到 csrftoken 和 LEETCODE_SESSION")
    print("5. 复制它们的值粘贴到这里")
    print()

    site = args.site or "leetcode.com"
    print(f"当前配置站点: {site}")
    print()

    csrftoken = input("请输入 csrftoken: ").strip()
    session = input("请输入 LEETCODE_SESSION: ").strip()

    if not csrftoken or not session:
        print("错误: csrftoken 和 LEETCODE_SESSION 都不能为空")
        return False

    set_cookies(site, csrftoken, session)

    # 验证登录
    print("\n正在验证登录状态...")
    api = LeetCodeAPI(site)
    if api.is_logged_in():
        user_info = api.get_user_info()
        username = user_info.get("username", "Unknown")
        print(f"登录成功！用户: {username}")
        return True
    else:
        print("登录验证失败，请检查 Cookie 是否正确")
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
    solutions_dir = ROOT_DIR / "solutions"

    if lang == "python":
        code_file = solutions_dir / "python" / f"{problem['id']:04d}_{problem['title_slug']}.py"
    elif lang == "typescript":
        code_file = solutions_dir / "typescript" / f"{problem['id']:04d}.ts"
    elif lang == "go":
        code_file = solutions_dir / "go" / f"{problem['id']:04d}_{problem['title_slug']}.go"
    elif lang == "rust":
        code_file = solutions_dir / "rust" / f"{problem['id']:04d}.rs"
    elif lang == "java":
        code_file = solutions_dir / "java" / f"{problem['id']:04d}_{problem['title_slug']}.java"
    else:
        print(f"不支持的语言: {lang}")
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
    solutions_dir = ROOT_DIR / "solutions"

    if lang == "python":
        code_file = solutions_dir / "python" / f"{problem['id']:04d}_{problem['title_slug']}.py"
        lang_slug = "python"
    elif lang == "typescript":
        code_file = solutions_dir / "typescript" / f"{problem['id']:04d}.ts"
        lang_slug = "typescript"
    elif lang == "go":
        code_file = solutions_dir / "go" / f"{problem['id']:04d}_{problem['title_slug']}.go"
        lang_slug = "go"
    elif lang == "rust":
        code_file = solutions_dir / "rust" / f"{problem['id']:04d}.rs"
        lang_slug = "rust"
    elif lang == "java":
        code_file = solutions_dir / "java" / f"{problem['id']:04d}_{problem['title_slug']}.java"
        lang_slug = "java"
    else:
        print(f"不支持的语言: {lang}")
        return False

    if not code_file.exists():
        print(f"代码文件不存在: {code_file}")
        return False

    with open(code_file, "r") as f:
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
    result = api.run_test(problem["title_slug"], lang_slug, code, test_case)

    if not result:
        print("提交失败")
        return False

    submission_id = result.get("submission_id")
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
    solutions_dir = ROOT_DIR / "solutions"

    if lang == "python":
        code_file = solutions_dir / "python" / f"{problem['id']:04d}_{problem['title_slug']}.py"
        lang_slug = "python"
    elif lang == "typescript":
        code_file = solutions_dir / "typescript" / f"{problem['id']:04d}.ts"
        lang_slug = "typescript"
    elif lang == "go":
        code_file = solutions_dir / "go" / f"{problem['id']:04d}_{problem['title_slug']}.go"
        lang_slug = "go"
    elif lang == "rust":
        code_file = solutions_dir / "rust" / f"{problem['id']:04d}.rs"
        lang_slug = "rust"
    elif lang == "java":
        code_file = solutions_dir / "java" / f"{problem['id']:04d}_{problem['title_slug']}.java"
        lang_slug = "java"
    else:
        print(f"不支持的语言: {lang}")
        return False

    if not code_file.exists():
        print(f"代码文件不存在: {code_file}")
        return False

    with open(code_file, "r") as f:
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
    result = api.submit_solution(problem["title_slug"], lang_slug, code)

    if not result:
        print("提交失败")
        return False

    submission_id = result.get("submission_id")
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
    # 登录配置
    python sync_and_test.py login

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
    login_parser = subparsers.add_parser("login", help="配置 LeetCode 登录信息")
    login_parser.add_argument("--site", choices=["leetcode.com", "leetcode.cn"],
                              help="指定站点")

    # status 命令
    status_parser = subparsers.add_parser("status", help="查看登录状态")

    # sync 命令
    sync_parser = subparsers.add_parser("sync", help="同步题目和提交状态")
    sync_parser.add_argument("--force", action="store_true", help="强制重新同步")

    # test 命令
    test_parser = subparsers.add_parser("test", help="本地测试代码")
    test_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    test_parser.add_argument("--language", default="python",
                             choices=["python", "typescript", "go", "rust", "java"],
                             help="编程语言")

    # remote-test 命令
    remote_parser = subparsers.add_parser("remote-test", help="远程测试代码")
    remote_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    remote_parser.add_argument("--language", default="python",
                               choices=["python", "typescript", "go", "rust", "java"],
                               help="编程语言")

    # submit 命令
    submit_parser = subparsers.add_parser("submit", help="提交代码到 LeetCode")
    submit_parser.add_argument("query", help="题目查询 (编号/名称/slug)")
    submit_parser.add_argument("--language", default="python",
                               choices=["python", "typescript", "go", "rust", "java"],
                               help="编程语言")

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
