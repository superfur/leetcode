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
     * 92. 反转链表 II
     * 一趟扫描：用哑头定位 left 前一个节点 prev，
     * 然后把 prev.next 之后的节点逐个摘下，头插到 prev 之后，
     * 重复 right - left 次即可完成 [left, right] 区间反转。
     */
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        for (int i = 0; i < left - 1; i++) {
            prev = prev.next;
        }
        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode nxt = curr.next;
            curr.next = nxt.next;
            nxt.next = prev.next;
            prev.next = nxt;
        }
        return dummy.next;
    }
}
