package main

// Definition for singly-linked list.
// type ListNode struct {
//     Val int
//     Next *ListNode
// }

// 141. 环形链表
// Floyd 快慢指针：slow 每次走 1 步，fast 每次走 2 步。
// 有环的话 fast 会在环里一直绕，最终必然追上 slow（相对速度为 1，每轮距离缩小 1）；
// 无环的话 fast 会先走到链表尽头（nil）。时间 O(n)，空间 O(1)。
func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}
