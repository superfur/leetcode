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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        148. 排序链表
        自底向上的归并排序，满足进阶要求：O(n log n) 时间、O(1) 额外空间（没有递归栈）。
        先数出长度 n，然后让子链表长度 step 依次取 1, 2, 4, ...：
        每一轮从头扫描，每次切出相邻的两段各 step 个节点，合并后接到已处理部分的末尾。
        合并时 `<=` 优先取左段，保证排序稳定。
        """
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        dummy = ListNode(0, head)
        step = 1
        while step < n:
            prev, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self._cut(left, step)
                cur = self._cut(right, step)
                prev = self._merge(left, right, prev)
            step *= 2
        return dummy.next

    @staticmethod
    def _cut(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """从 head 开始保留 n 个节点，断开并返回剩余部分的头。"""
        while head and n > 1:
            head = head.next
            n -= 1
        if not head:
            return None
        rest = head.next
        head.next = None
        return rest

    @staticmethod
    def _merge(a: Optional[ListNode], b: Optional[ListNode], tail: ListNode) -> ListNode:
        """把有序链表 a、b 合并接到 tail 后面，返回合并后的最后一个节点。"""
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a or b
        while tail.next:
            tail = tail.next
        return tail


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
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 3, 3], [3, 3, 3]),
        ([2, 1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2, 2]),
        ([-100000, 100000, 0, 100000, -100000], [-100000, -100000, 0, 100000, 100000]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        result = to_list(solution.sortList(build_list(values)))
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")

    # 规模：5*10^4 个节点，随机 / 逆序 / 全相等，用 sorted 校验
    random.seed(148)
    n = 50000
    big_cases = {
        "随机": [random.randint(-100000, 100000) for _ in range(n)],
        "逆序": list(range(n, 0, -1)),
        "全相等": [7] * n,
    }
    for name, values in big_cases.items():
        result = to_list(solution.sortList(build_list(values)))
        idx = len(test_cases) + 1 + list(big_cases).index(name)
        print(f"测试用例 {idx}: {'PASS' if result == sorted(values) else 'FAIL'} (n={n} {name})")

    # 随机对拍：节点是原节点、相同值保持原相对顺序（稳定），与稳定的 sorted 一致
    mismatches = 0
    for _ in range(500):
        values = [random.randint(-10, 10) for _ in range(random.randint(0, 60))]
        head = build_list(values)
        order = {}
        node, idx = head, 0
        while node:
            order[id(node)] = idx
            node, idx = node.next, idx + 1
        expected = sorted(range(len(values)), key=lambda k: values[k])
        out = solution.sortList(head)
        got = []
        while out:
            got.append(order[id(out)])
            out = out.next
        if got != expected:
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 4}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机链表与稳定 sorted 对拍，不一致 {mismatches} 组)")
