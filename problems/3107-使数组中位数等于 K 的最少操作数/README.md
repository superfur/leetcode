# 3107. 使数组中位数等于 K 的最少操作数

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>非负</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。一次操作中，你可以选择任一元素&nbsp;加&nbsp;<code>1</code>&nbsp;或者减&nbsp;<code>1</code>&nbsp;。</p>

<p>请你返回将 <code>nums</code>&nbsp;<strong>中位数</strong>&nbsp;变为 <code>k</code>&nbsp;所需要的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>一个数组的中位数指的是数组按非递减顺序排序后最中间的元素。如果数组长度为偶数，我们选择中间两个数的较大值为中位数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,5,6,8,5], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b>我们将&nbsp;<code>nums[1]</code> 和&nbsp;<code>nums[4]</code>&nbsp;减 <code>1</code>&nbsp;得到&nbsp;<code>[2, 4, 6, 8, 4]</code>&nbsp;。现在数组的中位数等于&nbsp;<code>k</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,5,6,8,5], k = 7</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b>我们将&nbsp;<code>nums[1]</code>&nbsp;增加 1 两次，并且将&nbsp;<code>nums[2]</code>&nbsp;增加 1 一次，得到&nbsp;<code>[2, 7, 7, 8, 5]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,5,6], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b>数组中位数已经等于 <code>k</code>&nbsp;了。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort <code>nums</code> in non-descending order.
2. For all the smaller values on the left side of the median, change them to <code>k</code> if they are larger than <code>k</code>.
3. For all the larger values on the right side of the median, change them to <code>k</code> if they are smaller than <code>k</code>.

## 示例

```
[2,5,6,8,5]
4
[2,5,6,8,5]
7
[1,2,3,4,5,6]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minOperationsToMakeMedianK(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long minOperationsToMakeMedianK(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long minOperationsToMakeMedianK(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinOperationsToMakeMedianK(int[] nums, int k) {
        
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
var minOperationsToMakeMedianK = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minOperationsToMakeMedianK(nums: number[], k: number): number {
    
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
    function minOperationsToMakeMedianK($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperationsToMakeMedianK(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperationsToMakeMedianK(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperationsToMakeMedianK(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minOperationsToMakeMedianK(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations_to_make_median_k(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minOperationsToMakeMedianK(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations_to_make_median_k(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations-to-make-median-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations_to_make_median_k(Nums :: [integer()], K :: integer()) -> integer().
min_operations_to_make_median_k(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations_to_make_median_k(nums :: [integer], k :: integer) :: integer
  def min_operations_to_make_median_k(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperationsToMakeMedianK(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

