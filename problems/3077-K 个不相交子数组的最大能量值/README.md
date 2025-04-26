# 3077. K 个不相交子数组的最大能量值

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正奇数</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。</p>

<p><code>x</code> 个子数组的能量值定义为&nbsp;<code>strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1</code> ，其中&nbsp;<code>sum[i]</code>&nbsp;是第 <code>i</code>&nbsp;个子数组的和。更正式的，能量值是满足&nbsp;<code>1 &lt;= i &lt;= x</code>&nbsp;的所有&nbsp;<code>i</code>&nbsp;对应的&nbsp;<code>(-1)<sup>i+1</sup> * sum[i] * (x - i + 1)</code>&nbsp;之和。</p>

<p>你需要在 <code>nums</code>&nbsp;中选择 <code>k</code>&nbsp;个 <strong>不相交</strong><strong>子数组</strong>&nbsp;，使得&nbsp;<strong>能量值最大</strong>&nbsp;。</p>

<p>请你返回可以得到的 <strong>最大</strong><strong>能量值</strong>&nbsp;。</p>

<p><strong>注意</strong>，选出来的所有子数组&nbsp;<strong>不</strong>&nbsp;需要覆盖整个数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,-1,2], k = 3
<b>输出：</b>22
<b>解释：</b>选择 3 个子数组的最好方式是选择：nums[0..2] ，nums[3..3] 和 nums[4..4] 。能量值为 (1 + 2 + 3) * 3 - (-1) * 2 + 2 * 1 = 22 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [12,-2,-2,-2,-2], k = 5
<b>输出：</b>64
<b>解释：</b>唯一一种选 5 个不相交子数组的方案是：nums[0..0] ，nums[1..1] ，nums[2..2] ，nums[3..3] 和 nums[4..4] 。能量值为 12 * 5 - (-2) * 4 + (-2) * 3 - (-2) * 2 + (-2) * 1 = 64 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [-1,-2,-3], k = 1
<b>输出：</b>-1
<b>解释：</b>选择 1 个子数组的最优方案是：nums[0..0] 。能量值为 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li><code>1 &lt;= n * k &lt;= 10<sup>6</sup></code></li>
	<li><code>k</code> 是奇数。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 前缀和

## 提示

1. Let <code>dp[i][j][x == 0/1]</code> be the maximum strength to select <code>j</code> disjoint subarrays from the original array’s suffix (<code>nums[i..(n - 1)]</code>), x denotes whether we select the element or not.
2. Initially <code>dp[n][0][0] == 0</code>.
3. We have 
<code>dp[i][j][1] = nums[i] * get(j) + max(dp[i + 1][j - 1][0], dp[i + 1][j][1])</code> where <code>get(j) = j</code> if <code>j</code> is odd, otherwise <code>-j</code>.
4. We can select <code>nums[i]</code> as a separate subarray or select at least <code>nums[i]</code> and <code>nums[i + 1]</code> as the first subarray.
<code>dp[i][j][0] = max(dp[i + 1][j][0], dp[i][j][1])</code>.
5. The answer is <code>dp[0][k][0]</code>.

## 示例

```
[1,2,3,-1,2]
3
[12,-2,-2,-2,-2]
5
[-1,-2,-3]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumStrength(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumStrength(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long maximumStrength(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumStrength(int[] nums, int k) {
        
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
var maximumStrength = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumStrength(nums: number[], k: number): number {
    
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
    function maximumStrength($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumStrength(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumStrength(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumStrength(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumStrength(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_strength(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumStrength(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_strength(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-strength nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_strength(Nums :: [integer()], K :: integer()) -> integer().
maximum_strength(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_strength(nums :: [integer], k :: integer) :: integer
  def maximum_strength(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumStrength(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

