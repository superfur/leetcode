// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

// 86. 分隔链表
// 两个哑头 + 两条尾链：small 串 < x 节点，large 串 >= x 节点，最后拼接。
func partition(head *ListNode, x int) *ListNode {
	sDummy := &ListNode{Val: 0}
	lDummy := &ListNode{Val: 0}
	s, l := sDummy, lDummy
	curr := head
	for curr != nil {
		nxt := curr.Next
		curr.Next = nil // 切断旧链
		if curr.Val < x {
			s.Next = curr
			s = curr
		} else {
			l.Next = curr
			l = curr
		}
		curr = nxt
	}
	s.Next = lDummy.Next
	return sDummy.Next
}