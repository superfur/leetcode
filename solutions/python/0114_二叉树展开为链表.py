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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        114. 二叉树展开为链表
        O(1) 额外空间：从根开始，若当前节点有左子树，
        就在左子树里一路往右找到最右节点（也就是左子树先序遍历的最后一个节点），
        把当前节点原来的右子树接到这个最右节点的 right 上，
        再把左子树整体搬到右边、左指针置空。
        这样处理完当前节点后，沿着 right 指针继续处理下一个节点，
        整体顺序正好等于先序遍历。
        """
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = node.right
                node.right = node.left
                node.left = None
            node = node.right


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


def to_right_chain(root: Optional[TreeNode]) -> List[int]:
    result = []
    node = root
    while node:
        result.append(node.val)
        assert node.left is None, "left 指针应该始终为空"
        node = node.right
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
        ([], []),
        ([0], [0]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        root = from_level_order(values)
        solution.flatten(root)
        result = to_right_chain(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")
