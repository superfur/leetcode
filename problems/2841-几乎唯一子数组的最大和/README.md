# 2841. 几乎唯一子数组的最大和

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和两个正整数&nbsp;<code>m</code>&nbsp;和&nbsp;<code>k</code>&nbsp;。</p>

<p>请你返回 <code>nums</code>&nbsp;中长度为 <code>k</code>&nbsp;的&nbsp;<strong>几乎唯一</strong>&nbsp;子数组的 <strong>最大和</strong>&nbsp;，如果不存在几乎唯一子数组，请你返回 <code>0</code>&nbsp;。</p>

<p>如果 <code>nums</code>&nbsp;的一个子数组有至少 <code>m</code>&nbsp;个互不相同的元素，我们称它是 <strong>几乎唯一</strong>&nbsp;子数组。</p>

<p>子数组指的是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,6,7,3,1,7], m = 3, k = 4
<b>输出：</b>18
<b>解释：</b>总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,9,9,2,4,5,4], m = 1, k = 3
<b>输出：</b>23
<b>解释：</b>总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,1,2,1,2,1], m = 3, k = 3
<b>输出：</b>0
<b>解释：</b>输入数组中不存在长度为 <code>k = 3</code> 的子数组含有至少  <code>m = 3</code> 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m &lt;= k &lt;= nums.length</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. Use a set or map to keep track of the number of distinct elements.
2. Use 2-pointers to maintain the size, the number of unique elements, and the sum of all the elements in all subarrays of size k from left to right dynamically.****

## 示例

```
[2,6,7,3,1,7]
3
4
[5,9,9,2,4,5,4]
1
3
[1,2,1,2,1,2,1]
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxSum(vector<int>& nums, int m, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxSum(List<Integer> nums, int m, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
```

### C

```c
long long maxSum(int* nums, int numsSize, int m, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxSum(IList<int> nums, int m, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var maxSum = function(nums, m, k) {
    
};
```

### TypeScript

```typescript
function maxSum(nums: number[], m: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function maxSum($nums, $m, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSum(_ nums: [Int], _ m: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSum(nums: List<Int>, m: Int, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSum(List<int> nums, int m, int k) {
    
  }
}
```

### Go

```golang
func maxSum(nums []int, m int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def max_sum(nums, m, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSum(nums: List[Int], m: Int, k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum nums m k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum(Nums :: [integer()], M :: integer(), K :: integer()) -> integer().
max_sum(Nums, M, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer], m :: integer, k :: integer) :: integer
  def max_sum(nums, m, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSum(nums: ArrayList<Int64>, m: Int64, k: Int64): Int64 {

    }
}
```

