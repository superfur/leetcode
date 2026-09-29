package main

// 120. 三角形最小路径和
// 自底向上一维滚动 DP：dp[j] 表示从当前行第 j 个位置走到底部的最小路径和。
// 从倒数第二行开始，dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
// （dp[j] 是正下方，dp[j+1] 是右下方，取较小的再加上当前值），
// 一路滚动到第 0 行，dp[0] 就是答案。
func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	dp := make([]int, len(triangle[n-1]))
	copy(dp, triangle[n-1])
	for i := n - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			next := dp[j]
			if dp[j+1] < next {
				next = dp[j+1]
			}
			dp[j] = triangle[i][j] + next
		}
	}
	return dp[0]
}
