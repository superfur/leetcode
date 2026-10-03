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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        124. 二叉树中的最大路径和
        后序递归：dfs(node) 返回「以 node 为起点、向下走的最大贡献值」
        （贡献为负就当作 0，即不选这条分支）；
        同时把「左贡献 + 节点值 + 右贡献」当作以 node 为最高点的路径和，更新全局答案。
        """
        best = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return best


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
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([2, -1], 2),
        ([-2, -1], -1),
        ([1, -2, 3], 4),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        result = solution.maxPathSum(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (root={values}, got={result}, expected={expected})")
