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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        83. 删除排序链表中的重复元素
        单次扫描：若 curr.val == curr.next.val 则跳过后者，
        否则 curr 前进一步。保留每个唯一元素一次。
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([-1, 0, 0, 0, 3, 3], [-1, 0, 3]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        head = from_values(values)
        result_head = solution.deleteDuplicates(head)
        result = to_list(result_head)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")