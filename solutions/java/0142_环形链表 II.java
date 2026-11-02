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
     * 142. 环形链表 II
     * Floyd 快慢指针分两阶段：
     * 1. slow 走 1 步、fast 走 2 步，若相遇说明有环；若 fast 走到尽头则无环。
     * 2. 设头到入环点 a 步，入环点到相遇点 b 步，环长 c。相遇时 fast 比 slow 多走整数圈：
     *    2(a+b) = a+b+k·c，即 a = (k-1)·c + (c-b)。
     *    所以让一个指针从头出发、另一个从相遇点出发，各走 1 步，必在入环点相遇。
     * 时间 O(n)，空间 O(1)，不修改链表。
     */
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                ListNode ptr = head;
                while (ptr != slow) {
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }
        return null;
    }
}
