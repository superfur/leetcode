from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        131. 分割回文串
        先用区间 DP 预处理 is_pal[i][j]（s[i..j] 是否回文），
        再回溯：从位置 start 开始，枚举每个能切出回文前缀 s[start..end] 的位置，
        选中后递归处理 end + 1，走到字符串末尾就收集一个方案。
        """
        n = len(s)
        is_pal = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]

        res: List[List[str]] = []
        path: List[str] = []

        def back(start: int) -> None:
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    back(end + 1)
                    path.pop()

        back(0)
        return res


if __name__ == "__main__":
    test_cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("ab", [["a", "b"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
        ("abba", [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]),
        ("abc", [["a", "b", "c"]]),
    ]
    solution = Solution()
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.partition(s)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (s={s!r}, got={result}, expected={expected})")

    count = len(solution.partition("a" * 16))
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if count == 2 ** 15 else 'FAIL'} (16 个 a，方案数={count}，期望 {2 ** 15})")
