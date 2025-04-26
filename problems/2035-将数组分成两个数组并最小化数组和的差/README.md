# 2035. 将数组分成两个数组并最小化数组和的差

## 题目描述

<p>给你一个长度为 <code>2 * n</code>&nbsp;的整数数组。你需要将&nbsp;<code>nums</code>&nbsp;分成&nbsp;<strong>两个</strong>&nbsp;长度为&nbsp;<code>n</code>&nbsp;的数组，分别求出两个数组的和，并 <strong>最小化</strong>&nbsp;两个数组和之&nbsp;<b>差的绝对值</b>&nbsp;。<code>nums</code>&nbsp;中每个元素都需要放入两个数组之一。</p>

<p>请你返回&nbsp;<strong>最小</strong>&nbsp;的数组和之差。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/02/ex1.png" style="width: 240px; height: 106px;"></p>

<pre><b>输入：</b>nums = [3,9,7,3]
<b>输出：</b>2
<strong>解释：</strong>最优分组方案是分成 [3,9] 和 [7,3] 。
数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [-36,36]
<b>输出：</b>72
<strong>解释：</strong>最优分组方案是分成 [-36] 和 [36] 。
数组和之差的绝对值为 abs((-36) - (36)) = 72 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="example-3" src="https://assets.leetcode.com/uploads/2021/10/02/ex3.png" style="width: 316px; height: 106px;"></p>

<pre><b>输入：</b>nums = [2,-1,0,4,-2,-9]
<b>输出：</b>0
<strong>解释：</strong>最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 双指针
- 二分查找
- 动态规划
- 状态压缩
- 有序集合

## 提示

1. The target sum for the two partitions is sum(nums) / 2.
2. Could you reduce the time complexity if you arbitrarily divide nums into two halves (two arrays)? Meet-in-the-Middle?
3. For both halves, pre-calculate a 2D array where the kth index will store all possible sum values if only k elements from this half are added.
4. For each sum of k elements in the first half, find the best sum of n-k elements in the second half such that the two sums add up to a value closest to the target sum from hint 1. These two subsets will form one array of the partition.

## 示例

```
[3,9,7,3]
[-36,36]
[2,-1,0,4,-2,-9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDifference(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDifference(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumDifference(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDifference(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumDifference(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDifference($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDifference(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDifference(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDifference(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumDifference(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumDifference(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_difference(Nums :: [integer()]) -> integer().
minimum_difference(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_difference(nums :: [integer]) :: integer
  def minimum_difference(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDifference(nums: Array<Int64>): Int64 {

    }
}
```

