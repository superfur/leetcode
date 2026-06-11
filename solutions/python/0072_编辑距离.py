class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]


if __name__ == "__main__":
    test_cases = [
        {"word1": "horse", "word2": "ros", "expected": 3},
        {"word1": "intention", "word2": "execution", "expected": 5},
        {"word1": "", "word2": "", "expected": 0},
        {"word1": "", "word2": "abc", "expected": 3},
        {"word1": "abc", "word2": "", "expected": 3},
        {"word1": "a", "word2": "b", "expected": 1},
        {"word1": "abc", "word2": "abc", "expected": 0},
    ]
    for i, tc in enumerate(test_cases, 1):
        result = Solution().minDistance(tc["word1"], tc["word2"])
        status = "PASS" if result == tc["expected"] else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={tc['expected']})")
