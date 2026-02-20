/**
 * 旋转链表：将链表向右旋转 k 个位置。O(n) 时间，O(1) 空间。
 * ListNode 由 LeetCode 环境提供。
 */
function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (!head || !head.next || k === 0) return head;

    let n = 1;
    let tail: ListNode = head;
    while (tail.next) {
        tail = tail.next;
        n++;
    }
    k = k % n;
    if (k === 0) return head;

    let slow: ListNode = head;
    let fast: ListNode = head;
    for (let i = 0; i < k; i++) fast = fast.next!;
    while (fast.next) {
        slow = slow.next!;
        fast = fast.next!;
    }

    const newHead = slow.next;
    slow.next = null;
    tail.next = head;
    return newHead;
}

function 旋转链表(...args: any[]): any {
    const head = args[0] as ListNode | null;
    const k = args[1] as number;
    return rotateRight(head, k);
}

export default 旋转链表;
