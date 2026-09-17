package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 112. 路径总和
// 递归：空树直接不存在路径；到达叶子节点时判断剩余目标值
// 是否正好等于该叶子的值；否则把目标值减去当前节点值，
// 分别在左右子树里继续找。
func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}
	remaining := targetSum - root.Val
	return hasPathSum(root.Left, remaining) || hasPathSum(root.Right, remaining)
}
