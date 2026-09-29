from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        120. 三角形最小路径和
        自底向上一维滚动 DP：dp[j] 表示从当前行第 j 个位置走到底部的最小路径和。
        从倒数第二行开始，dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        （dp[j] 是正下方，dp[j+1] 是右下方，取较小的再加上当前值），
        一路滚动到第 0 行，dp[0] 就是答案。
        """
        dp = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


if __name__ == "__main__":
    test_cases = [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
    ]
    solution = Solution()
    for i, (triangle, expected) in enumerate(test_cases, 1):
        result = solution.minimumTotal(triangle)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (triangle={triangle}, got={result}, expected={expected})")
