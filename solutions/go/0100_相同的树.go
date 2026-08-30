package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 100. 相同的树
// 递归：两个节点同时为空则相同；一空一非空或值不同则不同；
// 否则要求左子树和右子树都分别相同。
func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
