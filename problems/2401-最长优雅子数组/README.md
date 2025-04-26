# 2401. 最长优雅子数组

## 题目描述

<p>给你一个由 <strong>正</strong> 整数组成的数组 <code>nums</code> 。</p>

<p>如果&nbsp;<code>nums</code> 的子数组中位于 <strong>不同</strong> 位置的每对元素按位 <strong>与（AND）</strong>运算的结果等于 <code>0</code> ，则称该子数组为 <strong>优雅</strong> 子数组。</p>

<p>返回 <strong>最长</strong> 的优雅子数组的长度。</p>

<p><strong>子数组</strong> 是数组中的一个 <strong>连续</strong> 部分。</p>

<p><strong>注意：</strong>长度为 <code>1</code> 的子数组始终视作优雅子数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,8,48,10]
<strong>输出：</strong>3
<strong>解释：</strong>最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
- 3 AND 8 = 0
- 3 AND 48 = 0
- 8 AND 48 = 0
可以证明不存在更长的优雅子数组，所以返回 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [3,1,5,11,13]
<strong>输出：</strong>1
<strong>解释：</strong>最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 滑动窗口

## 提示

1. What is the maximum possible length of a nice subarray?
2. If two numbers have bitwise AND equal to zero, they do not have any common set bit. A number <code>x <= 10<sup>9</sup></code> only has 30 bits, hence the length of the longest nice subarray cannot exceed 30.

## 示例

```
[1,3,8,48,10]
[3,1,5,11,13]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestNiceSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int longestNiceSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestNiceSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function longestNiceSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestNiceSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestNiceSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestNiceSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestNiceSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestNiceSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_nice_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestNiceSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-nice-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_nice_subarray(Nums :: [integer()]) -> integer().
longest_nice_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_nice_subarray(nums :: [integer]) :: integer
  def longest_nice_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestNiceSubarray(nums: Array<Int64>): Int64 {

    }
}
```

