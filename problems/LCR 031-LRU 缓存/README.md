# LCR 031. LRU 缓存

## 题目描述

<div class="title__3Vvk">
<p>运用所掌握的数据结构，设计和实现一个&nbsp; <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (Least Recently Used，最近最少使用) 缓存机制</a> 。</p>

<p>实现 <code>LRUCache</code> 类：</p>

<ul>
	<li><code>LRUCache(int capacity)</code> 以正整数作为容量&nbsp;<code>capacity</code> 初始化 LRU 缓存</li>
	<li><code>int get(int key)</code> 如果关键字 <code>key</code> 存在于缓存中，则返回关键字的值，否则返回 <code>-1</code> 。</li>
	<li><code>void put(int key, int value)</code>&nbsp;如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>输出</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>解释</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10000</code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>2 * 10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code></li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>进阶</strong>：是否可以在&nbsp;<code>O(1)</code> 时间复杂度内完成这两种操作？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 146&nbsp;题相同：<a href="https://leetcode-cn.com/problems/lru-cache/">https://leetcode-cn.com/problems/lru-cache/</a>&nbsp;</p>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 链表
- 双向链表

## 示例

```
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
```

## 示例代码

### C++

```cpp
class LRUCache {
public:
    LRUCache(int capacity) {

    }
    
    int get(int key) {

    }
    
    void put(int key, int value) {

    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

### Java

```java
class LRUCache {

    public LRUCache(int capacity) {

    }
    
    public int get(int key) {

    }
    
    public void put(int key, int value) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

### Python

```python
class LRUCache(object):

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



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### Python3

```python3
class LRUCache:

    def __init__(self, capacity: int):


    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### C

```c



typedef struct {

} LRUCache;


LRUCache* lRUCacheCreate(int capacity) {

}

int lRUCacheGet(LRUCache* obj, int key) {

}

void lRUCachePut(LRUCache* obj, int key, int value) {

}

void lRUCacheFree(LRUCache* obj) {

}

/**
 * Your LRUCache struct will be instantiated and called as such:
 * LRUCache* obj = lRUCacheCreate(capacity);
 * int param_1 = lRUCacheGet(obj, key);
 
 * lRUCachePut(obj, key, value);
 
 * lRUCacheFree(obj);
*/
```

### C#

```csharp
public class LRUCache {

    public LRUCache(int capacity) {

    }
    
    public int Get(int key) {

    }
    
    public void Put(int key, int value) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
```

### JavaScript

```javascript
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {

};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {

};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### TypeScript

```typescript
class LRUCache {
    constructor(capacity: number) {

    }

    get(key: number): number {

    }

    put(key: number, value: number): void {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### PHP

```php
class LRUCache {
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
 * Your LRUCache object will be instantiated and called as such:
 * $obj = LRUCache($capacity);
 * $ret_1 = $obj->get($key);
 * $obj->put($key, $value);
 */
```

### Swift

```swift

class LRUCache {

    init(_ capacity: Int) {

    }
    
    func get(_ key: Int) -> Int {

    }
    
    func put(_ key: Int, _ value: Int) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
```

### Kotlin

```kotlin
class LRUCache(capacity: Int) {

    fun get(key: Int): Int {

    }

    fun put(key: Int, value: Int) {

    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### Go

```golang
type LRUCache struct {

}


func Constructor(capacity int) LRUCache {

}


func (this *LRUCache) Get(key int) int {

}


func (this *LRUCache) Put(key int, value int)  {

}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
```

### Ruby

```ruby
class LRUCache

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

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
```

### Scala

```scala
class LRUCache(_capacity: Int) {

    def get(key: Int): Int = {

    }

    def put(key: Int, value: Int) {

    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### Rust

```rust
struct LRUCache {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {

    fn new(capacity: i32) -> Self {

    }
    
    fn get(&self, key: i32) -> i32 {

    }
    
    fn put(&self, key: i32, value: i32) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
```

### Racket

```racket
(define lru-cache%
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

;; Your lru-cache% object will be instantiated and called as such:
;; (define obj (new lru-cache% [capacity capacity]))
;; (define param_1 (send obj get key))
;; (send obj put key value)
```

### Erlang

```erlang
-spec lru_cache_init_(Capacity :: integer()) -> any().
lru_cache_init_(Capacity) ->
  .

-spec lru_cache_get(Key :: integer()) -> integer().
lru_cache_get(Key) ->
  .

-spec lru_cache_put(Key :: integer(), Value :: integer()) -> any().
lru_cache_put(Key, Value) ->
  .


%% Your functions will be called as such:
%% lru_cache_init_(Capacity),
%% Param_1 = lru_cache_get(Key),
%% lru_cache_put(Key, Value),

%% lru_cache_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule LRUCache do
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
# LRUCache.init_(capacity)
# param_1 = LRUCache.get(key)
# LRUCache.put(key, value)

# LRUCache.init_ will be called before every test case, in which you can do some necessary initializations.
```

