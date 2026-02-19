package main

/*
 * 旋转链表（LeetCode 61）
 *
 * type ListNode struct { Val int; Next *ListNode }
 *
 * 将链表向右旋转 k 个位置。等价于把最后 k 个节点移到头部。
 *
 * 时间复杂度: O(n)
 * 空间复杂度: O(1)
 *
 * 思路:
 * 1. 求链表长度 n，k = k % n，若 k==0 直接返回 head
 * 2. 快指针先走 k 步，然后快慢指针一起走，直到快指针到最后一个节点
 *    此时慢指针指向新链表的尾节点，慢指针.Next 为新头
 * 3. 原尾.Next = head，新尾.Next = nil，返回新头
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil || k == 0 {
        return head
    }

    n := 1
    tail := head
    for tail.Next != nil {
        tail = tail.Next
        n++
    }
    k = k % n
    if k == 0 {
        return head
    }

    slow, fast := head, head
    for i := 0; i < k; i++ {
        fast = fast.Next
    }
    for fast.Next != nil {
        slow = slow.Next
        fast = fast.Next
    }

    newHead := slow.Next
    slow.Next = nil
    tail.Next = head
    return newHead
}
