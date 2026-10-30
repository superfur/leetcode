/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * 141. 环形链表
     * Floyd 快慢指针：slow 每次走 1 步，fast 每次走 2 步。
     * 有环的话 fast 会在环里一直绕，最终必然追上 slow（相对速度为 1，每轮距离缩小 1）；
     * 无环的话 fast 会先走到链表尽头（null）。时间 O(n)，空间 O(1)。
     */
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}
