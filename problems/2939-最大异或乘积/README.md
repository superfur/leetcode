# 2939. 最大异或乘积

## 题目描述

<p>给你三个整数&nbsp;<code>a</code>&nbsp;，<code>b</code>&nbsp;和&nbsp;<code>n</code>&nbsp;，请你返回&nbsp;<code>(a XOR x) * (b XOR x)</code>&nbsp;的&nbsp;<strong>最大值</strong>&nbsp;且 <code>x</code>&nbsp;需要满足 <code>0 &lt;= x &lt; 2<sup>n</sup></code>。</p>

<p>由于答案可能会很大，返回它对&nbsp;<code>10<sup>9 </sup>+ 7</code>&nbsp;<strong>取余</strong>&nbsp;后的结果。</p>

<p><strong>注意</strong>，<code>XOR</code>&nbsp;是按位异或操作。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>a = 12, b = 5, n = 4
<b>输出：</b>98
<b>解释：</b>当 x = 2 时，(a XOR x) = 14 且 (b XOR x) = 7 。所以，(a XOR x) * (b XOR x) = 98 。
98 是所有满足 0 &lt;= x &lt; 2<sup>n </sup>中 (a XOR x) * (b XOR x) 的最大值。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>a = 6, b = 7 , n = 5
<b>输出：</b>930
<b>解释：</b>当 x = 25 时，(a XOR x) = 31 且 (b XOR x) = 30 。所以，(a XOR x) * (b XOR x) = 930 。
930 是所有满足 0 &lt;= x &lt; 2<sup>n </sup>中 (a XOR x) * (b XOR x) 的最大值。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>a = 1, b = 6, n = 3
<b>输出：</b>12
<b>解释： </b>当 x = 5 时，(a XOR x) = 4 且 (b XOR x) = 3 。所以，(a XOR x) * (b XOR x) = 12 。
12 是所有满足 0 &lt;= x &lt; 2<sup>n </sup>中 (a XOR x) * (b XOR x) 的最大值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= a, b &lt; 2<sup>50</sup></code></li>
	<li><code>0 &lt;= n &lt;= 50</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数学

## 提示

1. Iterate over bits from most significant to least significant.
2. For the <code>i<sup>th</sup></code> bit, if both <code>a</code> and <code>b</code> have the same value, we can always make <code>x</code>’s <code>i<sup>th</sup></code> bit different from <code>a</code> and <code>b</code>, so <code>a ^ x</code> and <code>b ^ x</code> both have the <code>i<sup>th</sup></cod> bit set.
3. Otherwise, we can only set the <code>i<sup>th</sup></code> bit of one of <code>a ^ x</code> or <code>b ^ x</code>. Depending on the previous bits of  <code>a ^ x</code> or <code>b ^ x</code>, we should set the smaller value’s <code>i<sup>th</sup></code> bit.

## 示例

```
12
5
4
6
7
5
1
6
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumXorProduct(long long a, long long b, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumXorProduct(long a, long b, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumXorProduct(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        
```

### C

```c
int maximumXorProduct(long long a, long long b, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumXorProduct(long a, long b, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} n
 * @return {number}
 */
var maximumXorProduct = function(a, b, n) {
    
};
```

### TypeScript

```typescript
function maximumXorProduct(a: number, b: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $n
     * @return Integer
     */
    function maximumXorProduct($a, $b, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumXorProduct(_ a: Int, _ b: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumXorProduct(a: Long, b: Long, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumXorProduct(int a, int b, int n) {
    
  }
}
```

### Go

```golang
func maximumXorProduct(a int64, b int64, n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} n
# @return {Integer}
def maximum_xor_product(a, b, n)
    
end
```

### Scala

```scala
object Solution {
    def maximumXorProduct(a: Long, b: Long, n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_xor_product(a: i64, b: i64, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-xor-product a b n)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_xor_product(A :: integer(), B :: integer(), N :: integer()) -> integer().
maximum_xor_product(A, B, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_xor_product(a :: integer, b :: integer, n :: integer) :: integer
  def maximum_xor_product(a, b, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumXorProduct(a: Int64, b: Int64, n: Int64): Int64 {

    }
}
```

