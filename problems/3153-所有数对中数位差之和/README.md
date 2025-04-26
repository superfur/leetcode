# 3153. 所有数对中数位差之和

## 题目描述

<p>你有一个数组&nbsp;<code>nums</code>&nbsp;，它只包含 <strong>正</strong>&nbsp;整数，所有正整数的数位长度都 <strong>相同</strong>&nbsp;。</p>

<p>两个整数的 <strong>数位差</strong>&nbsp;指的是两个整数 <b>相同</b>&nbsp;位置上不同数字的数目。</p>

<p>请你返回 <code>nums</code>&nbsp;中 <strong>所有</strong>&nbsp;整数对里，<strong>数位差之和。</strong></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [13,23,12]</span></p>

<p><b>输出：</b>4</p>

<p><strong>解释：</strong><br />
计算过程如下：<br />
-&nbsp;<strong>1</strong>3 和&nbsp;<strong>2</strong>3 的数位差为&nbsp;1 。<br />
- 1<strong>3</strong> 和 1<strong>2</strong>&nbsp;的数位差为&nbsp;1 。<br />
-&nbsp;<strong>23</strong> 和&nbsp;<strong>12</strong>&nbsp;的数位差为&nbsp;2 。<br />
所以所有整数数对的数位差之和为&nbsp;<code>1 + 1 + 2 = 4</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [10,10,10,10]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong><br />
数组中所有整数都相同，所以所有整数数对的数位不同之和为 0 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt; 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;中的整数都有相同的数位长度。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 计数

## 提示

1. You can solve the problem for digits that are on the same position separately, and then sum up all the answers.
2. For each position, count the number of occurences of each digit from 0 to 9 that appear on that position.
3. Let <code>c</code> be the number of occurences of a digit on a position, that will contribute with <code>c * (n - c)</code> to the final answer, where <code>n</code> is the number of integers in <code>nums</code>.

## 示例

```
[13,23,12]
[10,10,10,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long sumDigitDifferences(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
```

### C

```c
long long sumDigitDifferences(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long SumDigitDifferences(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumDigitDifferences = function(nums) {
    
};
```

### TypeScript

```typescript
function sumDigitDifferences(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumDigitDifferences($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumDigitDifferences(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumDigitDifferences(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumDigitDifferences(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumDigitDifferences(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_digit_differences(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumDigitDifferences(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_digit_differences(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-digit-differences nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_digit_differences(Nums :: [integer()]) -> integer().
sum_digit_differences(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_digit_differences(nums :: [integer]) :: integer
  def sum_digit_differences(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumDigitDifferences(nums: Array<Int64>): Int64 {

    }
}
```

