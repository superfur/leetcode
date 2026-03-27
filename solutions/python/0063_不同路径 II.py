from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    """
    不同路径 II：m×n 网格中有障碍物(1表示)，从左上角到右下角的路径数。
    DP 一维：dp[j] = 0(有障碍) 或 dp[j] + dp[j-1](无障碍)。时间 O(mn)，空间 O(n)。
    """
    if not obstacle_grid or not obstacle_grid[0]:
        return 0

    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [0] * n

    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                dp[j] = 0
            elif j == 0:
                dp[j] = 1 if (i == 0 or dp[j] == 1) else 0
            else:
                dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


def 不同路径Ii(*args, **kwargs):
    """支持传入 obstacleGrid: List[List[int]]"""
    if args and len(args) >= 1:
        grid = args[0]
    elif "obstacleGrid" in kwargs:
        grid = kwargs["obstacleGrid"]
    else:
        return 0
    return unique_paths_with_obstacles(grid)


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        return unique_paths_with_obstacles(obstacle_grid)


if __name__ == "__main__":
    test_cases = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[1, 0]], 0),
        ([[0, 0], [0, 0]], 2),
    ]
    for i, (grid, expected) in enumerate(test_cases, 1):
        got = unique_paths_with_obstacles(grid)
        status = "通过" if got == expected else "失败"
        print(f"测试用例 {i}: {status} (期望={expected}, 实际={got})")
