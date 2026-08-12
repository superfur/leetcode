/**
 * 86. 分隔链表
 * 给定链表头 head 和 x，将所有小于 x 的节点排在 >= x 的节点之前，
 * 保留各分区节点的初始相对位置。
 * 两个哑头 + 两条尾链：small 串 < x 节点，large 串 >= x 节点，最后拼接。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function partition(head: LNode | null, x: number): LNode | null {
    const sDummy: LNode = { val: 0, next: null };
    const lDummy: LNode = { val: 0, next: null };
    let s: LNode = sDummy;
    let l: LNode = lDummy;
    let curr: LNode | null = head;
    while (curr) {
        const nxt = curr.next;
        curr.next = null; // 切断旧链
        if (curr.val < x) {
            s.next = curr;
            s = curr;
        } else {
            l.next = curr;
            l = curr;
        }
        curr = nxt;
    }
    s.next = lDummy.next;
    return sDummy.next;
}

export default partition;