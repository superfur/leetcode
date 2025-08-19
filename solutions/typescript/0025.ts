/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (!head || k === 1) return head;
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let current = head;
    while (current) {
        // 检查是否有足够的节点进行反转
        let tail = current;
        let count = 1;
        while (tail.next && count < k) {
            tail = tail.next;
            count++;
        }
        
        // 如果节点数量不足k个，直接返回
        if (count < k) break;
        
        const next = tail.next;
        tail.next = null;
        const [newHead, newTail] = reverse(current);
        prev.next = newHead;
        newTail.next = next;
        prev = newTail;
        current = next;
    }
    return dummy.next;
};

function reverse(head: ListNode | null): [ListNode | null, ListNode | null] {
    let prev = null;
    let current = head;
    while (current) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return [prev, head];
}