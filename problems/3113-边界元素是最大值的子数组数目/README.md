# 3113. 边界元素是最大值的子数组数目

## 题目描述

<p>给你一个 <strong>正</strong>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>请你求出&nbsp;<code>nums</code>&nbsp;中有多少个子数组，满足子数组中&nbsp;<strong>第一个</strong>&nbsp;和 <strong>最后一个</strong>&nbsp;元素都是这个子数组中的 <strong>最大</strong>&nbsp;值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,4,3,3,2]</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><strong>解释：</strong></p>

<p>总共有 6 个子数组满足第一个元素和最后一个元素都是子数组中的最大值：</p>

<ul>
	<li>子数组&nbsp;<code>[<u><em><strong>1</strong></em></u>,4,3,3,2]</code>&nbsp;，最大元素为 1 ，第一个和最后一个元素都是 1 。</li>
	<li>子数组&nbsp;<code>[1,<u><em><strong>4</strong></em></u>,3,3,2]</code>&nbsp;，最大元素为 4 ，第一个和最后一个元素都是 4 。</li>
	<li>子数组&nbsp;<code>[1,4,<u><em><strong>3</strong></em></u>,3,2]</code>&nbsp;，最大元素为 3 ，第一个和最后一个元素都是 3 。</li>
	<li>子数组&nbsp;<code>[1,4,3,<u><em><strong>3</strong></em></u>,2]</code>&nbsp;，最大元素为 3 ，第一个和最后一个元素都是 3 。</li>
	<li>子数组&nbsp;<code>[1,4,3,3,<u><em><strong>2</strong></em></u>]</code>&nbsp;，最大元素为 2 ，第一个和最后一个元素都是 2 。</li>
	<li>子数组&nbsp;<code>[1,4,<u><em><strong>3,3</strong></em></u>,2]</code>&nbsp;，最大元素为 3 ，第一个和最后一个元素都是 3 。</li>
</ul>

<p>所以我们返回 6 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,3,3]</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><strong>解释：</strong></p>

<p>总共有 6 个子数组满足第一个元素和最后一个元素都是子数组中的最大值：</p>

<ul>
	<li>子数组 <code>[<u><em><strong>3</strong></em></u>,3,3]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
	<li>子数组 <code>[3,<u><em><strong>3</strong></em></u>,3]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
	<li>子数组 <code>[3,3,<u><em><strong>3</strong></em></u>]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
	<li>子数组 <code>[<u><em><strong>3,3</strong></em></u>,3]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
	<li>子数组 <code>[3,<u><em><strong>3,3</strong></em></u>]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
	<li>子数组 <code>[<u><em><strong>3,3,3</strong></em></u>]</code>&nbsp;，最大元素为 3&nbsp;，第一个和最后一个元素都是 3&nbsp;。</li>
</ul>

<p>所以我们返回 6 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中只有一个子数组&nbsp;<code>[<em><strong>1</strong></em>]</code>&nbsp;，最大元素为 1 ，第一个和最后一个元素都是 1 。</p>

<p>所以我们返回 1 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 二分查找
- 单调栈

## 提示

1. For each element <code>nums[i]</code>, we can count the number of valid subarrays ending with it.
2. For each index <code>i</code>, find the nearest index <code>j</code> on its left <code>(j < i)</code> such that <code>nums[j] < nums[i]</code>. This can be done via a monotonic stack.
3. For each index <code>i</code>, find the number of indices <code>k</code> in the window <code>[j + 1, i]</code> such that <code>nums[k] == nums[i]</code>, this is the number of the valid subarrays ending with <code>nums[i]</code>. This can be done by sliding window.
4. Sum the answer of all the indices <code>i</code> to get the final result.
5. Is it possible to use DSU as an alternate solution?

## 示例

```
[1,4,3,3,2]
[3,3,3]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long numberOfSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long numberOfSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
long long numberOfSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long NumberOfSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfSubarrays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubarrays(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfSubarrays(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def number_of_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubarrays(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_subarrays(Nums :: [integer()]) -> integer().
number_of_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_subarrays(nums :: [integer]) :: integer
  def number_of_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubarrays(nums: Array<Int64>): Int64 {

    }
}
```

