/**
 * 148. 排序链表
 * 自底向上的归并排序，满足进阶要求：O(n log n) 时间、O(1) 额外空间（没有递归栈）。
 * 先数出长度 n，然后让子链表长度 step 依次取 1, 2, 4, ...：
 * 每一轮从头扫描，每次切出相邻的两段各 step 个节点，合并后接到已处理部分的末尾。
 * 合并时 `<=` 优先取左段，保证排序稳定。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

/** 从 head 开始保留 n 个节点，断开并返回剩余部分的头。 */
function cut(head: LNode | null, n: number): LNode | null {
    while (head && n > 1) {
        head = head.next;
        n--;
    }
    if (!head) return null;
    const rest = head.next;
    head.next = null;
    return rest;
}

/** 把有序链表 a、b 合并接到 tail 后面，返回合并后的最后一个节点。 */
function merge(a: LNode | null, b: LNode | null, tail: LNode): LNode {
    while (a && b) {
        if (a.val <= b.val) {
            tail.next = a;
            a = a.next;
        } else {
            tail.next = b;
            b = b.next;
        }
        tail = tail.next;
    }
    tail.next = a ?? b;
    while (tail.next) tail = tail.next;
    return tail;
}

function sortList(head: LNode | null): LNode | null {
    let n = 0;
    for (let node = head; node; node = node.next) n++;

    const dummy: LNode = { val: 0, next: head };
    for (let step = 1; step < n; step *= 2) {
        let prev: LNode = dummy;
        let cur = dummy.next;
        while (cur) {
            const left: LNode = cur;
            const right = cut(left, step);
            cur = cut(right, step);
            prev = merge(left, right, prev);
        }
    }
    return dummy.next;
}

export default sortList;
