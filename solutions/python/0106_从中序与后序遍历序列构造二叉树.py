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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        106. 从中序与后序遍历序列构造二叉树
        后序的最后一个元素永远是当前子树的根；在中序里找到这个根的位置，
        左边是左子树的中序、右边是右子树的中序。
        用 value -> 下标 的哈希表 O(1) 定位根在中序里的位置，
        用一个从末尾向前推进的 post_idx 指针避免对 postorder 做切片；
        因为指针从后往前走，必须先递归构建右子树、再构建左子树。
        """
        index_of = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            mid = index_of[root_val]
            root.right = build(mid + 1, in_right)
            root.left = build(in_left, mid - 1)
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
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ]
    solution = Solution()
    for i, (inorder, postorder, expected) in enumerate(test_cases, 1):
        root = solution.buildTree(inorder, postorder)
        result = to_level_order(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (inorder={inorder}, postorder={postorder}, got={result}, expected={expected})")
