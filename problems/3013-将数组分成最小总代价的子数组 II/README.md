# 3013. 将数组分成最小总代价的子数组 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和两个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code> 和&nbsp;<code>dist</code>&nbsp;。</p>

<p>一个数组的 <strong>代价</strong>&nbsp;是数组中的 <strong>第一个</strong>&nbsp;元素。比方说，<code>[1,2,3]</code>&nbsp;的代价为&nbsp;<code>1</code>&nbsp;，<code>[3,4,1]</code>&nbsp;的代价为&nbsp;<code>3</code>&nbsp;。</p>

<p>你需要将 <code>nums</code>&nbsp;分割成 <code>k</code>&nbsp;个 <strong>连续且互不相交</strong>&nbsp;的<span data-keyword="subarray">子数组</span>，满足 <strong>第二</strong>&nbsp;个子数组与第 <code>k</code>&nbsp;个子数组中第一个元素的下标距离 <strong>不超过</strong>&nbsp;<code>dist</code>&nbsp;。换句话说，如果你将&nbsp;<code>nums</code>&nbsp;分割成子数组&nbsp;<code>nums[0..(i<sub>1</sub> - 1)], nums[i<sub>1</sub>..(i<sub>2</sub> - 1)], ..., nums[i<sub>k-1</sub>..(n - 1)]</code>&nbsp;，那么它需要满足&nbsp;<code>i<sub>k-1</sub> - i<sub>1</sub> &lt;= dist</code>&nbsp;。</p>

<p>请你返回这些子数组的 <strong>最小</strong>&nbsp;总代价。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,2,6,4,2], k = 3, dist = 3
<b>输出：</b>5
<b>解释：</b>将数组分割成 3 个子数组的最优方案是：[1,3] ，[2,6,4] 和 [2] 。这是一个合法分割，因为 i<sub>k-1</sub> - i<sub>1</sub> 等于 5 - 2 = 3 ，等于 dist 。总代价为 nums[0] + nums[2] + nums[5] ，也就是 1 + 2 + 2 = 5 。
5 是分割成 3 个子数组的最小总代价。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,1,2,2,2,1], k = 4, dist = 3
<b>输出：</b>15
<b>解释：</b>将数组分割成 4 个子数组的最优方案是：[10] ，[1] ，[2] 和 [2,2,1] 。这是一个合法分割，因为 i<sub>k-1</sub> - i<sub>1</sub> 等于 3 - 1 = 2 ，小于 dist 。总代价为 nums[0] + nums[1] + nums[2] + nums[3] ，也就是 10 + 1 + 2 + 2 = 15 。
分割 [10] ，[1] ，[2,2,2] 和 [1] 不是一个合法分割，因为 i<sub>k-1</sub> 和 i<sub>1</sub> 的差为 5 - 1 = 4 ，大于 dist 。
15 是分割成 4 个子数组的最小总代价。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [10,8,18,9], k = 3, dist = 1
<b>输出：</b>36
<b>解释：</b>将数组分割成 4 个子数组的最优方案是：[10] ，[8] 和 [18,9] 。这是一个合法分割，因为 i<sub>k-1</sub> - i<sub>1</sub> 等于 2 - 1 = 1 ，等于 dist 。总代价为 nums[0] + nums[1] + nums[2] ，也就是 10 + 8 + 18 = 36 。
分割 [10] ，[8,18] 和 [9] 不是一个合法分割，因为 i<sub>k-1</sub> 和 i<sub>1</sub> 的差为 3 - 1 = 2 ，大于 dist 。
36 是分割成 3 个子数组的最小总代价。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>3 &lt;= k &lt;= n</code></li>
	<li><code>k - 2 &lt;= dist &lt;= n - 2</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 滑动窗口
- 堆（优先队列）

## 提示

1. For each <code>i > 0</code>, try each <code>nums[i]</code> as the first element of the second subarray. We need to find the sum of <code>k - 2</code> smallest values in the index range <code>[i + 1, min(i + dist, n - 1)]</code>.
2. Typically, we use a max heap to maintain the top <code>k - 2</code> smallest values dynamically. Here we also have a sliding window, which is the index range <code>[i + 1, min(i + dist, n - 1)]</code>. We can use another min heap to put unselected values for future use.
3. Update the two heaps when iteration over <code>i</code>. Ordered/Tree sets are also a good choice since we have to delete elements.
4. If the max heap’s size is less than <code>k - 2</code>, use the min heap’s value to fill it. If the maximum value in the max heap is larger than the smallest value in the min heap, swap them in the two heaps.

## 示例

```
[1,3,2,6,4,2]
3
3
[10,1,2,2,2,1]
4
3
[10,8,18,9]
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(int[] nums, int k, int dist) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
```

### C

```c
long long minimumCost(int* nums, int numsSize, int k, int dist) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(int[] nums, int k, int dist) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} dist
 * @return {number}
 */
var minimumCost = function(nums, k, dist) {
    
};
```

### TypeScript

```typescript
function minimumCost(nums: number[], k: number, dist: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $dist
     * @return Integer
     */
    function minimumCost($nums, $k, $dist) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int], _ k: Int, _ dist: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(nums: IntArray, k: Int, dist: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> nums, int k, int dist) {
    
  }
}
```

### Go

```golang
func minimumCost(nums []int, k int, dist int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} dist
# @return {Integer}
def minimum_cost(nums, k, dist)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int], k: Int, dist: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost nums k dist)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Nums :: [integer()], K :: integer(), Dist :: integer()) -> integer().
minimum_cost(Nums, K, Dist) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer], k :: integer, dist :: integer) :: integer
  def minimum_cost(nums, k, dist) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(nums: Array<Int64>, k: Int64, dist: Int64): Int64 {

    }
}
```

