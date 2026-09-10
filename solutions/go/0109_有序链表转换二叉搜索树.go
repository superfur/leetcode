package main

// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// 109. 有序链表转换二叉搜索树
// 先把链表一次性摊平成数组（O(n)），之后就是 108 题的做法：
// 取区间中点为根递归划分左右子树，天然保证高度平衡。
func sortedListToBST(head *ListNode) *TreeNode {
	values := []int{}
	for node := head; node != nil; node = node.Next {
		values = append(values, node.Val)
	}

	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		mid := (left + right) / 2
		root := &TreeNode{Val: values[mid]}
		root.Left = build(left, mid-1)
		root.Right = build(mid+1, right)
		return root
	}

	return build(0, len(values)-1)
}
