# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current and current.next:
            next = current.next
            current.next = next.next
            next.next = current
            prev.next = next
            prev = current
            current = current.next
        return dummy.next