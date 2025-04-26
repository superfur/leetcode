# 1862. 向下取整数对和

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，请你返回所有下标对 <code>0 &lt;= i, j &lt; nums.length</code> 的 <code>floor(nums[i] / nums[j])</code> 结果之和。由于答案可能会很大，请你返回答案对<code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>函数 <code>floor()</code> 返回输入数字的整数部分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,5,9]
<b>输出：</b>10
<strong>解释：</strong>
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
我们计算每一个数对商向下取整的结果并求和得到 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [7,7,7,7,7,7,7]
<b>输出：</b>49
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 二分查找
- 前缀和

## 提示

1. Find the frequency (number of occurrences) of all elements in the array.
2. For each element, iterate through its multiples and multiply frequencies to find the answer.

## 示例

```
[2,5,9]
[7,7,7,7,7,7,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfFlooredPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        
```

### C

```c
int sumOfFlooredPairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfFlooredPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfFlooredPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function sumOfFlooredPairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfFlooredPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfFlooredPairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfFlooredPairs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfFlooredPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumOfFlooredPairs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_of_floored_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumOfFlooredPairs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_floored_pairs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-floored-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_floored_pairs(Nums :: [integer()]) -> integer().
sum_of_floored_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_floored_pairs(nums :: [integer]) :: integer
  def sum_of_floored_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfFlooredPairs(nums: Array<Int64>): Int64 {

    }
}
```

