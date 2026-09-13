package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 111. 二叉树的最小深度
// 最小深度要求到最近的“叶子节点”，所以只有一个子节点的节点
// 不能直接取 min(0, 子树深度)——必须沿着那个唯一的非空子节点继续走。
// 只有左右子节点都为空（真正的叶子）时深度才是 1。
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left == nil {
		return 1 + minDepth(root.Right)
	}
	if root.Right == nil {
		return 1 + minDepth(root.Left)
	}
	left := minDepth(root.Left)
	right := minDepth(root.Right)
	if left < right {
		return left + 1
	}
	return right + 1
}
