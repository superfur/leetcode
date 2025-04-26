# 2972. 统计移除递增子数组的数目 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的 <b>正</b>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果 <code>nums</code>&nbsp;的一个子数组满足：移除这个子数组后剩余元素 <strong>严格递增</strong>&nbsp;，那么我们称这个子数组为 <strong>移除递增</strong>&nbsp;子数组。比方说，<code>[5, 3, 4, 6, 7]</code>&nbsp;中的 <code>[3, 4]</code>&nbsp;是一个移除递增子数组，因为移除该子数组后，<code>[5, 3, 4, 6, 7]</code>&nbsp;变为&nbsp;<code>[5, 6, 7]</code>&nbsp;，是严格递增的。</p>

<p>请你返回 <code>nums</code>&nbsp;中 <b>移除递增</b>&nbsp;子数组的总数目。</p>

<p><b>注意</b>&nbsp;，剩余元素为空的数组也视为是递增的。</p>

<p><strong>子数组</strong> 指的是一个数组中一段连续的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>10
<b>解释：</b>10 个移除递增子数组分别为：[1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4] 和 [1,2,3,4]。移除任意一个子数组后，剩余元素都是递增的。注意，空数组不是移除递增子数组。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [6,5,7,8]
<b>输出：</b>7
<b>解释：</b>7<strong>&nbsp;</strong>个移除递增子数组分别为：[5], [6], [5,7], [6,5], [5,7,8], [6,5,7] 和 [6,5,7,8] 。
nums 中只有这 7 个移除递增子数组。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [8,7,6,6]
<b>输出：</b>3
<b>解释：</b>3 个移除递增子数组分别为：[8,7,6], [7,6,6] 和 [8,7,6,6] 。注意 [8,7] 不是移除递增子数组因为移除 [8,7] 后 nums 变为 [6,6] ，它不是严格递增的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 双指针
- 二分查找

## 提示

1. Calculate the largest <code>x</code> such that <code>nums[0..x]</code> is strictly increasing.
2. Calculate the smallest <code>y</code> such that <code>nums[y..nums.length-1]</code> is strictly increasing.
3. For each <code>i</code> in <code>[0, x]</code>, select the smallest <code>j</code> in <code>[y, nums.length - 1]</code>. Then we can keep the prefix with any suffix of <code>[j, nums.length - 1]</code> (including the empty one).
4. Note that when <code>i</code> increases, <code>j</code> won’t decrease. Use two-pointers.
5. Note that we cannot delete an empty array, but we can delete the whole array.

## 示例

```
[1,2,3,4]
[6,5,7,8]
[8,7,6,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long incremovableSubarrayCount(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long incremovableSubarrayCount(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
```

### C

```c
long long incremovableSubarrayCount(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long IncremovableSubarrayCount(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var incremovableSubarrayCount = function(nums) {
    
};
```

### TypeScript

```typescript
function incremovableSubarrayCount(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function incremovableSubarrayCount($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func incremovableSubarrayCount(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun incremovableSubarrayCount(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int incremovableSubarrayCount(List<int> nums) {
    
  }
}
```

### Go

```golang
func incremovableSubarrayCount(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
    
end
```

### Scala

```scala
object Solution {
    def incremovableSubarrayCount(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (incremovable-subarray-count nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec incremovable_subarray_count(Nums :: [integer()]) -> integer().
incremovable_subarray_count(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec incremovable_subarray_count(nums :: [integer]) :: integer
  def incremovable_subarray_count(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func incremovableSubarrayCount(nums: Array<Int64>): Int64 {

    }
}
```

