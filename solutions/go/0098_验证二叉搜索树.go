package main

import "math"

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 98. 验证二叉搜索树
// 区间递归：每个节点携带一个开区间 (low, high)，其值必须落在区间内；
// 向左递归时收紧上界为当前值，向右递归时收紧下界为当前值。
func isValidBST(root *TreeNode) bool {
	var validate func(node *TreeNode, low, high float64) bool
	validate = func(node *TreeNode, low, high float64) bool {
		if node == nil {
			return true
		}
		v := float64(node.Val)
		if !(v > low && v < high) {
			return false
		}
		return validate(node.Left, low, v) && validate(node.Right, v, high)
	}

	return validate(root, math.Inf(-1), math.Inf(1))
}
