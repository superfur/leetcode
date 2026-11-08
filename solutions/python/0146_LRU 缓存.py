import random
from collections import OrderedDict
from typing import Dict, List, Optional


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUCache:
    """
    146. LRU 缓存
    哈希表 + 双向链表：
    - 链表按「最近使用」排序，head 侧是最新、tail 侧是最久未使用；用两个哨兵节点省去边界判断。
    - 哈希表 key -> 节点，保证 get / put 定位节点 O(1)；节点摘除、插到表头也都是 O(1)。
    - get 命中后把节点移到表头；put 已存在则改值并移到表头，不存在则新建插到表头，
      超出容量时淘汰 tail.prev（最久未使用）并从哈希表删除。
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, _Node] = {}
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: _Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        node = _Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def run_ops(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    cache: Optional[LRUCache] = None
    out: List[Optional[int]] = []
    for op, arg in zip(ops, args):
        if op == "LRUCache":
            cache = LRUCache(*arg)
            out.append(None)
        elif op == "put":
            cache.put(*arg)
            out.append(None)
        else:
            out.append(cache.get(*arg))
    return out


class OracleLRU:
    """用 OrderedDict 实现的参照解，仅用于对拍。"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: "OrderedDict[int, int]" = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


if __name__ == "__main__":
    test_cases = [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        # 容量 1：每次 put 新 key 都淘汰旧 key
        (
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[1], [2, 1], [2], [3, 2], [2], [3]],
            [None, None, 1, None, -1, 2],
        ),
        # 更新已有 key 也算「使用」，应刷新其新旧程度
        (
            ["LRUCache", "put", "put", "put", "put", "get", "get"],
            [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
            [None, None, None, None, None, -1, 3],
        ),
        # value 为 0 与「不存在」(-1) 要区分开
        (
            ["LRUCache", "put", "get", "get"],
            [[2], [0, 0], [0], [1]],
            [None, None, 0, -1],
        ),
    ]
    for i, (ops, args, expected) in enumerate(test_cases, 1):
        result = run_ops(ops, args)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (got={result}, expected={expected})")

    random.seed(146)
    mismatches = 0
    for _ in range(500):
        capacity = random.randint(1, 6)
        mine, oracle = LRUCache(capacity), OracleLRU(capacity)
        for _ in range(200):
            key = random.randint(0, 10)
            if random.random() < 0.5:
                value = random.randint(0, 100)
                mine.put(key, value)
                oracle.put(key, value)
            elif mine.get(key) != oracle.get(key):
                mismatches += 1
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if mismatches == 0 else 'FAIL'} (500 组随机操作序列与 OrderedDict 对拍，不一致 {mismatches} 次)")

    # 规模：容量 3000，2*10^5 次操作，确认 O(1) 实现不会超时
    big = LRUCache(3000)
    for step in range(200000):
        key = step % 10001
        if step % 2:
            big.get(key)
        else:
            big.put(key, step)
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if len(big.cache) == 3000 else 'FAIL'} (2*10^5 次操作，缓存大小={len(big.cache)})")
