# 2104. 子数组范围和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。<code>nums</code> 中，子数组的 <strong>范围</strong> 是子数组中最大元素和最小元素的差值。</p>

<p>返回 <code>nums</code> 中 <strong>所有</strong> 子数组范围的 <strong>和</strong> <em>。</em></p>

<p>子数组是数组中一个连续 <strong>非空</strong> 的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>4
<strong>解释：</strong>nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,3]
<strong>输出：</strong>4
<strong>解释：</strong>nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,-2,-3,4,1]
<strong>输出：</strong>59
<strong>解释：</strong>nums 中所有子数组范围的和是 59
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计一种时间复杂度为 <code>O(n)</code> 的解决方案吗？</p>


## 难度

Medium

## 标签

- 栈
- 数组
- 单调栈

## 提示

1. Can you get the max/min of a certain subarray by using the max/min of a smaller subarray within it?
2. Notice that the max of the subarray from index i to j is equal to max of (max of the subarray from index i to j-1) and nums[j].

## 示例

```
[1,2,3]
[1,3,3]
[4,-2,-3,4,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long subArrayRanges(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
```

### C

```c
long long subArrayRanges(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long SubArrayRanges(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var subArrayRanges = function(nums) {
    
};
```

### TypeScript

```typescript
function subArrayRanges(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subArrayRanges($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subArrayRanges(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subArrayRanges(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int subArrayRanges(List<int> nums) {
    
  }
}
```

### Go

```golang
func subArrayRanges(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sub_array_ranges(nums)
    
end
```

### Scala

```scala
object Solution {
    def subArrayRanges(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sub_array_ranges(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (sub-array-ranges nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sub_array_ranges(Nums :: [integer()]) -> integer().
sub_array_ranges(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sub_array_ranges(nums :: [integer]) :: integer
  def sub_array_ranges(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subArrayRanges(nums: Array<Int64>): Int64 {

    }
}
```

