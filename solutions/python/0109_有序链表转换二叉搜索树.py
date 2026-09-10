from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

try:
    ListNode
except NameError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        109. 有序链表转换二叉搜索树
        先把链表一次性摊平成数组（O(n)），之后就是 108 题的做法：
        取区间中点为根递归划分左右子树，天然保证高度平衡。
        """
        values: List[int] = []
        node = head
        while node:
            values.append(node.val)
            node = node.next

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(values) - 1)


# ---------- helpers ----------
def from_values(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def inorder_values(node: Optional[TreeNode]) -> List[int]:
    if node is None:
        return []
    return inorder_values(node.left) + [node.val] + inorder_values(node.right)


def height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_balanced(node: Optional[TreeNode]) -> bool:
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


if __name__ == "__main__":
    test_cases = [
        [-10, -3, 0, 5, 9],
        [],
    ]
    solution = Solution()
    for i, values in enumerate(test_cases, 1):
        head = from_values(values)
        root = solution.sortedListToBST(head)
        got_inorder = inorder_values(root)
        balanced = is_balanced(root)
        ok = got_inorder == values and balanced
        status = "PASS" if ok else "FAIL"
        print(f"测试用例 {i}: {status} (values={values}, 中序={got_inorder}, 平衡={balanced})")
