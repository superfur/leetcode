# 384. 打乱数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是&nbsp;<strong>等可能</strong>&nbsp;的。</p>

<p>实现 <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int[] nums)</code> 使用整数数组 <code>nums</code> 初始化对象</li>
	<li><code>int[] reset()</code> 重设数组到它的初始状态并返回</li>
	<li><code>int[] shuffle()</code> 返回数组随机打乱后的结果</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
<strong>输出</strong>
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

<strong>解释</strong>
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>nums</code> 中的所有元素都是 <strong>唯一的</strong></li>
	<li>最多可以调用 <code>10<sup>4</sup></code> 次 <code>reset</code> 和 <code>shuffle</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 数学
- 随机化

## 提示

1. The solution expects that we always use the original array to shuffle() else some of the test cases fail. (Credits; @snehasingh31)

## 示例

```
["Solution","shuffle","reset","shuffle"]
[[[1,2,3]],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(vector<int>& nums) {
        
    }
    
    vector<int> reset() {
        
    }
    
    vector<int> shuffle() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```

### Java

```java
class Solution {

    public Solution(int[] nums) {
        
    }
    
    public int[] reset() {
        
    }
    
    public int[] shuffle() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        

    def reset(self):
        """
        :rtype: List[int]
        """
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

### Python3

```python3
class Solution:

    def __init__(self, nums: List[int]):
        

    def reset(self) -> List[int]:
        

    def shuffle(self) -> List[int]:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int* nums, int numsSize) {
    
}

int* solutionReset(Solution* obj, int* retSize) {
    
}

int* solutionShuffle(Solution* obj, int* retSize) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(nums, numsSize);
 * int* param_1 = solutionReset(obj, retSize);
 
 * int* param_2 = solutionShuffle(obj, retSize);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int[] nums) {
        
    }
    
    public int[] Reset() {
        
    }
    
    public int[] Shuffle() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.Reset();
 * int[] param_2 = obj.Shuffle();
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(nums: number[]) {
        
    }

    reset(): number[] {
        
    }

    shuffle(): number[] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        
    }
  
    /**
     * @return Integer[]
     */
    function reset() {
        
    }
  
    /**
     * @return Integer[]
     */
    function shuffle() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($nums);
 * $ret_1 = $obj->reset();
 * $ret_2 = $obj->shuffle();
 */
```

### Swift

```swift

class Solution {

    init(_ nums: [Int]) {
        
    }
    
    func reset() -> [Int] {
        
    }
    
    func shuffle() -> [Int] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(nums)
 * let ret_1: [Int] = obj.reset()
 * let ret_2: [Int] = obj.shuffle()
 */
```

### Kotlin

```kotlin
class Solution(nums: IntArray) {

    fun reset(): IntArray {
        
    }

    fun shuffle(): IntArray {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

### Dart

```dart
class Solution {

  Solution(List<int> nums) {
    
  }
  
  List<int> reset() {
    
  }
  
  List<int> shuffle() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(nums);
 * List<int> param1 = obj.reset();
 * List<int> param2 = obj.shuffle();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(nums []int) Solution {
    
}


func (this *Solution) Reset() []int {
    
}


func (this *Solution) Shuffle() []int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
        
    end


=begin
    :rtype: Integer[]
=end
    def reset()
        
    end


=begin
    :rtype: Integer[]
=end
    def shuffle()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

### Scala

```scala
class Solution(_nums: Array[Int]) {

    def reset(): Array[Int] = {
        
    }

    def shuffle(): Array[Int] = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(nums)
 * val param_1 = obj.reset()
 * val param_2 = obj.shuffle()
 */
```

### Rust

```rust
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(nums: Vec<i32>) -> Self {
        
    }
    
    fn reset(&self) -> Vec<i32> {
        
    }
    
    fn shuffle(&self) -> Vec<i32> {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: Vec<i32> = obj.reset();
 * let ret_2: Vec<i32> = obj.shuffle();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; nums : (listof exact-integer?)
    (init-field
      nums)
    
    ; reset : -> (listof exact-integer?)
    (define/public (reset)
      )
    ; shuffle : -> (listof exact-integer?)
    (define/public (shuffle)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [nums nums]))
;; (define param_1 (send obj reset))
;; (define param_2 (send obj shuffle))
```

### Erlang

```erlang
-spec solution_init_(Nums :: [integer()]) -> any().
solution_init_(Nums) ->
  .

-spec solution_reset() -> [integer()].
solution_reset() ->
  .

-spec solution_shuffle() -> [integer()].
solution_shuffle() ->
  .


%% Your functions will be called as such:
%% solution_init_(Nums),
%% Param_1 = solution_reset(),
%% Param_2 = solution_shuffle(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    
  end

  @spec reset() :: [integer]
  def reset() do
    
  end

  @spec shuffle() :: [integer]
  def shuffle() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(nums)
# param_1 = Solution.reset()
# param_2 = Solution.shuffle()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(nums: Array<Int64>) {

    }
    
    func reset(): Array<Int64> {

    }
    
    func shuffle(): Array<Int64> {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(nums)
 * let param_1 = obj.reset()
 * let param_2 = obj.shuffle()
 */
```

