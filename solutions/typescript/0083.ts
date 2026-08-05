/**
 * 83. 删除排序链表中的重复元素
 * 给定已排序链表头，删除重复元素使每个元素只出现一次，返回已排序链表。
 * 单次扫描：curr.val === curr.next.val 时跳过后者，否则 curr 前进一步。
 *
 * 注：ListNode 类型由 LeetCode 平台注入，本文件用 untyped LNode 接口避免冲突。
 */

interface LNode { val: number; next: LNode | null }

function deleteDuplicates(head: LNode | null): LNode | null {
    let curr: LNode | null = head;
    while (curr && curr.next) {
        if (curr.val === curr.next.val) {
            curr.next = curr.next.next;
        } else {
            curr = curr.next;
        }
    }
    return head;
}

export default deleteDuplicates;