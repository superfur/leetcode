import random
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        143. 重排链表
        Do not return anything, modify head in-place instead.
        三步走：
        1. 快慢指针找中点（偶数长度时 slow 停在前半段最后一个节点），把链表断成前后两半；
        2. 反转后半段；
        3. 前半段与反转后的后半段交替拼接。
        时间 O(n)，空间 O(1)，只改 next 指针不改节点值。
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        second = prev

        first = head
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def expected_order(values: List[int]) -> List[int]:
    res, i, j = [], 0, len(values) - 1
    while i <= j:
        res.append(values[i])
        if i != j:
            res.append(values[j])
        i += 1
        j -= 1
    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        head = build_list(values)
        solution.reorderList(head)
        result = to_list(head)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (values={values}, got={result}, expected={expected})")

    # 大规模：长度 5*10^4，同时检查节点是原节点（只换指针）且链表无环、长度不变
    n = 50000
    head = build_list(list(range(1, n + 1)))
    ids = set()
    node = head
    while node:
        ids.add(id(node))
        node = node.next
    solution.reorderList(head)
    result = to_list(head)
    same_nodes = set()
    node = head
    while node and len(same_nodes) <= n:
        same_nodes.add(id(node))
        node = node.next
    ok = result == expected_order(list(range(1, n + 1))) and same_nodes == ids
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if ok else 'FAIL'} (n={n}，顺序正确且复用原节点)")

    random.seed(143)
    mismatches = 0
    for _ in range(500):
        values = [random.randint(1, 1000) for _ in range(random.randint(1, 30))]
        head = build_list(values)
        solution.reorderList(head)
        if to_list(head) != expected_order(values):
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机链表与双端取数法对拍，不一致 {mismatches} 组)")
