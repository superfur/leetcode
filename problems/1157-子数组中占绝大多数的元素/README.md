# 1157. 子数组中占绝大多数的元素

## 题目描述

<p>设计一个数据结构，有效地找到给定子数组的 <strong>多数元素</strong> 。</p>

<p>子数组的 <strong>多数元素</strong> 是在子数组中出现&nbsp;<code>threshold</code>&nbsp;次数或次数以上的元素。</p>

<p>实现 <code>MajorityChecker</code> 类:</p>

<ul>
	<li><code>MajorityChecker(int[] arr)</code>&nbsp;会用给定的数组 <code>arr</code>&nbsp;对&nbsp;<code>MajorityChecker</code> 初始化。</li>
	<li><code>int query(int left, int right, int threshold)</code>&nbsp;返回子数组中的元素 &nbsp;<code>arr[left...right]</code>&nbsp;至少出现&nbsp;<code>threshold</code>&nbsp;次数，如果不存在这样的元素则返回 <code>-1</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong>
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
<strong>输出：</strong>
[null, 1, -1, 2]

<b>解释：</b>
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // 返回 1
majorityChecker.query(0,3,3); // 返回 -1
majorityChecker.query(2,3,2); // 返回 2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt; arr.length</code></li>
	<li><code>threshold &lt;= right - left + 1</code></li>
	<li><code>2 * threshold &gt; right - left + 1</code></li>
	<li>调用&nbsp;<code>query</code>&nbsp;的次数最多为&nbsp;<code>10<sup>4</sup></code>&nbsp;</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 树状数组
- 线段树
- 数组
- 二分查找

## 提示

1. What's special about a majority element ?
2. A majority element appears more than half the length of the array number of times.
3. If we tried a random index of the array, what's the probability that this index has a majority element ?
4. It's more than 50% if that array has a majority element.
5. Try a random index for a proper number of times so that the probability of not finding the answer tends to zero.

## 示例

```
["MajorityChecker","query","query","query"]
[[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]
```

## 示例代码

### C++

```cpp
class MajorityChecker {
public:
    MajorityChecker(vector<int>& arr) {
        
    }
    
    int query(int left, int right, int threshold) {
        
    }
};

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker* obj = new MajorityChecker(arr);
 * int param_1 = obj->query(left,right,threshold);
 */
```

### Java

```java
class MajorityChecker {

    public MajorityChecker(int[] arr) {
        
    }
    
    public int query(int left, int right, int threshold) {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.query(left,right,threshold);
 */
```

### Python

```python
class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
```

### Python3

```python3
class MajorityChecker:

    def __init__(self, arr: List[int]):
        

    def query(self, left: int, right: int, threshold: int) -> int:
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
```

### C

```c



typedef struct {
    
} MajorityChecker;


MajorityChecker* majorityCheckerCreate(int* arr, int arrSize) {
    
}

int majorityCheckerQuery(MajorityChecker* obj, int left, int right, int threshold) {
    
}

void majorityCheckerFree(MajorityChecker* obj) {
    
}

/**
 * Your MajorityChecker struct will be instantiated and called as such:
 * MajorityChecker* obj = majorityCheckerCreate(arr, arrSize);
 * int param_1 = majorityCheckerQuery(obj, left, right, threshold);
 
 * majorityCheckerFree(obj);
*/
```

### C#

```csharp
public class MajorityChecker {

    public MajorityChecker(int[] arr) {
        
    }
    
    public int Query(int left, int right, int threshold) {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.Query(left,right,threshold);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 */
var MajorityChecker = function(arr) {
    
};

/** 
 * @param {number} left 
 * @param {number} right 
 * @param {number} threshold
 * @return {number}
 */
MajorityChecker.prototype.query = function(left, right, threshold) {
    
};

/** 
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = new MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */
```

### TypeScript

```typescript
class MajorityChecker {
    constructor(arr: number[]) {
        
    }

    query(left: number, right: number, threshold: number): number {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = new MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */
```

### PHP

```php
class MajorityChecker {
    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $threshold
     * @return Integer
     */
    function query($left, $right, $threshold) {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * $obj = MajorityChecker($arr);
 * $ret_1 = $obj->query($left, $right, $threshold);
 */
```

### Swift

```swift

class MajorityChecker {

    init(_ arr: [Int]) {
        
    }
    
    func query(_ left: Int, _ right: Int, _ threshold: Int) -> Int {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * let obj = MajorityChecker(arr)
 * let ret_1: Int = obj.query(left, right, threshold)
 */
```

### Kotlin

```kotlin
class MajorityChecker(arr: IntArray) {

    fun query(left: Int, right: Int, threshold: Int): Int {
        
    }

}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */
```

### Dart

```dart
class MajorityChecker {

  MajorityChecker(List<int> arr) {
    
  }
  
  int query(int left, int right, int threshold) {
    
  }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = MajorityChecker(arr);
 * int param1 = obj.query(left,right,threshold);
 */
```

### Go

```golang
type MajorityChecker struct {
    
}


func Constructor(arr []int) MajorityChecker {
    
}


func (this *MajorityChecker) Query(left int, right int, threshold int) int {
    
}


/**
 * Your MajorityChecker object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,threshold);
 */
```

### Ruby

```ruby
class MajorityChecker

=begin
    :type arr: Integer[]
=end
    def initialize(arr)
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :type threshold: Integer
    :rtype: Integer
=end
    def query(left, right, threshold)
        
    end


end

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker.new(arr)
# param_1 = obj.query(left, right, threshold)
```

### Scala

```scala
class MajorityChecker(_arr: Array[Int]) {

    def query(left: Int, right: Int, threshold: Int): Int = {
        
    }

}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * val obj = new MajorityChecker(arr)
 * val param_1 = obj.query(left,right,threshold)
 */
```

### Rust

```rust
struct MajorityChecker {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MajorityChecker {

    fn new(arr: Vec<i32>) -> Self {
        
    }
    
    fn query(&self, left: i32, right: i32, threshold: i32) -> i32 {
        
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * let obj = MajorityChecker::new(arr);
 * let ret_1: i32 = obj.query(left, right, threshold);
 */
```

### Racket

```racket
(define majority-checker%
  (class object%
    (super-new)
    
    ; arr : (listof exact-integer?)
    (init-field
      arr)
    
    ; query : exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (query left right threshold)
      )))

;; Your majority-checker% object will be instantiated and called as such:
;; (define obj (new majority-checker% [arr arr]))
;; (define param_1 (send obj query left right threshold))
```

### Erlang

```erlang
-spec majority_checker_init_(Arr :: [integer()]) -> any().
majority_checker_init_(Arr) ->
  .

-spec majority_checker_query(Left :: integer(), Right :: integer(), Threshold :: integer()) -> integer().
majority_checker_query(Left, Right, Threshold) ->
  .


%% Your functions will be called as such:
%% majority_checker_init_(Arr),
%% Param_1 = majority_checker_query(Left, Right, Threshold),

%% majority_checker_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MajorityChecker do
  @spec init_(arr :: [integer]) :: any
  def init_(arr) do
    
  end

  @spec query(left :: integer, right :: integer, threshold :: integer) :: integer
  def query(left, right, threshold) do
    
  end
end

# Your functions will be called as such:
# MajorityChecker.init_(arr)
# param_1 = MajorityChecker.query(left, right, threshold)

# MajorityChecker.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MajorityChecker {
    init(arr: Array<Int64>) {

    }
    
    func query(left: Int64, right: Int64, threshold: Int64): Int64 {

    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * let obj: MajorityChecker = MajorityChecker(arr)
 * let param_1 = obj.query(left,right,threshold)
 */
```

