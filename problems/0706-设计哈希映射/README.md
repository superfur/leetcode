# 706. 设计哈希映射

## 题目描述

<p>不使用任何内建的哈希表库设计一个哈希映射（HashMap）。</p>

<p>实现 <code>MyHashMap</code> 类：</p>

<ul>
	<li><code>MyHashMap()</code> 用空映射初始化对象</li>
	<li><code>void put(int key, int value)</code> 向 HashMap 插入一个键值对 <code>(key, value)</code> 。如果 <code>key</code> 已经存在于映射中，则更新其对应的值 <code>value</code> 。</li>
	<li><code>int get(int key)</code> 返回特定的 <code>key</code> 所映射的 <code>value</code> ；如果映射中不包含 <code>key</code> 的映射，返回 <code>-1</code> 。</li>
	<li><code>void remove(key)</code> 如果映射中存在 <code>key</code> 的映射，则移除 <code>key</code> 和它所对应的 <code>value</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
<strong>输出</strong>：
[null, null, null, 1, -1, null, 1, null, -1]

<strong>解释</strong>：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= key, value &lt;= 10<sup>6</sup></code></li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>put</code>、<code>get</code> 和 <code>remove</code> 方法</li>
</ul>


## 难度

Easy

## 标签

- 设计
- 数组
- 哈希表
- 链表
- 哈希函数

## 示例

```
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
```

## 示例代码

### C++

```cpp
class MyHashMap {
public:
    MyHashMap() {
        
    }
    
    void put(int key, int value) {
        
    }
    
    int get(int key) {
        
    }
    
    void remove(int key) {
        
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```

### Java

```java
class MyHashMap {

    public MyHashMap() {
        
    }
    
    public void put(int key, int value) {
        
    }
    
    public int get(int key) {
        
    }
    
    public void remove(int key) {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

### Python

```python
class MyHashMap(object):

    def __init__(self):
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

### Python3

```python3
class MyHashMap:

    def __init__(self):
        

    def put(self, key: int, value: int) -> None:
        

    def get(self, key: int) -> int:
        

    def remove(self, key: int) -> None:
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

### C

```c



typedef struct {
    
} MyHashMap;


MyHashMap* myHashMapCreate() {
    
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    
}

int myHashMapGet(MyHashMap* obj, int key) {
    
}

void myHashMapRemove(MyHashMap* obj, int key) {
    
}

void myHashMapFree(MyHashMap* obj) {
    
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/
```

### C#

```csharp
public class MyHashMap {

    public MyHashMap() {
        
    }
    
    public void Put(int key, int value) {
        
    }
    
    public int Get(int key) {
        
    }
    
    public void Remove(int key) {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.Put(key,value);
 * int param_2 = obj.Get(key);
 * obj.Remove(key);
 */
```

### JavaScript

```javascript

var MyHashMap = function() {
    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    
};

/** 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
```

### TypeScript

```typescript
class MyHashMap {
    constructor() {
        
    }

    put(key: number, value: number): void {
        
    }

    get(key: number): number {
        
    }

    remove(key: number): void {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
```

### PHP

```php
class MyHashMap {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $key
     * @param Integer $value
     * @return NULL
     */
    function put($key, $value) {
        
    }
  
    /**
     * @param Integer $key
     * @return Integer
     */
    function get($key) {
        
    }
  
    /**
     * @param Integer $key
     * @return NULL
     */
    function remove($key) {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * $obj = MyHashMap();
 * $obj->put($key, $value);
 * $ret_2 = $obj->get($key);
 * $obj->remove($key);
 */
```

### Swift

```swift

class MyHashMap {

    init() {
        
    }
    
    func put(_ key: Int, _ value: Int) {
        
    }
    
    func get(_ key: Int) -> Int {
        
    }
    
    func remove(_ key: Int) {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap()
 * obj.put(key, value)
 * let ret_2: Int = obj.get(key)
 * obj.remove(key)
 */
```

### Kotlin

```kotlin
class MyHashMap() {

    fun put(key: Int, value: Int) {
        
    }

    fun get(key: Int): Int {
        
    }

    fun remove(key: Int) {
        
    }

}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
```

### Dart

```dart
class MyHashMap {

  MyHashMap() {
    
  }
  
  void put(int key, int value) {
    
  }
  
  int get(int key) {
    
  }
  
  void remove(int key) {
    
  }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = MyHashMap();
 * obj.put(key,value);
 * int param2 = obj.get(key);
 * obj.remove(key);
 */
```

### Go

```golang
type MyHashMap struct {
    
}


func Constructor() MyHashMap {
    
}


func (this *MyHashMap) Put(key int, value int)  {
    
}


func (this *MyHashMap) Get(key int) int {
    
}


func (this *MyHashMap) Remove(key int)  {
    
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
```

### Ruby

```ruby
class MyHashMap
    def initialize()
        
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        
    end


end

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap.new()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
```

### Scala

```scala
class MyHashMap() {

    def put(key: Int, value: Int): Unit = {
        
    }

    def get(key: Int): Int = {
        
    }

    def remove(key: Int): Unit = {
        
    }

}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * val obj = new MyHashMap()
 * obj.put(key,value)
 * val param_2 = obj.get(key)
 * obj.remove(key)
 */
```

### Rust

```rust
struct MyHashMap {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {

    fn new() -> Self {
        
    }
    
    fn put(&self, key: i32, value: i32) {
        
    }
    
    fn get(&self, key: i32) -> i32 {
        
    }
    
    fn remove(&self, key: i32) {
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */
```

### Racket

```racket
(define my-hash-map%
  (class object%
    (super-new)
    
    (init-field)
    
    ; put : exact-integer? exact-integer? -> void?
    (define/public (put key value)
      )
    ; get : exact-integer? -> exact-integer?
    (define/public (get key)
      )
    ; remove : exact-integer? -> void?
    (define/public (remove key)
      )))

;; Your my-hash-map% object will be instantiated and called as such:
;; (define obj (new my-hash-map%))
;; (send obj put key value)
;; (define param_2 (send obj get key))
;; (send obj remove key)
```

### Erlang

```erlang
-spec my_hash_map_init_() -> any().
my_hash_map_init_() ->
  .

-spec my_hash_map_put(Key :: integer(), Value :: integer()) -> any().
my_hash_map_put(Key, Value) ->
  .

-spec my_hash_map_get(Key :: integer()) -> integer().
my_hash_map_get(Key) ->
  .

-spec my_hash_map_remove(Key :: integer()) -> any().
my_hash_map_remove(Key) ->
  .


%% Your functions will be called as such:
%% my_hash_map_init_(),
%% my_hash_map_put(Key, Value),
%% Param_2 = my_hash_map_get(Key),
%% my_hash_map_remove(Key),

%% my_hash_map_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyHashMap do
  @spec init_() :: any
  def init_() do
    
  end

  @spec put(key :: integer, value :: integer) :: any
  def put(key, value) do
    
  end

  @spec get(key :: integer) :: integer
  def get(key) do
    
  end

  @spec remove(key :: integer) :: any
  def remove(key) do
    
  end
end

# Your functions will be called as such:
# MyHashMap.init_()
# MyHashMap.put(key, value)
# param_2 = MyHashMap.get(key)
# MyHashMap.remove(key)

# MyHashMap.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyHashMap {
    init() {

    }
    
    func put(key: Int64, value: Int64): Unit {

    }
    
    func get(key: Int64): Int64 {

    }
    
    func remove(key: Int64): Unit {

    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj: MyHashMap = MyHashMap()
 * obj.put(key,value)
 * let param_2 = obj.get(key)
 * obj.remove(key)
 */
```

