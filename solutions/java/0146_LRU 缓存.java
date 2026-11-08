/**
 * 146. LRU 缓存
 * 哈希表 + 双向链表：
 * - 链表按「最近使用」排序，head 侧是最新、tail 侧是最久未使用；用两个哨兵节点省去边界判断。
 * - HashMap key -> 节点，保证 get / put 定位节点 O(1)；节点摘除、插到表头也都是 O(1)。
 * - get 命中后把节点移到表头；put 已存在则改值并移到表头，不存在则新建插到表头，
 *   超出容量时淘汰 tail.prev（最久未使用）并从 HashMap 删除。
 */
class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;

        Node() {}

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final java.util.Map<Integer, Node> cache = new java.util.HashMap<>();
    private final Node head = new Node();
    private final Node tail = new Node();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addToFront(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) {
            return -1;
        }
        remove(node);
        addToFront(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = cache.get(key);
        if (node != null) {
            node.value = value;
            remove(node);
            addToFront(node);
            return;
        }
        node = new Node(key, value);
        cache.put(key, node);
        addToFront(node);
        if (cache.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            cache.remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
