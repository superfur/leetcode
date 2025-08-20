# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current:
            count = 0
            tail = current
            # 先找到第k个节点
            while tail and count < k - 1:
                tail = tail.next
                count += 1
            if not tail:
                break
            next_group = tail.next
            # 断开当前k组
            tail.next = None
            # 反转当前k组
            reversed_head = self.reverse(current)
            # 连接前一组和当前反转后的头
            prev.next = reversed_head
            # 找到当前反转后链表的尾部（即原current）
            tail_of_reversed = current
            # 连接尾部和下一组
            tail_of_reversed.next = next_group
            # 移动prev和current指针
            prev = tail_of_reversed
            current = next_group
        return dummy.next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev