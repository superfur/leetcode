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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        100. 相同的树
        递归：两个节点同时为空则相同；一空一非空或值不同则不同；
        否则要求左子树和右子树都分别相同。
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
    ]
    solution = Solution()
    for i, (p_values, q_values, expected) in enumerate(test_cases, 1):
        p = from_level_order(p_values)
        q = from_level_order(q_values)
        result = solution.isSameTree(p, q)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (p={p_values}, q={q_values}, got={result}, expected={expected})")
