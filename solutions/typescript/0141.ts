/**
 * 141. 环形链表
 * Floyd 快慢指针：slow 每次走 1 步，fast 每次走 2 步。
 * 有环的话 fast 会在环里一直绕，最终必然追上 slow（相对速度为 1，每轮距离缩小 1）；
 * 无环的话 fast 会先走到链表尽头（null）。时间 O(n)，空间 O(1)。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function hasCycle(head: LNode | null): boolean {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}

export default hasCycle;
