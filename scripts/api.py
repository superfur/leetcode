"""
LeetCode API 调用模块
支持 leetcode.com 和 leetcode.cn
"""
import requests
import time
import random
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from config import get_site_config, get_cookies


class LeetCodeSite(Enum):
    COM = "leetcode.com"
    CN = "leetcode.cn"


class LeetCodeAPI:
    """LeetCode API 封装"""

    def __init__(self, site: str = None):
        self.site = site or get_site_config().get("base_url", LeetCodeSite.COM.value)
        self.config = get_site_config(self.site)
        self.graphql_url = self.config.get("graphql_url", "")
        self.api_url = self.config.get("api_url", "")
        self.cookies = get_cookies(self.site)
        self.csrftoken = self.cookies.get("csrftoken", "")
        self.session = self.cookies.get("LEETCODE_SESSION", "")

        # 创建 session
        self.session_obj = requests.Session()
        self.session_obj.cookies.update(self.cookies)

    def _get_headers(self, referer: str = None) -> Dict:
        """获取请求头"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "x-csrftoken": self.csrftoken,
        }
        if referer:
            headers["Referer"] = referer
        return headers

    def is_logged_in(self) -> bool:
        """检查是否已登录"""
        if not self.csrftoken or not self.session:
            return False

        try:
            # 尝试访问用户信息
            query = """
            query userStatus {
                userStatus {
                    isSignedIn
                    username
                }
            }
            """
            response = self.session_obj.post(
                self.graphql_url,
                json={"query": query},
                headers=self._get_headers(f"{self.site}/")
            )
            data = response.json()
            return data.get("data", {}).get("userStatus", {}).get("isSignedIn", False)
        except Exception as e:
            print(f"检查登录状态失败: {e}")
            return False

    def fetch_problem_list(self) -> List[Dict]:
        """获取题目列表"""
        try:
            response = self.session_obj.get(self.api_url, headers=self._get_headers())
            if response.status_code == 200:
                data = response.json()
                return data.get("stat_status_pairs", [])
            else:
                print(f"获取题目列表失败: {response.status_code}")
                return []
        except Exception as e:
            print(f"获取题目列表出错: {e}")
            return []

    def fetch_problem_detail(self, title_slug: str) -> Optional[Dict]:
        """获取题目详情"""
        query = """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                titleSlug
                content
                difficulty
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                sampleTestCase
                exampleTestcases
                hints
                metaData
            }
        }
        """
        variables = {"titleSlug": title_slug}

        try:
            response = self.session_obj.post(
                self.graphql_url,
                json={"query": query, "variables": variables},
                headers=self._get_headers(f"{self.site}/problems/{title_slug}/")
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("question")
            return None
        except Exception as e:
            print(f"获取题目详情出错: {e}")
            return None

    def fetch_user_submissions(self, limit: int = 20) -> List[Dict]:
        """获取用户最近的提交记录"""
        query = """
        query recentSubmissionList($username: String!, $limit: Int!) {
            recentSubmissionList(username: $username, limit: $limit) {
                id
                title
                titleSlug
                status
                lang
                timestamp
            }
        }
        """
        user_info = self.get_user_info()
        username = user_info.get("username", "") if user_info else ""

        if not username:
            return []

        variables = {"username": username, "limit": limit}

        try:
            response = self.session_obj.post(
                self.graphql_url,
                json={"query": query, "variables": variables},
                headers=self._get_headers(f"{self.site}/")
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("recentSubmissionList", [])
            return []
        except Exception as e:
            print(f"获取提交记录出错: {e}")
            return []

    def get_user_info(self) -> Dict:
        """获取用户信息"""
        query = """
        query userStatus {
            userStatus {
                isSignedIn
                username
                realName
                avatar
                totalSolved
                totalQuestions
                easySolved
                mediumSolved
                hardSolved
            }
        }
        """
        try:
            response = self.session_obj.post(
                self.graphql_url,
                json={"query": query},
                headers=self._get_headers(f"{self.site}/")
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("userStatus", {})
            return {}
        except Exception as e:
            print(f"获取用户信息出错: {e}")
            return {}

    def submit_solution(self, title_slug: str, lang: str, code: str) -> Optional[Dict]:
        """提交代码"""
        submit_url = self.config.get("submit_url", "").format(slug=title_slug)

        data = {
            "question_id": "",  # LeetCode 会自动填充
            "lang": lang,
            "code": code,
            "test_mode": False,
            "test_case": "",
        }

        try:
            response = self.session_obj.post(
                submit_url,
                json=data,
                headers=self._get_headers(f"{self.site}/problems/{title_slug}/")
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"提交失败: {response.status_code}")
                return None
        except Exception as e:
            print(f"提交出错: {e}")
            return None

    def check_submission(self, submission_id: str) -> Optional[Dict]:
        """检查提交结果"""
        check_url = self.config.get("check_url", "").format(submission_id=submission_id)

        try:
            response = self.session_obj.get(
                check_url,
                headers=self._get_headers(f"{self.site}/submissions/")
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"检查提交结果出错: {e}")
            return None

    def run_test(self, title_slug: str, lang: str, code: str, test_case: str) -> Optional[Dict]:
        """运行测试（不计入提交）"""
        submit_url = self.config.get("submit_url", "").format(slug=title_slug)

        data = {
            "question_id": "",
            "lang": lang,
            "code": code,
            "test_mode": True,
            "test_case": test_case,
        }

        try:
            response = self.session_obj.post(
                submit_url,
                json=data,
                headers=self._get_headers(f"{self.site}/problems/{title_slug}/")
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"运行测试出错: {e}")
            return None


def wait_for_result(submission_id: str, api: LeetCodeAPI, max_wait: int = 60) -> Optional[Dict]:
    """等待提交结果"""
    start_time = time.time()
    while time.time() - start_time < max_wait:
        result = api.check_submission(submission_id)
        if result:
            state = result.get("state", "")
            if state in ["SUCCESS", "FAILURE"]:
                return result
        time.sleep(1)
    return None
