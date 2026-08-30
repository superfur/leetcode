package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 99. 恢复二叉搜索树
// 中序遍历（迭代，栈）应严格递增；用 prev 记录上一个访问节点，
// 每次出现 prev.Val > cur.Val 就是一次“逆序对”：
// 第一次出现记录 (prev, cur) 为 first/second 候选；
// 若又出现第二次逆序（两个交换节点不相邻），把 second 更新为这次的 cur。
// 最后交换 first 和 second 的值即可恢复。
func recoverTree(root *TreeNode) {
	var stack []*TreeNode
	var prev, first, second *TreeNode
	node := root

	for node != nil || len(stack) > 0 {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
		node = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if prev != nil && prev.Val > node.Val {
			if first == nil {
				first = prev
			}
			second = node
		}
		prev = node
		node = node.Right
	}

	if first != nil && second != nil {
		first.Val, second.Val = second.Val, first.Val
	}
}
