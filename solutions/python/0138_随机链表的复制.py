from typing import List, Optional


# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

try:
    Node
except NameError:
    class Node:
        def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
            self.val = int(x)
            self.next = next
            self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        138. 随机链表的复制
        哈希表 + 两遍遍历：
        第一遍只复制节点的 val，建立「原节点 -> 克隆节点」的映射；
        第二遍再通过映射给每个克隆节点接上 next 和 random（指向 None 就映射成 None）。
        哈希表保证同一个原节点只会有一个克隆体，所以 random 指向的共享节点不会被复制多份。
        时间 O(n)，空间 O(n)。
        """
        if head is None:
            return None

        clones = {}
        cur = head
        while cur:
            clones[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            clones[cur].next = clones.get(cur.next)
            clones[cur].random = clones.get(cur.random)
            cur = cur.next
        return clones[head]


def build_list(pairs: List[list]) -> Optional[Node]:
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rand_idx) in enumerate(pairs):
        nodes[i].next = nodes[i + 1] if i + 1 < len(nodes) else None
        nodes[i].random = nodes[rand_idx] if rand_idx is not None else None
    return nodes[0]


def to_pairs(head: Optional[Node]) -> List[list]:
    order = []
    cur = head
    while cur:
        order.append(cur)
        cur = cur.next
    index = {id(n): i for i, n in enumerate(order)}
    return [[n.val, index[id(n.random)] if n.random else None] for n in order]


def node_ids(head: Optional[Node]) -> set:
    ids = set()
    cur = head
    while cur:
        ids.add(id(cur))
        cur = cur.next
    return ids


if __name__ == "__main__":
    test_cases = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        [],
        [[5, None]],
        [[5, 0]],
        [[-10000, 2], [10000, 0], [0, 1]],
    ]
    solution = Solution()
    for i, pairs in enumerate(test_cases, 1):
        original = build_list(pairs)
        cloned = solution.copyRandomList(original)
        same_shape = to_pairs(cloned) == pairs
        deep = node_ids(cloned).isdisjoint(node_ids(original))
        random_ok = True
        cur = cloned
        old_ids = node_ids(original)
        while cur:
            if cur.random is not None and id(cur.random) in old_ids:
                random_ok = False
            cur = cur.next
        status = "PASS" if same_shape and deep and random_ok else "FAIL"
        print(f"测试用例 {i}: {status} (pairs={pairs}, 结构一致={same_shape}, 无共享节点={deep}, random 不指回原链表={random_ok})")

    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if solution.copyRandomList(None) is None else 'FAIL'} (head=None 返回 None)")
