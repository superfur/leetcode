class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        97. 交错字符串
        一维滚动 DP：dp[j] 表示 s3 的前 i+j 个字符能否由
        s1 的前 i 个字符和 s2 的前 j 个字符交错组成（i 随外层循环推进）。
        长度不匹配直接返回 False。
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("abc", "def", "abcdefx", False),
    ]
    solution = Solution()
    for i, (s1, s2, s3, expected) in enumerate(test_cases, 1):
        result = solution.isInterleave(s1, s2, s3)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (s1={s1!r}, s2={s2!r}, s3={s3!r}, got={result}, expected={expected})")
