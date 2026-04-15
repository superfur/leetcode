from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    最小路径和：m×n 网格，从左上角到右下角的最小路径和（只能向右或向下）。
    DP 一维：dp[j] = min(dp[j], dp[j-1]) + grid[i][j]。时间 O(mn)，空间 O(n)。
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[n - 1]


def 最小路径和(*args, **kwargs):
    """支持传入 grid: List[List[int]]"""
    if args and len(args) >= 1:
        grid = args[0]
    elif "grid" in kwargs:
        grid = kwargs["grid"]
    else:
        return 0
    return min_path_sum(grid)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return min_path_sum(grid)


if __name__ == "__main__":
    test_cases = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
        ([[1]], 1),
        ([[0, 1], [1, 0]], 1),
    ]
    for i, (grid, expected) in enumerate(test_cases, 1):
        got = min_path_sum(grid)
        status = "通过" if got == expected else "失败"
        print(f"测试用例 {i}: {status} (期望={expected}, 实际={got})")