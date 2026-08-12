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
     * 86. 分隔链表
     * 两个哑头 + 两条尾链：small 串 < x 节点，large 串 >= x 节点，最后拼接。
     */
    public ListNode partition(ListNode head, int x) {
        ListNode sDummy = new ListNode(0);
        ListNode lDummy = new ListNode(0);
        ListNode s = sDummy;
        ListNode l = lDummy;
        ListNode curr = head;
        while (curr != null) {
            ListNode nxt = curr.next;
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
}