package main

// Definition for singly-linked list.
// type ListNode struct {
//     Val int
//     Next *ListNode
// }

// 147. 对链表进行插入排序
// 用哨兵节点 dummy 作为已排序部分的前驱，tail 记录已排序部分的最后一个节点。
// 依次取出 cur = tail.Next：
//   - 若 tail.Val <= cur.Val，说明 cur 已经在正确位置，直接把 tail 后移（常见于已有序的输入，省去扫描）；
//   - 否则从 dummy 开始找到第一个「下一个节点值 > cur.Val」的位置 prev，把 cur 摘下来插到 prev 后面。
//
// 用 `<=` 找位置，相同值的节点保持原相对顺序（稳定）。
// 最坏时间 O(n^2)，空间 O(1)，只改 Next 指针。
func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	tail := head
	for tail.Next != nil {
		cur := tail.Next
		if tail.Val <= cur.Val {
			tail = cur
			continue
		}
		tail.Next = cur.Next
		prev := dummy
		for prev.Next.Val <= cur.Val {
			prev = prev.Next
		}
		cur.Next = prev.Next
		prev.Next = cur
	}
	return dummy.Next
}
