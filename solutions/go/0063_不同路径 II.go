package main

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	/*
	 * 不同路径 II：m×n 网格中有障碍物(1表示)，从左上角到右下角的路径数。
	 * DP 一维：dp[j] = 0(有障碍) 或 dp[j] + dp[j-1](无障碍)。时间 O(mn)，空间 O(n)。
	 */
	if len(obstacleGrid) == 0 || len(obstacleGrid[0]) == 0 {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])
	dp := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[j] = 0
			} else if j == 0 {
				if i == 0 || dp[j] == 1 {
					dp[j] = 1
				} else {
					dp[j] = 0
				}
			} else {
				dp[j] = dp[j] + dp[j-1]
			}
		}
	}

	return dp[n-1]
}

func 不同路径Ii(...args interface{}) interface{} {
	grid := args[0].([][]int)
	return uniquePathsWithObstacles(grid)
}

func main() {
	// 测试用例
	println("不同路径 II")
}
