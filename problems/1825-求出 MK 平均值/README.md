# 1825. 求出 MK 平均值

## 题目描述

<p>给你两个整数&nbsp;<code>m</code>&nbsp;和&nbsp;<code>k</code>&nbsp;，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 <b>MK 平均值</b>&nbsp;。</p>

<p><strong>MK 平均值</strong>&nbsp;按照如下步骤计算：</p>

<ol>
	<li>如果数据流中的整数少于 <code>m</code>&nbsp;个，<strong>MK 平均值</strong>&nbsp;为 <code>-1</code>&nbsp;，否则将数据流中最后 <code>m</code>&nbsp;个元素拷贝到一个独立的容器中。</li>
	<li>从这个容器中删除最小的 <code>k</code>&nbsp;个数和最大的 <code>k</code>&nbsp;个数。</li>
	<li>计算剩余元素的平均值，并 <strong>向下取整到最近的整数</strong>&nbsp;。</li>
</ol>

<p>请你实现&nbsp;<code>MKAverage</code>&nbsp;类：</p>

<ul>
	<li><code>MKAverage(int m, int k)</code>&nbsp;用一个空的数据流和两个整数 <code>m</code>&nbsp;和 <code>k</code>&nbsp;初始化&nbsp;<strong>MKAverage</strong>&nbsp;对象。</li>
	<li><code>void addElement(int num)</code>&nbsp;往数据流中插入一个新的元素&nbsp;<code>num</code>&nbsp;。</li>
	<li><code>int calculateMKAverage()</code>&nbsp;对当前的数据流计算并返回 <strong>MK 平均数</strong>&nbsp;，结果需 <strong>向下取整到最近的整数</strong> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
<strong>输出：</strong>
[null, null, null, -1, null, 3, null, null, null, 5]

<strong>解释：</strong>
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k*2 &lt; m</code></li>
	<li><code>1 &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li><code>addElement</code> 与&nbsp;<code>calculateMKAverage</code>&nbsp;总操作次数不超过 <code>10<sup>5</sup></code> 次。</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 队列
- 数据流
- 有序集合
- 堆（优先队列）

## 提示

1. At each query, try to save and update the sum of the elements needed to calculate MKAverage.
2. You can use BSTs for fast insertion and deletion of the elements.

## 示例

```
["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]
[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]
```

## 示例代码

### C++

```cpp
class MKAverage {
public:
    MKAverage(int m, int k) {
        
    }
    
    void addElement(int num) {
        
    }
    
    int calculateMKAverage() {
        
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */
```

### Java

```java
class MKAverage {

    public MKAverage(int m, int k) {
        
    }
    
    public void addElement(int num) {
        
    }
    
    public int calculateMKAverage() {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = new MKAverage(m, k);
 * obj.addElement(num);
 * int param_2 = obj.calculateMKAverage();
 */
```

### Python

```python
class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
```

### Python3

```python3
class MKAverage:

    def __init__(self, m: int, k: int):
        

    def addElement(self, num: int) -> None:
        

    def calculateMKAverage(self) -> int:
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
```

### C

```c



typedef struct {
    
} MKAverage;


MKAverage* mKAverageCreate(int m, int k) {
    
}

void mKAverageAddElement(MKAverage* obj, int num) {
    
}

int mKAverageCalculateMKAverage(MKAverage* obj) {
    
}

void mKAverageFree(MKAverage* obj) {
    
}

/**
 * Your MKAverage struct will be instantiated and called as such:
 * MKAverage* obj = mKAverageCreate(m, k);
 * mKAverageAddElement(obj, num);
 
 * int param_2 = mKAverageCalculateMKAverage(obj);
 
 * mKAverageFree(obj);
*/
```

### C#

```csharp
public class MKAverage {

    public MKAverage(int m, int k) {
        
    }
    
    public void AddElement(int num) {
        
    }
    
    public int CalculateMKAverage() {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = new MKAverage(m, k);
 * obj.AddElement(num);
 * int param_2 = obj.CalculateMKAverage();
 */
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} k
 */
var MKAverage = function(m, k) {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
MKAverage.prototype.addElement = function(num) {
    
};

/**
 * @return {number}
 */
MKAverage.prototype.calculateMKAverage = function() {
    
};

/** 
 * Your MKAverage object will be instantiated and called as such:
 * var obj = new MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

### TypeScript

```typescript
class MKAverage {
    constructor(m: number, k: number) {
        
    }

    addElement(num: number): void {
        
    }

    calculateMKAverage(): number {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * var obj = new MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

### PHP

```php
class MKAverage {
    /**
     * @param Integer $m
     * @param Integer $k
     */
    function __construct($m, $k) {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function addElement($num) {
        
    }
  
    /**
     * @return Integer
     */
    function calculateMKAverage() {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * $obj = MKAverage($m, $k);
 * $obj->addElement($num);
 * $ret_2 = $obj->calculateMKAverage();
 */
```

### Swift

```swift

class MKAverage {

    init(_ m: Int, _ k: Int) {
        
    }
    
    func addElement(_ num: Int) {
        
    }
    
    func calculateMKAverage() -> Int {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * let obj = MKAverage(m, k)
 * obj.addElement(num)
 * let ret_2: Int = obj.calculateMKAverage()
 */
```

### Kotlin

```kotlin
class MKAverage(m: Int, k: Int) {

    fun addElement(num: Int) {
        
    }

    fun calculateMKAverage(): Int {
        
    }

}

/**
 * Your MKAverage object will be instantiated and called as such:
 * var obj = MKAverage(m, k)
 * obj.addElement(num)
 * var param_2 = obj.calculateMKAverage()
 */
```

### Dart

```dart
class MKAverage {

  MKAverage(int m, int k) {
    
  }
  
  void addElement(int num) {
    
  }
  
  int calculateMKAverage() {
    
  }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage obj = MKAverage(m, k);
 * obj.addElement(num);
 * int param2 = obj.calculateMKAverage();
 */
```

### Go

```golang
type MKAverage struct {
    
}


func Constructor(m int, k int) MKAverage {
    
}


func (this *MKAverage) AddElement(num int)  {
    
}


func (this *MKAverage) CalculateMKAverage() int {
    
}


/**
 * Your MKAverage object will be instantiated and called as such:
 * obj := Constructor(m, k);
 * obj.AddElement(num);
 * param_2 := obj.CalculateMKAverage();
 */
```

### Ruby

```ruby
class MKAverage

=begin
    :type m: Integer
    :type k: Integer
=end
    def initialize(m, k)
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_element(num)
        
    end


=begin
    :rtype: Integer
=end
    def calculate_mk_average()
        
    end


end

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage.new(m, k)
# obj.add_element(num)
# param_2 = obj.calculate_mk_average()
```

### Scala

```scala
class MKAverage(_m: Int, _k: Int) {

    def addElement(num: Int): Unit = {
        
    }

    def calculateMKAverage(): Int = {
        
    }

}

/**
 * Your MKAverage object will be instantiated and called as such:
 * val obj = new MKAverage(m, k)
 * obj.addElement(num)
 * val param_2 = obj.calculateMKAverage()
 */
```

### Rust

```rust
struct MKAverage {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MKAverage {

    fn new(m: i32, k: i32) -> Self {
        
    }
    
    fn add_element(&self, num: i32) {
        
    }
    
    fn calculate_mk_average(&self) -> i32 {
        
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * let obj = MKAverage::new(m, k);
 * obj.add_element(num);
 * let ret_2: i32 = obj.calculate_mk_average();
 */
```

### Racket

```racket
(define mk-average%
  (class object%
    (super-new)
    
    ; m : exact-integer?
    ; k : exact-integer?
    (init-field
      m
      k)
    
    ; add-element : exact-integer? -> void?
    (define/public (add-element num)
      )
    ; calculate-mk-average : -> exact-integer?
    (define/public (calculate-mk-average)
      )))

;; Your mk-average% object will be instantiated and called as such:
;; (define obj (new mk-average% [m m] [k k]))
;; (send obj add-element num)
;; (define param_2 (send obj calculate-mk-average))
```

### Erlang

```erlang
-spec mk_average_init_(M :: integer(), K :: integer()) -> any().
mk_average_init_(M, K) ->
  .

-spec mk_average_add_element(Num :: integer()) -> any().
mk_average_add_element(Num) ->
  .

-spec mk_average_calculate_mk_average() -> integer().
mk_average_calculate_mk_average() ->
  .


%% Your functions will be called as such:
%% mk_average_init_(M, K),
%% mk_average_add_element(Num),
%% Param_2 = mk_average_calculate_mk_average(),

%% mk_average_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MKAverage do
  @spec init_(m :: integer, k :: integer) :: any
  def init_(m, k) do
    
  end

  @spec add_element(num :: integer) :: any
  def add_element(num) do
    
  end

  @spec calculate_mk_average() :: integer
  def calculate_mk_average() do
    
  end
end

# Your functions will be called as such:
# MKAverage.init_(m, k)
# MKAverage.add_element(num)
# param_2 = MKAverage.calculate_mk_average()

# MKAverage.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MKAverage {
    init(m: Int64, k: Int64) {

    }
    
    func addElement(num: Int64): Unit {

    }
    
    func calculateMKAverage(): Int64 {

    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * let obj: MKAverage = MKAverage(m, k)
 * obj.addElement(num)
 * let param_2 = obj.calculateMKAverage()
 */
```

