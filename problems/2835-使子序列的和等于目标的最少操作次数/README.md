# 2835. 使子序列的和等于目标的最少操作次数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums</code>&nbsp;，它包含 <strong>非负</strong>&nbsp;整数，且全部为 <code>2</code>&nbsp;的幂，同时给你一个整数&nbsp;<code>target</code>&nbsp;。</p>

<p>一次操作中，你必须对数组做以下修改：</p>

<ul>
	<li>选择数组中一个元素&nbsp;<code>nums[i]</code>&nbsp;，满足&nbsp;<code>nums[i] &gt; 1</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[i]</code>&nbsp;从数组中删除。</li>
	<li>在 <code>nums</code>&nbsp;的 <strong>末尾</strong>&nbsp;添加 <strong>两个</strong>&nbsp;数，值都为&nbsp;<code>nums[i] / 2</code>&nbsp;。</li>
</ul>

<p>你的目标是让 <code>nums</code>&nbsp;的一个 <strong>子序列</strong>&nbsp;的元素和等于&nbsp;<code>target</code>&nbsp;，请你返回达成这一目标的 <strong>最少操作次数</strong>&nbsp;。如果无法得到这样的子序列，请你返回 <code>-1</code>&nbsp;。</p>

<p>数组中一个 <strong>子序列</strong>&nbsp;是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,8], target = 7
<b>输出：</b>1
<b>解释：</b>第一次操作中，我们选择元素 nums[2] 。数组变为 nums = [1,2,4,4] 。
这时候，nums 包含子序列 [1,2,4] ，和为 7 。
无法通过更少的操作得到和为 7 的子序列。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,32,1,2], target = 12
<b>输出：</b>2
<b>解释：</b>第一次操作中，我们选择元素 nums[1] 。数组变为 nums = [1,1,2,16,16] 。
第二次操作中，我们选择元素 nums[3] 。数组变为 nums = [1,1,2,16,8,8] 。
这时候，nums 包含子序列 [1,1,2,8] ，和为 12 。
无法通过更少的操作得到和为 12 的子序列。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,32,1], target = 35
<b>输出：</b>-1
<b>解释：</b>无法得到和为 35 的子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2<sup>30</sup></code></li>
	<li><code>nums</code>&nbsp;只包含非负整数，且均为 2 的幂。</li>
	<li><code>1 &lt;= target &lt; 2<sup>31</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 位运算
- 数组

## 提示

1. <div class="_1l1MA">if <code>target > sum(nums[i]) </code>, return <code>-1</code>. Otherwise, an answer exists</div>
2. <div class="_1l1MA">Solve the problem for each set bit of <code>target</code>, independently, from least significant to most significant bit. </div>
3. <div class="_1l1MA">For each set <code>bit</code> of <code>target</code> from least to most significant, let <code>X = sum(nums[i])</code> for <code>nums[i] <= 2^bit</code>.</div>
4. <div class="_1l1MA">
if <code>X >= 2^bit</code>, repeatedly select the maximum <code>nums[i]</code> such that <code>nums[i]<=2^bit</code> that has not been selected yet, until the sum of selected elements equals <code>2^bit</code>. The selected <code>nums[i]</code> will be part of the subsequence whose elements sum to target, so those elements can not be selected again.
</div>
5. <div class="_1l1MA">Otherwise, select the smallest <code>nums[i]</code> such that <code>nums[i] > 2^bit</code>, delete <code>nums[i]</code> and add two occurences of <code>nums[i]/2</code>. Without moving to the next <code>bit</code>, go back to the step in hint 3.</div>

## 示例

```
[1,2,8]
7
[1,32,1,2]
12
[1,32,1]
35
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(List<Integer> nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(IList<int> nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minOperations = function(nums, target) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function minOperations($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: List<Int>, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_operations(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: List[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()], Target :: integer()) -> integer().
min_operations(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], target :: integer) :: integer
  def min_operations(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: ArrayList<Int64>, target: Int64): Int64 {

    }
}
```

