/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    dummy := &ListNode{0, head}
    prev := dummy
    current := head
    for current != nil && current.Next != nil {
        next := current.Next
        current.Next = next.Next
        next.Next = current
        prev.Next = next
        prev = current
        current = current.Next
    }
    return dummy.Next
 }