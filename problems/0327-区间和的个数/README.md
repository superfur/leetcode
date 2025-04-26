# 327. 区间和的个数

## 题目描述

<p>给你一个整数数组 <code>nums</code> 以及两个整数 <code>lower</code> 和 <code>upper</code> 。求数组中，值位于范围 <code>[lower, upper]</code> （包含 <code>lower</code> 和 <code>upper</code>）之内的 <strong>区间和的个数</strong> 。</p>

<p><strong>区间和</strong> <code>S(i, j)</code> 表示在 <code>nums</code> 中，位置从 <code>i</code> 到 <code>j</code> 的元素之和，包含 <code>i</code> 和 <code>j</code> (<code>i</code> ≤ <code>j</code>)。</p>

<p> </p>
<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [-2,5,-1], lower = -2, upper = 2
<strong>输出：</strong>3
<strong>解释：</strong>存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0], lower = 0, upper = 0
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code></li>
	<li><code>-10<sup>5</sup> <= lower <= upper <= 10<sup>5</sup></code></li>
	<li>题目数据保证答案是一个 <strong>32 位</strong> 的整数</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 示例

```
[-2,5,-1]
-2
2
[0]
0
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        
    }
};
```

### Java

```java
class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
```

### C

```c
int countRangeSum(int* nums, int numsSize, int lower, int upper) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountRangeSum(int[] nums, int lower, int upper) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countRangeSum = function(nums, lower, upper) {
    
};
```

### TypeScript

```typescript
function countRangeSum(nums: number[], lower: number, upper: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function countRangeSum($nums, $lower, $upper) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countRangeSum(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countRangeSum(List<int> nums, int lower, int upper) {
    
  }
}
```

### Go

```golang
func countRangeSum(nums []int, lower int, upper int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def count_range_sum(nums, lower, upper)
    
end
```

### Scala

```scala
object Solution {
    def countRangeSum(nums: Array[Int], lower: Int, upper: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_range_sum(nums: Vec<i32>, lower: i32, upper: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-range-sum nums lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_range_sum(Nums :: [integer()], Lower :: integer(), Upper :: integer()) -> integer().
count_range_sum(Nums, Lower, Upper) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_range_sum(nums :: [integer], lower :: integer, upper :: integer) :: integer
  def count_range_sum(nums, lower, upper) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countRangeSum(nums: Array<Int64>, lower: Int64, upper: Int64): Int64 {

    }
}
```

