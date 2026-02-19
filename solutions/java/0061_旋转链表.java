/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 *
 * 旋转链表：将链表向右旋转 k 个位置。时间复杂度 O(n)，空间 O(1)。
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        int n = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            n++;
        }
        k = k % n;
        if (k == 0) {
            return head;
        }

        ListNode slow = head, fast = head;
        for (int i = 0; i < k; i++) {
            fast = fast.next;
        }
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }

        ListNode newHead = slow.next;
        slow.next = null;
        tail.next = head;
        return newHead;
    }

    /** 中文包装：args[0]=head, args[1]=k */
    public Object 旋转链表(Object... args) {
        if (args == null || args.length < 2) return null;
        return rotateRight((ListNode) args[0], (Integer) args[1]);
    }
}
