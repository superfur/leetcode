# 3048. 标记所有下标的最早秒数 I

## 题目描述

<p>给你两个下标从 <strong>1</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code> 和&nbsp;<code>changeIndices</code>&nbsp;，数组的长度分别为&nbsp;<code>n</code> 和&nbsp;<code>m</code>&nbsp;。</p>

<p>一开始，<code>nums</code>&nbsp;中所有下标都是未标记的，你的任务是标记 <code>nums</code>&nbsp;中 <strong>所有</strong>&nbsp;下标。</p>

<p>从第 <code>1</code>&nbsp;秒到第 <code>m</code>&nbsp;秒（<b>包括&nbsp;</b>第&nbsp;<code>m</code>&nbsp;秒），对于每一秒 <code>s</code>&nbsp;，你可以执行以下操作 <strong>之一</strong>&nbsp;：</p>

<ul>
	<li>选择范围&nbsp;<code>[1, n]</code>&nbsp;中的一个下标 <code>i</code>&nbsp;，并且将&nbsp;<code>nums[i]</code> <strong>减少</strong>&nbsp;<code>1</code>&nbsp;。</li>
	<li>如果&nbsp;<code>nums[changeIndices[s]]</code>&nbsp;<strong>等于</strong>&nbsp;<code>0</code>&nbsp;，<strong>标记</strong>&nbsp;下标&nbsp;<code>changeIndices[s]</code>&nbsp;。</li>
	<li>什么也不做。</li>
</ul>

<p>请你返回范围 <code>[1, m]</code>&nbsp;中的一个整数，表示最优操作下，标记&nbsp;<code>nums</code>&nbsp;中 <strong>所有</strong>&nbsp;下标的 <strong>最早秒数</strong>&nbsp;，如果无法标记所有下标，返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]
<b>输出：</b>8
<b>解释：</b>这个例子中，我们总共有 8 秒。按照以下操作标记所有下标：
第 1 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [1,2,0] 。
第 2 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,2,0] 。
第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,1,0] 。
第 4 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,0,0] 。
第 5 秒，标​​​​​记 changeIndices[5] ，也就是标记下标 3 ，因为 nums[3] 等于 0 。
第 6 秒，标​​​​​记 changeIndices[6] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。
第 7 秒，什么也不做。
第 8 秒，标记 changeIndices[8] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。
现在所有下标已被标记。
最早可以在第 8 秒标记所有下标。
所以答案是 8 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,3], changeIndices = [1,1,1,2,1,1,1]
<b>输出：</b>6
<b>解释：</b>这个例子中，我们总共有 7 秒。按照以下操作标记所有下标：
第 1 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,2] 。
第 2 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,1] 。
第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,0] 。
第 4 秒：标​​​​​记 changeIndices[4] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。
第 5 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,0] 。
第 6 秒：标​​​​​记 changeIndices[6] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。
现在所有下标已被标记。
最早可以在第 6 秒标记所有下标。
所以答案是 6 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1], changeIndices = [2,2,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 这个例子中，无法标记所有下标，因为下标 1 不在 changeIndices 中。
所以答案是 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= m == changeIndices.length &lt;= 2000</code></li>
	<li><code>1 &lt;= changeIndices[i] &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Consider using binary search.
2. Suppose the <code>answer <= x</code>; we can mark each index as late as possible. Namely, mark each index at the last occurrence in the array <code>changeIndices[1..x]</code>.
3. When marking an index, which is the last occurrence at the second <code>i</code>, we check whether we have a sufficient number of decrement operations to mark all the previous indices whose last occurrences have already been marked, and the current index, i.e., <code>i - sum_of_marked_indices_values - cnt_of_marked_indices >= nums[changeIndices[i]]</code>.
4. The answer is the earliest second when all indices can be marked after running the binary search or <code>-1</code> if there is no such second.

## 示例

```
[2,2,0]
[2,2,2,2,3,2,2,1]
[1,3]
[1,1,1,2,1,1,1]
[0,1]
[2,2,2]
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

