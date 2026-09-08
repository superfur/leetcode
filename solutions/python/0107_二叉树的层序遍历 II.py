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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        107. 二叉树的层序遍历 II
        与普通层序遍历（102 题）完全相同的 BFS，
        只是最后把层的顺序整体反转，变成从叶子层到根层。
        """
        if root is None:
            return []
        result: List[List[int]] = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        result.reverse()
        return result


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


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]]),
        ([1], [[1]]),
        ([], []),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        result = solution.levelOrderBottom(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
