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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        95. 不同的二叉搜索树 II
        区间递归：generate(start, end) 枚举 [start, end] 内每个值作为根，
        左子树取 generate(start, root-1)，右子树取 generate(root+1, end)，
        两两组合得到该区间内所有可能的 BST。
        """
        if n == 0:
            return []

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            result = []
            for root_val in range(start, end + 1):
                for left in generate(start, root_val - 1):
                    for right in generate(root_val + 1, end):
                        result.append(TreeNode(root_val, left, right))
            return result

        return generate(1, n)


# ---------- helpers ----------
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


def is_valid_bst(node, low=float("-inf"), high=float("inf")) -> bool:
    if node is None:
        return True
    if not (low < node.val < high):
        return False
    return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)


def count_nodes(node) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == "__main__":
    test_cases = [
        (3, 5),
        (1, 1),
    ]
    solution = Solution()
    for i, (n, expected_count) in enumerate(test_cases, 1):
        trees = solution.generateTrees(n)
        all_valid_bst = all(is_valid_bst(t) for t in trees)
        all_have_n_nodes = all(count_nodes(t) == n for t in trees)
        serialized = [tuple(to_level_order(t)) for t in trees]
        no_duplicates = len(set(serialized)) == len(serialized)
        ok = len(trees) == expected_count and all_valid_bst and all_have_n_nodes and no_duplicates
        status = "PASS" if ok else "FAIL"
        print(
            f"测试用例 {i}: {status} (n={n}, 生成数量={len(trees)}, 期望数量={expected_count}, "
            f"均为合法BST={all_valid_bst}, 均含{n}个节点={all_have_n_nodes}, 无重复={no_duplicates})"
        )
