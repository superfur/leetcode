from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

try:
    TreeNode
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        99. 恢复二叉搜索树
        中序遍历（迭代，栈）应严格递增；用 prev 记录上一个访问节点，
        每次出现 prev.val > cur.val 就是一次"逆序对"：
        第一次出现记录 (prev, cur) 为 first/second 候选；
        若又出现第二次逆序（两个交换节点不相邻），把 second 更新为这次的 cur。
        最后交换 first 和 second 的值即可恢复。
        """
        stack: List[TreeNode] = []
        prev: Optional[TreeNode] = None
        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node
            node = node.right

        if first and second:
            first.val, second.val = second.val, first.val


# ---------- helpers ----------
def from_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def to_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 3, None, None, 2], [3, 1, None, None, 2]),
        ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        solution.recoverTree(root)
        result = to_level_order(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
