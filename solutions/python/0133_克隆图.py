from collections import deque
from typing import List, Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

try:
    Node
except NameError:
    class Node:
        def __init__(self, val=0, neighbors=None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Optional[Node]") -> "Optional[Node]":
        """
        133. 克隆图
        BFS 遍历原图，用哈希表记录「原节点 -> 克隆节点」：
        遇到还没克隆的邻居就新建克隆并入队，
        然后把邻居对应的克隆节点挂到当前节点的克隆体的 neighbors 上。
        哈希表同时起到「已访问」的作用，所以环不会死循环。
        """
        if node is None:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in clones:
                    clones[nb] = Node(nb.val)
                    queue.append(nb)
                clones[cur].neighbors.append(clones[nb])
        return clones[node]


def build_graph(adj: List[List[int]]) -> Optional[Node]:
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def to_adj(node: Optional[Node]) -> List[List[int]]:
    if node is None:
        return []
    seen = {node.val: node}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                queue.append(nb)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)]


def collect(node: Optional[Node]) -> List[Node]:
    if node is None:
        return []
    seen = {id(node): node}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for nb in cur.neighbors:
            if id(nb) not in seen:
                seen[id(nb)] = nb
                queue.append(nb)
    return list(seen.values())


if __name__ == "__main__":
    test_cases = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        [],
        [[2], [1]],
        [[2, 3], [1, 3], [1, 2]],
        [[2, 3, 4], [1], [1], [1]],
    ]
    solution = Solution()
    for i, adj in enumerate(test_cases, 1):
        original = build_graph(adj)
        cloned = solution.cloneGraph(original)
        same_shape = to_adj(cloned) == adj
        old_ids = {id(n) for n in collect(original)}
        deep = all(id(n) not in old_ids for n in collect(cloned))
        status = "PASS" if same_shape and deep else "FAIL"
        print(f"测试用例 {i}: {status} (adj={adj}, 结构一致={same_shape}, 无共享节点={deep})")

    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if solution.cloneGraph(None) is None else 'FAIL'} (node=None 返回 None)")
