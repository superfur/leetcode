# 2809. 使数组和小于等于 x 的最少时间

## 题目描述

<p>给你两个长度相等下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;。每一秒，对于所有下标&nbsp;<code>0 &lt;= i &lt; nums1.length</code>&nbsp;，<code>nums1[i]</code>&nbsp;的值都增加&nbsp;<code>nums2[i]</code>&nbsp;。操作&nbsp;<strong>完成后</strong>&nbsp;，你可以进行如下操作：</p>

<ul>
	<li>选择任一满足&nbsp;<code>0 &lt;= i &lt; nums1.length</code>&nbsp;的下标 <code>i</code>&nbsp;，并使&nbsp;<code>nums1[i] = 0</code>&nbsp;。</li>
</ul>

<p>同时给你一个整数&nbsp;<code>x</code>&nbsp;。</p>

<p>请你返回使&nbsp;<code>nums1</code>&nbsp;中所有元素之和 <strong>小于等于</strong>&nbsp;<code>x</code>&nbsp;所需要的 <strong>最少</strong>&nbsp;时间，如果无法实现，那么返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,2,3], nums2 = [1,2,3], x = 4
<b>输出：</b>3
<b>解释：</b>
第 1 秒，我们对 i = 0 进行操作，得到 nums1 = [0,2+2,3+3] = [0,4,6] 。
第 2 秒，我们对 i = 1 进行操作，得到 nums1 = [0+1,0,6+3] = [1,0,9] 。
第 3 秒，我们对 i = 2 进行操作，得到 nums1 = [1+1,0+2,0] = [2,2,0] 。
现在 nums1 的和为 4 。不存在更少次数的操作，所以我们返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,2,3], nums2 = [3,3,3], x = 4
<b>输出：</b>-1
<b>解释：</b>不管如何操作，nums1 的和总是会超过 x 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 10<sup>3</sup></code></li>
	<li><code>0 &lt;= nums2[i] &lt;= 10<sup>3</sup></code></li>
	<li><code>nums1.length == nums2.length</code></li>
	<li><code>0 &lt;= x &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. <div class="_1l1MA">It can be proven that in the optimal solution, for each index <code>i</code>, we only need to set <code>nums1[i]</code> to <code>0</code> at most once. (If we have to set it twice, we can simply remove the earlier set and all the operations “shift left” by <code>1</code>.)</div>
2. <div class="_1l1MA">It can also be proven that if we select several indexes <code>i<sub>1</sub>, i<sub>2</sub>, ..., i<sub>k</sub></code> and set <code>nums1[i<sub>1</sub>], nums1[i<sub>2</sub>], ..., nums1[i<sub>k</sub>]</code> to <code>0</code>, it’s always optimal to set them in the order of <code>nums2[i<sub>1</sub>] <= nums2[i<sub>2</sub>] <= ... <= nums2[i<sub>k</sub>]</code> (the larger the increase is, the later we should set it to <code>0</code>).</div>
3. <div class="_1l1MA">Let’s sort all the values by <code>nums2</code> (in non-decreasing order). Let <code>dp[i][j]</code> represent the maximum total value that can be reduced if we do <code>j</code> operations on the first <code>i</code> elements. Then we have <code>dp[i][0] = 0</code> (for all <code>i = 0, 1, ..., n</code>) and <code>dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums2[i - 1] * j + nums1[i - 1])</code> (for <code>1 <= i <= n</code> and <code>1 <= j <= i</code>).</div>
4. <div class="_1l1MA">The answer is the minimum value of <code>t</code>, such that <code>0 <= t <= n</code> and <code>sum(nums1) + sum(nums2) * t - dp[n][t] <= x</code>, or <code>-1</code> if it doesn’t exist.</div>

## 示例

```
[1,2,3]
[1,2,3]
4
[1,2,3]
[3,3,3]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTime(vector<int>& nums1, vector<int>& nums2, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTime(List<Integer> nums1, List<Integer> nums2, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTime(self, nums1, nums2, x):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        
```

### C

```c
int minimumTime(int* nums1, int nums1Size, int* nums2, int nums2Size, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTime(IList<int> nums1, IList<int> nums2, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} x
 * @return {number}
 */
var minimumTime = function(nums1, nums2, x) {
    
};
```

### TypeScript

```typescript
function minimumTime(nums1: number[], nums2: number[], x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $x
     * @return Integer
     */
    function minimumTime($nums1, $nums2, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTime(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTime(nums1: List<Int>, nums2: List<Int>, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTime(List<int> nums1, List<int> nums2, int x) {
    
  }
}
```

### Go

```golang
func minimumTime(nums1 []int, nums2 []int, x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} x
# @return {Integer}
def minimum_time(nums1, nums2, x)
    
end
```

### Scala

```scala
object Solution {
    def minimumTime(nums1: List[Int], nums2: List[Int], x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time(nums1: Vec<i32>, nums2: Vec<i32>, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time nums1 nums2 x)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time(Nums1 :: [integer()], Nums2 :: [integer()], X :: integer()) -> integer().
minimum_time(Nums1, Nums2, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time(nums1 :: [integer], nums2 :: [integer], x :: integer) :: integer
  def minimum_time(nums1, nums2, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTime(nums1: ArrayList<Int64>, nums2: ArrayList<Int64>, x: Int64): Int64 {

    }
}
```

