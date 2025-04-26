# 380. O(1) 时间插入、删除和获取随机元素

## 题目描述

<p>实现<code>RandomizedSet</code> 类：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>RandomizedSet()</code> 初始化 <code>RandomizedSet</code> 对象</li>
	<li><code>bool insert(int val)</code> 当元素 <code>val</code> 不存在时，向集合中插入该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>bool remove(int val)</code> 当元素 <code>val</code> 存在时，从集合中移除该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>int getRandom()</code> 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 <strong>相同的概率</strong> 被返回。</li>
</ul>

<p>你必须实现类的所有函数，并满足每个函数的 <strong>平均</strong> 时间复杂度为 <code>O(1)</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<strong>输出</strong>
[null, true, false, true, 2, true, false, 2]

<strong>解释</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>最多调用 <code>insert</code>、<code>remove</code> 和 <code>getRandom</code> 函数 <code>2 *&nbsp;</code><code>10<sup>5</sup></code> 次</li>
	<li>在调用 <code>getRandom</code> 方法时，数据结构中 <strong>至少存在一个</strong> 元素。</li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 数学
- 随机化

## 示例

```
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]
```

## 示例代码

### C++

```cpp
class RandomizedSet {
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        
    }
    
    bool remove(int val) {
        
    }
    
    int getRandom() {
        
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

### Java

```java
class RandomizedSet {

    public RandomizedSet() {
        
    }
    
    public boolean insert(int val) {
        
    }
    
    public boolean remove(int val) {
        
    }
    
    public int getRandom() {
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

### Python

```python
class RandomizedSet(object):

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
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

### Python3

```python3
class RandomizedSet:

    def __init__(self):
        

    def insert(self, val: int) -> bool:
        

    def remove(self, val: int) -> bool:
        

    def getRandom(self) -> int:
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

### C

```c



typedef struct {
    
} RandomizedSet;


RandomizedSet* randomizedSetCreate() {
    
}

bool randomizedSetInsert(RandomizedSet* obj, int val) {
    
}

bool randomizedSetRemove(RandomizedSet* obj, int val) {
    
}

int randomizedSetGetRandom(RandomizedSet* obj) {
    
}

void randomizedSetFree(RandomizedSet* obj) {
    
}

/**
 * Your RandomizedSet struct will be instantiated and called as such:
 * RandomizedSet* obj = randomizedSetCreate();
 * bool param_1 = randomizedSetInsert(obj, val);
 
 * bool param_2 = randomizedSetRemove(obj, val);
 
 * int param_3 = randomizedSetGetRandom(obj);
 
 * randomizedSetFree(obj);
*/
```

### C#

```csharp
public class RandomizedSet {

    public RandomizedSet() {
        
    }
    
    public bool Insert(int val) {
        
    }
    
    public bool Remove(int val) {
        
    }
    
    public int GetRandom() {
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
```

### JavaScript

```javascript

var RandomizedSet = function() {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

### TypeScript

```typescript
class RandomizedSet {
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
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

### PHP

```php
class RandomizedSet {
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
 * Your RandomizedSet object will be instantiated and called as such:
 * $obj = RandomizedSet();
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->remove($val);
 * $ret_3 = $obj->getRandom();
 */
```

### Swift

```swift

class RandomizedSet {

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
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet()
 * let ret_1: Bool = obj.insert(val)
 * let ret_2: Bool = obj.remove(val)
 * let ret_3: Int = obj.getRandom()
 */
```

### Kotlin

```kotlin
class RandomizedSet() {

    fun insert(`val`: Int): Boolean {
        
    }

    fun remove(`val`: Int): Boolean {
        
    }

    fun getRandom(): Int {
        
    }

}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = RandomizedSet()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
 */
```

### Dart

```dart
class RandomizedSet {

  RandomizedSet() {
    
  }
  
  bool insert(int val) {
    
  }
  
  bool remove(int val) {
    
  }
  
  int getRandom() {
    
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = RandomizedSet();
 * bool param1 = obj.insert(val);
 * bool param2 = obj.remove(val);
 * int param3 = obj.getRandom();
 */
```

### Go

```golang
type RandomizedSet struct {
    
}


func Constructor() RandomizedSet {
    
}


func (this *RandomizedSet) Insert(val int) bool {
    
}


func (this *RandomizedSet) Remove(val int) bool {
    
}


func (this *RandomizedSet) GetRandom() int {
    
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```

### Ruby

```ruby
class RandomizedSet
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

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()
```

### Scala

```scala
class RandomizedSet() {

    def insert(`val`: Int): Boolean = {
        
    }

    def remove(`val`: Int): Boolean = {
        
    }

    def getRandom(): Int = {
        
    }

}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * val obj = new RandomizedSet()
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.remove(`val`)
 * val param_3 = obj.getRandom()
 */
```

### Rust

```rust
struct RandomizedSet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

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
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
```

### Racket

```racket
(define randomized-set%
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

;; Your randomized-set% object will be instantiated and called as such:
;; (define obj (new randomized-set%))
;; (define param_1 (send obj insert val))
;; (define param_2 (send obj remove val))
;; (define param_3 (send obj get-random))
```

### Erlang

```erlang
-spec randomized_set_init_() -> any().
randomized_set_init_() ->
  .

-spec randomized_set_insert(Val :: integer()) -> boolean().
randomized_set_insert(Val) ->
  .

-spec randomized_set_remove(Val :: integer()) -> boolean().
randomized_set_remove(Val) ->
  .

-spec randomized_set_get_random() -> integer().
randomized_set_get_random() ->
  .


%% Your functions will be called as such:
%% randomized_set_init_(),
%% Param_1 = randomized_set_insert(Val),
%% Param_2 = randomized_set_remove(Val),
%% Param_3 = randomized_set_get_random(),

%% randomized_set_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RandomizedSet do
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
# RandomizedSet.init_()
# param_1 = RandomizedSet.insert(val)
# param_2 = RandomizedSet.remove(val)
# param_3 = RandomizedSet.get_random()

# RandomizedSet.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class RandomizedSet {
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
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj: RandomizedSet = RandomizedSet()
 * let param_1 = obj.insert(val)
 * let param_2 = obj.remove(val)
 * let param_3 = obj.getRandom()
 */
```

