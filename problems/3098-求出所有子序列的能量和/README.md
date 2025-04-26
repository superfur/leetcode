# 3098. 求出所有子序列的能量和

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一个 <span data-keyword="subsequence-array">子序列</span> 的 <strong>能量</strong>&nbsp;定义为子序列中&nbsp;<strong>任意</strong>&nbsp;两个元素的差值绝对值的 <strong>最小值</strong>&nbsp;。</p>

<p>请你返回 <code>nums</code>&nbsp;中长度 <strong>等于</strong>&nbsp;<code>k</code>&nbsp;的 <strong>所有</strong>&nbsp;子序列的 <strong>能量和</strong>&nbsp;。</p>

<p>由于答案可能会很大，将答案对&nbsp;<code>10<sup>9 </sup>+ 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中总共有 4 个长度为 3 的子序列：<code>[1,2,3]</code>&nbsp;，<code>[1,3,4]</code>&nbsp;，<code>[1,2,4]</code>&nbsp;和&nbsp;<code>[2,3,4]</code>&nbsp;。能量和为 <code>|2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中唯一一个长度为 2 的子序列是&nbsp;<code>[2,2]</code>&nbsp;。能量和为&nbsp;<code>|2 - 2| = 0</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [4,3,-1], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>10</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;总共有 3 个长度为 2 的子序列：<code>[4,3]</code>&nbsp;，<code>[4,-1]</code>&nbsp;和&nbsp;<code>[3,-1]</code>&nbsp;。能量和为&nbsp;<code>|4 - 3| + |4 - (-1)| + |3 - (-1)| = 10</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>-10<sup>8</sup> &lt;= nums[i] &lt;= 10<sup>8</sup> </code></li>
	<li><code>2 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. Sort <code>nums</code>.
2. There are at most <code>n<sup>2</sup></code> distinct differences.
3. For a particular difference <code>d</code>, let <code>dp[len][i][j]</code> be the number of subsequences of length <code>len</code> in the subarray <code>nums[0..i]</code> where the last element picked was at index <code>j</code>.
4. For each index, we can check if it can be picked if <code>nums[i] - nums[j] <= d</code>.

## 示例

```
[1,2,3,4]
3
[2,2]
2
[4,3,-1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfPowers(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfPowers(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfPowers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int sumOfPowers(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfPowers(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var sumOfPowers = function(nums, k) {
    
};
```

### TypeScript

```typescript
function sumOfPowers(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function sumOfPowers($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfPowers(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfPowers(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfPowers(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func sumOfPowers(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_powers(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def sumOfPowers(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_powers(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-powers nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_powers(Nums :: [integer()], K :: integer()) -> integer().
sum_of_powers(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_powers(nums :: [integer], k :: integer) :: integer
  def sum_of_powers(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfPowers(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

