# 1749. 任意子数组和的绝对值的最大值

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。一个子数组 <code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> 的 <strong>和的绝对值</strong> 为 <code>abs(nums<sub>l</sub> + nums<sub>l+1</sub> + ... + nums<sub>r-1</sub> + nums<sub>r</sub>)</code> 。</p>

<p>请你找出 <code>nums</code> 中 <strong>和的绝对值</strong> 最大的任意子数组（<b>可能为空</b>），并返回该 <strong>最大值</strong> 。</p>

<p><code>abs(x)</code> 定义如下：</p>

<ul>
	<li>如果 <code>x</code> 是负整数，那么 <code>abs(x) = -x</code> 。</li>
	<li>如果 <code>x</code> 是非负整数，那么 <code>abs(x) = x</code> 。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,-3,2,3,-4]
<b>输出：</b>5
<b>解释：</b>子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,-5,1,-4,3,-2]
<b>输出：</b>8
<b>解释：</b>子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. What if we asked for maximum sum, not absolute sum?
2. It's a standard problem that can be solved by Kadane's algorithm.
3. The key idea is the max absolute sum will be either the max sum or the min sum.
4. So just run kadane twice, once calculating the max sum and once calculating the min sum.

## 示例

```
[1,-3,2,3,-4]
[2,-5,1,-4,3,-2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxAbsoluteSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
```

### C

```c
int maxAbsoluteSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxAbsoluteSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAbsoluteSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxAbsoluteSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAbsoluteSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAbsoluteSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAbsoluteSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAbsoluteSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxAbsoluteSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_absolute_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxAbsoluteSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-absolute-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_absolute_sum(Nums :: [integer()]) -> integer().
max_absolute_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_absolute_sum(nums :: [integer]) :: integer
  def max_absolute_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAbsoluteSum(nums: Array<Int64>): Int64 {

    }
}
```

