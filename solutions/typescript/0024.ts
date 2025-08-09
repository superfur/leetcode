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

function swapPairs(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let current = head;
    while (current && current.next) {
        const next = current.next;
        current.next = next.next;
        next.next = current;
        prev.next = next;
        prev = current;
        current = current.next;
    }
    return dummy.next;
};