package main

import "math"

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 124. 二叉树中的最大路径和
// 后序递归：dfs(node) 返回「以 node 为起点、向下走的最大贡献值」
// （贡献为负就当作 0，即不选这条分支）；
// 同时把「左贡献 + 节点值 + 右贡献」当作以 node 为最高点的路径和，更新全局答案。
func maxPathSum(root *TreeNode) int {
	best := math.MinInt64

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := max(dfs(node.Left), 0)
		right := max(dfs(node.Right), 0)
		if node.Val+left+right > best {
			best = node.Val + left + right
		}
		return node.Val + max(left, right)
	}

	dfs(root)
	return best
}
