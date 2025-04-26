# 1856. 子数组最小乘积的最大值

## 题目描述

<p>一个数组的 <strong>最小乘积</strong> 定义为这个数组中 <strong>最小值</strong> <strong>乘以 </strong>数组的 <strong>和</strong> 。</p>

<ul>
	<li>比方说，数组 <code>[3,2,5]</code> （最小值是 <code>2</code>）的最小乘积为 <code>2 * (3+2+5) = 2 * 10 = 20</code> 。</li>
</ul>

<p>给你一个正整数数组 <code>nums</code> ，请你返回 <code>nums</code> 任意 <strong>非空子数组</strong> 的<strong>最小乘积</strong> 的 <strong>最大值</strong> 。由于答案可能很大，请你返回答案对  <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>的结果。</p>

<p>请注意，最小乘积的最大值考虑的是取余操作 <strong>之前</strong> 的结果。题目保证最小乘积的最大值在 <strong>不取余</strong> 的情况下可以用 <strong>64 位有符号整数</strong> 保存。</p>

<p><strong>子数组</strong> 定义为一个数组的 <strong>连续</strong> 部分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,<strong>2,3,2</strong>]
<b>输出：</b>14
<b>解释：</b>最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,<strong>3,3</strong>,1,2]
<b>输出：</b>18
<b>解释：</b>最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
3 * (3+3) = 3 * 6 = 18 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [3,1,<strong>5,6,4</strong>,2]
<b>输出：</b>60
<b>解释：</b>最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
4 * (5+6+4) = 4 * 15 = 60 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 前缀和
- 单调栈

## 提示

1. Is there a way we can sort the elements to simplify the problem?
2. Can we find the maximum min-product for every value in the array?

## 示例

```
[1,2,3,2]
[2,3,3,1,2]
[3,1,5,6,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumMinProduct(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSumMinProduct(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumMinProduct = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSumMinProduct(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumMinProduct($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumMinProduct(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumMinProduct(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumMinProduct(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSumMinProduct(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_sum_min_product(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSumMinProduct(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_min_product(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-min-product nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_min_product(Nums :: [integer()]) -> integer().
max_sum_min_product(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_min_product(nums :: [integer]) :: integer
  def max_sum_min_product(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumMinProduct(nums: Array<Int64>): Int64 {

    }
}
```

