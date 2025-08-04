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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const result: number[] = [];
    for (const list of lists) {
        let current = list;
        while (current) {
            result.push(current.val);
            current = current.next;
        }
    }
    result.sort((a, b) => a - b);
    const dummy = new ListNode();
    let current = dummy;
    for (const val of result) {
        current.next = new ListNode(val);
        current = current.next;
    }
    return dummy.next;
};