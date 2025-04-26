# 795. 区间子数组个数

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数：<code>left</code> 及 <code>right</code> 。找出 <code>nums</code> 中连续、非空且其中最大元素在范围&nbsp;<code>[left, right]</code> 内的子数组，并返回满足条件的子数组的个数。</p>

<p>生成的测试用例保证结果符合 <strong>32-bit</strong> 整数范围。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,4,3], left = 2, right = 3
<strong>输出：</strong>3
<strong>解释：</strong>满足条件的三个子数组：[2], [2, 1], [3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,9,2,5,6], left = 2, right = 8
<strong>输出：</strong>7
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针

## 示例

```
[2,1,4,3]
2
3
[2,9,2,5,6]
2
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
```

### C

```c
int numSubarrayBoundedMax(int* nums, int numsSize, int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSubarrayBoundedMax(int[] nums, int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var numSubarrayBoundedMax = function(nums, left, right) {
    
};
```

### TypeScript

```typescript
function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function numSubarrayBoundedMax($nums, $left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSubarrayBoundedMax(_ nums: [Int], _ left: Int, _ right: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubarrayBoundedMax(nums: IntArray, left: Int, right: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSubarrayBoundedMax(List<int> nums, int left, int right) {
    
  }
}
```

### Go

```golang
func numSubarrayBoundedMax(nums []int, left int, right int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def num_subarray_bounded_max(nums, left, right)
    
end
```

### Scala

```scala
object Solution {
    def numSubarrayBoundedMax(nums: Array[Int], left: Int, right: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-subarray-bounded-max nums left right)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_subarray_bounded_max(Nums :: [integer()], Left :: integer(), Right :: integer()) -> integer().
num_subarray_bounded_max(Nums, Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_subarray_bounded_max(nums :: [integer], left :: integer, right :: integer) :: integer
  def num_subarray_bounded_max(nums, left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSubarrayBoundedMax(nums: Array<Int64>, left: Int64, right: Int64): Int64 {

    }
}
```

