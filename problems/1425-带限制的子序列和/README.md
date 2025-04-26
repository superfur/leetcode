# 1425. 带限制的子序列和

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，请你返回 <strong>非空</strong>&nbsp;子序列元素和的最大值，子序列需要满足：子序列中每两个 <strong>相邻</strong>&nbsp;的整数&nbsp;<code>nums[i]</code>&nbsp;和&nbsp;<code>nums[j]</code>&nbsp;，它们在原数组中的下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;满足&nbsp;<code>i &lt; j</code>&nbsp;且 <code>j - i &lt;= k</code> 。</p>

<p>数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [10,2,-10,5,20], k = 2
<strong>输出：</strong>37
<strong>解释：</strong>子序列为 [10, 2, 5, 20] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [-1,-2,-3], k = 1
<strong>输出：</strong>-1
<strong>解释：</strong>子序列必须是非空的，所以我们选择最大的数字。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [10,-2,-10,-5,20], k = 2
<strong>输出：</strong>23
<strong>解释：</strong>子序列为 [10, -2, -5, 20] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>-10^4&nbsp;&lt;= nums[i] &lt;= 10^4</code></li>
</ul>


## 难度

Hard

## 标签

- 队列
- 数组
- 动态规划
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 提示

1. Use dynamic programming.
2. Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.
3. dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])
4. Use a heap with the sliding window technique to optimize the dp.

## 示例

```
[10,2,-10,5,20]
2
[-1,-2,-3]
1
[10,-2,-10,-5,20]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int constrainedSubsetSum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ConstrainedSubsetSum(int[] nums, int k) {
        
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
var constrainedSubsetSum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function constrainedSubsetSum(nums: number[], k: number): number {
    
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
    function constrainedSubsetSum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constrainedSubsetSum(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constrainedSubsetSum(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int constrainedSubsetSum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func constrainedSubsetSum(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def constrained_subset_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def constrainedSubsetSum(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn constrained_subset_sum(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (constrained-subset-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec constrained_subset_sum(Nums :: [integer()], K :: integer()) -> integer().
constrained_subset_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec constrained_subset_sum(nums :: [integer], k :: integer) :: integer
  def constrained_subset_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func constrainedSubsetSum(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

