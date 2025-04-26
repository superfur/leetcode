# 3049. 标记所有下标的最早秒数 II

## 题目描述

<p>给你两个下标从 <strong>1</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code> 和&nbsp;<code>changeIndices</code>&nbsp;，数组的长度分别为&nbsp;<code>n</code> 和&nbsp;<code>m</code>&nbsp;。</p>

<p>一开始，<code>nums</code>&nbsp;中所有下标都是未标记的，你的任务是标记 <code>nums</code>&nbsp;中 <strong>所有</strong>&nbsp;下标。</p>

<p>从第 <code>1</code>&nbsp;秒到第 <code>m</code>&nbsp;秒（<b>包括&nbsp;</b>第&nbsp;<code>m</code>&nbsp;秒），对于每一秒 <code>s</code>&nbsp;，你可以执行以下操作 <strong>之一</strong>&nbsp;：</p>

<ul>
	<li>选择范围&nbsp;<code>[1, n]</code>&nbsp;中的一个下标 <code>i</code>&nbsp;，并且将&nbsp;<code>nums[i]</code> <strong>减少</strong>&nbsp;<code>1</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[changeIndices[s]]</code>&nbsp;设置成任意的 <strong>非负</strong>&nbsp;整数。</li>
	<li>选择范围&nbsp;<code>[1, n]</code>&nbsp;中的一个下标&nbsp;<code>i</code>&nbsp;， 满足&nbsp;<code>nums[i]</code> <strong>等于</strong> <code>0</code>, 并 <strong>标记</strong>&nbsp;下标&nbsp;<code>i</code> 。</li>
	<li>什么也不做。</li>
</ul>

<p>请你返回范围 <code>[1, m]</code>&nbsp;中的一个整数，表示最优操作下，标记&nbsp;<code>nums</code>&nbsp;中 <strong>所有</strong>&nbsp;下标的 <strong>最早秒数</strong>&nbsp;，如果无法标记所有下标，返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]
<b>输出：</b>6
<b>解释：</b>这个例子中，我们总共有 7 秒。按照以下操作标记所有下标：
第 1 秒：将 nums[changeIndices[1]] 变为 0 。nums 变为 [0,2,3] 。
第 2 秒：将 nums[changeIndices[2]] 变为 0 。nums 变为 [0,2,0] 。
第 3 秒：将 nums[changeIndices[3]] 变为 0 。nums 变为 [0,0,0] 。
第 4 秒：标记下标 1 ，因为 nums[1] 等于 0 。
第 5 秒：标记下标 2 ，因为 nums[2] 等于 0 。
第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。
现在所有下标已被标记。
最早可以在第 6 秒标记所有下标。
所以答案是 6 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]
<b>输出：</b>7
<b>解释：</b>这个例子中，我们总共有 8 秒。按照以下操作标记所有下标：
第 1 秒：标记下标 1 ，因为 nums[1] 等于 0 。
第 2 秒：标记下标 2 ，因为 nums[2] 等于 0 。
第 3 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,1] 。
第 4 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,0] 。
第 5 秒：将 nums[3] 减少 1 。nums 变为 [0,0,0,0] 。
第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。
第 7 秒：标记下标 4 ，因为 nums[4] 等于 0 。
现在所有下标已被标记。
最早可以在第 7 秒标记所有下标。
所以答案是 7 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3], changeIndices = [1,2,3]
<b>输出：</b>-1
<strong>解释：</strong>这个例子中，无法标记所有下标，因为我们没有足够的秒数。
所以答案是 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 5000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= m == changeIndices.length &lt;= 5000</code></li>
	<li><code>1 &lt;= changeIndices[i] &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 二分查找
- 堆（优先队列）

## 提示

1. We need at least <code>n</code> seconds, and at most <code>sum(nums[i]) + n</code> seconds.
2. We can binary search the earliest second where all indices can be marked.
3. If there is an operation where we change <code>nums[changeIndices[i]]</code> to a non-negative value, it is best for it to satisfy the following constraints:<ul>
<li><code>nums[changeIndices[i]]</code> should not be equal to <code>0</code>.</li>
<li><code>nums[changeIndices[i]]</code> should be changed to <code>0</code>.</li>
<li>It should be the first position where <code>changeIndices[i]</code> occurs in <code>changeIndices</code>.</li>
<li>There should be another second, <code>j</code>, where <code>changeIndices[i]</code> will be marked. <code>j</code> is in the range <code>[i + 1, m]</code>.</li>
</ul>
4. Let <code>time_needed = sum(nums[i]) + n</code>. To check if we can mark all indices at some second <code>x</code>, we need to make <code>time_needed <= x</code>, using non-negative change operations as described previously.
5. Using a non-negative change operation on some <code>nums[changeIndices[i]]</code> that satisfies the constraints described previously reduces <code>time_needed</code> by <code>nums[changeIndices[i]] - 1</code>. So, we need to maximize the sum of <code>(nums[changeIndices[i]] - 1)</code> while ensuring that the non-negative change operations still satisfy the constraints.
6. Maximizing the sum of <code>(nums[changeIndices[i]] - 1)</code> can be done greedily using a min-priority queue and going in reverse starting from second <code>x</code> to second <code>1</code>, maximizing the sum of the values in the priority queue and ensuring that for every non-negative change operation on <code>nums[changeIndices[i]]</code> chosen, there is another second <code>j</code> in the range <code>[i + 1, x]</code> where <code>changeIndices[i]</code> can be marked.
7. The answer is the first value of <code>x</code> in the range <code>[1, m]</code> where it is possible to make <code>time_needed <= x</code>, or <code>-1</code> if there is no such second.

## 示例

```
[3,2,3]
[1,3,2,2,2,2,3]
[0,0,1,2]
[1,2,1,2,1,2,1,2]
[1,2,3]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int earliestSecondToMarkIndices(vector<int>& nums, vector<int>& changeIndices) {
        
    }
};
```

### Java

```java
class Solution {
    public int earliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        
```

### C

```c
int earliestSecondToMarkIndices(int* nums, int numsSize, int* changeIndices, int changeIndicesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} changeIndices
 * @return {number}
 */
var earliestSecondToMarkIndices = function(nums, changeIndices) {
    
};
```

### TypeScript

```typescript
function earliestSecondToMarkIndices(nums: number[], changeIndices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $changeIndices
     * @return Integer
     */
    function earliestSecondToMarkIndices($nums, $changeIndices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func earliestSecondToMarkIndices(_ nums: [Int], _ changeIndices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun earliestSecondToMarkIndices(nums: IntArray, changeIndices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int earliestSecondToMarkIndices(List<int> nums, List<int> changeIndices) {
    
  }
}
```

### Go

```golang
func earliestSecondToMarkIndices(nums []int, changeIndices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} change_indices
# @return {Integer}
def earliest_second_to_mark_indices(nums, change_indices)
    
end
```

### Scala

```scala
object Solution {
    def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (earliest-second-to-mark-indices nums changeIndices)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec earliest_second_to_mark_indices(Nums :: [integer()], ChangeIndices :: [integer()]) -> integer().
earliest_second_to_mark_indices(Nums, ChangeIndices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec earliest_second_to_mark_indices(nums :: [integer], change_indices :: [integer]) :: integer
  def earliest_second_to_mark_indices(nums, change_indices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func earliestSecondToMarkIndices(nums: Array<Int64>, changeIndices: Array<Int64>): Int64 {

    }
}
```

