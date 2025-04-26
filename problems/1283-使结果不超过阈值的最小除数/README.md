# 1283. 使结果不超过阈值的最小除数

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 和一个正整数&nbsp;<code>threshold</code> &nbsp;，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。</p>

<p>请你找出能够使上述结果小于等于阈值&nbsp;<code>threshold</code>&nbsp;的除数中 <strong>最小</strong> 的那个。</p>

<p>每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。</p>

<p>题目保证一定有解。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,5,9], threshold = 6
<strong>输出：</strong>5
<strong>解释：</strong>如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,5,7,11], threshold = 11
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [19], threshold = 5
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10^4</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^6</code></li>
	<li><code>nums.length &lt;=&nbsp;threshold &lt;= 10^6</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Examine every possible number for solution. Choose the largest of them.
2. Use binary search to reduce the time complexity.

## 示例

```
[1,2,5,9]
6
[44,22,33,11,1]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
```

### C

```c
int smallestDivisor(int* nums, int numsSize, int threshold) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestDivisor(int[] nums, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
    
};
```

### TypeScript

```typescript
function smallestDivisor(nums: number[], threshold: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function smallestDivisor($nums, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestDivisor(_ nums: [Int], _ threshold: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestDivisor(nums: IntArray, threshold: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestDivisor(List<int> nums, int threshold) {
    
  }
}
```

### Go

```golang
func smallestDivisor(nums []int, threshold int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def smallest_divisor(nums, threshold)
    
end
```

### Scala

```scala
object Solution {
    def smallestDivisor(nums: Array[Int], threshold: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-divisor nums threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_divisor(Nums :: [integer()], Threshold :: integer()) -> integer().
smallest_divisor(Nums, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_divisor(nums :: [integer], threshold :: integer) :: integer
  def smallest_divisor(nums, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestDivisor(nums: Array<Int64>, threshold: Int64): Int64 {

    }
}
```

