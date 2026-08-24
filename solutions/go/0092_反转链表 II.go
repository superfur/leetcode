// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

// 92. 反转链表 II
// 一趟扫描：用哑头定位 left 前一个节点 prev，
// 然后把 prev.Next 之后的节点逐个摘下，头插到 prev 之后，
// 重复 right - left 次即可完成 [left, right] 区间反转。
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	dummy := &ListNode{Val: 0, Next: head}
	prev := dummy
	for i := 0; i < left-1; i++ {
		prev = prev.Next
	}
	curr := prev.Next
	for i := 0; i < right-left; i++ {
		nxt := curr.Next
		curr.Next = nxt.Next
		nxt.Next = prev.Next
		prev.Next = nxt
	}
	return dummy.Next
}
