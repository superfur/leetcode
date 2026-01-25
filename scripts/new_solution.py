#!/usr/bin/env python3
"""
快速生成 LeetCode 题目解法文件的脚本

用法:
    python new_solution.py "two_sum"              # 通过 slug 名称
    python new_solution.py "两数之和"              # 通过中文名称
    python new_solution.py 1                      # 通过题目编号
    python new_solution.py "1" --all              # 生成所有语言的解法
    python new_solution.py "two_sum" --python     # 只生成 Python 解法
    python new_solution.py "two_sum" --ts --go    # 生成多种语言
"""

import argparse
import os
import re
import json
import sys
from pathlib import Path
from typing import Dict, Optional, List

# 支持的语言
LANGUAGES = {
    "python": {"ext": "py", "folder": "solutions/python", "template": "python"},
    "typescript": {"ext": "ts", "folder": "solutions/typescript", "template": "typescript"},
    "go": {"ext": "go", "folder": "solutions/go", "template": "go"},
    "rust": {"ext": "rs", "folder": "solutions/rust", "template": "rust"},
    "java": {"ext": "java", "folder": "solutions/java", "template": "java"},
}

# 当前目录
ROOT_DIR = Path(__file__).parent.parent


def find_problem(query: str) -> Optional[Dict]:
    """
    根据查询找到对应的题目
    支持: 数字编号、slug、中文名称
    """
    query = query.strip()

    # 1. 通过数字编号精确查找
    if query.isdigit():
        problem_id = int(query)
        # 直接构建目录名，不使用通配符
        dir_name = f"{problem_id:04d}-"
        problem_dir = ROOT_DIR / "problems"
        for child in problem_dir.iterdir():
            if child.is_dir() and child.name.startswith(dir_name):
                return load_problem_info(child, problem_id)

    # 2. 精确匹配中文名称
    for dir_path in (ROOT_DIR / "problems").iterdir():
        if dir_path.is_dir():
            folder_name = dir_path.name
            match = re.match(r"\d+-(.+)", folder_name)
            if match:
                chinese_name = match.group(1)
            else:
                chinese_name = folder_name

            # 精确匹配中文名
            if query == chinese_name:
                return load_problem_info(dir_path)

    # 3. 尝试作为 slug 查找 (从目录名中提取)
    problem_dir = ROOT_DIR / "problems" / f"*-{query}"
    dirs = list(problem_dir.glob("*"))
    if dirs:
        return load_problem_info(dirs[0])

    # 4. 部分匹配 (只对单字符查询跳过)
    if len(query) <= 2:
        return None

    for dir_path in (ROOT_DIR / "problems").iterdir():
        if dir_path.is_dir():
            folder_name = dir_path.name
            match = re.match(r"\d+-(.+)", folder_name)
            if match:
                chinese_name = match.group(1)
            else:
                chinese_name = folder_name

            # 部分匹配
            if query in chinese_name:
                return load_problem_info(dir_path)

    return None


def load_problem_info(problem_dir: Path, expected_id: int = None) -> Dict:
    """加载题目信息"""
    # 提取题目编号
    folder_name = problem_dir.name
    match = re.match(r"(\d+)-(.*)", folder_name)
    if match:
        problem_id = int(match.group(1))
        title_slug = match.group(2)
    else:
        # 处理非数字编号的题目
        problem_id = expected_id or 0
        title_slug = folder_name

    # 读取 README 获取标题和描述
    readme_path = problem_dir / "README.md"
    title = title_slug.replace("-", " ").title()
    description = ""

    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            # 提取标题
            title_match = re.search(r"#\s*(\d+)[.-]?\s*(.+)", content)
            if title_match:
                title = title_match.group(2).strip()
            # 简单提取描述 (第一段非空内容)
            lines = content.split("\n")
            in_code = False
            for line in lines:
                if "```" in line:
                    in_code = not in_code
                elif not in_code and line.strip() and not line.startswith("#"):
                    description = line.strip()[:200]
                    break

    # 读取测试用例
    test_cases_path = problem_dir / "test_cases.json"
    test_cases = []
    if test_cases_path.exists():
        with open(test_cases_path, "r", encoding="utf-8") as f:
            try:
                test_cases = json.load(f).get("test_cases", [])
            except:
                pass

    return {
        "id": problem_id,
        "title_slug": title_slug,
        "title": title,
        "description": description,
        "test_cases": test_cases,
        "folder_name": folder_name,
    }


def to_camel_case(s: str) -> str:
    """转换为 camelCase (用于函数名)"""
    parts = s.replace("-", " ").replace("_", " ").split()
    if not parts:
        return "solution"
    return parts[0].lower() + "".join(p.title() for p in parts[1:])


def to_pascal_case(s: str) -> str:
    """转换为 PascalCase (用于类名)"""
    parts = s.replace("-", " ").replace("_", " ").split()
    return "".join(p.title() for p in parts)


def generate_template(lang: str, problem: Dict) -> str:
    """根据语言生成解法模板"""
    func_name = to_camel_case(problem["title_slug"])
    class_name = to_pascal_case(problem["title_slug"])
    title = problem["title"]
    title_slug = problem["title_slug"]

    templates = {
        "python": f'''from typing import List

def {func_name}(*args, **kwargs):
    """
    {title}
    """
    # TODO: 实现你的解法
    pass

if __name__ == "__main__":
    # 测试用例
    test_cases = {json.dumps(problem["test_cases"][:3] if problem["test_cases"] else [], indent=4)}
    for i, test_case in enumerate(test_cases, 1):
        print(f"测试用例 {{i}}: {{test_case}}")
''',
        "typescript": f'''/**
 * {title}
 */
function {func_name}(...args: any[]): any {{
    // TODO: 实现你的解法
    return null;
}}

export default {func_name};
''',
        "go": f'''package main

func {func_name}(...args interface{{}}) interface{{}} {{
    // TODO: 实现你的解法
    return nil
}}

func main() {{
    // 测试用例
    println("{title}")
}}
''',
        "rust": f'''use std::collections::HashMap;

impl Solution {{
    pub fn {func_name}(nums: Vec<i32>, target: i32) -> Vec<i32> {{
        // TODO: 实现你的解法
        vec![]
    }}
}}
''',
        "java": f'''package com.leetcode;

public class Solution {{
    /**
     * {title}
     */
    public Object {func_name}(Object... args) {{
        // TODO: 实现你的解法
        return null;
    }}
}}
''',
    }

    return templates.get(lang, "# 未支持的语言")


def generate_solution_file(lang: str, problem: Dict, overwrite: bool = False) -> bool:
    """生成单个语言的解法文件"""
    lang_info = LANGUAGES.get(lang)
    if not lang_info:
        print(f"不支持的语言: {lang}")
        return False

    folder = ROOT_DIR / lang_info["folder"]
    folder.mkdir(parents=True, exist_ok=True)

    # 根据语言确定文件名格式
    if lang == "python":
        filename = f"{problem['id']:04d}_{problem['title_slug']}.{lang_info['ext']}"
    elif lang == "typescript":
        filename = f"{problem['id']:04d}.{lang_info['ext']}"
    elif lang == "rust":
        # Rust 使用纯数字命名，如 0001.rs
        filename = f"{problem['id']:04d}.{lang_info['ext']}"
    else:
        filename = f"{problem['id']:04d}_{problem['title_slug']}.{lang_info['ext']}"

    file_path = folder / filename

    if file_path.exists() and not overwrite:
        print(f"  [跳过] {filename} (已存在)")
        return False

    # 生成模板内容
    template = generate_template(lang, problem)

    # 写入文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"  [创建] {filename}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="快速生成 LeetCode 题目解法文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python new_solution.py "two_sum"                    # 通过 slug
    python new_solution.py "两数之和"                    # 通过中文名
    python new_solution.py 1                            # 通过编号
    python new_solution.py "two_sum" --all              # 所有语言
    python new_solution.py "two_sum" --python --ts      # 指定语言
    python new_solution.py "two_sum" -f                 # 强制覆盖
        """,
    )

    parser.add_argument("query", nargs="?", help="题目查询 (编号/slug/中文名)")
    parser.add_argument("--all", action="store_true", help="生成所有语言的解法")
    parser.add_argument("-f", "--force", action="store_true", help="覆盖已存在的文件")
    parser.add_argument("--python", action="store_true", help="生成 Python 解法")
    parser.add_argument("--typescript", action="store_true", help="生成 TypeScript 解法")
    parser.add_argument("--go", action="store_true", help="生成 Go 解法")
    parser.add_argument("--rust", action="store_true", help="生成 Rust 解法")
    parser.add_argument("--java", action="store_true", help="生成 Java 解法")

    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        print("\n请提供题目查询参数")
        sys.exit(1)

    # 查找题目
    print(f"正在查找题目: {args.query}")
    problem = find_problem(args.query)

    if not problem:
        print(f"未找到题目: {args.query}")
        print("请尝试:")
        print("  - 使用题目编号: python new_solution.py 1")
        print("  - 使用 slug: python new_solution.py two-sum")
        print("  - 使用中文名: python new_solution.py 两数之和")
        sys.exit(1)

    print(f"找到题目: #{problem['id']} - {problem['title']}")
    print(f"Slug: {problem['title_slug']}")
    print(f"文件夹: {problem['folder_name']}")
    print()

    # 确定要生成的语言
    if args.all:
        languages = list(LANGUAGES.keys())
    else:
        languages = []
        for lang in LANGUAGES:
            if getattr(args, lang, False):
                languages.append(lang)

        if not languages:
            # 默认只生成 Python
            languages = ["python"]

    # 生成解法文件
    print(f"生成解法文件:")
    for lang in languages:
        generate_solution_file(lang, problem, args.force)

    print("\n完成!")


if __name__ == "__main__":
    main()
