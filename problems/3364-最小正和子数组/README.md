# 3364. 最小正和子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和 <strong>两个</strong> 整数 <code>l</code> 和 <code>r</code>。你的任务是找到一个长度在 <code>l</code> 和 <code>r</code> 之间（包含）且和大于 0 的 <strong>子数组</strong> 的 <strong>最小</strong> 和。</p>

<p>返回满足条件的子数组的 <strong>最小</strong> 和。如果不存在这样的子数组，则返回 -1。</p>

<p><strong>子数组</strong> 是数组中的一个连续 <b>非空</b> 元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3, -2, 1, 4], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>长度在 <code>l = 2</code> 和 <code>r = 3</code> 之间且和大于 0 的子数组有：</p>

<ul>
	<li><code>[3, -2]</code> 和为 1</li>
	<li><code>[1, 4]</code> 和为 5</li>
	<li><code>[3, -2, 1]</code> 和为 2</li>
	<li><code>[-2, 1, 4]</code> 和为 3</li>
</ul>

<p>其中，子数组 <code>[3, -2]</code> 的和为 1，是所有正和中最小的。因此，答案为 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-2, 2, -3, 1], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>不存在长度在 <code>l</code> 和 <code>r</code> 之间且和大于 0 的子数组。因此，答案为 -1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1, 2, 3, 4], l = 2, r = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>子数组 <code>[1, 2]</code> 的长度为 2，和为&nbsp;3，是所有正和中最小的。因此，答案为 3。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= l &lt;= r &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 前缀和
- 滑动窗口

## 提示

1. Check every subarray, since constraints are small.

## 示例

```
[3,-2,1,4]
2
3
[-2,2,-3,1]
2
3
[1,2,3,4]
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
```

### C

```c
int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var minimumSumSubarray = function(nums, l, r) {
    
};
```

### TypeScript

```typescript
function minimumSumSubarray(nums: number[], l: number, r: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function minimumSumSubarray($nums, $l, $r) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSumSubarray(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSumSubarray(List<int> nums, int l, int r) {
    
  }
}
```

### Go

```golang
func minimumSumSubarray(nums []int, l int, r int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def minimum_sum_subarray(nums, l, r)
    
end
```

### Scala

```scala
object Solution {
    def minimumSumSubarray(nums: List[Int], l: Int, r: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-sum-subarray nums l r)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_sum_subarray(Nums :: [integer()], L :: integer(), R :: integer()) -> integer().
minimum_sum_subarray(Nums, L, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_sum_subarray(nums :: [integer], l :: integer, r :: integer) :: integer
  def minimum_sum_subarray(nums, l, r) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSumSubarray(nums: ArrayList<Int64>, l: Int64, r: Int64): Int64 {

    }
}
```

