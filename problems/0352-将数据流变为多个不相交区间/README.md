# 352. 将数据流变为多个不相交区间

## 题目描述

<p>&nbsp;给你一个由非负整数&nbsp;<code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code> 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。</p>

<p>实现 <code>SummaryRanges</code> 类：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>SummaryRanges()</code> 使用一个空数据流初始化对象。</li>
	<li><code>void addNum(int val)</code> 向数据流中加入整数 <code>val</code> 。</li>
	<li><code>int[][] getIntervals()</code> 以不相交区间&nbsp;<code>[start<sub>i</sub>, end<sub>i</sub>]</code> 的列表形式返回对数据流中整数的总结。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
<strong>输出：</strong>
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

<strong>解释：</strong>
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>最多调用&nbsp;<code>addNum</code> 和 <code>getIntervals</code> 方法 <code>3 * 10<sup>4</sup></code> 次</li>
</ul>
</div>
</div>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?</p>


## 难度

Hard

## 标签

- 设计
- 二分查找
- 有序集合

## 示例

```
["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
[[],[1],[],[3],[],[7],[],[2],[],[6],[]]
```

## 示例代码

### C++

```cpp
class SummaryRanges {
public:
    SummaryRanges() {
        
    }
    
    void addNum(int value) {
        
    }
    
    vector<vector<int>> getIntervals() {
        
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
```

### Java

```java
class SummaryRanges {

    public SummaryRanges() {
        
    }
    
    public void addNum(int value) {
        
    }
    
    public int[][] getIntervals() {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(value);
 * int[][] param_2 = obj.getIntervals();
 */
```

### Python

```python
class SummaryRanges(object):

    def __init__(self):
        

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
```

### Python3

```python3
class SummaryRanges:

    def __init__(self):
        

    def addNum(self, value: int) -> None:
        

    def getIntervals(self) -> List[List[int]]:
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
```

### C

```c



typedef struct {
    
} SummaryRanges;


SummaryRanges* summaryRangesCreate() {
    
}

void summaryRangesAddNum(SummaryRanges* obj, int value) {
    
}

int** summaryRangesGetIntervals(SummaryRanges* obj, int* retSize, int** retColSize) {
    
}

void summaryRangesFree(SummaryRanges* obj) {
    
}

/**
 * Your SummaryRanges struct will be instantiated and called as such:
 * SummaryRanges* obj = summaryRangesCreate();
 * summaryRangesAddNum(obj, value);
 
 * int** param_2 = summaryRangesGetIntervals(obj, retSize, retColSize);
 
 * summaryRangesFree(obj);
*/
```

### C#

```csharp
public class SummaryRanges {

    public SummaryRanges() {
        
    }
    
    public void AddNum(int value) {
        
    }
    
    public int[][] GetIntervals() {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.AddNum(value);
 * int[][] param_2 = obj.GetIntervals();
 */
```

### JavaScript

```javascript

var SummaryRanges = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
SummaryRanges.prototype.addNum = function(value) {
    
};

/**
 * @return {number[][]}
 */
SummaryRanges.prototype.getIntervals = function() {
    
};

/** 
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = new SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
```

### TypeScript

```typescript
class SummaryRanges {
    constructor() {
        
    }

    addNum(value: number): void {
        
    }

    getIntervals(): number[][] {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = new SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
```

### PHP

```php
class SummaryRanges {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $value
     * @return NULL
     */
    function addNum($value) {
        
    }
  
    /**
     * @return Integer[][]
     */
    function getIntervals() {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * $obj = SummaryRanges();
 * $obj->addNum($value);
 * $ret_2 = $obj->getIntervals();
 */
```

### Swift

```swift

class SummaryRanges {

    init() {
        
    }
    
    func addNum(_ value: Int) {
        
    }
    
    func getIntervals() -> [[Int]] {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj = SummaryRanges()
 * obj.addNum(value)
 * let ret_2: [[Int]] = obj.getIntervals()
 */
```

### Kotlin

```kotlin
class SummaryRanges() {

    fun addNum(value: Int) {
        
    }

    fun getIntervals(): Array<IntArray> {
        
    }

}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
```

### Dart

```dart
class SummaryRanges {

  SummaryRanges() {
    
  }
  
  void addNum(int value) {
    
  }
  
  List<List<int>> getIntervals() {
    
  }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = SummaryRanges();
 * obj.addNum(value);
 * List<List<int>> param2 = obj.getIntervals();
 */
```

### Go

```golang
type SummaryRanges struct {
    
}


func Constructor() SummaryRanges {
    
}


func (this *SummaryRanges) AddNum(value int)  {
    
}


func (this *SummaryRanges) GetIntervals() [][]int {
    
}


/**
 * Your SummaryRanges object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(value);
 * param_2 := obj.GetIntervals();
 */
```

### Ruby

```ruby
class SummaryRanges
    def initialize()
        
    end


=begin
    :type value: Integer
    :rtype: Void
=end
    def add_num(value)
        
    end


=begin
    :rtype: Integer[][]
=end
    def get_intervals()
        
    end


end

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges.new()
# obj.add_num(value)
# param_2 = obj.get_intervals()
```

### Scala

```scala
class SummaryRanges() {

    def addNum(value: Int): Unit = {
        
    }

    def getIntervals(): Array[Array[Int]] = {
        
    }

}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * val obj = new SummaryRanges()
 * obj.addNum(value)
 * val param_2 = obj.getIntervals()
 */
```

### Rust

```rust
struct SummaryRanges {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SummaryRanges {

    fn new() -> Self {
        
    }
    
    fn add_num(&self, value: i32) {
        
    }
    
    fn get_intervals(&self) -> Vec<Vec<i32>> {
        
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj = SummaryRanges::new();
 * obj.add_num(value);
 * let ret_2: Vec<Vec<i32>> = obj.get_intervals();
 */
```

### Racket

```racket
(define summary-ranges%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add-num : exact-integer? -> void?
    (define/public (add-num value)
      )
    ; get-intervals : -> (listof (listof exact-integer?))
    (define/public (get-intervals)
      )))

;; Your summary-ranges% object will be instantiated and called as such:
;; (define obj (new summary-ranges%))
;; (send obj add-num value)
;; (define param_2 (send obj get-intervals))
```

### Erlang

```erlang
-spec summary_ranges_init_() -> any().
summary_ranges_init_() ->
  .

-spec summary_ranges_add_num(Value :: integer()) -> any().
summary_ranges_add_num(Value) ->
  .

-spec summary_ranges_get_intervals() -> [[integer()]].
summary_ranges_get_intervals() ->
  .


%% Your functions will be called as such:
%% summary_ranges_init_(),
%% summary_ranges_add_num(Value),
%% Param_2 = summary_ranges_get_intervals(),

%% summary_ranges_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SummaryRanges do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add_num(value :: integer) :: any
  def add_num(value) do
    
  end

  @spec get_intervals() :: [[integer]]
  def get_intervals() do
    
  end
end

# Your functions will be called as such:
# SummaryRanges.init_()
# SummaryRanges.add_num(value)
# param_2 = SummaryRanges.get_intervals()

# SummaryRanges.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SummaryRanges {
    init() {

    }
    
    func addNum(value: Int64): Unit {

    }
    
    func getIntervals(): Array<Array<Int64>> {

    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj: SummaryRanges = SummaryRanges()
 * obj.addNum(value)
 * let param_2 = obj.getIntervals()
 */
```

