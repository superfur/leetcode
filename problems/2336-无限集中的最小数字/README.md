# 2336. 无限集中的最小数字

## 题目描述

<p>现有一个包含所有正整数的集合 <code>[1, 2, 3, 4, 5, ...]</code> 。</p>

<p>实现 <code>SmallestInfiniteSet</code> 类：</p>

<ul>
	<li><code>SmallestInfiniteSet()</code> 初始化 <strong>SmallestInfiniteSet</strong> 对象以包含 <strong>所有</strong> 正整数。</li>
	<li><code>int popSmallest()</code> <strong>移除</strong> 并返回该无限集中的最小整数。</li>
	<li><code>void addBack(int num)</code> 如果正整数 <code>num</code> <strong>不</strong> 存在于无限集中，则将一个 <code>num</code> <strong>添加</strong> 到该无限集中。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
<strong>输出</strong>
[null, null, 1, 2, 3, null, 1, 4, 5]

<strong>解释</strong>
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。
smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，
                                   // 且 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。
smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 1000</code></li>
	<li>最多调用 <code>popSmallest</code> 和 <code>addBack</code> 方法 <strong>共计</strong> <code>1000</code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 有序集合
- 堆（优先队列）

## 提示

1. Based on the constraints, what is the maximum element that can possibly be popped?
2. Maintain whether elements are in or not in the set. How many elements do we consider?

## 示例

```
["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
[[],[2],[],[],[],[1],[],[],[]]
```

## 示例代码

### C++

```cpp
class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
        
    }
    
    int popSmallest() {
        
    }
    
    void addBack(int num) {
        
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */
```

### Java

```java
class SmallestInfiniteSet {

    public SmallestInfiniteSet() {
        
    }
    
    public int popSmallest() {
        
    }
    
    public void addBack(int num) {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */
```

### Python

```python
class SmallestInfiniteSet(object):

    def __init__(self):
        

    def popSmallest(self):
        """
        :rtype: int
        """
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

### Python3

```python3
class SmallestInfiniteSet:

    def __init__(self):
        

    def popSmallest(self) -> int:
        

    def addBack(self, num: int) -> None:
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

### C

```c



typedef struct {
    
} SmallestInfiniteSet;


SmallestInfiniteSet* smallestInfiniteSetCreate() {
    
}

int smallestInfiniteSetPopSmallest(SmallestInfiniteSet* obj) {
    
}

void smallestInfiniteSetAddBack(SmallestInfiniteSet* obj, int num) {
    
}

void smallestInfiniteSetFree(SmallestInfiniteSet* obj) {
    
}

/**
 * Your SmallestInfiniteSet struct will be instantiated and called as such:
 * SmallestInfiniteSet* obj = smallestInfiniteSetCreate();
 * int param_1 = smallestInfiniteSetPopSmallest(obj);
 
 * smallestInfiniteSetAddBack(obj, num);
 
 * smallestInfiniteSetFree(obj);
*/
```

### C#

```csharp
public class SmallestInfiniteSet {

    public SmallestInfiniteSet() {
        
    }
    
    public int PopSmallest() {
        
    }
    
    public void AddBack(int num) {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.PopSmallest();
 * obj.AddBack(num);
 */
```

### JavaScript

```javascript

var SmallestInfiniteSet = function() {
    
};

/**
 * @return {number}
 */
SmallestInfiniteSet.prototype.popSmallest = function() {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
SmallestInfiniteSet.prototype.addBack = function(num) {
    
};

/** 
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = new SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

### TypeScript

```typescript
class SmallestInfiniteSet {
    constructor() {
        
    }

    popSmallest(): number {
        
    }

    addBack(num: number): void {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = new SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

### PHP

```php
class SmallestInfiniteSet {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @return Integer
     */
    function popSmallest() {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function addBack($num) {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * $obj = SmallestInfiniteSet();
 * $ret_1 = $obj->popSmallest();
 * $obj->addBack($num);
 */
```

### Swift

```swift

class SmallestInfiniteSet {

    init() {
        
    }
    
    func popSmallest() -> Int {
        
    }
    
    func addBack(_ num: Int) {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet()
 * let ret_1: Int = obj.popSmallest()
 * obj.addBack(num)
 */
```

### Kotlin

```kotlin
class SmallestInfiniteSet() {

    fun popSmallest(): Int {
        
    }

    fun addBack(num: Int) {
        
    }

}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

### Dart

```dart
class SmallestInfiniteSet {

  SmallestInfiniteSet() {
    
  }
  
  int popSmallest() {
    
  }
  
  void addBack(int num) {
    
  }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = SmallestInfiniteSet();
 * int param1 = obj.popSmallest();
 * obj.addBack(num);
 */
```

### Go

```golang
type SmallestInfiniteSet struct {
    
}


func Constructor() SmallestInfiniteSet {
    
}


func (this *SmallestInfiniteSet) PopSmallest() int {
    
}


func (this *SmallestInfiniteSet) AddBack(num int)  {
    
}


/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
```

### Ruby

```ruby
class SmallestInfiniteSet
    def initialize()
        
    end


=begin
    :rtype: Integer
=end
    def pop_smallest()
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_back(num)
        
    end


end

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet.new()
# param_1 = obj.pop_smallest()
# obj.add_back(num)
```

### Scala

```scala
class SmallestInfiniteSet() {

    def popSmallest(): Int = {
        
    }

    def addBack(num: Int): Unit = {
        
    }

}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * val obj = new SmallestInfiniteSet()
 * val param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

### Rust

```rust
struct SmallestInfiniteSet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SmallestInfiniteSet {

    fn new() -> Self {
        
    }
    
    fn pop_smallest(&self) -> i32 {
        
    }
    
    fn add_back(&self, num: i32) {
        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet::new();
 * let ret_1: i32 = obj.pop_smallest();
 * obj.add_back(num);
 */
```

### Racket

```racket
(define smallest-infinite-set%
  (class object%
    (super-new)
    
    (init-field)
    
    ; pop-smallest : -> exact-integer?
    (define/public (pop-smallest)
      )
    ; add-back : exact-integer? -> void?
    (define/public (add-back num)
      )))

;; Your smallest-infinite-set% object will be instantiated and called as such:
;; (define obj (new smallest-infinite-set%))
;; (define param_1 (send obj pop-smallest))
;; (send obj add-back num)
```

### Erlang

```erlang
-spec smallest_infinite_set_init_() -> any().
smallest_infinite_set_init_() ->
  .

-spec smallest_infinite_set_pop_smallest() -> integer().
smallest_infinite_set_pop_smallest() ->
  .

-spec smallest_infinite_set_add_back(Num :: integer()) -> any().
smallest_infinite_set_add_back(Num) ->
  .


%% Your functions will be called as such:
%% smallest_infinite_set_init_(),
%% Param_1 = smallest_infinite_set_pop_smallest(),
%% smallest_infinite_set_add_back(Num),

%% smallest_infinite_set_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SmallestInfiniteSet do
  @spec init_() :: any
  def init_() do
    
  end

  @spec pop_smallest() :: integer
  def pop_smallest() do
    
  end

  @spec add_back(num :: integer) :: any
  def add_back(num) do
    
  end
end

# Your functions will be called as such:
# SmallestInfiniteSet.init_()
# param_1 = SmallestInfiniteSet.pop_smallest()
# SmallestInfiniteSet.add_back(num)

# SmallestInfiniteSet.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SmallestInfiniteSet {
    init() {

    }
    
    func popSmallest(): Int64 {

    }
    
    func addBack(num: Int64): Unit {

    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj: SmallestInfiniteSet = SmallestInfiniteSet()
 * let param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

