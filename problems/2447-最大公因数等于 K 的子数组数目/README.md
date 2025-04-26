# 2447. 最大公因数等于 K 的子数组数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code> ，请你统计并返回 <code>nums</code>&nbsp;的子数组中元素的最大公因数等于 <code>k</code>&nbsp;的子数组数目。</p>

<p><strong>子数组</strong> 是数组中一个连续的非空序列。</p>

<p><strong>数组的最大公因数</strong>&nbsp;是能整除数组中所有元素的最大整数。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>nums = [9,3,1,2,6,3], k = 3
<b>输出：</b>4
<b>解释：</b>nums 的子数组中，以 3 作为最大公因数的子数组如下：
- [9,<strong><em>3</em></strong>,1,2,6,3]
- [9,3,1,2,6,<em><strong>3</strong></em>]
- [<strong><em>9,3</em></strong>,1,2,6,3]
- [9,3,1,2,<em><strong>6,3</strong></em>]
</pre>

<p><b>示例 2：</b></p>

<pre><b>输入：</b>nums = [4], k = 7
<b>输出：</b>0
<b>解释：</b>不存在以 7 作为最大公因数的子数组。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. The constraints on nums.length are small. It is possible to check every subarray.
2. To calculate GCD, you can use a built-in function or the Euclidean Algorithm.

## 示例

```
[9,3,1,2,6,3]
3
[4]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarrayGCD(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int subarrayGCD(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarrayGCD(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarrayGCD = function(nums, k) {
    
};
```

### TypeScript

```typescript
function subarrayGCD(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarrayGCD($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarrayGCD(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarrayGCD(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarrayGCD(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func subarrayGCD(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_gcd(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def subarrayGCD(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarray_gcd(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarray-gcd nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec subarray_gcd(Nums :: [integer()], K :: integer()) -> integer().
subarray_gcd(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarray_gcd(nums :: [integer], k :: integer) :: integer
  def subarray_gcd(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarrayGCD(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

