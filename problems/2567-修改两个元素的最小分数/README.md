# 2567. 修改两个元素的最小分数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<ul>
	<li><code>nums</code> 的 <strong>最小</strong>&nbsp;得分是满足 <code>0 &lt;= i &lt; j &lt; nums.length</code>&nbsp;的&nbsp;<code>|nums[i]&nbsp;- nums[j]|</code>&nbsp;的最小值。</li>
	<li><code>nums</code>的 <strong>最大 </strong>得分是满足 <code>0 &lt;= i &lt; j &lt; nums.length</code>&nbsp;的&nbsp;<code>|nums[i]&nbsp;- nums[j]|</code>&nbsp;的最大值。</li>
	<li><code>nums</code>&nbsp;的分数是 <strong>最大</strong>&nbsp;得分与 <strong>最小</strong>&nbsp;得分的和。</li>
</ul>

<p>我们的目标是最小化&nbsp;<code>nums</code>&nbsp;的分数。你 <strong>最多</strong> 可以修改&nbsp;<code>nums</code>&nbsp;中&nbsp;<strong>2</strong>&nbsp;个元素的值。</p>

<p>请你返回修改&nbsp;<code>nums</code>&nbsp;中&nbsp;<strong>至多两个</strong>&nbsp;元素的值后，可以得到的 <strong>最小分数</strong>&nbsp;。</p>

<p><code>|x|</code>&nbsp;表示 <code>x</code>&nbsp;的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,3]
<b>输出：</b>0
<b>解释：</b>将 nums[1] 和 nums[2] 的值改为 1 ，nums 变为 [1,1,1] 。<code>|nums[i] - nums[j]|</code> 的值永远为 0 ，所以我们返回 0 + 0 = 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,7,8,5]
<b>输出：</b>3
<b>解释：
</b>将 nums[0] 和 nums[1] 的值变为 6 ，nums 变为 [6,6,7,8,5] 。
最小得分是 i = 0 且 j = 1 时得到的 |<code>nums[i] - nums[j]</code>| = |6 - 6| = 0 。
最大得分是 i = 3 且 j = 4 时得到的 |<code>nums[i] - nums[j]</code>| = |8 - 5| = 3 。
最大得分与最小得分之和为 3 。这是最优答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Changing the minimum or maximum values will only minimize the score.
2. Think about what all possible pairs of minimum and maximum values can be changed to form the minimum score.

## 示例

```
[1,4,7,8,5]
[1,4,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
```

### C

```c
int minimizeSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeSum = function(nums) {
    
};
```

### TypeScript

```typescript
function minimizeSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimizeSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimizeSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimize_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimizeSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_sum(Nums :: [integer()]) -> integer().
minimize_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_sum(nums :: [integer]) :: integer
  def minimize_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeSum(nums: Array<Int64>): Int64 {

    }
}
```

