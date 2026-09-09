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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        108. 将有序数组转换为二叉搜索树
        每次取区间中点作为根（自然保证左右子树节点数最多差 1，即高度平衡），
        左半区间递归建左子树，右半区间递归建右子树。
        答案不唯一，只要是高度平衡的 BST 即可。
        """
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)


# ---------- helpers ----------
def inorder_values(node) -> List[int]:
    if node is None:
        return []
    return inorder_values(node.left) + [node.val] + inorder_values(node.right)


def height(node) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_balanced(node) -> bool:
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


if __name__ == "__main__":
    test_cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
    ]
    solution = Solution()
    for i, nums in enumerate(test_cases, 1):
        root = solution.sortedArrayToBST(nums)
        got_inorder = inorder_values(root)
        balanced = is_balanced(root)
        ok = got_inorder == nums and balanced
        status = "PASS" if ok else "FAIL"
        print(f"测试用例 {i}: {status} (nums={nums}, 中序={got_inorder}, 平衡={balanced})")
