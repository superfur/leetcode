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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112. 路径总和
        递归：空树直接不存在路径；到达叶子节点时判断剩余目标值
        是否正好等于该叶子的值；否则把目标值减去当前节点值，
        分别在左右子树里继续找。
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


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
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
    ]
    solution = Solution()
    for i, (values, target, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        result = solution.hasPathSum(root, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, target={target}, got={result}, expected={expected})")
