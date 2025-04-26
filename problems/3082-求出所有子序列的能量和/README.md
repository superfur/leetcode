# 3082. 求出所有子序列的能量和

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一个整数数组的 <strong>能量</strong>&nbsp;定义为和 <strong>等于</strong>&nbsp;<code>k</code>&nbsp;的子序列的数目。</p>

<p>请你返回 <code>nums</code>&nbsp;中所有子序列的 <strong>能量和</strong>&nbsp;。</p>

<p>由于答案可能很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 3 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 6 </span></p>

<p><strong>解释：</strong></p>

<p>总共有&nbsp;<code>5</code>&nbsp;个能量不为 0 的子序列：</p>

<ul>
	<li>子序列&nbsp;<code>[<u><em><strong>1</strong></em></u>,<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>]</code> 有&nbsp;<code>2</code>&nbsp;个和为&nbsp;<code>3</code>&nbsp;的子序列：<code>[1,2,<u><strong><em>3</em></strong></u>]</code> 和 <code>[<u><strong><em>1</em></strong></u>,<u><strong><em>2</em></strong></u>,3]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[<u><em><strong>1</strong></em></u>,2,<u><em><strong>3</strong></em></u>]</code>&nbsp;有 <code>1</code>&nbsp;个和为&nbsp;<code>3</code>&nbsp;的子序列：<code>[1,2,<u><strong><em>3</em></strong></u>]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[1,<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>]</code> 有&nbsp;<code>1</code>&nbsp;个和为&nbsp;<code>3</code>&nbsp;的子序列：<code>[1,2,<u><strong><em>3</em></strong></u>]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[<u><em><strong>1</strong></em></u>,<u><em><strong>2</strong></em></u>,3]</code>&nbsp;有&nbsp;<code>1</code>&nbsp;个和为&nbsp;<code>3</code>&nbsp;的子序列：<code>[<u><strong><em>1</em></strong></u>,<u><strong><em>2</em></strong></u>,3]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[1,2,<u><em><strong>3</strong></em></u>]</code>&nbsp;有&nbsp;<code>1</code>&nbsp;个和为&nbsp;<code>3</code>&nbsp;的子序列：<code>[1,2,<u><strong><em>3</em></strong></u>]</code>&nbsp;。</li>
</ul>

<p>所以答案为&nbsp;<code>2 + 1 + 1 + 1 + 1 = 6</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [2,3,3], k = 5 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 4 </span></p>

<p><strong>解释：</strong></p>

<p>总共有&nbsp;<code>3</code>&nbsp;个能量不为 0 的子序列：</p>

<ul>
	<li>子序列&nbsp;<code>[<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>,<u><em><strong>3</strong></em></u>]</code>&nbsp;有 2 个子序列和为&nbsp;<code>5</code>&nbsp;：<code>[<u><strong><em>2</em></strong></u>,3,<u><strong><em>3</em></strong></u>]</code> 和&nbsp;<code>[<u><strong><em>2</em></strong></u>,<u><strong><em>3</em></strong></u>,3]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[<u><em><strong>2</strong></em></u>,3,<u><em><strong>3</strong></em></u>]</code>&nbsp;有 1 个子序列和为&nbsp;<code>5</code>&nbsp;：<code>[<u><strong><em>2</em></strong></u>,3,<u><strong><em>3</em></strong></u>]</code>&nbsp;。</li>
	<li>子序列&nbsp;<code>[<u><em><strong>2</strong></em></u>,<u><em><strong>3</strong></em></u>,3]</code>&nbsp;有 1 个子序列和为 <code>5</code>&nbsp;：<code>[<u><strong><em>2</em></strong></u>,<u><strong><em>3</em></strong></u>,3]</code>&nbsp;。</li>
</ul>

<p>所以答案为&nbsp;<code>2 + 1 + 1 = 4</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 7 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 0 </span></p>

<p><strong>解释：</strong>不存在和为 <code>7</code>&nbsp;的子序列，所以 <code>nums</code>&nbsp;的能量和为&nbsp;<code>0</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. If there is a subsequence of length <code>j</code> with the sum of elements <code>k</code>, it contributes <code>2<sup>n - j</sup></code> to the answer.
2. Let <code>dp[i][j]</code> represent the number of subsequences in the subarray <code>nums[0..i]</code> which have a sum of <code>j</code>.
3. We can find the <code>dp[i][k]</code> for all <code>0 <= i <= n-1</code> and multiply them with <code>2<sup>n - j</sup></code> to get final answer.

## 示例

```
[1,2,3]
3
[2,3,3]
5
[1,2,3]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfPower(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfPower(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfPower(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int sumOfPower(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfPower(int[] nums, int k) {
        
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
var sumOfPower = function(nums, k) {
    
};
```

### TypeScript

```typescript
function sumOfPower(nums: number[], k: number): number {
    
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
    function sumOfPower($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfPower(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfPower(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfPower(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func sumOfPower(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_power(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def sumOfPower(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_power(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-power nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_power(Nums :: [integer()], K :: integer()) -> integer().
sum_of_power(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_power(nums :: [integer], k :: integer) :: integer
  def sum_of_power(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfPower(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

