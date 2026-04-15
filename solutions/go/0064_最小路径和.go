package main

func minPathSum(grid [][]int) int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return 0
    }
    m, n := len(grid), len(grid[0])
    dp := make([]int, n)
    dp[0] = grid[0][0]
    for j := 1; j < n; j++ {
        dp[j] = dp[j-1] + grid[0][j]
    }
    for i := 1; i < m; i++ {
        dp[0] += grid[i][0]
        for j := 1; j < n; j++ {
            if dp[j] < dp[j-1] {
                dp[j] = dp[j] + grid[i][j]
            } else {
                dp[j] = dp[j-1] + grid[i][j]
            }
        }
    }
    return dp[n-1]
}

func 最小路径和(grid [][]int) int {
    return minPathSum(grid)
}