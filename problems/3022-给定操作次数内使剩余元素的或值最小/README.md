# 3022. 给定操作次数内使剩余元素的或值最小

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一次操作中，你可以选择 <code>nums</code>&nbsp;中满足&nbsp;<code>0 &lt;= i &lt; nums.length - 1</code>&nbsp;的一个下标 <code>i</code>&nbsp;，并将&nbsp;<code>nums[i]</code> 和&nbsp;<code>nums[i + 1]</code>&nbsp;替换为数字&nbsp;<code>nums[i] &amp; nums[i + 1]</code>&nbsp;，其中&nbsp;<code>&amp;</code>&nbsp;表示按位&nbsp;<code>AND</code>&nbsp;操作。</p>

<p>请你返回 <strong>至多</strong>&nbsp;<code>k</code>&nbsp;次操作以内，使 <code>nums</code>&nbsp;中所有剩余元素按位 <code>OR</code>&nbsp;结果的 <strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,5,3,2,7], k = 2
<b>输出：</b>3
<b>解释：</b>执行以下操作：
1. 将 nums[0] 和 nums[1] 替换为 (nums[0] &amp; nums[1]) ，得到 nums 为 [1,3,2,7] 。
2. 将 nums[2] 和 nums[3] 替换为 (nums[2] &amp; nums[3]) ，得到 nums 为 [1,3,2] 。
最终数组的按位或值为 3 。
3 是 k 次操作以内，可以得到的剩余元素的最小按位或值。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [7,3,15,14,2,8], k = 4
<b>输出：</b>2
<b>解释：</b>执行以下操作：
1. 将 nums[0] 和 nums[1] 替换为 (nums[0] &amp; nums[1]) ，得到 nums 为 [3,15,14,2,8] 。
2. 将 nums[0] 和 nums[1] 替换为 (nums[0] &amp; nums[1]) ，得到 nums 为 [3,14,2,8] 。
3. 将 nums[0] 和 nums[1] 替换为 (nums[0] &amp; nums[1]) ，得到 nums 为 [2,2,8] 。
4. 将 nums[1] 和 nums[2] 替换为 (nums[1] &amp; nums[2]) ，得到 nums 为 [2,0] 。
最终数组的按位或值为 2 。
2 是 k 次操作以内，可以得到的剩余元素的最小按位或值。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [10,7,10,3,9,14,9,4], k = 1
<b>输出：</b>15
<b>解释：</b>不执行任何操作，nums 的按位或值为 15 。
15 是 k 次操作以内，可以得到的剩余元素的最小按位或值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; 2<sup>30</sup></code></li>
	<li><code>0 &lt;= k &lt; nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 位运算
- 数组

## 提示

1. From the most significant bit to the least significant bit, maintain the bits that will not be included in the final answer in a variable <code>mask</code>.
2. For a fixed bit, add it to <code>mask</code> then check if there exists some sequence of <code>k</code> operations such that <code>mask & answer == 0 </code> where <code>answer</code> is the bitwise-or of the remaining elements of <code>nums</code>. If there is no such sequence of operations, remove the current bit from <code>mask</code>. How can we perform this check?
3. Let <code>x</code> be the bitwise-and of all elements of <code>nums</code>. If <code>x AND mask != 0</code>, there is no sequence of operations that satisfies the condition in the previous hint. This is because even if we perform this operation <code>n - 1</code> times on the array, we will end up with <code>x</code> as the final element.
4. Otherwise, there exists at least one such sequence. It is sufficient to check if the number of operations in such a sequence is less than <code>k</code>. Let’s calculate the minimum number of operations in such a sequence.
5. Iterate over the array from left to right, if <code>nums[i] & mask != 0</code>, apply the operation on index <code>i</code>.
6. After iterating over all elements, let <code>x</code> be the bitwise-and of all elements of <code>nums</code>. If <code>x == 0</code>, then we have found the minimum number of operations. Otherwise, It can be proven that we need exactly one more operation so that <code>x == 0</code>.
7. The condition in the second hint is satisfied if and only if the minimum number of operations is less than or equal to <code>k</code>.

## 示例

```
[3,5,3,2,7]
2
[7,3,15,14,2,8]
4
[10,7,10,3,9,14,9,4]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOrAfterOperations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOrAfterOperations(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOrAfterOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minOrAfterOperations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOrAfterOperations(int[] nums, int k) {
        
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
var minOrAfterOperations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minOrAfterOperations(nums: number[], k: number): number {
    
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
    function minOrAfterOperations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOrAfterOperations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOrAfterOperations(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOrAfterOperations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minOrAfterOperations(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_or_after_operations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minOrAfterOperations(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_or_after_operations(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-or-after-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_or_after_operations(Nums :: [integer()], K :: integer()) -> integer().
min_or_after_operations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_or_after_operations(nums :: [integer], k :: integer) :: integer
  def min_or_after_operations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOrAfterOperations(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

