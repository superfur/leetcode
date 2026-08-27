package main

// 96. 不同的二叉搜索树
// 动态规划（卡特兰数）：dp[i] 表示 i 个节点能组成的 BST 数量。
// 以 k 为根时，左子树用 k-1 个节点、右子树用 i-k 个节点，
// dp[i] = sum(dp[k-1] * dp[i-k]) for k in 1..i。
func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		for k := 1; k <= i; k++ {
			dp[i] += dp[k-1] * dp[i-k]
		}
	}
	return dp[n]
}
