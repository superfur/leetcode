# 2771. 构造最长非递减子数组

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，长度均为 <code>n</code> 。</p>

<p>让我们定义另一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组，<code>nums3</code> 。对于范围&nbsp;<code>[0, n - 1]</code> 的每个下标 <code>i</code> ，你可以将 <code>nums1[i]</code> 或 <code>nums2[i]</code> 的值赋给 <code>nums3[i]</code> 。</p>

<p>你的任务是使用最优策略为 <code>nums3</code> 赋值，以最大化 <code>nums3</code> 中 <strong>最长非递减子数组</strong> 的长度。</p>

<p>以整数形式表示并返回 <code>nums3</code> 中 <strong>最长非递减</strong> 子数组的长度。</p>

<p><strong>注意：子数组</strong> 是数组中的一个连续非空元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums1 = [2,3,1], nums2 = [1,2,1]
<strong>输出：</strong>2
<strong>解释：</strong>构造 nums3 的方法之一是： 
nums3 = [nums1[0], nums2[1], nums2[2]] =&gt; [2,2,1]
从下标 0 开始到下标 1 结束，形成了一个长度为 2 的非递减子数组 [2,2] 。 
可以证明 2 是可达到的最大长度。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums1 = [1,3,2,1], nums2 = [2,2,3,4]
<strong>输出：</strong>4
<strong>解释：</strong>构造 nums3 的方法之一是： 
nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] =&gt; [1,2,3,4]
整个数组形成了一个长度为 4 的非递减子数组，并且是可达到的最大长度。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums1 = [1,1], nums2 = [2,2]
<strong>输出：</strong>2
<strong>解释：</strong>构造 nums3 的方法之一是： 
nums3 = [nums1[0], nums1[1]] =&gt; [1,1] 
整个数组形成了一个长度为 2 的非递减子数组，并且是可达到的最大长度。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length == nums2.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Consider using dynamic programming.
2. Let dp[i][0] (dp[i][1]) be the length of the longest non-decreasing ending with nums1[i] (nums2[i]).
3. Initialize dp[i][0] to 1. If nums1[i] >= nums1[i - 1] then dp[i][0] may be dp[i - 1][0] + 1. If nums1[i] >= nums2[i - 1] then dp[i][0] may be dp[i - 1][1] + 1. Perform a similar calculation for nums2[i] and dp[i][1].

## 示例

```
[2,3,1]
[1,2,1]
[1,3,2,1]
[2,2,3,4]
[1,1]
[2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNonDecreasingLength(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNonDecreasingLength(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int maxNonDecreasingLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNonDecreasingLength(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxNonDecreasingLength = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function maxNonDecreasingLength(nums1: number[], nums2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxNonDecreasingLength($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNonDecreasingLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNonDecreasingLength(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNonDecreasingLength(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func maxNonDecreasingLength(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_non_decreasing_length(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def maxNonDecreasingLength(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_non_decreasing_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-non-decreasing-length nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_non_decreasing_length(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
max_non_decreasing_length(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_non_decreasing_length(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_non_decreasing_length(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNonDecreasingLength(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

