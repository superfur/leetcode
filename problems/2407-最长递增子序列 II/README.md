# 2407. 最长递增子序列 II

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>找到&nbsp;<code>nums</code>&nbsp;中满足以下要求的最长子序列：</p>

<ul>
	<li>子序列 <strong>严格递增</strong></li>
	<li>子序列中相邻元素的差值 <strong>不超过</strong>&nbsp;<code>k</code>&nbsp;。</li>
</ul>

<p>请你返回满足上述要求的 <strong>最长子序列</strong>&nbsp;的长度。</p>

<p><strong>子序列</strong>&nbsp;是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [4,2,1,4,3,4,5,8,15], k = 3
<b>输出：</b>5
<strong>解释：</strong>
满足要求的最长子序列是 [1,3,4,5,8] 。
子序列长度为 5 ，所以我们返回 5 。
注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [7,4,5,1,8,12,4,7], k = 5
<b>输出：</b>4
<strong>解释：</strong>
满足要求的最长子序列是 [4,5,8,12] 。
子序列长度为 4 ，所以我们返回 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [1,5], k = 1
<b>输出：</b>1
<strong>解释：</strong>
满足要求的最长子序列是 [1] 。
子序列长度为 1 ，所以我们返回 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 队列
- 数组
- 分治
- 动态规划
- 单调队列

## 提示

1. We can use dynamic programming. Let dp[i][val] be the answer using only the first i + 1 elements, and the last element in the subsequence is equal to val.
2. The only value that might change between dp[i - 1] and dp[i] are dp[i - 1][val] and dp[i][val].
3. Try using dp[i - 1] and the fact that the second last element in the subsequence has to fall within a range to calculate dp[i][val].
4. We can use a segment tree to find the maximum value in dp[i - 1] within a certain range.

## 示例

```
[4,2,1,4,3,4,5,8,15]
3
[7,4,5,1,8,12,4,7]
5
[1,5]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int lengthOfLIS(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int lengthOfLIS(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LengthOfLIS(int[] nums, int k) {
        
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
var lengthOfLIS = function(nums, k) {
    
};
```

### TypeScript

```typescript
function lengthOfLIS(nums: number[], k: number): number {
    
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
    function lengthOfLIS($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lengthOfLIS(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lengthOfLIS(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lengthOfLIS(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func lengthOfLIS(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def length_of_lis(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def lengthOfLIS(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (length-of-lis nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec length_of_lis(Nums :: [integer()], K :: integer()) -> integer().
length_of_lis(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec length_of_lis(nums :: [integer], k :: integer) :: integer
  def length_of_lis(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lengthOfLIS(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

