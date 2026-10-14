package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 129. 求根节点到叶节点数字之和
// DFS 往下传「根到当前节点已经拼出的数字」（cur * 10 + val），
// 走到叶子节点时这个数字就是一条完整路径代表的数，累加进答案。
func sumNumbers(root *TreeNode) int {
	var dfs func(node *TreeNode, cur int) int
	dfs = func(node *TreeNode, cur int) int {
		if node == nil {
			return 0
		}
		cur = cur*10 + node.Val
		if node.Left == nil && node.Right == nil {
			return cur
		}
		return dfs(node.Left, cur) + dfs(node.Right, cur)
	}
	return dfs(root, 0)
}
