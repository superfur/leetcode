# 2915. 和为目标值的最长子序列的长度

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>target</code>&nbsp;。</p>

<p>返回和为 <code>target</code>&nbsp;的 <code>nums</code>&nbsp;子序列中，子序列&nbsp;<strong>长度的最大值&nbsp;</strong>。如果不存在和为 <code>target</code>&nbsp;的子序列，返回 <code>-1</code>&nbsp;。</p>

<p><strong>子序列</strong> 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5], target = 9
<b>输出：</b>3
<b>解释：</b>总共有 3 个子序列的和为 9 ：[4,5] ，[1,3,5] 和 [2,3,4] 。最长的子序列是 [1,3,5] 和 [2,3,4] 。所以答案为 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [4,1,3,2,1,5], target = 7
<b>输出：</b>4
<strong>解释：</strong>总共有 5 个子序列的和为 7 ：[4,3] ，[4,1,2] ，[4,2,1] ，[1,1,5] 和 [1,3,2,1] 。最长子序列为 [1,3,2,1] 。所以答案为 4 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,5,4,5], target = 3
<b>输出：</b>-1
<b>解释：</b>无法得到和为 3 的子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Use dynamic programming.
2. Let <code>dp[i][j]</code> be the maximum length of any subsequence of <code>nums[0..i - 1]</code> that sums to <code>j</code>.
3. <code>dp[0][0] = 1</code>, and <code>dp[0][j] = 1</code> for all <code>target ≥ j > 0</code>.
4. <code>dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i -1])</code> for all <code>n ≥ i > 0</code> and <code>target ≥ j > nums[i - 1]</code>.

## 示例

```
[1,2,3,4,5]
9
[4,1,3,2,1,5]
7
[1,1,5,4,5]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lengthOfLongestSubsequence(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int lengthOfLongestSubsequence(List<Integer> nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int lengthOfLongestSubsequence(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int LengthOfLongestSubsequence(IList<int> nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var lengthOfLongestSubsequence = function(nums, target) {
    
};
```

### TypeScript

```typescript
function lengthOfLongestSubsequence(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function lengthOfLongestSubsequence($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lengthOfLongestSubsequence(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lengthOfLongestSubsequence(nums: List<Int>, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lengthOfLongestSubsequence(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func lengthOfLongestSubsequence(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def length_of_longest_subsequence(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def lengthOfLongestSubsequence(nums: List[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn length_of_longest_subsequence(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (length-of-longest-subsequence nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec length_of_longest_subsequence(Nums :: [integer()], Target :: integer()) -> integer().
length_of_longest_subsequence(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec length_of_longest_subsequence(nums :: [integer], target :: integer) :: integer
  def length_of_longest_subsequence(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lengthOfLongestSubsequence(nums: ArrayList<Int64>, target: Int64): Int64 {

    }
}
```

