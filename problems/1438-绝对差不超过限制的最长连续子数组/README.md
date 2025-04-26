# 1438. 绝对差不超过限制的最长连续子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，和一个表示限制的整数 <code>limit</code>，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 <code>limit</code><em> 。</em></p>

<p>如果不存在满足条件的子数组，则返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [8,2,4,7], limit = 4
<strong>输出：</strong>2 
<strong>解释：</strong>所有子数组如下：
[8] 最大绝对差 |8-8| = 0 &lt;= 4.
[8,2] 最大绝对差 |8-2| = 6 &gt; 4. 
[8,2,4] 最大绝对差 |8-2| = 6 &gt; 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 &gt; 4.
[2] 最大绝对差 |2-2| = 0 &lt;= 4.
[2,4] 最大绝对差 |2-4| = 2 &lt;= 4.
[2,4,7] 最大绝对差 |2-7| = 5 &gt; 4.
[4] 最大绝对差 |4-4| = 0 &lt;= 4.
[4,7] 最大绝对差 |4-7| = 3 &lt;= 4.
[7] 最大绝对差 |7-7| = 0 &lt;= 4. 
因此，满足题意的最长子数组的长度为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [10,1,2,4,7,2], limit = 5
<strong>输出：</strong>4 
<strong>解释：</strong>满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 &lt;= 5 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [4,2,2,2,4,4,2,2], limit = 0
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= limit &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 队列
- 数组
- 有序集合
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 提示

1. Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.
2. More specifically, use the two pointer technique, moving the right pointer as far as possible to the right until the subarray is not valid (maxValue - minValue > limit), then moving the left pointer until the subarray is valid again (maxValue - minValue <= limit). Keep repeating this process.

## 示例

```
[8,2,4,7]
4
[10,1,2,4,7,2]
5
[4,2,2,2,4,4,2,2]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubarray(int[] nums, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
```

### C

```c
int longestSubarray(int* nums, int numsSize, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var longestSubarray = function(nums, limit) {
    
};
```

### TypeScript

```typescript
function longestSubarray(nums: number[], limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer
     */
    function longestSubarray($nums, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray, limit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubarray(List<int> nums, int limit) {
    
  }
}
```

### Go

```golang
func longestSubarray(nums []int, limit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer}
def longest_subarray(nums, limit)
    
end
```

### Scala

```scala
object Solution {
    def longestSubarray(nums: Array[Int], limit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subarray nums limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_subarray(Nums :: [integer()], Limit :: integer()) -> integer().
longest_subarray(Nums, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer], limit :: integer) :: integer
  def longest_subarray(nums, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubarray(nums: Array<Int64>, limit: Int64): Int64 {

    }
}
```

