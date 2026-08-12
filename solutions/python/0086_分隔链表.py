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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        86. 分隔链表
        两个哑头 + 两条尾链：small 串 < x 节点，large 串 >= x 节点，
        最后 large.next 置 None 后拼到 small 尾。
        """
        s_dummy = ListNode(0)
        l_dummy = ListNode(0)
        s, l = s_dummy, l_dummy
        curr = head
        while curr:
            nxt = curr.next
            curr.next = None  # 切断，避免旧 next 链进新链成环
            if curr.val < x:
                s.next = curr
                s = s.next
            else:
                l.next = curr
                l = l.next
            curr = nxt
        s.next = l_dummy.next
        return s_dummy.next


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
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
        ([], 0, []),
        ([1], 2, [1]),
        ([1, 2, 3], 2, [1, 2, 3]),
        ([3, 1, 2], 2, [1, 3, 2]),
    ]
    solution = Solution()
    for i, (values, x, expected) in enumerate(test_cases, 1):
        head = from_values(values)
        result_head = solution.partition(head, x)
        result = to_list(result_head)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, x={x}, got={result}, expected={expected})")