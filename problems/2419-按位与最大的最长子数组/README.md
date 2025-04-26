# 2419. 按位与最大的最长子数组

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> 。</p>

<p>考虑 <code>nums</code> 中进行 <strong>按位与（bitwise AND）</strong>运算得到的值 <strong>最大</strong> 的 <strong>非空</strong> 子数组。</p>

<ul>
	<li>换句话说，令 <code>k</code> 是 <code>nums</code> <strong>任意</strong> 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 <code>k</code> 的子数组。</li>
</ul>

<p>返回满足要求的 <strong>最长</strong> 子数组的长度。</p>

<p>数组的按位与就是对数组中的所有数字进行按位与运算。</p>

<p><strong>子数组</strong> 是数组中的一个连续元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,3,2,2]
<strong>输出：</strong>2
<strong>解释：</strong>
子数组按位与运算的最大值是 3 。
能得到此结果的最长子数组是 [3,3]，所以返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>1
<strong>解释：</strong>
子数组按位与运算的最大值是 4 。 
能得到此结果的最长子数组是 [4]，所以返回 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 脑筋急转弯
- 数组

## 提示

1. Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.
2. What does that tell us about the nature of the subarray that we should choose?

## 示例

```
[1,2,3,3,2,2]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int longestSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function longestSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_subarray(Nums :: [integer()]) -> integer().
longest_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer]) :: integer
  def longest_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubarray(nums: Array<Int64>): Int64 {

    }
}
```

