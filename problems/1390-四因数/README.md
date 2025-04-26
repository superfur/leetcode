# 1390. 四因数

## 题目描述

<p>给你一个整数数组 <code>nums</code>，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [21,4,7]
<strong>输出：</strong>32
<strong>解释：</strong>
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [21,21]
<strong>输出:</strong> 64
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3,4,5]
<strong>输出:</strong> 0</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. Find the divisors of each element in the array.
2. You only need to loop to the square root of a number to find its divisors.

## 示例

```
[21,4,7]
[21,21]
[1,2,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumFourDivisors(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
```

### C

```c
int sumFourDivisors(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumFourDivisors(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumFourDivisors = function(nums) {
    
};
```

### TypeScript

```typescript
function sumFourDivisors(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumFourDivisors($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumFourDivisors(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumFourDivisors(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_four_divisors(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumFourDivisors(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-four-divisors nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_four_divisors(Nums :: [integer()]) -> integer().
sum_four_divisors(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_four_divisors(nums :: [integer]) :: integer
  def sum_four_divisors(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumFourDivisors(nums: Array<Int64>): Int64 {

    }
}
```

