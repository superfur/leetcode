# 2817. 限制条件下元素之间的最小绝对差

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>x</code>&nbsp;。</p>

<p>请你找到数组中下标距离至少为 <code>x</code>&nbsp;的两个元素的 <strong>差值绝对值</strong>&nbsp;的 <strong>最小值</strong>&nbsp;。</p>

<p>换言之，请你找到两个下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，满足&nbsp;<code>abs(i - j) &gt;= x</code> 且&nbsp;<code>abs(nums[i] - nums[j])</code>&nbsp;的值最小。</p>

<p>请你返回一个整数，表示下标距离至少为 <code>x</code>&nbsp;的两个元素之间的差值绝对值的 <strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<b>输入：</b>nums = [4,3,2,4], x = 2
<b>输出：</b>0
<b>解释：</b>我们选择 nums[0] = 4 和 nums[3] = 4 。
它们下标距离满足至少为 2 ，差值绝对值为最小值 0 。
0 是最优解。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,3,2,10,15], x = 1
<b>输出：</b>1
<b>解释：</b>我们选择 nums[1] = 3 和 nums[2] = 2 。
它们下标距离满足至少为 1 ，差值绝对值为最小值 1 。
1 是最优解。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4], x = 3
<b>输出：</b>3
<strong>解释：</strong>我们选择 nums[0] = 1 和 nums[3] = 4 。
它们下标距离满足至少为 3 ，差值绝对值为最小值 3 。
3 是最优解。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= x &lt; nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 有序集合

## 提示

1. <div class="_1l1MA">Let's only consider the cases where <code>i < j</code>, as the problem is symmetric.</div>
2. <div class="_1l1MA">For an index <code>j</code>, we are interested in an index <code>i</code> in the range <code>[0, j - x]</code> that minimizes <code>abs(nums[i] - nums[j])</code>.</div>
3. <div class="_1l1MA">For every index <code>j</code>, while going from left to right, add <code>nums[j - x]</code> to a set (C++ set, Java TreeSet, and Python sorted set).</div>
4. <div class="_1l1MA">After inserting <code>nums[j - x]</code>, we can calculate the closest value to <code>nums[j]</code> in the set using binary search and store the absolute difference. In C++, we can achieve this by using lower_bound and/or upper_bound.</div>
5. <div class="_1l1MA">Calculate the minimum absolute difference among all indices.</div>

## 示例

```
[4,3,2,4]
2
[5,3,2,10,15]
1
[1,2,3,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int minAbsoluteDifference(List<Integer> nums, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
```

### C

```c
int minAbsoluteDifference(int* nums, int numsSize, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinAbsoluteDifference(IList<int> nums, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minAbsoluteDifference = function(nums, x) {
    
};
```

### TypeScript

```typescript
function minAbsoluteDifference(nums: number[], x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function minAbsoluteDifference($nums, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAbsoluteDifference(_ nums: [Int], _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAbsoluteDifference(nums: List<Int>, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minAbsoluteDifference(List<int> nums, int x) {
    
  }
}
```

### Go

```golang
func minAbsoluteDifference(nums []int, x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_absolute_difference(nums, x)
    
end
```

### Scala

```scala
object Solution {
    def minAbsoluteDifference(nums: List[Int], x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-absolute-difference nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_absolute_difference(Nums :: [integer()], X :: integer()) -> integer().
min_absolute_difference(Nums, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_absolute_difference(nums :: [integer], x :: integer) :: integer
  def min_absolute_difference(nums, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAbsoluteDifference(nums: ArrayList<Int64>, x: Int64): Int64 {

    }
}
```

