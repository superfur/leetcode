import requests
import json
import os
import time
import random
from typing import Dict, List

def fetch_problem_list(max_retries: int = 3) -> List[Dict]:
    """获取LeetCode问题列表"""
    url = "https://leetcode.cn/api/problems/all/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://leetcode.cn/problemset/all/"
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data["stat_status_pairs"]
            else:
                print(f"获取问题列表失败，状态码: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(random.uniform(1, 3))
        except Exception as e:
            print(f"获取问题列表时出错: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(random.uniform(1, 3))
    
    return []

def fetch_problem_detail(title_slug: str, max_retries: int = 3) -> Dict:
    """获取单个问题的详细信息"""
    url = "https://leetcode.cn/graphql"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Referer": f"https://leetcode.cn/problems/{title_slug}/"
    }
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            titleSlug
            translatedTitle
            content
            translatedContent
            difficulty
            codeSnippets {
                lang
                langSlug
                code
            }
            sampleTestCase
            exampleTestcases
            hints
            similarQuestions
            topicTags {
                name
                slug
                translatedName
            }
        }
    }
    """
    variables = {"titleSlug": title_slug}
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json={"query": query, "variables": variables}, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()["data"]["question"]
            else:
                print(f"获取问题详情失败，状态码: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(random.uniform(1, 3))
        except Exception as e:
            print(f"获取问题详情时出错: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(random.uniform(1, 3))
    
    return {}

def get_problem_detail(title_slug):
    """获取问题的详细信息"""
    url = "https://leetcode.cn/graphql"
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            translatedTitle
            translatedContent
            difficulty
            topicTags {
                name
                slug
                translatedName
            }
            hints
            exampleTestcases
            sampleTestCase
            metaData
            codeSnippets {
                lang
                langSlug
                code
            }
        }
    }
    """
    
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Referer": f"https://leetcode.cn/problems/{title_slug}/"
    }
    
    try:
        response = requests.post(url, 
                               json={"query": query, "variables": {"titleSlug": title_slug}},
                               headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('question', {})
    except Exception as e:
        print(f"获取问题详情时出错: {e}")
    return None

def create_problem_directory(problem):
    """创建问题目录和文件"""
    try:
        # 获取问题信息
        problem_id = problem["stat"]["frontend_question_id"]
        title_slug = problem["stat"].get("question__title_slug")
        
        # 如果title_slug为None，跳过这个问题
        if not title_slug:
            print(f"跳过问题 {problem_id}：缺少title_slug")
            return
            
        # 获取问题详情
        detail = fetch_problem_detail(title_slug)
        if not detail:
            print(f"无法获取问题 {problem_id} 的详情")
            return
            
        # 获取中文标题
        chinese_title = detail.get('translatedTitle', '')
        if not chinese_title:
            print(f"跳过问题 {problem_id}：缺少中文标题")
            return
            
        # 创建问题目录
        # 如果problem_id是纯数字，则格式化为4位数字
        # 否则直接使用原始ID
        try:
            dir_name = f"{int(problem_id):04d}-{chinese_title}"
        except ValueError:
            dir_name = f"{problem_id}-{chinese_title}"
            
        problem_dir = os.path.join("problems", dir_name)
        os.makedirs(problem_dir, exist_ok=True)
        
        # 创建问题描述文件
        with open(os.path.join(problem_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {problem_id}. {detail['translatedTitle']}\n\n")
            f.write("## 题目描述\n\n")
            f.write(detail["translatedContent"] + "\n")
            f.write("\n## 难度\n\n")
            f.write(f"{detail['difficulty']}\n")
            
            if detail.get("topicTags"):
                f.write("\n## 标签\n\n")
                for tag in detail["topicTags"]:
                    f.write(f"- {tag['translatedName']}\n")
            
            if detail.get("hints"):
                f.write("\n## 提示\n\n")
                for i, hint in enumerate(detail["hints"], 1):
                    f.write(f"{i}. {hint}\n")
            
            if detail.get("exampleTestcases"):
                f.write("\n## 示例\n\n```\n")
                f.write(detail["exampleTestcases"])
                f.write("\n```\n")
            
            # 添加示例代码
            if detail.get("codeSnippets"):
                f.write("\n## 示例代码\n\n")
                for snippet in detail["codeSnippets"]:
                    f.write(f"### {snippet['lang']}\n\n")
                    f.write("```" + snippet['langSlug'] + "\n")
                    f.write(snippet['code'] + "\n")
                    f.write("```\n\n")
        
        # 创建测试用例文件
        test_cases = {
            "test_cases": []
        }
        
        # 添加示例测试用例
        if detail.get("exampleTestcases"):
            examples = detail["exampleTestcases"].split("\n")
            for example in examples:
                if example.strip():
                    test_cases["test_cases"].append({
                        "input": example.strip(),
                        "expected": ""
                    })
        
        with open(os.path.join(problem_dir, "test_cases.json"), "w", encoding="utf-8") as f:
            json.dump(test_cases, f, indent=4, ensure_ascii=False)
        
        print(f"成功创建问题 {problem_id} 的目录和文件")
    except Exception as e:
        print(f"创建问题目录时出错: {str(e)}")

def main():
    """主函数"""
    try:
        # 创建必要的目录
        os.makedirs("problems", exist_ok=True)
        
        # 获取问题列表
        print("正在获取LeetCode问题列表...")
        problems = fetch_problem_list()
        
        if not problems:
            print("无法获取问题列表，请检查网络连接或稍后重试")
            return
        
        # 处理所有题目
        print(f"找到 {len(problems)} 道题目，开始处理...")
        for i, problem in enumerate(problems, 1):
            print(f"正在处理第 {i} 道题目...")
            create_problem_directory(problem)
            time.sleep(random.uniform(1, 3))  # 随机延迟，避免请求过于频繁
        
        print("所有题目处理完成！")
    except Exception as e:
        print(f"程序执行出错: {str(e)}")

if __name__ == "__main__":
    main() 