package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 145. 二叉树的后序遍历
// 后序是 左 → 右 → 根，它的逆序恰好是 根 → 右 → 左，
// 而后者就是前序遍历把左右孩子的入栈顺序对调（先压左、后压右）。
// 所以用显式栈按 根 → 右 → 左 收集值，最后整体反转即可。
// 不依赖递归深度，时间 O(n)，空间 O(h)（结果数组除外）。
func postorderTraversal(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, node.Val)
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}
