from typing import List, Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

try:
    Node
except NameError:
    class Node:
        def __init__(self, val=0, left=None, right=None, next=None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        """
        116. 填充每个节点的下一个右侧节点指针
        O(1) 额外空间：利用已经连好的上一层 next 指针去连接下一层——
        leftmost 指向当前层最左节点，用 head 沿着当前层的 next 链
        往右走，每一步把 head.left.next 接到 head.right，
        再把 head.right.next 接到 head.next.left（如果 head.next 存在）；
        走完当前层后，leftmost 下移一层，重复直到最底层（叶子层没有子节点）。
        这是完美二叉树，所以只要 leftmost.left 存在就说明还有下一层。
        """
        leftmost = root
        while leftmost and leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root


# ---------- helpers ----------
def from_perfect_level_order(values: List[Optional[int]]) -> Optional[Node]:
    if not values or values[0] is None:
        return None
    nodes = [Node(v) if v is not None else None for v in values]
    n = len(nodes)
    for i, node in enumerate(nodes):
        if node is None:
            continue
        li, ri = 2 * i + 1, 2 * i + 2
        if li < n:
            node.left = nodes[li]
        if ri < n:
            node.right = nodes[ri]
    return nodes[0]


def to_next_chains(root: Optional[Node]) -> List[List[int]]:
    result: List[List[int]] = []
    level_head = root
    while level_head:
        level = []
        node = level_head
        while node:
            level.append(node.val)
            node = node.next
        result.append(level)
        level_head = level_head.left
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([], []),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_perfect_level_order(values)
        solution.connect(root)
        result = to_next_chains(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
