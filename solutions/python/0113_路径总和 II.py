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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        113. 路径总和 II
        回溯：沿途把节点值压入 path，到叶子节点时若剩余目标值
        正好归零就把 path 的一份拷贝收进结果；不管是否匹配，
        递归返回前都要把刚压入的节点值弹出，恢复现场再试下一分支。
        """
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(node: Optional[TreeNode], remaining: int) -> None:
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:
                result.append(list(path))
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()

        dfs(root, targetSum)
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
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ([1, 2, 3], 5, []),
        ([1, 2], 0, []),
    ]
    solution = Solution()
    for i, (values, target, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        result = solution.pathSum(root, target)
        ok = sorted(result) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, target={target}, got={result}, expected={expected})")
