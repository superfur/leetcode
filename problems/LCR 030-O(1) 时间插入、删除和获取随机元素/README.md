# LCR 030. O(1) 时间插入、删除和获取随机元素

## 题目描述

<p>设计一个支持在<em>平均&nbsp;</em>时间复杂度 <strong>O(1)</strong>&nbsp;下，执行以下操作的数据结构：</p>

<ul>
	<li><code>insert(val)</code>：当元素 <code>val</code> 不存在时返回 <code>true</code>&nbsp;，并向集合中插入该项，否则返回 <code>false</code> 。</li>
	<li><code>remove(val)</code>：当元素 <code>val</code> 存在时返回 <code>true</code>&nbsp;，并从集合中移除该项，否则返回 <code>false</code>&nbsp;。</li>
	<li><code>getRandom</code>：随机返回现有集合中的一项。每个元素应该有&nbsp;<strong>相同的概率&nbsp;</strong>被返回。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>inputs = [&quot;RandomizedSet&quot;, &quot;insert&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;]
[[], [1], [2], [2], [], [1], [2], []]
<strong>输出: </strong>[null, true, false, true, 2, true, false, 2]
<strong>解释:
</strong>RandomizedSet randomSet = new RandomizedSet();  // 初始化一个空的集合
randomSet.insert(1); // 向集合中插入 1 ， 返回 true 表示 1 被成功地插入

randomSet.remove(2); // 返回 false，表示集合中不存在 2 

randomSet.insert(2); // 向集合中插入 2 返回 true ，集合现在包含 [1,2] 

randomSet.getRandom(); // getRandom 应随机返回 1 或 2 
  
randomSet.remove(1); // 从集合中移除 1 返回 true 。集合现在包含 [2] 

randomSet.insert(2); // 2 已在集合中，所以返回 false 

randomSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong><meta charset="UTF-8" /></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= val &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
	<li>最多进行<code> 2 * 10<sup>5</sup></code> 次&nbsp;<code>insert</code> ， <code>remove</code> 和 <code>getRandom</code> 方法调用</li>
	<li>当调用&nbsp;<code>getRandom</code> 方法时，集合中至少有一个元素</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 380&nbsp;题相同：<a href="https://leetcode-cn.com/problems/insert-delete-getrandom-o1/">https://leetcode-cn.com/problems/insert-delete-getrandom-o1/</a></p>


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
    /** Initialize your data structure here. */
    RandomizedSet() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {

    }
    
    /** Get a random element from the set. */
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

    /** Initialize your data structure here. */
    public RandomizedSet() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {

    }
    
    /** Get a random element from the set. */
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
        """
        Initialize your data structure here.
        """


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """


    def getRandom(self):
        """
        Get a random element from the set.
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
        """
        Initialize your data structure here.
        """


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """



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

/** Initialize your data structure here. */

RandomizedSet* randomizedSetCreate() {

}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
bool randomizedSetInsert(RandomizedSet* obj, int val) {

}

/** Removes a value from the set. Returns true if the set contained the specified element. */
bool randomizedSetRemove(RandomizedSet* obj, int val) {

}

/** Get a random element from the set. */
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

    /** Initialize your data structure here. */
    public RandomizedSet() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public bool Insert(int val) {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public bool Remove(int val) {

    }
    
    /** Get a random element from the set. */
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
/**
 * Initialize your data structure here.
 */
var RandomizedSet = function() {

};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {

};

/**
 * Removes a value from the set. Returns true if the set contained the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {

};

/**
 * Get a random element from the set.
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
     * Initialize your data structure here.
     */
    function __construct() {

    }

    /**
     * Inserts a value to the set. Returns true if the set did not already contain the specified element.
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {

    }

    /**
     * Removes a value from the set. Returns true if the set contained the specified element.
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {

    }

    /**
     * Get a random element from the set.
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

    /** Initialize your data structure here. */
    init() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    func insert(_ val: Int) -> Bool {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    func remove(_ val: Int) -> Bool {

    }
    
    /** Get a random element from the set. */
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

    /** Initialize your data structure here. */


    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    fun insert(`val`: Int): Boolean {

    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    fun remove(`val`: Int): Boolean {

    }

    /** Get a random element from the set. */
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

### Go

```golang
type RandomizedSet struct {

}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {

}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {

}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {

}


/** Get a random element from the set. */
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

=begin
    Initialize your data structure here.
=end
    def initialize()

    end


=begin
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)

    end


=begin
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)

    end


=begin
    Get a random element from the set.
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

    /** Initialize your data structure here. */


    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    def insert(`val`: Int): Boolean = {

    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    def remove(`val`: Int): Boolean = {

    }

    /** Get a random element from the set. */
    def getRandom(): Int = {

    }

}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
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

    /** Initialize your data structure here. */
    fn new() -> Self {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    fn insert(&self, val: i32) -> bool {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    fn remove(&self, val: i32) -> bool {

    }
    
    /** Get a random element from the set. */
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

