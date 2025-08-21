/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseKGroup(head *ListNode, k int) *ListNode {
    if head == nil || k == 1 {
        return head
    }
    dummy := &ListNode{0, head}
    prev := dummy
    current := head
    for current != nil {
        tail := current
        count := 0
        for tail != nil && count < k {
            tail = tail.Next
            count++
        }
        if count == k {
            newHead, newTail := reverse(current, tail)
            prev.Next = newHead
            prev = newTail
            current = tail
        } else {
            prev.Next = current
            break
        }
    }
    return dummy.Next
}

func reverse(head *ListNode, tail *ListNode) (*ListNode, *ListNode) {
    var prev *ListNode
    current := head
    for current != tail {
        next := current.Next
        current.Next = prev
        prev = current
        current = next
    }
    return prev, head
 }