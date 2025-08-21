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
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) {
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode current = head;
        while (current != null) {
            ListNode tail = current;
            int count = 0;
            while (tail != null && count < k) {
                tail = tail.next;
                count++;
            }
            if (count == k) {
                ListNode[] reversed = reverse(current, tail);
                prev.next = reversed[0];
                prev = reversed[1];
                current = tail;
            } else {
                // 当剩余节点数量不足k个时，保持原始顺序
                prev.next = current;
                break;
            }
        }
        return dummy.next;
    }
    
    private ListNode[] reverse(ListNode head, ListNode tail) {
        ListNode prev = null;
        ListNode current = head;
        while (current != tail) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return new ListNode[]{prev, head};
    }
}