# 2760. 最长奇偶子数组

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>threshold</code> 。</p>

<p>请你从 <code>nums</code> 的子数组中找出以下标 <code>l</code> 开头、下标 <code>r</code> 结尾 <code>(0 &lt;= l &lt;= r &lt; nums.length)</code> 且满足以下条件的 <strong>最长子数组</strong> ：</p>

<ul>
	<li><code>nums[l] % 2 == 0</code></li>
	<li>对于范围&nbsp;<code>[l, r - 1]</code> 内的所有下标 <code>i</code> ，<code>nums[i] % 2 != nums[i + 1] % 2</code></li>
	<li>对于范围&nbsp;<code>[l, r]</code> 内的所有下标 <code>i</code> ，<code>nums[i] &lt;= threshold</code></li>
</ul>

<p>以整数形式返回满足题目要求的最长子数组的长度。</p>

<p><strong>注意：子数组</strong> 是数组中的一个连续非空元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,2,5,4], threshold = 5
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 =&gt; [2,5,4] ，满足上述条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2], threshold = 2
<strong>输出：</strong>1
<strong>解释：</strong>
在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 =&gt; [2] 。
该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,4,5], threshold = 4
<strong>输出：</strong>3
<strong>解释：</strong>
在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 =&gt; [2,3,4] 。 
该子数组满足上述全部条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100 </code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100 </code></li>
	<li><code>1 &lt;= threshold &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 滑动窗口

## 提示

1. Brute force all the possible subarrays and find the longest that satisfies the conditions.

## 示例

```
[3,2,5,4]
5
[1,2]
2
[2,3,4,5]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        
```

### C

```c
int longestAlternatingSubarray(int* nums, int numsSize, int threshold) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestAlternatingSubarray(int[] nums, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var longestAlternatingSubarray = function(nums, threshold) {
    
};
```

### TypeScript

```typescript
function longestAlternatingSubarray(nums: number[], threshold: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function longestAlternatingSubarray($nums, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestAlternatingSubarray(_ nums: [Int], _ threshold: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestAlternatingSubarray(nums: IntArray, threshold: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestAlternatingSubarray(List<int> nums, int threshold) {
    
  }
}
```

### Go

```golang
func longestAlternatingSubarray(nums []int, threshold int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def longest_alternating_subarray(nums, threshold)
    
end
```

### Scala

```scala
object Solution {
    def longestAlternatingSubarray(nums: Array[Int], threshold: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_alternating_subarray(nums: Vec<i32>, threshold: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-alternating-subarray nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_alternating_subarray(Nums :: [integer()], Threshold :: integer()) -> integer().
longest_alternating_subarray(Nums, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_alternating_subarray(nums :: [integer], threshold :: integer) :: integer
  def longest_alternating_subarray(nums, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestAlternatingSubarray(nums: Array<Int64>, threshold: Int64): Int64 {

    }
}
```

