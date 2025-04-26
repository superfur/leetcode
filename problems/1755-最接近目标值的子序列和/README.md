# 1755. 最接近目标值的子序列和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个目标值 <code>goal</code> 。</p>

<p>你需要从 <code>nums</code> 中选出一个子序列，使子序列元素总和最接近 <code>goal</code> 。也就是说，如果子序列元素和为 <code>sum</code> ，你需要 <strong>最小化绝对差</strong> <code>abs(sum - goal)</code> 。</p>

<p>返回 <code>abs(sum - goal)</code> 可能的 <strong>最小值</strong> 。</p>

<p>注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [5,-7,3,5], goal = 6
<strong>输出：</strong>0
<strong>解释：</strong>选择整个数组作为选出的子序列，元素和为 6 。
子序列和与目标值相等，所以绝对差为 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [7,-9,15,-2], goal = -5
<strong>输出：</strong>1
<strong>解释：</strong>选出子序列 [7,-9,-2] ，元素和为 -4 。
绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3], goal = -7
<strong>输出：</strong>7
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 40</code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= goal &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 双指针
- 动态规划
- 状态压缩
- 排序

## 提示

1. The naive solution is to check all possible subsequences. This works in O(2^n).
2. Divide the array into two parts of nearly is equal size.
3. Consider all subsets of one part and make a list of all possible subset sums and sort this list.
4. Consider all subsets of the other part, and for each one, let its sum = x, do binary search to get the nearest possible value to goal - x in the first part.

## 示例

```
[5,-7,3,5]
6
[7,-9,15,-2]
-5
[1,2,3]
-7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minAbsDifference(vector<int>& nums, int goal) {
        
    }
};
```

### Java

```java
class Solution {
    public int minAbsDifference(int[] nums, int goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
```

### C

```c
int minAbsDifference(int* nums, int numsSize, int goal) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinAbsDifference(int[] nums, int goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var minAbsDifference = function(nums, goal) {
    
};
```

### TypeScript

```typescript
function minAbsDifference(nums: number[], goal: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $goal
     * @return Integer
     */
    function minAbsDifference($nums, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAbsDifference(_ nums: [Int], _ goal: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minAbsDifference(List<int> nums, int goal) {
    
  }
}
```

### Go

```golang
func minAbsDifference(nums []int, goal int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} goal
# @return {Integer}
def min_abs_difference(nums, goal)
    
end
```

### Scala

```scala
object Solution {
    def minAbsDifference(nums: Array[Int], goal: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_abs_difference(nums: Vec<i32>, goal: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-abs-difference nums goal)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_abs_difference(Nums :: [integer()], Goal :: integer()) -> integer().
min_abs_difference(Nums, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_abs_difference(nums :: [integer], goal :: integer) :: integer
  def min_abs_difference(nums, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAbsDifference(nums: Array<Int64>, goal: Int64): Int64 {

    }
}
```

