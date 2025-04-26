# 2521. 数组乘积中的不同质因数数目

## 题目描述

<p>给你一个正整数数组 <code>nums</code> ，对 <code>nums</code> 所有元素求积之后，找出并返回乘积中 <strong>不同质因数</strong> 的数目。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>质数</strong> 是指大于 <code>1</code> 且仅能被 <code>1</code> 及自身整除的数字。</li>
	<li>如果 <code>val2 / val1</code> 是一个整数，则整数 <code>val1</code> 是另一个整数 <code>val2</code> 的一个因数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,4,3,7,10,6]
<strong>输出：</strong>4
<strong>解释：</strong>
nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2<sup>5</sup> * 3<sup>2</sup> * 5 * 7 。
共有 4 个不同的质因数，所以返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [2,4,8,16]
<strong>输出：</strong>1
<strong>解释：</strong>
nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 2<sup>10</sup> 。
共有 1 个不同的质因数，所以返回 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 数论

## 提示

1. Do not multiply all the numbers together, as the product is too big to store.
2. Think about how each individual number's prime factors contribute to the prime factors of the product of the entire array.
3. Find the prime factors of each element in nums, and store all of them in a set to avoid duplicates.

## 示例

```
[2,4,3,7,10,6]
[2,4,8,16]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distinctPrimeFactors(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int distinctPrimeFactors(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
```

### C

```c
int distinctPrimeFactors(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistinctPrimeFactors(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctPrimeFactors = function(nums) {
    
};
```

### TypeScript

```typescript
function distinctPrimeFactors(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function distinctPrimeFactors($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distinctPrimeFactors(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distinctPrimeFactors(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distinctPrimeFactors(List<int> nums) {
    
  }
}
```

### Go

```golang
func distinctPrimeFactors(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def distinct_prime_factors(nums)
    
end
```

### Scala

```scala
object Solution {
    def distinctPrimeFactors(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distinct_prime_factors(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distinct-prime-factors nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec distinct_prime_factors(Nums :: [integer()]) -> integer().
distinct_prime_factors(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distinct_prime_factors(nums :: [integer]) :: integer
  def distinct_prime_factors(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distinctPrimeFactors(nums: Array<Int64>): Int64 {

    }
}
```

