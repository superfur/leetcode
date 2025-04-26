# 381. O(1) 时间插入、删除和获取随机元素 - 允许重复

## 题目描述

<p><code>RandomizedCollection</code> 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。</p>

<p>实现 <code>RandomizedCollection</code> 类:</p>

<ul>
	<li><code>RandomizedCollection()</code>初始化空的 <code>RandomizedCollection</code> 对象。</li>
	<li><code>bool insert(int val)</code>&nbsp;将一个 <code>val</code> 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 <code>true</code> ，否则返回 <code>false</code> 。</li>
	<li><code>bool remove(int val)</code>&nbsp;如果存在，从集合中移除一个 <code>val</code> 项。如果该项存在，则返回 <code>true</code> ，否则返回 <code>false</code> 。注意，如果 <code>val</code> 在集合中出现多次，我们只删除其中一个。</li>
	<li><code>int getRandom()</code> 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 <strong>线性相关</strong> 。</li>
</ul>

<p>您必须实现类的函数，使每个函数的 <strong>平均</strong> 时间复杂度为 <code>O(1)</code> 。</p>

<p><strong>注意：</strong>生成测试用例时，只有在 <code>RandomizedCollection</code> 中 <strong>至少有一项</strong> 时，才会调用 <code>getRandom</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入</strong>
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
<strong>输出</strong>
[null, true, false, true, 2, true, 1]

<strong>解释</strong>
RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
collection.insert(1);   // 返回 true，因为集合不包含 1。
                        // 将 1 插入到集合中。
collection.insert(1);   // 返回 false，因为集合包含 1。
&nbsp;                       // 将另一个 1 插入到集合中。集合现在包含 [1,1]。
collection.insert(2);   // 返回 true，因为集合不包含 2。
&nbsp;                       // 将 2 插入到集合中。集合现在包含 [1,1,2]。
collection.getRandom(); // getRandom 应当:
&nbsp;                       // 有 2/3 的概率返回 1,
&nbsp;                       // 1/3 的概率返回 2。
collection.remove(1);   // 返回 true，因为集合包含 1。
&nbsp;                       // 从集合中移除 1。集合现在包含 [1,2]。
collection.getRandom(); // getRandom 应该返回 1 或 2，两者的可能性相同。</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= val &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
	<li><code>insert</code>,&nbsp;<code>remove</code>&nbsp;和&nbsp;<code>getRandom</code>&nbsp;最多 <strong>总共</strong> 被调用&nbsp;<code>2 * 10<sup>5</sup></code>&nbsp;次</li>
	<li>当调用 <code>getRandom</code> 时，数据结构中 <strong>至少有一个</strong> 元素</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 数组
- 哈希表
- 数学
- 随机化

## 示例

```
["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]
[[],[1],[1],[2],[],[1],[]]
```

## 示例代码

### C++

```cpp
class RandomizedCollection {
public:
    RandomizedCollection() {
        
    }
    
    bool insert(int val) {
        
    }
    
    bool remove(int val) {
        
    }
    
    int getRandom() {
        
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

### Java

```java
class RandomizedCollection {

    public RandomizedCollection() {
        
    }
    
    public boolean insert(int val) {
        
    }
    
    public boolean remove(int val) {
        
    }
    
    public int getRandom() {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

### Python

```python
class RandomizedCollection(object):

    def __init__(self):
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        """
        :rtype: int
        """
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

### Python3

```python3
class RandomizedCollection:

    def __init__(self):
        

    def insert(self, val: int) -> bool:
        

    def remove(self, val: int) -> bool:
        

    def getRandom(self) -> int:
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

### C

```c



typedef struct {
    
} RandomizedCollection;


RandomizedCollection* randomizedCollectionCreate() {
    
}

bool randomizedCollectionInsert(RandomizedCollection* obj, int val) {
    
}

bool randomizedCollectionRemove(RandomizedCollection* obj, int val) {
    
}

int randomizedCollectionGetRandom(RandomizedCollection* obj) {
    
}

void randomizedCollectionFree(RandomizedCollection* obj) {
    
}

/**
 * Your RandomizedCollection struct will be instantiated and called as such:
 * RandomizedCollection* obj = randomizedCollectionCreate();
 * bool param_1 = randomizedCollectionInsert(obj, val);
 
 * bool param_2 = randomizedCollectionRemove(obj, val);
 
 * int param_3 = randomizedCollectionGetRandom(obj);
 
 * randomizedCollectionFree(obj);
*/
```

### C#

```csharp
public class RandomizedCollection {

    public RandomizedCollection() {
        
    }
    
    public bool Insert(int val) {
        
    }
    
    public bool Remove(int val) {
        
    }
    
    public int GetRandom() {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
```

### JavaScript

```javascript

var RandomizedCollection = function() {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedCollection.prototype.insert = function(val) {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedCollection.prototype.remove = function(val) {
    
};

/**
 * @return {number}
 */
RandomizedCollection.prototype.getRandom = function() {
    
};

/** 
 * Your RandomizedCollection object will be instantiated and called as such:
 * var obj = new RandomizedCollection()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

### TypeScript

```typescript
class RandomizedCollection {
    constructor() {
        
    }

    insert(val: number): boolean {
        
    }

    remove(val: number): boolean {
        
    }

    getRandom(): number {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * var obj = new RandomizedCollection()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

### PHP

```php
class RandomizedCollection {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        
    }
  
    /**
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        
    }
  
    /**
     * @return Integer
     */
    function getRandom() {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * $obj = RandomizedCollection();
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->remove($val);
 * $ret_3 = $obj->getRandom();
 */
```

### Swift

```swift

class RandomizedCollection {

    init() {
        
    }
    
    func insert(_ val: Int) -> Bool {
        
    }
    
    func remove(_ val: Int) -> Bool {
        
    }
    
    func getRandom() -> Int {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * let obj = RandomizedCollection()
 * let ret_1: Bool = obj.insert(val)
 * let ret_2: Bool = obj.remove(val)
 * let ret_3: Int = obj.getRandom()
 */
```

### Kotlin

```kotlin
class RandomizedCollection() {

    fun insert(`val`: Int): Boolean {
        
    }

    fun remove(`val`: Int): Boolean {
        
    }

    fun getRandom(): Int {
        
    }

}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * var obj = RandomizedCollection()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
 */
```

### Dart

```dart
class RandomizedCollection {

  RandomizedCollection() {
    
  }
  
  bool insert(int val) {
    
  }
  
  bool remove(int val) {
    
  }
  
  int getRandom() {
    
  }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = RandomizedCollection();
 * bool param1 = obj.insert(val);
 * bool param2 = obj.remove(val);
 * int param3 = obj.getRandom();
 */
```

### Go

```golang
type RandomizedCollection struct {
    
}


func Constructor() RandomizedCollection {
    
}


func (this *RandomizedCollection) Insert(val int) bool {
    
}


func (this *RandomizedCollection) Remove(val int) bool {
    
}


func (this *RandomizedCollection) GetRandom() int {
    
}


/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```

### Ruby

```ruby
class RandomizedCollection
    def initialize()
        
    end


=begin
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)
        
    end


=begin
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)
        
    end


=begin
    :rtype: Integer
=end
    def get_random()
        
    end


end

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()
```

### Scala

```scala
class RandomizedCollection() {

    def insert(`val`: Int): Boolean = {
        
    }

    def remove(`val`: Int): Boolean = {
        
    }

    def getRandom(): Int = {
        
    }

}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * val obj = new RandomizedCollection()
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.remove(`val`)
 * val param_3 = obj.getRandom()
 */
```

### Rust

```rust
struct RandomizedCollection {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedCollection {

    fn new() -> Self {
        
    }
    
    fn insert(&self, val: i32) -> bool {
        
    }
    
    fn remove(&self, val: i32) -> bool {
        
    }
    
    fn get_random(&self) -> i32 {
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * let obj = RandomizedCollection::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
```

### Racket

```racket
(define randomized-collection%
  (class object%
    (super-new)
    
    (init-field)
    
    ; insert : exact-integer? -> boolean?
    (define/public (insert val)
      )
    ; remove : exact-integer? -> boolean?
    (define/public (remove val)
      )
    ; get-random : -> exact-integer?
    (define/public (get-random)
      )))

;; Your randomized-collection% object will be instantiated and called as such:
;; (define obj (new randomized-collection%))
;; (define param_1 (send obj insert val))
;; (define param_2 (send obj remove val))
;; (define param_3 (send obj get-random))
```

### Erlang

```erlang
-spec randomized_collection_init_() -> any().
randomized_collection_init_() ->
  .

-spec randomized_collection_insert(Val :: integer()) -> boolean().
randomized_collection_insert(Val) ->
  .

-spec randomized_collection_remove(Val :: integer()) -> boolean().
randomized_collection_remove(Val) ->
  .

-spec randomized_collection_get_random() -> integer().
randomized_collection_get_random() ->
  .


%% Your functions will be called as such:
%% randomized_collection_init_(),
%% Param_1 = randomized_collection_insert(Val),
%% Param_2 = randomized_collection_remove(Val),
%% Param_3 = randomized_collection_get_random(),

%% randomized_collection_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RandomizedCollection do
  @spec init_() :: any
  def init_() do
    
  end

  @spec insert(val :: integer) :: boolean
  def insert(val) do
    
  end

  @spec remove(val :: integer) :: boolean
  def remove(val) do
    
  end

  @spec get_random() :: integer
  def get_random() do
    
  end
end

# Your functions will be called as such:
# RandomizedCollection.init_()
# param_1 = RandomizedCollection.insert(val)
# param_2 = RandomizedCollection.remove(val)
# param_3 = RandomizedCollection.get_random()

# RandomizedCollection.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class RandomizedCollection {
    init() {

    }
    
    func insert(val: Int64): Bool {

    }
    
    func remove(val: Int64): Bool {

    }
    
    func getRandom(): Int64 {

    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * let obj: RandomizedCollection = RandomizedCollection()
 * let param_1 = obj.insert(val)
 * let param_2 = obj.remove(val)
 * let param_3 = obj.getRandom()
 */
```

