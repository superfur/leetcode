package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 144. 二叉树的前序遍历
// 迭代 + 显式栈：弹出节点就记录它的值（根），再先压右孩子、后压左孩子，
// 这样下一次弹出的就是左孩子，顺序为 根 → 左 → 右。
// 不依赖递归深度，时间 O(n)，空间 O(h)。
func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, node.Val)
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
	}
	return res
}
