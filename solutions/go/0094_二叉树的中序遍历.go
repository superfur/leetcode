package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 94. 二叉树的中序遍历
// 迭代：用栈模拟递归——一路把左子树压栈到底，
// 弹出访问后转向右子树，重复直到栈空且当前节点为空。
func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	stack := []*TreeNode{}
	node := root
	for node != nil || len(stack) > 0 {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
		node = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, node.Val)
		node = node.Right
	}
	return result
}
