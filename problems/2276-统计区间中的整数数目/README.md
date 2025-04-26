# 2276. 统计区间中的整数数目

## 题目描述

<p>给你区间的 <strong>空</strong> 集，请你设计并实现满足要求的数据结构：</p>

<ul>
	<li><strong>新增：</strong>添加一个区间到这个区间集合中。</li>
	<li><strong>统计：</strong>计算出现在 <strong>至少一个</strong> 区间中的整数个数。</li>
</ul>

<p>实现 <code>CountIntervals</code> 类：</p>

<ul>
	<li><code>CountIntervals()</code> 使用区间的空集初始化对象</li>
	<li><code>void add(int left, int right)</code> 添加区间 <code>[left, right]</code> 到区间集合之中。</li>
	<li><code>int count()</code> 返回出现在 <strong>至少一个</strong> 区间中的整数个数。</li>
</ul>

<p><strong>注意：</strong>区间 <code>[left, right]</code> 表示满足 <code>left &lt;= x &lt;= right</code> 的所有整数 <code>x</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
<strong>输出</strong>
[null, null, null, 6, null, 8]

<strong>解释</strong>
CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
countIntervals.count();    // 返回 6
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 7、8、9、10 出现在区间 [7, 10] 中
countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
countIntervals.count();    // 返回 8
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 5 和 6 出现在区间 [5, 8] 中
                           // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
                           // 整数 9 和 10 出现在区间 [7, 10] 中</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>9</sup></code></li>
	<li>最多调用&nbsp; <code>add</code> 和 <code>count</code> 方法 <strong>总计</strong> <code>10<sup>5</sup></code> 次</li>
	<li>调用 <code>count</code> 方法至少一次</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 线段树
- 有序集合

## 提示

1. How can you efficiently add intervals to the set of intervals? Can a data structure like a Binary Search Tree help?
2. How can you ensure that the intervals present in the set are non-overlapping? Try merging the overlapping intervals whenever a new interval is added.
3. How can you update the count of integers present in at least one interval when a new interval is added to the set?

## 示例

```
["CountIntervals","add","add","count","add","count"]
[[],[2,3],[7,10],[],[5,8],[]]
```

## 示例代码

### C++

```cpp
class CountIntervals {
public:
    CountIntervals() {
        
    }
    
    void add(int left, int right) {
        
    }
    
    int count() {
        
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */
```

### Java

```java
class CountIntervals {

    public CountIntervals() {
        
    }
    
    public void add(int left, int right) {
        
    }
    
    public int count() {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = new CountIntervals();
 * obj.add(left,right);
 * int param_2 = obj.count();
 */
```

### Python

```python
class CountIntervals(object):

    def __init__(self):
        

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        

    def count(self):
        """
        :rtype: int
        """
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
```

### Python3

```python3
class CountIntervals:

    def __init__(self):
        

    def add(self, left: int, right: int) -> None:
        

    def count(self) -> int:
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
```

### C

```c



typedef struct {
    
} CountIntervals;


CountIntervals* countIntervalsCreate() {
    
}

void countIntervalsAdd(CountIntervals* obj, int left, int right) {
    
}

int countIntervalsCount(CountIntervals* obj) {
    
}

void countIntervalsFree(CountIntervals* obj) {
    
}

/**
 * Your CountIntervals struct will be instantiated and called as such:
 * CountIntervals* obj = countIntervalsCreate();
 * countIntervalsAdd(obj, left, right);
 
 * int param_2 = countIntervalsCount(obj);
 
 * countIntervalsFree(obj);
*/
```

### C#

```csharp
public class CountIntervals {

    public CountIntervals() {
        
    }
    
    public void Add(int left, int right) {
        
    }
    
    public int Count() {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = new CountIntervals();
 * obj.Add(left,right);
 * int param_2 = obj.Count();
 */
```

### JavaScript

```javascript

var CountIntervals = function() {
    
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
CountIntervals.prototype.add = function(left, right) {
    
};

/**
 * @return {number}
 */
CountIntervals.prototype.count = function() {
    
};

/** 
 * Your CountIntervals object will be instantiated and called as such:
 * var obj = new CountIntervals()
 * obj.add(left,right)
 * var param_2 = obj.count()
 */
```

### TypeScript

```typescript
class CountIntervals {
    constructor() {
        
    }

    add(left: number, right: number): void {
        
    }

    count(): number {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * var obj = new CountIntervals()
 * obj.add(left,right)
 * var param_2 = obj.count()
 */
```

### PHP

```php
class CountIntervals {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function add($left, $right) {
        
    }
  
    /**
     * @return Integer
     */
    function count() {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * $obj = CountIntervals();
 * $obj->add($left, $right);
 * $ret_2 = $obj->count();
 */
```

### Swift

```swift

class CountIntervals {

    init() {
        
    }
    
    func add(_ left: Int, _ right: Int) {
        
    }
    
    func count() -> Int {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * let obj = CountIntervals()
 * obj.add(left, right)
 * let ret_2: Int = obj.count()
 */
```

### Kotlin

```kotlin
class CountIntervals() {

    fun add(left: Int, right: Int) {
        
    }

    fun count(): Int {
        
    }

}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * var obj = CountIntervals()
 * obj.add(left,right)
 * var param_2 = obj.count()
 */
```

### Dart

```dart
class CountIntervals {

  CountIntervals() {
    
  }
  
  void add(int left, int right) {
    
  }
  
  int count() {
    
  }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = CountIntervals();
 * obj.add(left,right);
 * int param2 = obj.count();
 */
```

### Go

```golang
type CountIntervals struct {
    
}


func Constructor() CountIntervals {
    
}


func (this *CountIntervals) Add(left int, right int)  {
    
}


func (this *CountIntervals) Count() int {
    
}


/**
 * Your CountIntervals object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(left,right);
 * param_2 := obj.Count();
 */
```

### Ruby

```ruby
class CountIntervals
    def initialize()
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
    def add(left, right)
        
    end


=begin
    :rtype: Integer
=end
    def count()
        
    end


end

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals.new()
# obj.add(left, right)
# param_2 = obj.count()
```

### Scala

```scala
class CountIntervals() {

    def add(left: Int, right: Int): Unit = {
        
    }

    def count(): Int = {
        
    }

}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * val obj = new CountIntervals()
 * obj.add(left,right)
 * val param_2 = obj.count()
 */
```

### Rust

```rust
struct CountIntervals {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CountIntervals {

    fn new() -> Self {
        
    }
    
    fn add(&self, left: i32, right: i32) {
        
    }
    
    fn count(&self) -> i32 {
        
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * let obj = CountIntervals::new();
 * obj.add(left, right);
 * let ret_2: i32 = obj.count();
 */
```

### Racket

```racket
(define count-intervals%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : exact-integer? exact-integer? -> void?
    (define/public (add left right)
      )
    ; count : -> exact-integer?
    (define/public (count)
      )))

;; Your count-intervals% object will be instantiated and called as such:
;; (define obj (new count-intervals%))
;; (send obj add left right)
;; (define param_2 (send obj count))
```

### Erlang

```erlang
-spec count_intervals_init_() -> any().
count_intervals_init_() ->
  .

-spec count_intervals_add(Left :: integer(), Right :: integer()) -> any().
count_intervals_add(Left, Right) ->
  .

-spec count_intervals_count() -> integer().
count_intervals_count() ->
  .


%% Your functions will be called as such:
%% count_intervals_init_(),
%% count_intervals_add(Left, Right),
%% Param_2 = count_intervals_count(),

%% count_intervals_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule CountIntervals do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(left :: integer, right :: integer) :: any
  def add(left, right) do
    
  end

  @spec count() :: integer
  def count() do
    
  end
end

# Your functions will be called as such:
# CountIntervals.init_()
# CountIntervals.add(left, right)
# param_2 = CountIntervals.count()

# CountIntervals.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class CountIntervals {
    init() {

    }
    
    func add(left: Int64, right: Int64): Unit {

    }
    
    func count(): Int64 {

    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * let obj: CountIntervals = CountIntervals()
 * obj.add(left,right)
 * let param_2 = obj.count()
 */
```

