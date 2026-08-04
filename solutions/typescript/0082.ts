/**
 * 82. 删除排序链表中的重复元素 II
 * 给定已排序链表头，删除所有出现重复的数字节点，只保留出现一次的数字。
 * 哨兵 + 双指针：prev 指向最后一个确认唯一的节点；
 * 若 curr.val === curr.next.val 则一路跳过所有该值节点，prev.next = curr；
 * 否则 prev 前进一位。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped 写法以避免与
 * 本地测试或平台模板里的同名类冲突。
 */

interface LNode { val: number; next: LNode | null }

function deleteDuplicates(head: LNode | null): LNode | null {
    const sentinel: LNode = { val: 0, next: head };
    let prev: LNode = sentinel;
    let curr: LNode | null = head;
    while (curr) {
        if (curr.next && curr.val === curr.next.val) {
            const dup = curr.val;
            while (curr && curr.val === dup) {
                curr = curr.next;
            }
            prev.next = curr;
        } else {
            prev = curr;
            curr = curr.next;
        }
    }
    return sentinel.next;
}

export default deleteDuplicates;