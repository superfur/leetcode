# 1201. 丑数 III

## 题目描述

<p>丑数是可以被&nbsp;<code>a</code>&nbsp;<strong>或</strong>&nbsp;<code>b</code>&nbsp;<strong>或</strong> <code>c</code>&nbsp;整除的 <strong>正整数</strong> 。</p>

<p>给你四个整数：<code>n</code> 、<code>a</code> 、<code>b</code> 、<code>c</code> ，请你设计一个算法来找出第&nbsp;<code>n</code>&nbsp;个丑数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, a = 2, b = 3, c = 5
<strong>输出：</strong>4
<strong>解释：</strong>丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, a = 2, b = 3, c = 4
<strong>输出：</strong>6
<strong>解释：</strong>丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 5, a = 2, b = 11, c = 13
<strong>输出：</strong>10
<strong>解释：</strong>丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, a, b, c &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= a * b * c &lt;= 10<sup>18</sup></code></li>
	<li>本题结果在&nbsp;<code>[1,&nbsp;2 * 10<sup>9</sup>]</code>&nbsp;的范围内</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 二分查找
- 组合数学
- 数论

## 提示

1. Write a function f(k) to determine how many ugly numbers smaller than k. As f(k) is non-decreasing, try binary search.
2. Find all ugly numbers in [1, LCM(a, b, c)] (LCM is Least Common Multiple). Use inclusion-exclusion principle to expand the result.

## 示例

```
3
2
3
5
4
2
3
4
5
2
11
13
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nthUglyNumber(int n, int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
```

### C

```c
int nthUglyNumber(int n, int a, int b, int c) {
    
}
```

### C#

```csharp
public class Solution {
    public int NthUglyNumber(int n, int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var nthUglyNumber = function(n, a, b, c) {
    
};
```

### TypeScript

```typescript
function nthUglyNumber(n: number, a: number, b: number, c: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function nthUglyNumber($n, $a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nthUglyNumber(_ n: Int, _ a: Int, _ b: Int, _ c: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nthUglyNumber(int n, int a, int b, int c) {
    
  }
}
```

### Go

```golang
func nthUglyNumber(n int, a int, b int, c int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def nth_ugly_number(n, a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (nth-ugly-number n a b c)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec nth_ugly_number(N :: integer(), A :: integer(), B :: integer(), C :: integer()) -> integer().
nth_ugly_number(N, A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nth_ugly_number(n :: integer, a :: integer, b :: integer, c :: integer) :: integer
  def nth_ugly_number(n, a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nthUglyNumber(n: Int64, a: Int64, b: Int64, c: Int64): Int64 {

    }
}
```

