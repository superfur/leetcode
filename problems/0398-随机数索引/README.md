# 398. 随机数索引

## 题目描述

<p>给你一个可能含有 <strong>重复元素</strong> 的整数数组&nbsp;<code>nums</code> ，请你随机输出给定的目标数字&nbsp;<code>target</code> 的索引。你可以假设给定的数字一定存在于数组中。</p>

<p>实现 <code>Solution</code> 类：</p>

<ul>
	<li><code>Solution(int[] nums)</code> 用数组 <code>nums</code> 初始化对象。</li>
	<li><code>int pick(int target)</code> 从 <code>nums</code> 中选出一个满足 <code>nums[i] == target</code> 的随机索引 <code>i</code> 。如果存在多个有效的索引，则每个索引的返回概率应当相等。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
<strong>输出</strong>
[null, 4, 0, 2]

<strong>解释</strong>
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
</pre>

<p>&nbsp;</p>

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>target</code> 是 <code>nums</code> 中的一个整数</li>
	<li>最多调用 <code>pick</code> 函数 <code>10<sup>4</sup></code> 次</li>
</ul>
</div>
</div>
</div>

<div class="fullscreen-btn-layer__2kn7">&nbsp;</div>


## 难度

Medium

## 标签

- 水塘抽样
- 哈希表
- 数学
- 随机化

## 示例

```
["Solution","pick","pick","pick"]
[[[1,2,3,3,3]],[3],[1],[3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(vector<int>& nums) {
        
    }
    
    int pick(int target) {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```

### Java

```java
class Solution {

    public Solution(int[] nums) {
        
    }
    
    public int pick(int target) {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```

### Python

```python
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

### Python3

```python3
class Solution:

    def __init__(self, nums: List[int]):
        

    def pick(self, target: int) -> int:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int* nums, int numsSize) {
    
}

int solutionPick(Solution* obj, int target) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(nums, numsSize);
 * int param_1 = solutionPick(obj, target);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int[] nums) {
        
    }
    
    public int Pick(int target) {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.Pick(target);
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
 * @param {number} target
 * @return {number}
 */
Solution.prototype.pick = function(target) {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.pick(target)
 */
```

### TypeScript

```typescript
class Solution {
    constructor(nums: number[]) {
        
    }

    pick(target: number): number {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.pick(target)
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
     * @param Integer $target
     * @return Integer
     */
    function pick($target) {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($nums);
 * $ret_1 = $obj->pick($target);
 */
```

### Swift

```swift

class Solution {

    init(_ nums: [Int]) {
        
    }
    
    func pick(_ target: Int) -> Int {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(nums)
 * let ret_1: Int = obj.pick(target)
 */
```

### Kotlin

```kotlin
class Solution(nums: IntArray) {

    fun pick(target: Int): Int {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(nums)
 * var param_1 = obj.pick(target)
 */
```

### Dart

```dart
class Solution {

  Solution(List<int> nums) {
    
  }
  
  int pick(int target) {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(nums);
 * int param1 = obj.pick(target);
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(nums []int) Solution {
    
}


func (this *Solution) Pick(target int) int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
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
    :type target: Integer
    :rtype: Integer
=end
    def pick(target)
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(nums)
# param_1 = obj.pick(target)
```

### Scala

```scala
class Solution(_nums: Array[Int]) {

    def pick(target: Int): Int = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(nums)
 * val param_1 = obj.pick(target)
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
    
    fn pick(&self, target: i32) -> i32 {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: i32 = obj.pick(target);
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
    
    ; pick : exact-integer? -> exact-integer?
    (define/public (pick target)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [nums nums]))
;; (define param_1 (send obj pick target))
```

### Erlang

```erlang
-spec solution_init_(Nums :: [integer()]) -> any().
solution_init_(Nums) ->
  .

-spec solution_pick(Target :: integer()) -> integer().
solution_pick(Target) ->
  .


%% Your functions will be called as such:
%% solution_init_(Nums),
%% Param_1 = solution_pick(Target),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    
  end

  @spec pick(target :: integer) :: integer
  def pick(target) do
    
  end
end

# Your functions will be called as such:
# Solution.init_(nums)
# param_1 = Solution.pick(target)

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(nums: Array<Int64>) {

    }
    
    func pick(target: Int64): Int64 {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(nums)
 * let param_1 = obj.pick(target)
 */
```

