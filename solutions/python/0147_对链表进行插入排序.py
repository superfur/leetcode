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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        147. 对链表进行插入排序
        用哨兵节点 dummy 作为已排序部分的前驱，tail 记录已排序部分的最后一个节点。
        依次取出 cur = tail.next：
        - 若 tail.val <= cur.val，说明 cur 已经在正确位置，直接把 tail 后移（常见于已有序的输入，省去扫描）；
        - 否则从 dummy 开始找到第一个「下一个节点值 > cur.val」的位置 prev，把 cur 摘下来插到 prev 后面。
        用 `<=` 找位置，相同值的节点保持原相对顺序（稳定）。
        最坏时间 O(n^2)，空间 O(1)，只改 next 指针。
        """
        if not head:
            return head
        dummy = ListNode(0, head)
        tail = head
        while tail.next:
            cur = tail.next
            if tail.val <= cur.val:
                tail = cur
                continue
            tail.next = cur.next
            prev = dummy
            while prev.next.val <= cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
        return dummy.next


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


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 3, 3], [3, 3, 3]),
        ([2, 1, 2, 1, 2], [1, 1, 2, 2, 2]),
        ([-5000, 5000, 0, 5000, -5000], [-5000, -5000, 0, 5000, 5000]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        result = to_list(solution.insertionSortList(build_list(values)))
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")

    # 规模：5000 个节点，逆序是插入排序的最坏情况
    n = 5000
    result = to_list(solution.insertionSortList(build_list(list(range(n, 0, -1)))))
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if result == list(range(1, n + 1)) else 'FAIL'} (n={n} 逆序)")

    # 随机对拍：值与 sorted 一致；节点是原节点；相同值的节点保持原相对顺序（稳定）
    random.seed(147)
    mismatches = 0
    for _ in range(500):
        values = [random.randint(-10, 10) for _ in range(random.randint(1, 40))]
        head = build_list(values)
        order = {}
        node, idx = head, 0
        while node:
            order[id(node)] = idx
            node, idx = node.next, idx + 1
        expected = sorted(range(len(values)), key=lambda k: values[k])  # sorted 本身是稳定的
        out = solution.insertionSortList(head)
        got = []
        while out:
            got.append(order[id(out)])
            out = out.next
        if got != expected:
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机链表与稳定 sorted 对拍，不一致 {mismatches} 组)")
