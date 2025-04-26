# 2967. 使数组成为等数数组的最小代价

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以对 <code>nums</code>&nbsp;执行特殊操作 <strong>任意次</strong>&nbsp;（也可以 <strong>0</strong>&nbsp;次）。每一次特殊操作中，你需要 <strong>按顺序</strong>&nbsp;执行以下步骤：</p>

<ul>
	<li>从范围&nbsp;<code>[0, n - 1]</code>&nbsp;里选择一个下标 <code>i</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>x</code>&nbsp;。</li>
	<li>将&nbsp;<code>|nums[i] - x|</code>&nbsp;添加到总代价里。</li>
	<li>将 <code>nums[i]</code>&nbsp;变为&nbsp;<code>x</code>&nbsp;。</li>
</ul>

<p>如果一个正整数正着读和反着读都相同，那么我们称这个数是<strong>&nbsp;回文数</strong>&nbsp;。比方说，<code>121</code>&nbsp;，<code>2552</code> 和&nbsp;<code>65756</code>&nbsp;都是回文数，但是&nbsp;<code>24</code>&nbsp;，<code>46</code>&nbsp;，<code>235</code>&nbsp;都不是回文数。</p>

<p>如果一个数组中的所有元素都等于一个整数&nbsp;<code>y</code>&nbsp;，且&nbsp;<code>y</code>&nbsp;是一个小于&nbsp;<code>10<sup>9</sup></code>&nbsp;的&nbsp;<strong>回文数</strong>&nbsp;，那么我们称这个数组是一个 <strong>等数数组&nbsp;</strong>。</p>

<p>请你返回一个整数，表示执行任意次特殊操作后使 <code>nums</code>&nbsp;成为 <strong>等数数组</strong>&nbsp;的 <strong>最小</strong>&nbsp;总代价。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5]
<b>输出：</b>6
<b>解释：</b>我们可以将数组中所有元素变为回文数 3 得到等数数组，数组变成 [3,3,3,3,3] 需要执行 4 次特殊操作，代价为 |1 - 3| + |2 - 3| + |4 - 3| + |5 - 3| = 6 。
将所有元素变为其他回文数的总代价都大于 6 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [10,12,13,14,15]
<b>输出：</b>11
<b>解释：</b>我们可以将数组中所有元素变为回文数 11 得到等数数组，数组变成 [11,11,11,11,11] 需要执行 5 次特殊操作，代价为 |10 - 11| + |12 - 11| + |13 - 11| + |14 - 11| + |15 - 11| = 11 。
将所有元素变为其他回文数的总代价都大于 11 。
</pre>

<p><strong class="example">示例 3 ：</strong></p>

<pre>
<b>输入：</b>nums = [22,33,22,33,22]
<b>输出：</b>22
<b>解释：</b>我们可以将数组中所有元素变为回文数 22 得到等数数组，数组变为 [22,22,22,22,22] 需要执行 2 次特殊操作，代价为 |33 - 22| + |33 - 22| = 22 。
将所有元素变为其他回文数的总代价都大于 22 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 二分查找
- 排序

## 提示

1. Find the median of <code>nums</code> after sorting it (if the length is even, we can select any number from the two in the middle). Let’s call it <code>m</code>.
2. Try the smallest palindromic number that is larger than or equal to <code>m</code> (if any) and the largest palindromic number that is smaller than or equal to <code>m</code> (if any). These two values are the candidate palindromic numbers for values of all indices.
3. We can use math constructions to construct the two palindromic numbers in <code>O(log(m) / 2)</code> time or we can do it using brute-force by starting from m and checking smaller and larger values in <code>O(sqrt(10<sup>log(m)</sup>))</code>.
4. It is also possible to just generate all palindromic numbers using recursion in <code>O(sqrt(10<sup>9</sup>log(10<sup>9</sup>))</code>.

## 示例

```
[1,2,3,4,5]
[10,12,13,14,15]
[22,33,22,33,22]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
```

### C

```c
long long minimumCost(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumCost(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumCost($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumCost(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Nums :: [integer()]) -> integer().
minimum_cost(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(nums: Array<Int64>): Int64 {

    }
}
```

