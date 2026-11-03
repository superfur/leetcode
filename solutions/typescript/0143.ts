/**
 * 143. 重排链表
 * 三步走：
 * 1. 快慢指针找中点（偶数长度时 slow 停在前半段最后一个节点），把链表断成前后两半；
 * 2. 反转后半段；
 * 3. 前半段与反转后的后半段交替拼接。
 * 时间 O(n)，空间 O(1)，只改 next 指针不改节点值。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

/**
 Do not return anything, modify it in-place instead.
 */
function reorderList(head: LNode | null): void {
    if (!head || !head.next) return;
    let slow: LNode = head;
    let fast: LNode = head;
    while (fast.next && fast.next.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }
    let second: LNode | null = slow.next;
    slow.next = null;

    let prev: LNode | null = null;
    while (second) {
        const next: LNode | null = second.next;
        second.next = prev;
        prev = second;
        second = next;
    }
    second = prev;

    let first: LNode | null = head;
    while (second) {
        const firstNext: LNode | null = first!.next;
        const secondNext: LNode | null = second.next;
        first!.next = second;
        second.next = firstNext;
        first = firstNext;
        second = secondNext;
    }
}

export default reorderList;
