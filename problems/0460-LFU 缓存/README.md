# 460. LFU 缓存

## 题目描述

<p>请你为 <a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存算法设计并实现数据结构。</p>

<p>实现 <code>LFUCache</code> 类：</p>

<ul>
	<li><code>LFUCache(int capacity)</code> - 用数据结构的容量&nbsp;<code>capacity</code> 初始化对象</li>
	<li><code>int get(int key)</code>&nbsp;- 如果键&nbsp;<code>key</code> 存在于缓存中，则获取键的值，否则返回 <code>-1</code> 。</li>
	<li><code>void put(int key, int value)</code>&nbsp;- 如果键&nbsp;<code>key</code> 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量&nbsp;<code>capacity</code> 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 <strong>最久未使用</strong> 的键。</li>
</ul>

<p>为了确定最不常使用的键，可以为缓存中的每个键维护一个 <strong>使用计数器</strong> 。使用计数最小的键是最久未使用的键。</p>

<p>当一个键首次插入到缓存中时，它的使用计数器被设置为 <code>1</code> (由于 put 操作)。对缓存中的键执行 <code>get</code> 或 <code>put</code> 操作，使用计数器的值将会递增。</p>

<p>函数 <code>get</code> 和 <code>put</code> 必须以 <code>O(1)</code> 的平均时间复杂度运行。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
<strong>输出：</strong>
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

<strong>解释：</strong>
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // 返回 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // 返回 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= capacity&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>9</sup></code></li>
	<li>最多调用 <code>2 * 10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code> 方法</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 哈希表
- 链表
- 双向链表

## 示例

```
["LFUCache","put","put","get","put","get","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
```

## 示例代码

### C++

```cpp
class LFUCache {
public:
    LFUCache(int capacity) {
        
    }
    
    int get(int key) {
        
    }
    
    void put(int key, int value) {
        
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

### Java

```java
class LFUCache {

    public LFUCache(int capacity) {
        
    }
    
    public int get(int key) {
        
    }
    
    public void put(int key, int value) {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

### Python

```python
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### Python3

```python3
class LFUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### C

```c



typedef struct {
    
} LFUCache;


LFUCache* lFUCacheCreate(int capacity) {
    
}

int lFUCacheGet(LFUCache* obj, int key) {
    
}

void lFUCachePut(LFUCache* obj, int key, int value) {
    
}

void lFUCacheFree(LFUCache* obj) {
    
}

/**
 * Your LFUCache struct will be instantiated and called as such:
 * LFUCache* obj = lFUCacheCreate(capacity);
 * int param_1 = lFUCacheGet(obj, key);
 
 * lFUCachePut(obj, key, value);
 
 * lFUCacheFree(obj);
*/
```

### C#

```csharp
public class LFUCache {

    public LFUCache(int capacity) {
        
    }
    
    public int Get(int key) {
        
    }
    
    public void Put(int key, int value) {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
```

### JavaScript

```javascript
/**
 * @param {number} capacity
 */
var LFUCache = function(capacity) {
    
};

/** 
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function(key) {
    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function(key, value) {
    
};

/** 
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### TypeScript

```typescript
class LFUCache {
    constructor(capacity: number) {
        
    }

    get(key: number): number {
        
    }

    put(key: number, value: number): void {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### PHP

```php
class LFUCache {
    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        
    }
  
    /**
     * @param Integer $key
     * @return Integer
     */
    function get($key) {
        
    }
  
    /**
     * @param Integer $key
     * @param Integer $value
     * @return NULL
     */
    function put($key, $value) {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * $obj = LFUCache($capacity);
 * $ret_1 = $obj->get($key);
 * $obj->put($key, $value);
 */
```

### Swift

```swift

class LFUCache {

    init(_ capacity: Int) {
        
    }
    
    func get(_ key: Int) -> Int {
        
    }
    
    func put(_ key: Int, _ value: Int) {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * let obj = LFUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
```

### Kotlin

```kotlin
class LFUCache(capacity: Int) {

    fun get(key: Int): Int {
        
    }

    fun put(key: Int, value: Int) {
        
    }

}

/**
 * Your LFUCache object will be instantiated and called as such:
 * var obj = LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### Dart

```dart
class LFUCache {

  LFUCache(int capacity) {
    
  }
  
  int get(int key) {
    
  }
  
  void put(int key, int value) {
    
  }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = LFUCache(capacity);
 * int param1 = obj.get(key);
 * obj.put(key,value);
 */
```

### Go

```golang
type LFUCache struct {
    
}


func Constructor(capacity int) LFUCache {
    
}


func (this *LFUCache) Get(key int) int {
    
}


func (this *LFUCache) Put(key int, value int)  {
    
}


/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
```

### Ruby

```ruby
class LFUCache

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        
    end


end

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
```

### Scala

```scala
class LFUCache(_capacity: Int) {

    def get(key: Int): Int = {
        
    }

    def put(key: Int, value: Int): Unit = {
        
    }

}

/**
 * Your LFUCache object will be instantiated and called as such:
 * val obj = new LFUCache(capacity)
 * val param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### Rust

```rust
struct LFUCache {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LFUCache {

    fn new(capacity: i32) -> Self {
        
    }
    
    fn get(&self, key: i32) -> i32 {
        
    }
    
    fn put(&self, key: i32, value: i32) {
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * let obj = LFUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
```

### Racket

```racket
(define lfu-cache%
  (class object%
    (super-new)
    
    ; capacity : exact-integer?
    (init-field
      capacity)
    
    ; get : exact-integer? -> exact-integer?
    (define/public (get key)
      )
    ; put : exact-integer? exact-integer? -> void?
    (define/public (put key value)
      )))

;; Your lfu-cache% object will be instantiated and called as such:
;; (define obj (new lfu-cache% [capacity capacity]))
;; (define param_1 (send obj get key))
;; (send obj put key value)
```

### Erlang

```erlang
-spec lfu_cache_init_(Capacity :: integer()) -> any().
lfu_cache_init_(Capacity) ->
  .

-spec lfu_cache_get(Key :: integer()) -> integer().
lfu_cache_get(Key) ->
  .

-spec lfu_cache_put(Key :: integer(), Value :: integer()) -> any().
lfu_cache_put(Key, Value) ->
  .


%% Your functions will be called as such:
%% lfu_cache_init_(Capacity),
%% Param_1 = lfu_cache_get(Key),
%% lfu_cache_put(Key, Value),

%% lfu_cache_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule LFUCache do
  @spec init_(capacity :: integer) :: any
  def init_(capacity) do
    
  end

  @spec get(key :: integer) :: integer
  def get(key) do
    
  end

  @spec put(key :: integer, value :: integer) :: any
  def put(key, value) do
    
  end
end

# Your functions will be called as such:
# LFUCache.init_(capacity)
# param_1 = LFUCache.get(key)
# LFUCache.put(key, value)

# LFUCache.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class LFUCache {
    init(capacity: Int64) {

    }
    
    func get(key: Int64): Int64 {

    }
    
    func put(key: Int64, value: Int64): Unit {

    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * let obj: LFUCache = LFUCache(capacity)
 * let param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

