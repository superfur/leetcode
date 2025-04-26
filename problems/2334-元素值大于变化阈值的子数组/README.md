# 2334. 元素值大于变化阈值的子数组

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>threshold</code>&nbsp;。</p>

<p>找到长度为 <code>k</code>&nbsp;的&nbsp;<code>nums</code>&nbsp;子数组，满足数组中&nbsp;<strong>每个</strong>&nbsp;元素都 <strong>大于</strong>&nbsp;<code>threshold / k</code>&nbsp;。</p>

<p>请你返回满足要求的 <strong>任意</strong>&nbsp;子数组的 <strong>大小</strong>&nbsp;。如果没有这样的子数组，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p><strong>子数组</strong> 是数组中一段连续非空的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,3,4,3,1], threshold = 6
<b>输出：</b>3
<b>解释：</b>子数组 [3,4,3] 大小为 3 ，每个元素都大于 6 / 3 = 2 。
注意这是唯一合法的子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [6,5,6,5,8], threshold = 7
<b>输出：</b>1
<b>解释：</b>子数组 [8] 大小为 1 ，且 8 &gt; 7 / 1 = 7 。所以返回 1 。
注意子数组 [6,5] 大小为 2 ，每个元素都大于 7 / 2 = 3.5 。
类似的，子数组 [6,5,6] ，[6,5,6,5] ，[6,5,6,5,8] 都是符合条件的子数组。
所以返回 2, 3, 4 和 5 都可以。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], threshold &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 并查集
- 数组
- 单调栈

## 提示

1. For all elements to be greater than the threshold/length, the minimum element in the subarray must be greater than the threshold/length.
2. For a given index, could you find the largest subarray such that the given index is the minimum element?
3. Could you use a monotonic stack to get the next and previous smallest element for every index?

## 示例

```
[1,3,4,3,1]
6
[6,5,6,5,8]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int validSubarraySize(vector<int>& nums, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int validSubarraySize(int[] nums, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        
```

### C

```c
int validSubarraySize(int* nums, int numsSize, int threshold) {
    
}
```

### C#

```csharp
public class Solution {
    public int ValidSubarraySize(int[] nums, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var validSubarraySize = function(nums, threshold) {
    
};
```

### TypeScript

```typescript
function validSubarraySize(nums: number[], threshold: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function validSubarraySize($nums, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validSubarraySize(_ nums: [Int], _ threshold: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validSubarraySize(nums: IntArray, threshold: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int validSubarraySize(List<int> nums, int threshold) {
    
  }
}
```

### Go

```golang
func validSubarraySize(nums []int, threshold int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def valid_subarray_size(nums, threshold)
    
end
```

### Scala

```scala
object Solution {
    def validSubarraySize(nums: Array[Int], threshold: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_subarray_size(nums: Vec<i32>, threshold: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (valid-subarray-size nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec valid_subarray_size(Nums :: [integer()], Threshold :: integer()) -> integer().
valid_subarray_size(Nums, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_subarray_size(nums :: [integer], threshold :: integer) :: integer
  def valid_subarray_size(nums, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validSubarraySize(nums: Array<Int64>, threshold: Int64): Int64 {

    }
}
```

