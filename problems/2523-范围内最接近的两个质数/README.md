# 2523. 范围内最接近的两个质数

## 题目描述

<p>给你两个正整数&nbsp;<code>left</code> 和&nbsp;<code>right</code>&nbsp;，请你找到两个整数&nbsp;<code>num1</code> 和&nbsp;<code>num2</code>&nbsp;，它们满足：</p>

<ul>
	<li><code>left &lt;= nums1 &lt; nums2 &lt;= right&nbsp;</code>&nbsp;。</li>
	<li><code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;都是 <strong><span data-keyword="prime-number">质数</span></strong>&nbsp;。</li>
	<li><code>nums2 - nums1</code>&nbsp;是满足上述条件的质数对中的 <strong>最小值</strong>&nbsp;。</li>
</ul>

<p>请你返回正整数数组&nbsp;<code>ans = [nums1, nums2]</code>&nbsp;。如果有多个整数对满足上述条件，请你返回&nbsp;<code>nums1</code>&nbsp;最小的质数对。如果不存在符合题意的质数对，请你返回&nbsp;<code>[-1, -1]</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>left = 10, right = 19
<b>输出：</b>[11,13]
<b>解释：</b>10 到 19 之间的质数为 11 ，13 ，17 和 19 。
质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
由于 11 比 17 小，我们返回第一个质数对。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>left = 4, right = 6
<b>输出：</b>[-1,-1]
<b>解释：</b>给定范围内只有一个质数，所以题目条件无法被满足。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 数论

## 提示

1. Use Sieve of Eratosthenes to mark numbers that are primes.
2. Iterate from right to left and find pair with the minimum distance between marked numbers.

## 示例

```
10
19
4
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] closestPrimes(int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestPrimes(int left, int right, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ClosestPrimes(int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var closestPrimes = function(left, right) {
    
};
```

### TypeScript

```typescript
function closestPrimes(left: number, right: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer[]
     */
    function closestPrimes($left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestPrimes(_ left: Int, _ right: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestPrimes(left: Int, right: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> closestPrimes(int left, int right) {
    
  }
}
```

### Go

```golang
func closestPrimes(left int, right int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def closest_primes(left, right)
    
end
```

### Scala

```scala
object Solution {
    def closestPrimes(left: Int, right: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (closest-primes left right)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec closest_primes(Left :: integer(), Right :: integer()) -> [integer()].
closest_primes(Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_primes(left :: integer, right :: integer) :: [integer]
  def closest_primes(left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestPrimes(left: Int64, right: Int64): Array<Int64> {

    }
}
```

