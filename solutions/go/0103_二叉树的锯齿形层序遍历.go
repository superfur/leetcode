package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 103. 二叉树的锯齿形层序遍历
// 与普通层序遍历（BFS）相同，只是奇数层（从 0 计数的第 1、3、5... 层）
// 收集完之后把这一层的结果反转即可。
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	result := [][]int{}
	queue := []*TreeNode{root}
	leftToRight := true
	for len(queue) > 0 {
		size := len(queue)
		level := make([]int, 0, size)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			level = append(level, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if !leftToRight {
			for l, r := 0, len(level)-1; l < r; l, r = l+1, r-1 {
				level[l], level[r] = level[r], level[l]
			}
		}
		result = append(result, level)
		leftToRight = !leftToRight
	}
	return result
}
