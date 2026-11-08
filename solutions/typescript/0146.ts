/**
 * 146. LRU 缓存
 * 哈希表 + 双向链表：
 * - 链表按「最近使用」排序，head 侧是最新、tail 侧是最久未使用；用两个哨兵节点省去边界判断。
 * - Map key -> 节点，保证 get / put 定位节点 O(1)；节点摘除、插到表头也都是 O(1)。
 * - get 命中后把节点移到表头；put 已存在则改值并移到表头，不存在则新建插到表头，
 *   超出容量时淘汰 tail.prev（最久未使用）并从 Map 删除。
 *
 * 注：为避免与 DOM 的 Node 类型冲突，链表节点命名为 LRUNode。
 */

class LRUNode {
    key: number;
    value: number;
    prev: LRUNode | null = null;
    next: LRUNode | null = null;

    constructor(key: number = 0, value: number = 0) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    private capacity: number;
    private cache: Map<number, LRUNode> = new Map();
    private head: LRUNode = new LRUNode();
    private tail: LRUNode = new LRUNode();

    constructor(capacity: number) {
        this.capacity = capacity;
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    private remove(node: LRUNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
    }

    private addToFront(node: LRUNode): void {
        node.prev = this.head;
        node.next = this.head.next;
        this.head.next!.prev = node;
        this.head.next = node;
    }

    get(key: number): number {
        const node = this.cache.get(key);
        if (node === undefined) return -1;
        this.remove(node);
        this.addToFront(node);
        return node.value;
    }

    put(key: number, value: number): void {
        const existing = this.cache.get(key);
        if (existing !== undefined) {
            existing.value = value;
            this.remove(existing);
            this.addToFront(existing);
            return;
        }
        const node = new LRUNode(key, value);
        this.cache.set(key, node);
        this.addToFront(node);
        if (this.cache.size > this.capacity) {
            const lru = this.tail.prev!;
            this.remove(lru);
            this.cache.delete(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

export default LRUCache;
