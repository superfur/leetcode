import random
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        145. 二叉树的后序遍历
        后序是 左 → 右 → 根，它的逆序恰好是 根 → 右 → 左，
        而后者就是前序遍历把左右孩子的入栈顺序对调（先压左、后压右）。
        所以用显式栈按 根 → 右 → 左 收集值，最后整体反转即可。
        不依赖递归深度，时间 O(n)，空间 O(h)（结果数组除外）。
        """
        res: List[int] = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.reverse()
        return res


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


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def random_tree(n: int) -> Optional[TreeNode]:
    if n == 0:
        return None
    nodes = [TreeNode(random.randint(-100, 100)) for _ in range(n)]
    # 随机挂到某个还有空位的已有节点上，得到形态各异的二叉树
    free = [(nodes[0], "left"), (nodes[0], "right")]
    for node in nodes[1:]:
        parent, side = free.pop(random.randrange(len(free)))
        setattr(parent, side, node)
        free += [(node, "left"), (node, "right")]
    return nodes[0]


if __name__ == "__main__":
    test_cases = [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 3, 1]),
        ([1, 2, None, 3, None, 4], [4, 3, 2, 1]),
        ([1, None, 2, None, 3, None, 4], [4, 3, 2, 1]),
    ]
    solution = Solution()
    for i, (values, expected) in enumerate(test_cases, 1):
        result = solution.postorderTraversal(from_level_order(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (input={values}, got={result}, expected={expected})")

    # 极端深度：单侧 5000 层的链，迭代写法不应受递归深度限制
    chain = TreeNode(0)
    cur = chain
    for v in range(1, 5000):
        cur.left = TreeNode(v)
        cur = cur.left
    ok = solution.postorderTraversal(chain) == list(range(4999, -1, -1))
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if ok else 'FAIL'} (5000 层左链)")

    random.seed(145)
    mismatches = 0
    for _ in range(500):
        root = random_tree(random.randint(0, 40))
        if solution.postorderTraversal(root) != postorder_recursive(root):
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if mismatches == 0 else 'FAIL'} (500 棵随机二叉树与递归后序对拍，不一致 {mismatches} 棵)")
