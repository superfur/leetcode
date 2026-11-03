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
     * 143. 重排链表
     * 三步走：
     * 1. 快慢指针找中点（偶数长度时 slow 停在前半段最后一个节点），把链表断成前后两半；
     * 2. 反转后半段；
     * 3. 前半段与反转后的后半段交替拼接。
     * 时间 O(n)，空间 O(1)，只改 next 指针不改节点值。
     */
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = slow.next;
        slow.next = null;

        ListNode prev = null;
        while (second != null) {
            ListNode next = second.next;
            second.next = prev;
            prev = second;
            second = next;
        }
        second = prev;

        ListNode first = head;
        while (second != null) {
            ListNode firstNext = first.next, secondNext = second.next;
            first.next = second;
            second.next = firstNext;
            first = firstNext;
            second = secondNext;
        }
    }
}
