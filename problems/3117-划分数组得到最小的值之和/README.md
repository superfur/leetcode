# 3117. 划分数组得到最小的值之和

## 题目描述

<p>给你两个数组 <code>nums</code> 和 <code>andValues</code>，长度分别为 <code>n</code> 和 <code>m</code>。</p>

<p>数组的 <strong>值 </strong>等于该数组的 <strong>最后一个 </strong>元素。</p>

<p>你需要将 <code>nums</code> 划分为 <code>m</code> 个 <strong>不相交的连续 </strong><span data-keyword="subarray-nonempty">子数组</span>，对于第 <code>i<sup>th</sup></code> 个子数组 <code>[l<sub>i</sub>, r<sub>i</sub>]</code>，子数组元素的按位&nbsp;<code>AND</code>&nbsp;运算结果等于 <code>andValues[i]</code>，换句话说，对所有的 <code>1 &lt;= i &lt;= m</code>，<code>nums[l<sub>i</sub>] &amp; nums[l<sub>i</sub> + 1] &amp; ... &amp; nums[r<sub>i</sub>] == andValues[i]</code> ，其中 <code>&amp;</code> 表示按位&nbsp;<code>AND</code>&nbsp;运算符。</p>

<p>返回将 <code>nums</code> 划分为 <code>m</code> 个子数组所能得到的可能的 <strong>最小 </strong>子数组 <strong>值</strong> 之和。如果无法完成这样的划分，则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,4,3,3,2], andValues = [0,3,3,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p>唯一可能的划分方法为：</p>

<ol>
	<li><code>[1,4]</code> 因为 <code>1 &amp; 4 == 0</code></li>
	<li><code>[3]</code> 因为单元素子数组的按位 <code>AND</code> 结果就是该元素本身</li>
	<li><code>[3]</code> 因为单元素子数组的按位 <code>AND</code> 结果就是该元素本身</li>
	<li><code>[2]</code> 因为单元素子数组的按位 <code>AND</code> 结果就是该元素本身</li>
</ol>

<p>这些子数组的值之和为 <code>4 + 3 + 3 + 2 = 12</code></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,5,7,7,7,5], andValues = [0,7,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">17</span></p>

<p><strong>解释：</strong></p>

<p>划分 <code>nums</code> 的三种方式为：</p>

<ol>
	<li><code>[[2,3,5],[7,7,7],[5]]</code> 其中子数组的值之和为 <code>5 + 7 + 5 = 17</code></li>
	<li><code>[[2,3,5,7],[7,7],[5]]</code> 其中子数组的值之和为 <code>7 + 7 + 5 = 19</code></li>
	<li><code>[[2,3,5,7,7],[7],[5]]</code> 其中子数组的值之和为 <code>7 + 7 + 5 = 19</code></li>
</ol>

<p>子数组值之和的最小可能值为 <code>17</code></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4], andValues = [2]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>整个数组 <code>nums</code> 的按位 <code>AND</code> 结果为 <code>0</code>。由于无法将 <code>nums</code> 划分为单个子数组使得元素的按位 <code>AND</code> 结果为 <code>2</code>，因此返回 <code>-1</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m == andValues.length &lt;= min(n, 10)</code></li>
	<li><code>1 &lt;= nums[i] &lt; 10<sup>5</sup></code></li>
	<li><code>0 &lt;= andValues[j] &lt; 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 线段树
- 队列
- 数组
- 二分查找
- 动态规划

## 提示

1. Let <code>dp[i][j]</code> be the optimal answer to split  <code>nums[0..(i - 1)]</code> into the first <code>j</code> andValues.
2. <code>dp[i][j] = min(dp[(i - z)][j - 1]) + nums[i - 1]</code> over all <code>x <= z <= y</code> and <code>dp[0][0] = 0</code>, where <code>x</code> and <code>y</code> are the longest and shortest subarrays ending with <code>nums[i - 1]</code> and the bitwise-and of all the values in it is <code>andValues[j - 1]</code>.
3. The answer is <code>dp[n][m]</code>.
4. To calculate <code>x</code> and <code>y</code>, we can use binary search (or sliding window). Note that the more values we have, the smaller the <code>AND</code> value is.
5. To calculate the result, we need to support RMQ (range minimum query). Segment tree is one way to do it in <code>O(log(n))</code>. But we can use Monotonic Queue since the ranges are indeed “sliding to right” which can be reduced to the classical minimum value in sliding window problem, for a <code>O(n)</code> solution.

## 示例

```
[1,4,3,3,2]
[0,3,3,2]
[2,3,5,7,7,7,5]
[0,7,5]
[1,2,3,4]
[2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumValueSum(vector<int>& nums, vector<int>& andValues) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumValueSum(int[] nums, int[] andValues) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        
```

### C

```c
int minimumValueSum(int* nums, int numsSize, int* andValues, int andValuesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumValueSum(int[] nums, int[] andValues) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} andValues
 * @return {number}
 */
var minimumValueSum = function(nums, andValues) {
    
};
```

### TypeScript

```typescript
function minimumValueSum(nums: number[], andValues: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $andValues
     * @return Integer
     */
    function minimumValueSum($nums, $andValues) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumValueSum(_ nums: [Int], _ andValues: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumValueSum(nums: IntArray, andValues: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumValueSum(List<int> nums, List<int> andValues) {
    
  }
}
```

### Go

```golang
func minimumValueSum(nums []int, andValues []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} and_values
# @return {Integer}
def minimum_value_sum(nums, and_values)
    
end
```

### Scala

```scala
object Solution {
    def minimumValueSum(nums: Array[Int], andValues: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_value_sum(nums: Vec<i32>, and_values: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-value-sum nums andValues)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_value_sum(Nums :: [integer()], AndValues :: [integer()]) -> integer().
minimum_value_sum(Nums, AndValues) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_value_sum(nums :: [integer], and_values :: [integer]) :: integer
  def minimum_value_sum(nums, and_values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumValueSum(nums: Array<Int64>, andValues: Array<Int64>): Int64 {

    }
}
```

