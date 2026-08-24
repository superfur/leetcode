from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
#         self.val = val
#         self.next = next

try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
            self.val = val
            self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        92. 反转链表 II
        一趟扫描：用哑头定位 left 前一个节点 prev，
        然后把 prev.next 之后的节点逐个摘下，头插到 prev 之后，
        重复 right - left 次即可完成 [left, right] 区间反转。
        """
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next


# ---------- helpers ----------
def from_values(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ]
    solution = Solution()
    for i, (values, left, right, expected) in enumerate(test_cases, 1):
        head = from_values(values)
        result_head = solution.reverseBetween(head, left, right)
        result = to_list(result_head)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, left={left}, right={right}, got={result}, expected={expected})")
