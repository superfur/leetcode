package main

// 82. 删除排序链表中的重复元素 II
// 删除所有出现重复的数字节点，只保留出现一次的。
// 哨兵 + 双指针：若 curr.Val == curr.Next.Val 则一路跳过所有该值的节点；
// 否则 prev 前进一位。
// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func deleteDuplicates(head *ListNode) *ListNode {
	sentinel := &ListNode{Val: 0, Next: head}
	prev := sentinel
	curr := head
	for curr != nil {
		if curr.Next != nil && curr.Val == curr.Next.Val {
			dup := curr.Val
			for curr != nil && curr.Val == dup {
				curr = curr.Next
			}
			prev.Next = curr
		} else {
			prev = curr
			curr = curr.Next
		}
	}
	return sentinel.Next
}