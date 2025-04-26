# 3471. 找出最大的几近缺失整数

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code> 。</p>

<p>如果整数 <code>x</code>&nbsp;恰好仅出现在&nbsp;<code>nums</code>&nbsp;中的一个大小为 <code>k</code>&nbsp;的子数组中，则认为&nbsp;<code>x</code>&nbsp;是 <code>nums</code>&nbsp;中的几近缺失（<strong>almost missing</strong>）整数。</p>

<p>返回 <code>nums</code> 中 <strong>最大的几近缺失</strong> 整数，如果不存在这样的整数，返回&nbsp;<code>-1</code>&nbsp;。</p>
<strong>子数组</strong> 是数组中的一个连续元素序列。

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,9,2,1,7], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>7</span></p>

<p><b>解释：</b></p>

<ul>
	<li>1 出现在两个大小为 3 的子数组中：<code>[9, 2, 1]</code>、<code>[2, 1, 7]</code></li>
	<li>2 出现在三个大小为&nbsp;3 的子数组中：<code>[3, 9, 2]</code>、<code>[9, 2, 1]</code>、<code>[2, 1, 7]</code></li>
	<li index="2">3 出现在一个大小为 3 的子数组中：<code>[3, 9, 2]</code></li>
	<li index="3">7 出现在一个大小为 3 的子数组中：<code>[2, 1, 7]</code></li>
	<li index="4">9 出现在两个大小为 3 的子数组中：<code>[3, 9, 2]</code>、<code>[9, 2, 1]</code></li>
</ul>

<p>返回 7 ，因为它满足题意的所有整数中最大的那个。</p>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,9,7,2,1,7], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<ul>
	<li>1 出现在两个大小为 3 的子数组中：<code>[9, 7, 2, 1]</code>、<code>[7, 2, 1, 7]</code></li>
	<li>2 出现在三个大小为 3 的子数组中：<code>[3, 9, 7, 2]</code>、<code>[9, 7, 2, 1]</code>、<code>[7, 2, 1, 7]</code></li>
	<li>3 出现在一个大小为 3 的子数组中：<code>[3, 9, 7, 2]</code></li>
	<li>7 出现在三个大小为 3 的子数组中：<code>[3, 9, 7, 2]</code>、<code>[9, 7, 2, 1]</code>、<code>[7, 2, 1, 7]</code></li>
	<li>9 出现在两个大小为 3 的子数组中：<code>[3, 9, 7, 2]</code>、<code>[9, 7, 2, 1]</code></li>
</ul>

<p>返回 3&nbsp;，因为它满足题意的所有整数中最大的那个。</p>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,0], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><b>解释：</b></p>

<p>不存在满足题意的整数。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Solve the problem for three different cases: <code>k = 1</code>, <code>k = n</code>, and <code>1 < k < n</code>
2. If <code>k = 1</code>, return the largest element that occurs exactly once in <code>nums</code>
3. If <code>k = n</code>, return the largest element in <code>nums</code>
4. If <code>1 < k < n</code>, all elements different from <code>nums[0]</code> and <code>nums[n - 1]</code> will occur in more than one subarray of size <code>k</code>. Hence, the answer is the largest of <code>nums[0]</code> and <code>nums[n - 1]</code> if they both occur exactly once in the array. If one of them occurs more than once, return the other. If both of them occur more than once, return -1.

## 示例

```
[3,9,2,1,7]
3
[3,9,7,2,1,7]
4
[0,0]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestInteger(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int largestInteger(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestInteger(int[] nums, int k) {
        
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
var largestInteger = function(nums, k) {
    
};
```

### TypeScript

```typescript
function largestInteger(nums: number[], k: number): number {
    
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
    function largestInteger($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestInteger(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestInteger(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestInteger(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func largestInteger(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_integer(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def largestInteger(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-integer nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_integer(Nums :: [integer()], K :: integer()) -> integer().
largest_integer(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_integer(nums :: [integer], k :: integer) :: integer
  def largest_integer(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestInteger(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

