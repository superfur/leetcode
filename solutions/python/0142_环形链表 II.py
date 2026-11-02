import random
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        142. 环形链表 II
        Floyd 快慢指针分两阶段：
        1. slow 走 1 步、fast 走 2 步，若相遇说明有环；若 fast 走到尽头则无环。
        2. 设头到入环点 a 步，入环点到相遇点 b 步，环长 c。相遇时 fast 比 slow 多走整数圈：
           2(a+b) = a+b+k·c，即 a = k·c - b = (k-1)·c + (c-b)。
           所以让一个指针从头出发、另一个从相遇点出发，各走 1 步，必在入环点相遇。
        时间 O(n)，空间 O(1)，不修改链表。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                ptr = head
                while ptr is not slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None


def build_list(values: List[int], pos: int):
    if not values:
        return None, []
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0], nodes


def detect_by_set(head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    while head:
        if id(head) in seen:
            return head
        seen.add(id(head))
        head = head.next
    return None


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
        ([], -1),
        ([1], 0),
        ([1, 2, 3, 4, 5], -1),
        ([1, 2, 3, 4, 5], 4),
        ([1, 2, 3, 4, 5], 2),
        (list(range(10000)), 5000),
        (list(range(10000)), -1),
        (list(range(10000)), 0),
        (list(range(10000)), 9999),
    ]
    solution = Solution()
    for i, (values, pos) in enumerate(test_cases, 1):
        head, nodes = build_list(values, pos)
        result = solution.detectCycle(head)
        expected = nodes[pos] if pos >= 0 else None
        status = "PASS" if result is expected else "FAIL"
        shown = values if len(values) <= 6 else f"(len={len(values)})"
        got = "None" if result is None else f"节点 val={result.val}"
        print(f"测试用例 {i}: {status} (values={shown}, pos={pos}, got={got}, expected 索引={pos if pos >= 0 else None})")

    random.seed(142)
    mismatches = 0
    for _ in range(500):
        n = random.randint(0, 30)
        values = [random.randint(-100, 100) for _ in range(n)]
        pos = random.randint(-1, n - 1) if n else -1
        head, nodes = build_list(values, pos)
        if solution.detectCycle(head) is not detect_by_set(head):
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机链表与哈希集合法对拍，不一致 {mismatches} 组)")
