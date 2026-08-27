class Solution:
    def numTrees(self, n: int) -> int:
        """
        96. 不同的二叉搜索树
        动态规划（卡特兰数）：dp[i] 表示 i 个节点能组成的 BST 数量。
        以 k 为根时，左子树用 k-1 个节点、右子树用 i-k 个节点，
        dp[i] = sum(dp[k-1] * dp[i-k]) for k in 1..i。
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for k in range(1, i + 1):
                dp[i] += dp[k - 1] * dp[i - k]
        return dp[n]


if __name__ == "__main__":
    test_cases = [
        (3, 5),
        (1, 1),
        (0, 1),
        (5, 42),
    ]
    solution = Solution()
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.numTrees(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (n={n}, got={result}, expected={expected})")
