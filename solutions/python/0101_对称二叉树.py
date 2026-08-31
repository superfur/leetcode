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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        101. 对称二叉树
        递归判断两棵子树是否互为镜像：值相同，且 t1 的左子树与 t2 的右子树
        互为镜像、t1 的右子树与 t2 的左子树互为镜像。
        """
        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return root is None or is_mirror(root.left, root.right)


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
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1], True),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        result = solution.isSymmetric(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
