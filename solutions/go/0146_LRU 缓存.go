package main

// 146. LRU 缓存
// 哈希表 + 双向链表：
//   - 链表按「最近使用」排序，head 侧是最新、tail 侧是最久未使用；用两个哨兵节点省去边界判断。
//   - map key -> 节点，保证 Get / Put 定位节点 O(1)；节点摘除、插到表头也都是 O(1)。
//   - Get 命中后把节点移到表头；Put 已存在则改值并移到表头，不存在则新建插到表头，
//     超出容量时淘汰 tail.prev（最久未使用）并从 map 删除。
type lruNode struct {
	key, value int
	prev, next *lruNode
}

type LRUCache struct {
	capacity   int
	cache      map[int]*lruNode
	head, tail *lruNode
}

func Constructor(capacity int) LRUCache {
	head, tail := &lruNode{}, &lruNode{}
	head.next = tail
	tail.prev = head
	return LRUCache{
		capacity: capacity,
		cache:    make(map[int]*lruNode, capacity),
		head:     head,
		tail:     tail,
	}
}

func (c *LRUCache) remove(node *lruNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (c *LRUCache) addToFront(node *lruNode) {
	node.prev = c.head
	node.next = c.head.next
	c.head.next.prev = node
	c.head.next = node
}

func (c *LRUCache) Get(key int) int {
	node, ok := c.cache[key]
	if !ok {
		return -1
	}
	c.remove(node)
	c.addToFront(node)
	return node.value
}

func (c *LRUCache) Put(key int, value int) {
	if node, ok := c.cache[key]; ok {
		node.value = value
		c.remove(node)
		c.addToFront(node)
		return
	}
	node := &lruNode{key: key, value: value}
	c.cache[key] = node
	c.addToFront(node)
	if len(c.cache) > c.capacity {
		lru := c.tail.prev
		c.remove(lru)
		delete(c.cache, lru.key)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
