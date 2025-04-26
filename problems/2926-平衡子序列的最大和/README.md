# 2926. 平衡子序列的最大和

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p><code>nums</code>&nbsp;一个长度为 <code>k</code>&nbsp;的 <strong>子序列</strong>&nbsp;指的是选出 <code>k</code>&nbsp;个 <strong>下标</strong>&nbsp;<code>i<sub>0</sub>&nbsp;&lt;&nbsp;i<sub>1</sub> &lt;&nbsp;... &lt; i<sub>k-1</sub></code>&nbsp;，如果这个子序列满足以下条件，我们说它是 <strong>平衡的</strong>&nbsp;：</p>

<ul>
	<li>对于范围&nbsp;<code>[1, k - 1]</code>&nbsp;内的所有&nbsp;<code>j</code>&nbsp;，<code>nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] &gt;= i<sub>j</sub> - i<sub>j-1</sub></code>&nbsp;都成立。</li>
</ul>

<p><code>nums</code>&nbsp;长度为 <code>1</code>&nbsp;的 <strong>子序列</strong>&nbsp;是平衡的。</p>

<p>请你返回一个整数，表示 <code>nums</code>&nbsp;<strong>平衡</strong>&nbsp;子序列里面的 <strong>最大元素和</strong>&nbsp;。</p>

<p>一个数组的 <strong>子序列</strong>&nbsp;指的是从原数组中删除一些元素（<strong>也可能一个元素也不删除</strong>）后，剩余元素保持相对顺序得到的 <strong>非空</strong>&nbsp;新数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,3,5,6]
<b>输出：</b>14
<b>解释：</b>这个例子中，选择子序列 [3,5,6] ，下标为 0 ，2 和 3 的元素被选中。
nums[2] - nums[0] &gt;= 2 - 0 。
nums[3] - nums[2] &gt;= 3 - 2 。
所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
包含下标 1 ，2 和 3 的子序列也是一个平衡的子序列。
最大平衡子序列和为 14 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,-1,-3,8]
<b>输出：</b>13
<b>解释：</b>这个例子中，选择子序列 [5,8] ，下标为 0 和 3 的元素被选中。
nums[3] - nums[0] &gt;= 3 - 0 。
所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
最大平衡子序列和为 13 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [-2,-1]
<b>输出：</b>-1
<b>解释：</b>这个例子中，选择子序列 [-1] 。
这是一个平衡子序列，而且它的和是 nums 所有平衡子序列里最大的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 动态规划

## 提示

1. Let <code>dp[x]</code> represent the maximum sum of a balanced subsequence ending at <code>x</code>.
2. Rewriting the formula <code>nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] >= i<sub>j</sub> - i<sub>j-1</sub></code> gives <code>nums[i<sub>j</sub>] - i<sub>j</sub> >= nums[i<sub>j-1</sub>] - i<sub>j-1</sub></code>.
3. So, for some index <code>x</code>, we need to find an index <code>y</code>, <code>y < x</code>, such that <code>dp[x] = nums[x] + dp[y]</code> is maximized, and <code>nums[x] - x >= nums[y] - y</code>.
4. There are many ways to achieve this. One method involves sorting the values of <code>nums[x] - x</code> for all indices <code>x</code> and using a segment/Fenwick tree with coordinate compression.
5. Hence, using a dictionary or map, let's call it <code>dict</code>, where <code>dict[nums[x] - x]</code> represents the position of the value, <code>nums[x] - x</code>, in the segment tree.
6. The tree is initialized with zeros initially.
7. For indices <code>x</code> in order from <code>[0, n - 1]</code>, <code>dp[x] = max(nums[x]</code>, <code>nums[x]</code> + the maximum query from the tree in the range <code>[0, dict[nums[x] - x]])</code>, and if <code>dp[x]</code> is greater than the value in the tree at position <code>dict[nums[x] - x]</code>, we update the value in the tree.
8. The answer to the problem is the maximum value in <code>dp</code>.

## 示例

```
[3,3,5,6]
[5,-1,-3,8]
[-2,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxBalancedSubsequenceSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxBalancedSubsequenceSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        
```

### C

```c
long long maxBalancedSubsequenceSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxBalancedSubsequenceSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxBalancedSubsequenceSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxBalancedSubsequenceSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxBalancedSubsequenceSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxBalancedSubsequenceSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxBalancedSubsequenceSum(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxBalancedSubsequenceSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxBalancedSubsequenceSum(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_balanced_subsequence_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxBalancedSubsequenceSum(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_balanced_subsequence_sum(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-balanced-subsequence-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_balanced_subsequence_sum(Nums :: [integer()]) -> integer().
max_balanced_subsequence_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_balanced_subsequence_sum(nums :: [integer]) :: integer
  def max_balanced_subsequence_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxBalancedSubsequenceSum(nums: Array<Int64>): Int64 {

    }
}
```

