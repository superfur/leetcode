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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        129. 求根节点到叶节点数字之和
        DFS 往下传「根到当前节点已经拼出的数字」（cur * 10 + val），
        走到叶子节点时这个数字就是一条完整路径代表的数，累加进答案。
        """

        def dfs(node: Optional[TreeNode], cur: int) -> int:
            if node is None:
                return 0
            cur = cur * 10 + node.val
            if node.left is None and node.right is None:
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    children = iter(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        node.left = next(children, None)
        node.right = next(children, None)
    return nodes[0]


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026),
        ([0], 0),
        ([5], 5),
        ([1, 0], 10),
        ([1, None, 2], 12),
        ([9, 9, 9, 9, 9, 9, 9], 3996),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        result = solution.sumNumbers(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (root={values}, got={result}, expected={expected})")
