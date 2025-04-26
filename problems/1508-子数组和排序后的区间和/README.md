# 1508. 子数组和排序后的区间和

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;，它包含&nbsp;<code>n</code>&nbsp;个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含&nbsp;<code>n * (n + 1) / 2</code>&nbsp;个数字的数组。</p>

<p>请你返回在新数组中下标为<em>&nbsp;</em><code>left</code>&nbsp;到&nbsp;<code>right</code> <strong>（下标从 1 开始）</strong>的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], n = 4, left = 1, right = 5
<strong>输出：</strong>13 
<strong>解释：</strong>所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], n = 4, left = 3, right = 4
<strong>输出：</strong>6
<strong>解释：</strong>给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 3 + 3 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], n = 4, left = 1, right = 10
<strong>输出：</strong>50
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^3</code></li>
	<li><code>nums.length == n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= left &lt;= right&nbsp;&lt;= n * (n + 1) / 2</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 前缀和
- 排序

## 提示

1. Compute all sums and save it in array.
2. Then just go from LEFT to RIGHT index and calculate answer modulo 1e9 + 7.

## 示例

```
[1,2,3,4]
4
1
5
[1,2,3,4]
4
3
4
[1,2,3,4]
4
1
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
```

### C

```c
int rangeSum(int* nums, int numsSize, int n, int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public int RangeSum(int[] nums, int n, int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    
};
```

### TypeScript

```typescript
function rangeSum(nums: number[], n: number, left: number, right: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function rangeSum($nums, $n, $left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rangeSum(_ nums: [Int], _ n: Int, _ left: Int, _ right: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rangeSum(nums: IntArray, n: Int, left: Int, right: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int rangeSum(List<int> nums, int n, int left, int right) {
    
  }
}
```

### Go

```golang
func rangeSum(nums []int, n int, left int, right int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} n
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def range_sum(nums, n, left, right)
    
end
```

### Scala

```scala
object Solution {
    def rangeSum(nums: Array[Int], n: Int, left: Int, right: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn range_sum(nums: Vec<i32>, n: i32, left: i32, right: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (range-sum nums n left right)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec range_sum(Nums :: [integer()], N :: integer(), Left :: integer(), Right :: integer()) -> integer().
range_sum(Nums, N, Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec range_sum(nums :: [integer], n :: integer, left :: integer, right :: integer) :: integer
  def range_sum(nums, n, left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rangeSum(nums: Array<Int64>, n: Int64, left: Int64, right: Int64): Int64 {

    }
}
```

