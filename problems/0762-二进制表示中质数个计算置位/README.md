# 762. 二进制表示中质数个计算置位

## 题目描述

<p>给你两个整数&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code> ，在闭区间 <code>[left, right]</code>&nbsp;范围内，统计并返回 <strong>计算置位位数为质数</strong> 的整数个数。</p>

<p><strong>计算置位位数</strong> 就是二进制表示中 <code>1</code> 的个数。</p>

<ul>
	<li>例如， <code>21</code>&nbsp;的二进制表示&nbsp;<code>10101</code>&nbsp;有 <code>3</code> 个计算置位。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>left = 6, right = 10
<strong>输出：</strong>4
<strong>解释：</strong>
6 -&gt; 110 (2 个计算置位，2 是质数)
7 -&gt; 111 (3 个计算置位，3 是质数)
9 -&gt; 1001 (2 个计算置位，2 是质数)
10-&gt; 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>left = 10, right = 15
<strong>输出：</strong>5
<strong>解释：</strong>
10 -&gt; 1010 (2 个计算置位, 2 是质数)
11 -&gt; 1011 (3 个计算置位, 3 是质数)
12 -&gt; 1100 (2 个计算置位, 2 是质数)
13 -&gt; 1101 (3 个计算置位, 3 是质数)
14 -&gt; 1110 (3 个计算置位, 3 是质数)
15 -&gt; 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= right - left &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数学

## 提示

1. Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.

## 示例

```
6
10
10
15
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPrimeSetBits(int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
```

### C

```c
int countPrimeSetBits(int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPrimeSetBits(int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var countPrimeSetBits = function(left, right) {
    
};
```

### TypeScript

```typescript
function countPrimeSetBits(left: number, right: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function countPrimeSetBits($left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPrimeSetBits(_ left: Int, _ right: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPrimeSetBits(left: Int, right: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPrimeSetBits(int left, int right) {
    
  }
}
```

### Go

```golang
func countPrimeSetBits(left int, right int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def count_prime_set_bits(left, right)
    
end
```

### Scala

```scala
object Solution {
    def countPrimeSetBits(left: Int, right: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-prime-set-bits left right)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_prime_set_bits(Left :: integer(), Right :: integer()) -> integer().
count_prime_set_bits(Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_prime_set_bits(left :: integer, right :: integer) :: integer
  def count_prime_set_bits(left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPrimeSetBits(left: Int64, right: Int64): Int64 {

    }
}
```

