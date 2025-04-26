# 3026. 最大好子数组和

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。</p>

<p>如果&nbsp;<code>nums</code>&nbsp;的一个<span data-keyword="subarray">子数组</span>中，第一个元素和最后一个元素 <strong>差的绝对值恰好</strong>&nbsp;为&nbsp;<code>k</code>&nbsp;，我们称这个子数组为&nbsp;<strong>好</strong>&nbsp;的。换句话说，如果子数组&nbsp;<code>nums[i..j]</code>&nbsp;满足&nbsp;<code>|nums[i] - nums[j]| == k</code>&nbsp;，那么它是一个好子数组。</p>

<p>请你返回&nbsp;<code>nums</code>&nbsp;中&nbsp;<strong>好</strong>&nbsp;子数组的&nbsp;<strong>最大</strong>&nbsp;和，如果没有好子数组，返回<em>&nbsp;</em><code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5,6], k = 1
<b>输出：</b>11
<b>解释：</b>好子数组中第一个元素和最后一个元素的差的绝对值必须为 1 。好子数组有 [1,2] ，[2,3] ，[3,4] ，[4,5] 和 [5,6] 。最大子数组和为 11 ，对应的子数组为 [5,6] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [-1,3,2,4,5], k = 3
<b>输出：</b>11
<b>解释：</b>好子数组中第一个元素和最后一个元素的差的绝对值必须为 3 。好子数组有 [-1,3,2] 和 [2,4,5] 。最大子数组和为 11 ，对应的子数组为 [2,4,5] 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [-1,-2,-3,-4], k = 2
<b>输出：</b>-6
<b>解释：</b>好子数组中第一个元素和最后一个元素的差的绝对值必须为 2 。好子数组有 [-1,-2,-3] 和 [-2,-3,-4] 。最大子数组和为 -6 ，对应的子数组为 [-1,-2,-3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Save all the prefix sums into a HashMap.
2. For the index <code>i</code> store the element at index <code>i + 1</code> as the key and the prefix sum till <code>i</code> as the value.
3. For each prefix sum ending at <code>nums[i]</code>, try finding <code>nums[i] - k</code> and <code>nums[i] + k</code> in the HashMap and update the answer.

## 示例

```
[1,2,3,4,5,6]
1
[-1,3,2,4,5]
3
[-1,-2,-3,-4]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long maximumSubarraySum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumSubarraySum(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumSubarraySum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSubarraySum(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSubarraySum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumSubarraySum(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_subarray_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
maximum_subarray_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_subarray_sum(nums :: [integer], k :: integer) :: integer
  def maximum_subarray_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSubarraySum(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

