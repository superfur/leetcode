# 2968. 执行操作使频率分数最大

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你可以对数组执行 <strong>至多</strong>&nbsp;<code>k</code>&nbsp;次操作：</p>

<ul>
	<li>从数组中选择一个下标 <code>i</code>&nbsp;，将&nbsp;<code>nums[i]</code> <strong>增加</strong>&nbsp;或者&nbsp;<strong>减少</strong>&nbsp;<code>1</code>&nbsp;。</li>
</ul>

<p>最终数组的频率分数定义为数组中众数的 <strong>频率</strong>&nbsp;。</p>

<p>请你返回你可以得到的 <strong>最大</strong>&nbsp;频率分数。</p>

<p>众数指的是数组中出现次数最多的数。一个元素的频率指的是数组中这个元素的出现次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,6,4], k = 3
<b>输出：</b>3
<b>解释：</b>我们可以对数组执行以下操作：
- 选择 i = 0 ，将 nums[0] 增加 1 。得到数组 [2,2,6,4] 。
- 选择 i = 3 ，将 nums[3] 减少 1 ，得到数组 [2,2,6,3] 。
- 选择 i = 3 ，将 nums[3] 减少 1 ，得到数组 [2,2,6,2] 。
元素 2 是最终数组中的众数，出现了 3 次，所以频率分数为 3 。
3 是所有可行方案里的最大频率分数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,4,2,4], k = 0
<b>输出：</b>3
<b>解释：</b>我们无法执行任何操作，所以得到的频率分数是原数组中众数的频率 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>14</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 前缀和
- 排序
- 滑动窗口

## 提示

1. If you sort the original array, it is optimal to apply the operations on one subarray such that all the elements of that subarray become equal.
2. You can use binary search to find the longest subarray where we can make the elements equal in at most <code>k</code> operations.

## 示例

```
[1,2,6,4]
3
[1,4,4,2,4]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxFrequencyScore(vector<int>& nums, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxFrequencyScore(int[] nums, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maxFrequencyScore(int* nums, int numsSize, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxFrequencyScore(int[] nums, long k) {
        
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
var maxFrequencyScore = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxFrequencyScore(nums: number[], k: number): number {
    
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
    function maxFrequencyScore($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxFrequencyScore(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxFrequencyScore(nums: IntArray, k: Long): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxFrequencyScore(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxFrequencyScore(nums []int, k int64) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency_score(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxFrequencyScore(nums: Array[Int], k: Long): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_frequency_score(nums: Vec<i32>, k: i64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-frequency-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_frequency_score(Nums :: [integer()], K :: integer()) -> integer().
max_frequency_score(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_frequency_score(nums :: [integer], k :: integer) :: integer
  def max_frequency_score(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxFrequencyScore(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

