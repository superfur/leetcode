# 1913. 两个数对之间的最大乘积差

## 题目描述

<p>两个数对 <code>(a, b)</code> 和 <code>(c, d)</code> 之间的 <strong>乘积差</strong> 定义为 <code>(a * b) - (c * d)</code> 。</p>

<ul>
	<li>例如，<code>(5, 6)</code> 和 <code>(2, 7)</code> 之间的乘积差是 <code>(5 * 6) - (2 * 7) = 16</code> 。</li>
</ul>

<p>给你一个整数数组 <code>nums</code> ，选出四个 <strong>不同的</strong> 下标 <code>w</code>、<code>x</code>、<code>y</code> 和 <code>z</code> ，使数对 <code>(nums[w], nums[x])</code> 和 <code>(nums[y], nums[z])</code> 之间的 <strong>乘积差</strong> 取到 <strong>最大值</strong> 。</p>

<p>返回以这种方式取得的乘积差中的 <strong>最大值</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [5,6,2,7,4]
<strong>输出：</strong>34
<strong>解释：</strong>可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
乘积差是 (6 * 7) - (2 * 4) = 34
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [4,2,5,9,7,4,8]
<strong>输出：</strong>64
<strong>解释：</strong>可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
乘积差是 (9 * 8) - (2 * 4) = 64
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. If you only had to find the maximum product of 2 numbers in an array, which 2 numbers should you choose?
2. We only need to worry about 4 numbers in the array.

## 示例

```
[5,6,2,7,4]
[4,2,5,9,7,4,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProductDifference(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
```

### C

```c
int maxProductDifference(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProductDifference(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    
};
```

### TypeScript

```typescript
function maxProductDifference(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProductDifference($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProductDifference(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProductDifference(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxProductDifference(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_product_difference(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxProductDifference(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-product-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_product_difference(Nums :: [integer()]) -> integer().
max_product_difference(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product_difference(nums :: [integer]) :: integer
  def max_product_difference(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProductDifference(nums: Array<Int64>): Int64 {

    }
}
```

