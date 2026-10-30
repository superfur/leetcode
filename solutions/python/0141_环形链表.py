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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        141. 环形链表
        Floyd 快慢指针：slow 每次走 1 步，fast 每次走 2 步。
        有环的话 fast 会在环里一直绕，最终必然追上 slow（相对速度为 1，每轮距离缩小 1）；
        无环的话 fast 会先走到链表尽头（None）。时间 O(n)，空间 O(1)。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build_list(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def has_cycle_by_set(head: Optional[ListNode]) -> bool:
    seen = set()
    while head:
        if id(head) in seen:
            return True
        seen.add(id(head))
        head = head.next
    return False


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1], 0, True),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 4, True),
        (list(range(10000)), 5000, True),
        (list(range(10000)), -1, False),
        (list(range(10000)), 0, True),
    ]
    solution = Solution()
    for i, (values, pos, expected) in enumerate(test_cases, 1):
        result = solution.hasCycle(build_list(values, pos))
        status = "PASS" if result == expected else "FAIL"
        shown = values if len(values) <= 6 else f"(len={len(values)})"
        print(f"测试用例 {i}: {status} (values={shown}, pos={pos}, got={result}, expected={expected})")

    random.seed(141)
    mismatches = 0
    for _ in range(500):
        n = random.randint(0, 30)
        values = [random.randint(-100, 100) for _ in range(n)]
        pos = random.randint(-1, n - 1) if n else -1
        head = build_list(values, pos)
        if solution.hasCycle(head) != has_cycle_by_set(head):
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机链表与哈希集合法对拍，不一致 {mismatches} 组)")
