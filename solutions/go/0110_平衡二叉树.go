package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 110. 平衡二叉树
// 自底向上后序遍历，一趟同时算高度和判平衡：
// 用 -1 作为“已经不平衡”的哨兵值向上传播，一旦子树出现
// 不平衡或左右高度差超过 1，就不再继续计算，直接短路返回。
func isBalanced(root *TreeNode) bool {
	var height func(node *TreeNode) int
	height = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := height(node.Left)
		if left == -1 {
			return -1
		}
		right := height(node.Right)
		diff := left - right
		if right == -1 || diff > 1 || diff < -1 {
			return -1
		}
		if left > right {
			return left + 1
		}
		return right + 1
	}

	return height(root) != -1
}
