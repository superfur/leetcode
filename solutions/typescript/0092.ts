/**
 * 92. 反转链表 II
 * 一趟扫描：用哑头定位 left 前一个节点 prev，
 * 然后把 prev.next 之后的节点逐个摘下，头插到 prev 之后，
 * 重复 right - left 次即可完成 [left, right] 区间反转。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function reverseBetween(head: LNode | null, left: number, right: number): LNode | null {
    const dummy: LNode = { val: 0, next: head };
    let prev: LNode = dummy;
    for (let i = 0; i < left - 1; i++) {
        prev = prev.next as LNode;
    }
    let curr = prev.next as LNode;
    for (let i = 0; i < right - left; i++) {
        const nxt = curr.next as LNode;
        curr.next = nxt.next;
        nxt.next = prev.next;
        prev.next = nxt;
    }
    return dummy.next;
}

export default reverseBetween;
