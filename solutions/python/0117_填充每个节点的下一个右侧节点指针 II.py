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
    def connect(self, root: "Node") -> "Node":
        """
        117. 填充每个节点的下一个右侧节点指针 II
        普通二叉树，不能像完美二叉树那样直接假设子节点都存在，
        但同样可以做到 O(1) 额外空间：用一个 dummy 节点作为
        "下一层"链表的临时尾巴，沿着当前层的 next 链遍历，
        把每个节点存在的 left/right 依次接到 dummy 链的末尾；
        当前层走完后，下一层的头就是 dummy.next。
        """
        node = root
        while node:
            dummy = Node()
            tail = dummy
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                node = node.next
            node = dummy.next
        return root


# ---------- helpers ----------
def from_level_order(values: List[Optional[int]]) -> Optional[Node]:
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
    return root


def to_next_chains(root: Optional[Node]) -> List[List[int]]:
    """按普通层序找到每一层最左的节点作为入口，再顺着 next 链读出整层。"""
    result: List[List[int]] = []
    if root is None:
        return result

    entries = [root]
    queue = [root]
    while queue:
        next_entry = None
        for _ in range(len(queue)):
            node = queue.pop(0)
            for child in (node.left, node.right):
                if child:
                    if next_entry is None:
                        next_entry = child
                    queue.append(child)
        if next_entry:
            entries.append(next_entry)

    for entry in entries:
        level = []
        node = entry
        while node:
            level.append(node.val)
            node = node.next
        result.append(level)
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, None, 7], [[1], [2, 3], [4, 5, 7]]),
        ([], []),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        solution.connect(root)
        result = to_next_chains(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
