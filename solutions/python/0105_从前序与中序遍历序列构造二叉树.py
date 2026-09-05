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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        105. 从前序与中序遍历序列构造二叉树
        前序的第一个元素永远是当前子树的根；在中序里找到这个根的位置，
        左边就是左子树的中序、右边是右子树的中序。
        用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
        用一个全局推进的 pre_idx 指针避免对 preorder 做切片，
        只在中序区间 [in_left, in_right] 上递归划分左右子树。
        """
        index_of = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = index_of[root_val]
            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)
            return root

        return build(0, len(inorder) - 1)


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


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ]
    solution = Solution()
    for i, (preorder, inorder, expected) in enumerate(test_cases, 1):
        root = solution.buildTree(preorder, inorder)
        result = to_level_order(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (preorder={preorder}, inorder={inorder}, got={result}, expected={expected})")
