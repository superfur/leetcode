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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        98. 验证二叉搜索树
        区间递归：每个节点携带一个开区间 (low, high)，其值必须落在区间内；
        向左递归时收紧上界为当前值，向右递归时收紧下界为当前值。
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))


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
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([2, 2, 2], False),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        result = solution.isValidBST(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
