use std::collections::HashMap;

const NIL: usize = usize::MAX;

struct Entry {
    key: i32,
    value: i32,
    prev: usize,
    next: usize,
}

/// 146. LRU 缓存
/// 哈希表 + 双向链表，链表用 Vec 做「节点池」，用下标代替指针，避开 Rc/RefCell：
/// - 下标 0、1 是头、尾哨兵；链表按「最近使用」排序，head 侧最新、tail 侧最久未使用。
/// - HashMap key -> 节点下标，get / put 定位节点 O(1)；摘除、插到表头也都是 O(1)。
/// - get 命中后移到表头；put 已存在则改值并移到表头，不存在则新建插到表头，
///   超出容量时淘汰 tail 前一个节点，并把它的槽位直接复用给新节点。
struct LRUCache {
    capacity: usize,
    map: HashMap<i32, usize>,
    nodes: Vec<Entry>,
}

const HEAD: usize = 0;
const TAIL: usize = 1;

impl LRUCache {
    fn new(capacity: i32) -> Self {
        let nodes = vec![
            Entry { key: 0, value: 0, prev: NIL, next: TAIL },
            Entry { key: 0, value: 0, prev: HEAD, next: NIL },
        ];
        LRUCache {
            capacity: capacity as usize,
            map: HashMap::with_capacity(capacity as usize),
            nodes,
        }
    }

    fn detach(&mut self, idx: usize) {
        let (prev, next) = (self.nodes[idx].prev, self.nodes[idx].next);
        self.nodes[prev].next = next;
        self.nodes[next].prev = prev;
    }

    fn attach_front(&mut self, idx: usize) {
        let first = self.nodes[HEAD].next;
        self.nodes[idx].prev = HEAD;
        self.nodes[idx].next = first;
        self.nodes[first].prev = idx;
        self.nodes[HEAD].next = idx;
    }

    fn get(&mut self, key: i32) -> i32 {
        match self.map.get(&key).copied() {
            None => -1,
            Some(idx) => {
                self.detach(idx);
                self.attach_front(idx);
                self.nodes[idx].value
            }
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(idx) = self.map.get(&key).copied() {
            self.nodes[idx].value = value;
            self.detach(idx);
            self.attach_front(idx);
            return;
        }
        let idx = if self.map.len() == self.capacity {
            let lru = self.nodes[TAIL].prev;
            self.detach(lru);
            self.map.remove(&self.nodes[lru].key);
            self.nodes[lru].key = key;
            self.nodes[lru].value = value;
            lru
        } else {
            self.nodes.push(Entry { key, value, prev: NIL, next: NIL });
            self.nodes.len() - 1
        };
        self.map.insert(key, idx);
        self.attach_front(idx);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
