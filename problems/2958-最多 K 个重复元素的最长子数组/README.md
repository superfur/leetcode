# 2958. 最多 K 个重复元素的最长子数组

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一个元素 <code>x</code>&nbsp;在数组中的 <strong>频率</strong>&nbsp;指的是它在数组中的出现次数。</p>

<p>如果一个数组中所有元素的频率都 <strong>小于等于&nbsp;</strong><code>k</code>&nbsp;，那么我们称这个数组是 <strong>好</strong>&nbsp;数组。</p>

<p>请你返回 <code>nums</code>&nbsp;中 <strong>最长好</strong>&nbsp;子数组的长度。</p>

<p><strong>子数组</strong> 指的是一个数组中一段连续非空的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,1,2,3,1,2], k = 2
<b>输出：</b>6
<strong>解释：</strong>最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。
最长好子数组的长度为 6 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1,2,1,2], k = 1
<b>输出：</b>2
<b>解释：</b>最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
最长好子数组的长度为 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [5,5,5,5,5,5,5], k = 4
<b>输出：</b>4
<b>解释：</b>最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
最长好子数组的长度为 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. For each index <code>i</code>, find the rightmost index <code>j >= i</code> such that the frequency of each element in the subarray <code>[i, j]</code> is at most <code>k</code>.
2. We can use 2 pointers / sliding window to achieve it.

## 示例

```
[1,2,3,1,2,3,1,2]
2
[1,2,1,2,1,2,1,2]
1
[5,5,5,5,5,5,5]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maxSubarrayLength(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
        
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
var maxSubarrayLength = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxSubarrayLength(nums: number[], k: number): number {
    
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
    function maxSubarrayLength($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSubarrayLength(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxSubarrayLength(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_length(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-subarray-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_subarray_length(Nums :: [integer()], K :: integer()) -> integer().
max_subarray_length(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_subarray_length(nums :: [integer], k :: integer) :: integer
  def max_subarray_length(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSubarrayLength(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

