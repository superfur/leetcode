# 705. 设计哈希集合

## 题目描述

<p>不使用任何内建的哈希表库设计一个哈希集合（HashSet）。</p>

<p>实现 <code>MyHashSet</code> 类：</p>

<ul>
	<li><code>void add(key)</code> 向哈希集合中插入值 <code>key</code> 。</li>
	<li><code>bool contains(key)</code> 返回哈希集合中是否存在这个值 <code>key</code> 。</li>
	<li><code>void remove(key)</code> 将给定值 <code>key</code> 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。</li>
</ul>
&nbsp;

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>输出：</strong>
[null, null, null, true, false, null, true, null, false]

<strong>解释：</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>add</code>、<code>remove</code> 和 <code>contains</code></li>
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
["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
[[],[1],[2],[1],[3],[2],[2],[2],[2]]
```

## 示例代码

### C++

```cpp
class MyHashSet {
public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        
    }
    
    void remove(int key) {
        
    }
    
    bool contains(int key) {
        
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
```

### Java

```java
class MyHashSet {

    public MyHashSet() {
        
    }
    
    public void add(int key) {
        
    }
    
    public void remove(int key) {
        
    }
    
    public boolean contains(int key) {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
```

### Python

```python
class MyHashSet(object):

    def __init__(self):
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

### Python3

```python3
class MyHashSet:

    def __init__(self):
        

    def add(self, key: int) -> None:
        

    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

### C

```c



typedef struct {
    
} MyHashSet;


MyHashSet* myHashSetCreate() {
    
}

void myHashSetAdd(MyHashSet* obj, int key) {
    
}

void myHashSetRemove(MyHashSet* obj, int key) {
    
}

bool myHashSetContains(MyHashSet* obj, int key) {
    
}

void myHashSetFree(MyHashSet* obj) {
    
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/
```

### C#

```csharp
public class MyHashSet {

    public MyHashSet() {
        
    }
    
    public void Add(int key) {
        
    }
    
    public void Remove(int key) {
        
    }
    
    public bool Contains(int key) {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */
```

### JavaScript

```javascript

var MyHashSet = function() {
    
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    
};

/** 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
    
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```

### TypeScript

```typescript
class MyHashSet {
    constructor() {
        
    }

    add(key: number): void {
        
    }

    remove(key: number): void {
        
    }

    contains(key: number): boolean {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```

### PHP

```php
class MyHashSet {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $key
     * @return NULL
     */
    function add($key) {
        
    }
  
    /**
     * @param Integer $key
     * @return NULL
     */
    function remove($key) {
        
    }
  
    /**
     * @param Integer $key
     * @return Boolean
     */
    function contains($key) {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * $obj = MyHashSet();
 * $obj->add($key);
 * $obj->remove($key);
 * $ret_3 = $obj->contains($key);
 */
```

### Swift

```swift

class MyHashSet {

    init() {
        
    }
    
    func add(_ key: Int) {
        
    }
    
    func remove(_ key: Int) {
        
    }
    
    func contains(_ key: Int) -> Bool {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * let ret_3: Bool = obj.contains(key)
 */
```

### Kotlin

```kotlin
class MyHashSet() {

    fun add(key: Int) {
        
    }

    fun remove(key: Int) {
        
    }

    fun contains(key: Int): Boolean {
        
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```

### Dart

```dart
class MyHashSet {

  MyHashSet() {
    
  }
  
  void add(int key) {
    
  }
  
  void remove(int key) {
    
  }
  
  bool contains(int key) {
    
  }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * bool param3 = obj.contains(key);
 */
```

### Go

```golang
type MyHashSet struct {
    
}


func Constructor() MyHashSet {
    
}


func (this *MyHashSet) Add(key int)  {
    
}


func (this *MyHashSet) Remove(key int)  {
    
}


func (this *MyHashSet) Contains(key int) bool {
    
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
```

### Ruby

```ruby
class MyHashSet
    def initialize()
        
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def add(key)
        
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        
    end


=begin
    :type key: Integer
    :rtype: Boolean
=end
    def contains(key)
        
    end


end

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet.new()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

### Scala

```scala
class MyHashSet() {

    def add(key: Int): Unit = {
        
    }

    def remove(key: Int): Unit = {
        
    }

    def contains(key: Int): Boolean = {
        
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * val obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * val param_3 = obj.contains(key)
 */
```

### Rust

```rust
struct MyHashSet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {
        
    }
    
    fn add(&self, key: i32) {
        
    }
    
    fn remove(&self, key: i32) {
        
    }
    
    fn contains(&self, key: i32) -> bool {
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
```

### Racket

```racket
(define my-hash-set%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : exact-integer? -> void?
    (define/public (add key)
      )
    ; remove : exact-integer? -> void?
    (define/public (remove key)
      )
    ; contains : exact-integer? -> boolean?
    (define/public (contains key)
      )))

;; Your my-hash-set% object will be instantiated and called as such:
;; (define obj (new my-hash-set%))
;; (send obj add key)
;; (send obj remove key)
;; (define param_3 (send obj contains key))
```

### Erlang

```erlang
-spec my_hash_set_init_() -> any().
my_hash_set_init_() ->
  .

-spec my_hash_set_add(Key :: integer()) -> any().
my_hash_set_add(Key) ->
  .

-spec my_hash_set_remove(Key :: integer()) -> any().
my_hash_set_remove(Key) ->
  .

-spec my_hash_set_contains(Key :: integer()) -> boolean().
my_hash_set_contains(Key) ->
  .


%% Your functions will be called as such:
%% my_hash_set_init_(),
%% my_hash_set_add(Key),
%% my_hash_set_remove(Key),
%% Param_3 = my_hash_set_contains(Key),

%% my_hash_set_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyHashSet do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(key :: integer) :: any
  def add(key) do
    
  end

  @spec remove(key :: integer) :: any
  def remove(key) do
    
  end

  @spec contains(key :: integer) :: boolean
  def contains(key) do
    
  end
end

# Your functions will be called as such:
# MyHashSet.init_()
# MyHashSet.add(key)
# MyHashSet.remove(key)
# param_3 = MyHashSet.contains(key)

# MyHashSet.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyHashSet {
    init() {

    }
    
    func add(key: Int64): Unit {

    }
    
    func remove(key: Int64): Unit {

    }
    
    func contains(key: Int64): Bool {

    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj: MyHashSet = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * let param_3 = obj.contains(key)
 */
```

