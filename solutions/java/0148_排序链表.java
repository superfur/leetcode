/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class Solution {
    /**
     * 148. 排序链表
     * 自底向上的归并排序，满足进阶要求：O(n log n) 时间、O(1) 额外空间（没有递归栈）。
     * 先数出长度 n，然后让子链表长度 step 依次取 1, 2, 4, ...：
     * 每一轮从头扫描，每次切出相邻的两段各 step 个节点，合并后接到已处理部分的末尾。
     * 合并时 `<=` 优先取左段，保证排序稳定。
     */
    public ListNode sortList(ListNode head) {
        int n = 0;
        for (ListNode node = head; node != null; node = node.next) {
            n++;
        }

        ListNode dummy = new ListNode(0, head);
        for (int step = 1; step < n; step *= 2) {
            ListNode prev = dummy, cur = dummy.next;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = cut(left, step);
                cur = cut(right, step);
                prev = merge(left, right, prev);
            }
        }
        return dummy.next;
    }

    /** 从 head 开始保留 n 个节点，断开并返回剩余部分的头。 */
    private ListNode cut(ListNode head, int n) {
        while (head != null && n > 1) {
            head = head.next;
            n--;
        }
        if (head == null) {
            return null;
        }
        ListNode rest = head.next;
        head.next = null;
        return rest;
    }

    /** 把有序链表 a、b 合并接到 tail 后面，返回合并后的最后一个节点。 */
    private ListNode merge(ListNode a, ListNode b, ListNode tail) {
        while (a != null && b != null) {
            if (a.val <= b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }
        tail.next = a != null ? a : b;
        while (tail.next != null) {
            tail = tail.next;
        }
        return tail;
    }
}
