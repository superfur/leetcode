# 2547. 拆分数组的最小代价

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p>将数组拆分成一些非空子数组。拆分的 <strong>代价</strong> 是每个子数组中的 <strong>重要性</strong> 之和。</p>

<p>令 <code>trimmed(subarray)</code> 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。</p>

<ul>
	<li>例如，<code>trimmed([3,1,2,4,3,4]) = [3,4,3,4]</code> 。</li>
</ul>

<p>子数组的 <strong>重要性</strong> 定义为 <code>k + trimmed(subarray).length</code> 。</p>

<ul>
	<li>例如，如果一个子数组是 <code>[1,2,3,3,3,4,4]</code> ，<code>trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4]</code> 。这个子数组的重要性就是 <code>k + 5</code> 。</li>
</ul>

<p>找出并返回拆分 <code>nums</code> 的所有可行方案中的最小代价。</p>

<p><strong>子数组</strong> 是数组的一个连续 <strong>非空</strong> 元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1,3,3], k = 2
<strong>输出：</strong>8
<strong>解释：</strong>将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1] 的重要性是 2 + (2) = 4 。
拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1], k = 5
<strong>输出：</strong>10
<strong>解释：</strong>将 nums 拆分成一个子数组：[1,2,1,2,1].
[1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 动态规划
- 计数

## 提示

1. Let's denote dp[r] = minimum cost to partition the first r elements of nums. What would be the transitions of such dynamic programming?
2. dp[r] = min(dp[l] + importance(nums[l..r])) over all 0 <= l < r. This already gives us an O(n^3) approach, as importance can be calculated in linear time, and there are a total of O(n^2) transitions.
3. Can you think of a way to compute multiple importance values of related subarrays faster?
4. importance(nums[l-1..r]) is either importance(nums[l..r]) if a new unique element is added, importance(nums[l..r]) + 1 if an old element that appeared at least twice is added, or importance(nums[l..r]) + 2, if a previously unique element is duplicated. This allows us to compute importance(nums[l..r]) for all 0 <= l < r in O(n) by keeping a frequency table and decreasing l from r-1 down to 0.

## 示例

```
[1,2,1,2,1,3,3]
2
[1,2,1,2,1]
2
[1,2,1,2,1]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minCost(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int[] nums, int k) {
        
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
var minCost = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minCost(nums: number[], k: number): number {
    
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
    function minCost($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minCost(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_cost(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minCost(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Nums :: [integer()], K :: integer()) -> integer().
min_cost(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(nums :: [integer], k :: integer) :: integer
  def min_cost(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

