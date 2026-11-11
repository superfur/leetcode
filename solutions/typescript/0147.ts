/**
 * 147. 对链表进行插入排序
 * 用哨兵节点 dummy 作为已排序部分的前驱，tail 记录已排序部分的最后一个节点。
 * 依次取出 cur = tail.next：
 * - 若 tail.val <= cur.val，说明 cur 已经在正确位置，直接把 tail 后移（常见于已有序的输入，省去扫描）；
 * - 否则从 dummy 开始找到第一个「下一个节点值 > cur.val」的位置 prev，把 cur 摘下来插到 prev 后面。
 * 用 `<=` 找位置，相同值的节点保持原相对顺序（稳定）。
 * 最坏时间 O(n^2)，空间 O(1)，只改 next 指针。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function insertionSortList(head: LNode | null): LNode | null {
    if (!head) return head;
    const dummy: LNode = { val: 0, next: head };
    let tail: LNode = head;
    while (tail.next) {
        const cur: LNode = tail.next;
        if (tail.val <= cur.val) {
            tail = cur;
            continue;
        }
        tail.next = cur.next;
        let prev: LNode = dummy;
        while (prev.next!.val <= cur.val) {
            prev = prev.next!;
        }
        cur.next = prev.next;
        prev.next = cur;
    }
    return dummy.next;
}

export default insertionSortList;
