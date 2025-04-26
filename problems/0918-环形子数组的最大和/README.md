# 918. 环形子数组的最大和

## 题目描述

<p>给定一个长度为 <code>n</code> 的<strong>环形整数数组</strong>&nbsp;<code>nums</code>&nbsp;，返回<em>&nbsp;<code>nums</code>&nbsp;的非空 <strong>子数组</strong> 的最大可能和&nbsp;</em>。</p>

<p><strong>环形数组</strong><em>&nbsp;</em>意味着数组的末端将会与开头相连呈环状。形式上， <code>nums[i]</code> 的下一个元素是 <code>nums[(i + 1) % n]</code> ， <code>nums[i]</code>&nbsp;的前一个元素是 <code>nums[(i - 1 + n) % n]</code> 。</p>

<p><strong>子数组</strong> 最多只能包含固定缓冲区&nbsp;<code>nums</code>&nbsp;中的每个元素一次。形式上，对于子数组&nbsp;<code>nums[i], nums[i + 1], ..., nums[j]</code>&nbsp;，不存在&nbsp;<code>i &lt;= k1, k2 &lt;= j</code>&nbsp;其中&nbsp;<code>k1 % n == k2 % n</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-2,3,-2]
<strong>输出：</strong>3
<strong>解释：</strong>从子数组 [3] 得到最大和 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,-3,5]
<strong>输出：</strong>10
<strong>解释：</strong>从子数组 [5,5] 得到最大和 5 + 5 = 10
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,-2,2,-3]
<strong>输出：</strong>3
<strong>解释：</strong>从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code>​​​​​​​</li>
</ul>


## 难度

Medium

## 标签

- 队列
- 数组
- 分治
- 动态规划
- 单调队列

## 提示

1. For those of you who are familiar with the <b>Kadane's algorithm</b>, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
2. What is an alternate way of representing a circular array so that it appears to be a straight array?
Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:

<br>
<img src="https://assets.leetcode.com/uploads/2019/10/20/circular_subarray_hint_1.png" width="700"/>
3. The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?

## 示例

```
[1,-2,3,-2]
[5,-3,5]
[-3,-2,-3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSubarraySumCircular(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSubarraySumCircular(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySumCircular = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSubarraySumCircular(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubarraySumCircular($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSubarraySumCircular(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSubarraySumCircular(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSubarraySumCircular(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSubarraySumCircular(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_subarray_sum_circular(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSubarraySumCircular(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-subarray-sum-circular nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_subarray_sum_circular(Nums :: [integer()]) -> integer().
max_subarray_sum_circular(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_subarray_sum_circular(nums :: [integer]) :: integer
  def max_subarray_sum_circular(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSubarraySumCircular(nums: Array<Int64>): Int64 {

    }
}
```

