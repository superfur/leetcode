/**
 * 142. 环形链表 II
 * Floyd 快慢指针分两阶段：
 * 1. slow 走 1 步、fast 走 2 步，若相遇说明有环；若 fast 走到尽头则无环。
 * 2. 设头到入环点 a 步，入环点到相遇点 b 步，环长 c。相遇时 fast 比 slow 多走整数圈：
 *    2(a+b) = a+b+k·c，即 a = (k-1)·c + (c-b)。
 *    所以让一个指针从头出发、另一个从相遇点出发，各走 1 步，必在入环点相遇。
 * 时间 O(n)，空间 O(1)，不修改链表。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function detectCycle(head: LNode | null): LNode | null {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
        if (slow === fast) {
            let ptr = head;
            while (ptr !== slow) {
                ptr = ptr!.next;
                slow = slow!.next;
            }
            return ptr;
        }
    }
    return null;
}

export default detectCycle;
