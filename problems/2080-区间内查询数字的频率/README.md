# 2080. 区间内查询数字的频率

## 题目描述

<p>请你设计一个数据结构，它能求出给定子数组内一个给定值的 <strong>频率</strong>&nbsp;。</p>

<p>子数组中一个值的 <strong>频率</strong>&nbsp;指的是这个子数组中这个值的出现次数。</p>

<p>请你实现&nbsp;<code>RangeFreqQuery</code>&nbsp;类：</p>

<ul>
	<li><code>RangeFreqQuery(int[] arr)</code>&nbsp;用下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>arr</code>&nbsp;构造一个类的实例。</li>
	<li><code>int query(int left, int right, int value)</code>&nbsp;返回子数组&nbsp;<code>arr[left...right]</code>&nbsp;中&nbsp;<code>value</code>&nbsp;的&nbsp;<strong>频率</strong>&nbsp;。</li>
</ul>

<p>一个 <strong>子数组</strong> 指的是数组中一段连续的元素。<code>arr[left...right]</code>&nbsp;指的是 <code>nums</code>&nbsp;中包含下标 <code>left</code>&nbsp;和 <code>right</code>&nbsp;<strong>在内</strong>&nbsp;的中间一段连续元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
<strong>输出：</strong>
[null, 1, 2]

<strong>解释：</strong>
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], value &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt; arr.length</code></li>
	<li>调用&nbsp;<code>query</code>&nbsp;不超过&nbsp;<code>10<sup>5</sup></code>&nbsp;次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 线段树
- 数组
- 哈希表
- 二分查找

## 提示

1. The queries must be answered efficiently to avoid time limit exceeded verdict.
2. Store the elements of the array in a data structure that helps answering the queries efficiently.
3. Use a hash table that stored for each value, the indices where that value appeared.
4. Use binary search over the indices of a value to find its range frequency.

## 示例

```
["RangeFreqQuery","query","query"]
[[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]
```

## 示例代码

### C++

```cpp
class RangeFreqQuery {
public:
    RangeFreqQuery(vector<int>& arr) {
        
    }
    
    int query(int left, int right, int value) {
        
    }
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */
```

### Java

```java
class RangeFreqQuery {

    public RangeFreqQuery(int[] arr) {
        
    }
    
    public int query(int left, int right, int value) {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.query(left,right,value);
 */
```

### Python

```python
class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```

### Python3

```python3
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        

    def query(self, left: int, right: int, value: int) -> int:
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```

### C

```c



typedef struct {
    
} RangeFreqQuery;


RangeFreqQuery* rangeFreqQueryCreate(int* arr, int arrSize) {
    
}

int rangeFreqQueryQuery(RangeFreqQuery* obj, int left, int right, int value) {
    
}

void rangeFreqQueryFree(RangeFreqQuery* obj) {
    
}

/**
 * Your RangeFreqQuery struct will be instantiated and called as such:
 * RangeFreqQuery* obj = rangeFreqQueryCreate(arr, arrSize);
 * int param_1 = rangeFreqQueryQuery(obj, left, right, value);
 
 * rangeFreqQueryFree(obj);
*/
```

### C#

```csharp
public class RangeFreqQuery {

    public RangeFreqQuery(int[] arr) {
        
    }
    
    public int Query(int left, int right, int value) {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.Query(left,right,value);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 */
var RangeFreqQuery = function(arr) {
    
};

/** 
 * @param {number} left 
 * @param {number} right 
 * @param {number} value
 * @return {number}
 */
RangeFreqQuery.prototype.query = function(left, right, value) {
    
};

/** 
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = new RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */
```

### TypeScript

```typescript
class RangeFreqQuery {
    constructor(arr: number[]) {
        
    }

    query(left: number, right: number, value: number): number {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = new RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */
```

### PHP

```php
class RangeFreqQuery {
    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $value
     * @return Integer
     */
    function query($left, $right, $value) {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * $obj = RangeFreqQuery($arr);
 * $ret_1 = $obj->query($left, $right, $value);
 */
```

### Swift

```swift

class RangeFreqQuery {

    init(_ arr: [Int]) {
        
    }
    
    func query(_ left: Int, _ right: Int, _ value: Int) -> Int {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * let obj = RangeFreqQuery(arr)
 * let ret_1: Int = obj.query(left, right, value)
 */
```

### Kotlin

```kotlin
class RangeFreqQuery(arr: IntArray) {

    fun query(left: Int, right: Int, value: Int): Int {
        
    }

}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */
```

### Dart

```dart
class RangeFreqQuery {

  RangeFreqQuery(List<int> arr) {
    
  }
  
  int query(int left, int right, int value) {
    
  }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = RangeFreqQuery(arr);
 * int param1 = obj.query(left,right,value);
 */
```

### Go

```golang
type RangeFreqQuery struct {
    
}


func Constructor(arr []int) RangeFreqQuery {
    
}


func (this *RangeFreqQuery) Query(left int, right int, value int) int {
    
}


/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */
```

### Ruby

```ruby
class RangeFreqQuery

=begin
    :type arr: Integer[]
=end
    def initialize(arr)
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :type value: Integer
    :rtype: Integer
=end
    def query(left, right, value)
        
    end


end

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery.new(arr)
# param_1 = obj.query(left, right, value)
```

### Scala

```scala
class RangeFreqQuery(_arr: Array[Int]) {

    def query(left: Int, right: Int, value: Int): Int = {
        
    }

}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * val obj = new RangeFreqQuery(arr)
 * val param_1 = obj.query(left,right,value)
 */
```

### Rust

```rust
struct RangeFreqQuery {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RangeFreqQuery {

    fn new(arr: Vec<i32>) -> Self {
        
    }
    
    fn query(&self, left: i32, right: i32, value: i32) -> i32 {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * let obj = RangeFreqQuery::new(arr);
 * let ret_1: i32 = obj.query(left, right, value);
 */
```

### Racket

```racket
(define range-freq-query%
  (class object%
    (super-new)
    
    ; arr : (listof exact-integer?)
    (init-field
      arr)
    
    ; query : exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (query left right value)
      )))

;; Your range-freq-query% object will be instantiated and called as such:
;; (define obj (new range-freq-query% [arr arr]))
;; (define param_1 (send obj query left right value))
```

### Erlang

```erlang
-spec range_freq_query_init_(Arr :: [integer()]) -> any().
range_freq_query_init_(Arr) ->
  .

-spec range_freq_query_query(Left :: integer(), Right :: integer(), Value :: integer()) -> integer().
range_freq_query_query(Left, Right, Value) ->
  .


%% Your functions will be called as such:
%% range_freq_query_init_(Arr),
%% Param_1 = range_freq_query_query(Left, Right, Value),

%% range_freq_query_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RangeFreqQuery do
  @spec init_(arr :: [integer]) :: any
  def init_(arr) do
    
  end

  @spec query(left :: integer, right :: integer, value :: integer) :: integer
  def query(left, right, value) do
    
  end
end

# Your functions will be called as such:
# RangeFreqQuery.init_(arr)
# param_1 = RangeFreqQuery.query(left, right, value)

# RangeFreqQuery.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class RangeFreqQuery {
    init(arr: Array<Int64>) {

    }
    
    func query(left: Int64, right: Int64, value: Int64): Int64 {

    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * let obj: RangeFreqQuery = RangeFreqQuery(arr)
 * let param_1 = obj.query(left,right,value)
 */
```

