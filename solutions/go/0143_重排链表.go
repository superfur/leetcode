package main

// Definition for singly-linked list.
// type ListNode struct {
//     Val int
//     Next *ListNode
// }

// 143. 重排链表
// 三步走：
// 1. 快慢指针找中点（偶数长度时 slow 停在前半段最后一个节点），把链表断成前后两半；
// 2. 反转后半段；
// 3. 前半段与反转后的后半段交替拼接。
// 时间 O(n)，空间 O(1)，只改 Next 指针不改节点值。
func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	second := slow.Next
	slow.Next = nil

	var prev *ListNode
	for second != nil {
		next := second.Next
		second.Next = prev
		prev = second
		second = next
	}
	second = prev

	first := head
	for second != nil {
		firstNext, secondNext := first.Next, second.Next
		first.Next = second
		second.Next = firstNext
		first, second = firstNext, secondNext
	}
}
