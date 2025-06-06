# 2916. 子数组不同元素数目的平方和 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>定义 <code>nums</code>&nbsp;一个子数组的 <strong>不同计数</strong>&nbsp;值如下：</p>

<ul>
	<li>令&nbsp;<code>nums[i..j]</code>&nbsp;表示 <code>nums</code> 中所有下标在 <code>i</code> 到 <code>j</code> 范围内的元素构成的子数组（满足 <code>0 &lt;= i &lt;= j &lt; nums.length</code> ），那么我们称子数组&nbsp;<code>nums[i..j]</code>&nbsp;中不同值的数目为&nbsp;<code>nums[i..j]</code>&nbsp;的不同计数。</li>
</ul>

<p>请你返回 <code>nums</code>&nbsp;中所有子数组的 <strong>不同计数</strong>&nbsp;的 <strong>平方</strong>&nbsp;和。</p>

<p>由于答案可能会很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>子数组指的是一个数组里面一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,1]
<b>输出：</b>15
<b>解释：</b>六个子数组分别为：
[1]: 1 个互不相同的元素。
[2]: 1 个互不相同的元素。
[1]: 1 个互不相同的元素。
[1,2]: 2 个互不相同的元素。
[2,1]: 2 个互不相同的元素。
[1,2,1]: 2 个互不相同的元素。
所有不同计数的平方和为 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 15 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,2]
<b>输出：3</b>
<strong>解释：</strong>三个子数组分别为：
[2]: 1 个互不相同的元素。
[2]: 1 个互不相同的元素。
[2,2]: 1 个互不相同的元素。
所有不同计数的平方和为 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 动态规划

## 提示

1. Consider the sum of the count of distinct values of subarrays ending with index <code>i</code>, let’s call it <code>sum</code>. Now if you need the sum of all subarrays ending with index <code>i + 1</code> think how it can be related to <code>sum</code> and what extra will be needed to add to this.
2. You can find that extra sum using the segment tree.

## 示例

```
[1,2,1]
[2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumCounts(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumCounts(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
```

### C

```c
int sumCounts(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumCounts(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {
    
};
```

### TypeScript

```typescript
function sumCounts(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumCounts($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumCounts(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumCounts(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumCounts(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumCounts(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-counts nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_counts(Nums :: [integer()]) -> integer().
sum_counts(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumCounts(nums: Array<Int64>): Int64 {

    }
}
```

