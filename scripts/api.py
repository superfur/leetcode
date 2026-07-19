"""
LeetCode API 调用模块
支持 leetcode.com 和 leetcode.cn

注意: leetcode.cn 由阿里云 WAF 保护，会拦截非浏览器请求。
本模块优先使用 curl_cffi（模拟 Chrome 的 TLS/指纹）绕过 WAF；
若未安装 curl_cffi 则回退到标准 requests（此时 leetcode.cn 的 API 会被拦截）。
"""
import time
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent))

# 优先 curl_cffi（模拟浏览器 TLS/指纹，绕过 leetcode.cn 的阿里云 WAF）
try:
    from curl_cffi import requests
    _HAS_CURL_CFFI = True
except ImportError:
    import requests
    _HAS_CURL_CFFI = False

from config import get_site_config, get_cookies, get_all_cookies, load_config

# Windows 控制台编码兼容
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


class LeetCodeSite(Enum):
    COM = "leetcode.com"
    CN = "leetcode.cn"


class LeetCodeAPI:
    """LeetCode API 封装"""

    # leetcode.cn 与 leetcode.com 的语言 slug 映射存在差异
    # 参考: https://leetcode.cn 与 https://leetcode.com 的代码提交 lang 字段
    LANG_MAP = {
        "leetcode.cn": {
            "python": "python3",
            "typescript": "typescript",
            "go": "golang",
            "rust": "rust",
            "java": "java",
        },
        "leetcode.com": {
            "python": "python3",
            "typescript": "typescript",
            "go": "go",
            "rust": "rust",
            "java": "java",
        },
    }

    def __init__(self, site: str = None):
        # site 形如 "leetcode.cn" / "leetcode.com"；为 None 时取默认站点
        self.site = site or load_config().get("default_site", "leetcode.cn")
        self.config = get_site_config(self.site)
        self.base_url = self.config.get("base_url", f"https://{self.site}")
        self.graphql_url = self.config.get("graphql_url", f"{self.base_url}/graphql")
        self.api_url = self.config.get("api_url", f"{self.base_url}/api/problems/all/")

        # 用全部浏览器 cookie（含 WAF 验证 cookie 如 aliyungf_tc）
        all_cookies = get_all_cookies(self.site)
        self.cookies = all_cookies
        self.csrftoken = all_cookies.get("csrftoken", "")
        self.session = all_cookies.get("LEETCODE_SESSION", "")

        # 创建 session；curl_cffi 模拟 chrome 指纹以绕过 WAF
        if _HAS_CURL_CFFI:
            self.session_obj = requests.Session(impersonate="chrome")
        else:
            if self.site == "leetcode.cn":
                print("[!] 警告: 未安装 curl_cffi，leetcode.cn 的请求会被阿里云 WAF 拦截。")
                print("    请运行: pip install curl_cffi")
            self.session_obj = requests.Session()
        self.session_obj.cookies.update(all_cookies)

    def _map_lang(self, lang: str) -> str:
        """把通用语言名 (python/go/...) 映射为对应站点的 lang slug。"""
        return self.LANG_MAP.get(self.site, {}).get(lang, lang)

    def _get_headers(self, referer: str = None) -> Dict:
        """获取请求头。

        重要: 使用 curl_cffi (impersonate="chrome") 时，不能手动设置
        User-Agent / Accept —— 否则会覆盖 impersonate 伪造的浏览器指纹，
        导致 TLS 指纹与 UA 不一致，被阿里云 WAF 识破拦截。
        """
        headers = {
            "Content-Type": "application/json",
            "Origin": self.base_url,
            "Referer": referer or f"{self.base_url}/",
            "x-csrftoken": self.csrftoken,
        }
        if not _HAS_CURL_CFFI:
            # 回退到标准 requests 时（无 impersonate），需手动设 UA
            headers["User-Agent"] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/120.0.0.0 Safari/537.36")
            headers["Accept"] = "application/json, text/plain, */*"
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
                headers=self._get_headers(f"{self.base_url}/")
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
                headers=self._get_headers(f"{self.base_url}/problems/{title_slug}/")
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
                headers=self._get_headers(f"{self.base_url}/")
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("recentSubmissionList", [])
            return []
        except Exception as e:
            print(f"获取提交记录出错: {e}")
            return []

    def get_user_info(self) -> Dict:
        """获取用户信息（含解题统计）。

        leetcode.cn 的 userStatus 没有 totalSolved/easySolved 等字段，
        需要用 userProfileUserQuestionProgress 单独查；leetcode.com 则一次拿到。
        """
        if self.site == "leetcode.cn":
            return self._get_user_info_cn()
        return self._get_user_info_com()

    def _get_user_info_cn(self) -> Dict:
        query = """
        query userStatus {
            userStatus { isSignedIn username realName avatar }
        }
        """
        try:
            response = self.session_obj.post(
                self.graphql_url,
                json={"query": query},
                headers=self._get_headers(f"{self.base_url}/")
            )
            if response.status_code != 200:
                return {}
            data = response.json().get("data", {}).get("userStatus", {})
        except Exception as e:
            print(f"获取用户信息出错: {e}")
            return {}

        username = data.get("username", "")
        if username:
            progress = self._fetch_progress_cn(username)
            if progress:
                data.update(progress)
        return data

    def _fetch_progress_cn(self, username: str) -> Dict:
        """leetcode.cn 解题统计：userProfileUserQuestionProgress(userSlug:)"""
        query = """
        query progress($s: String!) {
            userProfileUserQuestionProgress(userSlug: $s) {
                numAcceptedQuestions { difficulty count }
                numUntouchedQuestions { difficulty count }
            }
        }
        """
        try:
            r = self.session_obj.post(
                self.graphql_url,
                json={"query": query, "variables": {"s": username}},
                headers=self._get_headers(f"{self.base_url}/"),
            )
            if r.status_code != 200:
                return {}
            prog = r.json().get("data", {}).get("userProfileUserQuestionProgress", {})
            acc = {it["difficulty"]: it["count"] for it in prog.get("numAcceptedQuestions", [])}
            unt = {it["difficulty"]: it["count"] for it in prog.get("numUntouchedQuestions", [])}
            easy = acc.get("EASY", 0)
            medium = acc.get("MEDIUM", 0)
            hard = acc.get("HARD", 0)
            easy_total = easy + unt.get("EASY", 0)
            medium_total = medium + unt.get("MEDIUM", 0)
            hard_total = hard + unt.get("HARD", 0)
            return {
                "easySolved": easy,
                "mediumSolved": medium,
                "hardSolved": hard,
                "totalSolved": easy + medium + hard,
                "easyTotal": easy_total,
                "mediumTotal": medium_total,
                "hardTotal": hard_total,
                "totalQuestions": easy_total + medium_total + hard_total,
            }
        except Exception as e:
            print(f"获取解题统计出错: {e}")
            return {}

    def _get_user_info_com(self) -> Dict:
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
                headers=self._get_headers(f"{self.base_url}/")
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("userStatus", {})
            return {}
        except Exception as e:
            print(f"获取用户信息出错: {e}")
            return {}

    def get_slug_by_id(self, problem_id) -> Optional[str]:
        """通过题号查英文 title_slug。

        本地 problems/ 目录用中文名 (如 0001-两数之和)，但 leetcode API 需要英文 slug
        (如 two-sum)。这里拉取一次题目列表建立映射并缓存到实例上。
        """
        if not hasattr(self, "_slug_map"):
            problems = self.fetch_problem_list()
            self._slug_map = {
                str(p.get("stat", {}).get("frontend_question_id", "")):
                    p.get("stat", {}).get("question__title_slug", "")
                for p in problems
            }
        return self._slug_map.get(str(problem_id))

    def _get_question_id(self, title_slug: str) -> Optional[str]:
        """通过题目 slug 获取真实 questionId。

        leetcode.cn 的提交接口要求 question_id 必须是真实数字，
        不能像原来那样传空字符串。
        """
        detail = self.fetch_problem_detail(title_slug)
        if not detail:
            return None
        return detail.get("questionId") or detail.get("question_id")

    def submit_solution(self, title_slug: str, lang: str, code: str) -> Optional[Dict]:
        """提交代码（会计入提交记录）"""
        submit_url = self.config.get("submit_url", "").format(slug=title_slug)
        if not submit_url:
            submit_url = f"{self.base_url}/problems/{title_slug}/submit/"

        question_id = self._get_question_id(title_slug)
        if not question_id:
            print(f"[!] 无法获取 questionId，无法提交。请确认题目 slug: {title_slug}")
            return None

        lang_slug = self._map_lang(lang)
        data = self._build_submission_payload(
            question_id=question_id,
            lang_slug=lang_slug,
            code=code,
            test_case="",
            test_mode=False,
        )

        try:
            response = self.session_obj.post(
                submit_url,
                json=data,
                headers=self._get_headers(f"{self.base_url}/problems/{title_slug}/")
            )
            if response.status_code == 200:
                return response.json()
            print(f"[!] 提交失败: HTTP {response.status_code}")
            try:
                print(f"    响应: {response.text[:300]}")
            except Exception:
                pass
            return None
        except Exception as e:
            print(f"[!] 提交出错: {e}")
            return None

    def _build_submission_payload(self, question_id, lang_slug, code, test_case, test_mode):
        """构造提交/测试请求体。leetcode.cn 与 leetcode.com 字段名不同。"""
        if self.site == "leetcode.cn":
            # leetcode.cn 字段: typed_code / data_input / judge_type
            return {
                "question_id": question_id,
                "lang": lang_slug,
                "typed_code": code,
                "data_input": test_case or "",
                "judge_type": "small",
                "test_mode": test_mode,
            }
        # leetcode.com 字段: code / test_case
        return {
            "question_id": question_id,
            "lang": lang_slug,
            "code": code,
            "test_case": test_case or "",
            "test_mode": test_mode,
        }

    def check_submission(self, submission_id) -> Optional[Dict]:
        """查询提交结果。

        用 REST /submissions/detail/{id}/check/ —— 实测它返回最完整的字段
        (status_code / status_runtime / memory / compare_result 等)。
        判题完成时返回 status_code(10=AC, 11=WA, 13=TLE, 14=RE ...)；
        判题中时返回 {"state": "PENDING"}。
        """
        check_url = self.config.get("check_url", "").format(submission_id=submission_id)
        if not check_url:
            check_url = f"{self.base_url}/submissions/detail/{submission_id}/check/"
        try:
            response = self.session_obj.get(
                check_url,
                headers=self._get_headers(f"{self.base_url}/submissions/")
            )
            if response.status_code == 200:
                return self._normalize_submission(response.json())
            return None
        except Exception as e:
            print(f"[!] 检查提交结果出错: {e}")
            return None

    def _normalize_submission(self, data: Dict) -> Dict:
        """规范化 REST check 响应。"""
        status_code = data.get("status_code")
        if status_code is not None:
            return {
                "state": "SUCCESS",
                "status_code": status_code,
                "total_correct": data.get("total_correct"),
                "total_testcase": data.get("total_testcase"),
                "status_runtime": data.get("status_runtime"),
                "status_memory": data.get("status_memory"),
                "error": (data.get("compile_error") or data.get("full_compile_error")
                          or data.get("runtime_error")),
            }
        # 未完成
        state = data.get("state", "")
        return {"state": state or "PENDING", "status_code": None}

    def run_test(self, title_slug: str, lang: str, code: str, test_case: str) -> Optional[Dict]:
        """运行测试（不计入提交记录）"""
        submit_url = self.config.get("submit_url", "").format(slug=title_slug)
        if not submit_url:
            submit_url = f"{self.base_url}/problems/{title_slug}/submit/"

        question_id = self._get_question_id(title_slug)
        if not question_id:
            print(f"[!] 无法获取 questionId，无法测试。请确认题目 slug: {title_slug}")
            return None

        lang_slug = self._map_lang(lang)
        data = self._build_submission_payload(
            question_id=question_id,
            lang_slug=lang_slug,
            code=code,
            test_case=test_case or "",
            test_mode=True,
        )

        try:
            response = self.session_obj.post(
                submit_url,
                json=data,
                headers=self._get_headers(f"{self.base_url}/problems/{title_slug}/")
            )
            if response.status_code == 200:
                return response.json()
            print(f"[!] 远程测试失败: HTTP {response.status_code}")
            try:
                print(f"    响应: {response.text[:300]}")
            except Exception:
                pass
            return None
        except Exception as e:
            print(f"[!] 远程测试出错: {e}")
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
