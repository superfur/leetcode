# 2818. 操作使得分最大

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的正整数数组&nbsp;<code>nums</code>&nbsp;和一个整数 <code>k</code>&nbsp;。</p>

<p>一开始，你的分数为 <code>1</code>&nbsp;。你可以进行以下操作至多 <code>k</code>&nbsp;次，目标是使你的分数最大：</p>

<ul>
	<li>选择一个之前没有选过的 <strong>非空</strong>&nbsp;子数组&nbsp;<code>nums[l, ..., r]</code>&nbsp;。</li>
	<li>从&nbsp;<code>nums[l, ..., r]</code>&nbsp;里面选择一个 <strong>质数分数</strong>&nbsp;最高的元素 <code>x</code>&nbsp;。如果多个元素质数分数相同且最高，选择下标最小的一个。</li>
	<li>将你的分数乘以&nbsp;<code>x</code>&nbsp;。</li>
</ul>

<p><code>nums[l, ..., r]</code>&nbsp;表示&nbsp;<code>nums</code>&nbsp;中起始下标为&nbsp;<code>l</code>&nbsp;，结束下标为 <code>r</code>&nbsp;的子数组，两个端点都包含。</p>

<p>一个整数的 <strong>质数分数</strong>&nbsp;等于&nbsp;<code>x</code>&nbsp;不同质因子的数目。比方说，&nbsp;<code>300</code>&nbsp;的质数分数为&nbsp;<code>3</code>&nbsp;，因为&nbsp;<code>300 = 2 * 2 * 3 * 5 * 5</code>&nbsp;。</p>

<p>请你返回进行至多 <code>k</code>&nbsp;次操作后，可以得到的 <strong>最大分数</strong>&nbsp;。</p>

<p>由于答案可能很大，请你将结果对&nbsp;<code>10<sup>9 </sup>+ 7</code>&nbsp;取余后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [8,3,9,3,8], k = 2
<b>输出：</b>81
<b>解释：</b>进行以下操作可以得到分数 81 ：
- 选择子数组 nums[2, ..., 2] 。nums[2] 是子数组中唯一的元素。所以我们将分数乘以 nums[2] ，分数变为 1 * 9 = 9 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 1 ，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为 9 * 9 = 81 。
81 是可以得到的最高得分。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [19,12,14,6,10,18], k = 3
<b>输出：</b>4788
<b>解释：</b>进行以下操作可以得到分数 4788 ：
- 选择子数组 nums[0, ..., 0] 。nums[0] 是子数组中唯一的元素。所以我们将分数乘以 nums[0] ，分数变为 1 * 19 = 19 。
- 选择子数组 nums[5, ..., 5] 。nums[5] 是子数组中唯一的元素。所以我们将分数乘以 nums[5] ，分数变为 19 * 18 = 342 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 2，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为  342 * 14 = 4788 。
4788 是可以得到的最高的分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(n * (n + 1) / 2, 10<sup>9</sup>)</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 数学
- 数论
- 排序
- 单调栈

## 提示

1. <div class="_1l1MA">Calculate <code>nums[i]</code>'s prime score <code>s[i]</code> by factoring in <code>O(sqrt(nums[i]))</code> time.</div>
2. <div class="_1l1MA">For each <code>nums[i]</code>, find the nearest index <code>left[i]</code> on the left (if any) such that <code>s[left[i]] >= s[i]</code>. if none is found, set <code>left[i]</code> to <code>-1</code>. Similarly, find the nearest index <code>right[i]</code> on the right (if any) such that <code>s[right[i]] > s[i]</code>. If none is found, set <code>right[i]</code> to <code>n</code>.</div>
3. <div class="_1l1MA">Use a monotonic stack to compute <code>right[i]</code> and <code>left[i]</code>.</div>
4. <div class="_1l1MA">For each index <code>i</code>, if <code>left[i] + 1 <= l <= i <= r <= right[i] - 1</code>, then <code>s[i]</code> is the maximum value in the range <code>[l, r]</code>. For this particular <code>i</code>, there are <code>ranges[i] = (i - left[i]) * (right[i] - i)</code> ranges where index <code>i</code> will be chosen.</div>
5. <div class="_1l1MA">Loop over all elements of <code>nums</code> by non-increasing prime score, each element will be chosen <code>min(ranges[i], remainingK)</code> times, where <code>reaminingK</code> denotes the number of remaining operations. Therefore, the score will be multiplied by <code>s[i]^min(ranges[i],remainingK)</code>.</div>
6. <div class="_1l1MA">Use fast exponentiation to quickly calculate <code>A^B mod C</code>.</div>

## 示例

```
[8,3,9,3,8]
2
[19,12,14,6,10,18]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumScore(List<Integer> nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumScore(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(IList<int> nums, int k) {
        
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
var maximumScore = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumScore(nums: number[], k: number): number {
    
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
    function maximumScore($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(nums: List<Int>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumScore(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(nums: List[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(Nums :: [integer()], K :: integer()) -> integer().
maximum_score(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(nums :: [integer], k :: integer) :: integer
  def maximum_score(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(nums: ArrayList<Int64>, k: Int64): Int64 {

    }
}
```

