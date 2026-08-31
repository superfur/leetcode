package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 101. 对称二叉树
// 递归判断两棵子树是否互为镜像：值相同，且 t1 的左子树与 t2 的右子树
// 互为镜像、t1 的右子树与 t2 的左子树互为镜像。
func isSymmetric(root *TreeNode) bool {
	var isMirror func(t1, t2 *TreeNode) bool
	isMirror = func(t1, t2 *TreeNode) bool {
		if t1 == nil && t2 == nil {
			return true
		}
		if t1 == nil || t2 == nil {
			return false
		}
		if t1.Val != t2.Val {
			return false
		}
		return isMirror(t1.Left, t2.Right) && isMirror(t1.Right, t2.Left)
	}

	return root == nil || isMirror(root.Left, root.Right)
}
