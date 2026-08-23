class Solution:
    def numDecodings(self, s: str) -> int:
        """
        91. 解码方法
        动态规划：dp[i] 表示 s[:i] 的解码方法数。
        单字符有效（非 '0'）时可从 dp[i-1] 转移；
        双字符在 10~26 之间时可从 dp[i-2] 转移。
        用两个变量滚动即可，无需数组。
        """
        n = len(s)
        prev2, prev1 = 1, 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            cur = 0
            if s[i - 1] != '0':
                cur += prev1
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur
        return prev1


if __name__ == "__main__":
    test_cases = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]
    solution = Solution()
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.numDecodings(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (s={s!r}, got={result}, expected={expected})")
