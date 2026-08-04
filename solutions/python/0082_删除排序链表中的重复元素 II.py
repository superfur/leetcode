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
        82. 删除排序链表中的重复元素 II
        删除所有出现重复的数字节点，只保留出现一次的。
        哨兵 + 双指针：prev 指向上一个确认唯一的节点，
        若 head 与 head.next 值相等则一路跳过所有该值的节点；
        否则 prev 前进一位。
        """
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                dup = curr.val
                while curr and curr.val == dup:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return sentinel.next


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
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([], []),
        ([1, 2, 2], [1]),
        ([1, 1, 2, 2], []),
        ([1, 2, 3], [1, 2, 3]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        head = from_values(values)
        result_head = solution.deleteDuplicates(head)
        result = to_list(result_head)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")