# 2289. 使数组按非递减顺序排列

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。在一步操作中，移除所有满足&nbsp;<code>nums[i - 1] &gt; nums[i]</code> 的 <code>nums[i]</code> ，其中 <code>0 &lt; i &lt; nums.length</code> 。</p>

<p>重复执行步骤，直到 <code>nums</code> 变为 <strong>非递减</strong> 数组，返回所需执行的操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,3,4,4,7,3,6,11,8,5,11]
<strong>输出：</strong>3
<strong>解释：</strong>执行下述几个步骤：
- 步骤 1 ：[5,<em><strong>3</strong></em>,4,4,7,<em><strong>3</strong></em>,6,11,<em><strong>8</strong></em>,<em><strong>5</strong></em>,11] 变为 [5,4,4,7,6,11,11]
- 步骤 2 ：[5,<em><strong>4</strong></em>,4,7,<em><strong>6</strong></em>,11,11] 变为 [5,4,7,11,11]
- 步骤 3 ：[5,<em><strong>4</strong></em>,7,11,11] 变为 [5,7,11,11]
[5,7,11,11] 是一个非递减数组，因此，返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,7,7,13]
<strong>输出：</strong>0
<strong>解释：</strong>nums 已经是一个非递减数组，因此，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 链表
- 单调栈

## 提示

1. Notice that an element will be removed if and only if there exists a strictly greater element to the left of it in the array.
2. For each element, we need to find the number of rounds it will take for it to be removed. The answer is the maximum number of rounds for all elements. Build an array dp to hold this information where the answer is the maximum value of dp.
3. Use a stack of the indices. While processing element nums[i], remove from the stack all the indices of elements that are smaller than nums[i]. dp[i] should be set to the maximum of dp[i] + 1 and dp[removed index].

## 示例

```
[5,3,4,4,7,3,6,11,8,5,11]
[4,5,7,7,13]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalSteps(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        
```

### C

```c
int totalSteps(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalSteps(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var totalSteps = function(nums) {
    
};
```

### TypeScript

```typescript
function totalSteps(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function totalSteps($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalSteps(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalSteps(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalSteps(List<int> nums) {
    
  }
}
```

### Go

```golang
func totalSteps(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def total_steps(nums)
    
end
```

### Scala

```scala
object Solution {
    def totalSteps(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_steps(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-steps nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec total_steps(Nums :: [integer()]) -> integer().
total_steps(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_steps(nums :: [integer]) :: integer
  def total_steps(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalSteps(nums: Array<Int64>): Int64 {

    }
}
```

