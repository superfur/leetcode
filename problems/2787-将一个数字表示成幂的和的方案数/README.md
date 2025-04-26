# 2787. 将一个数字表示成幂的和的方案数

## 题目描述

<p>给你两个 <strong>正</strong>&nbsp;整数&nbsp;<code>n</code> 和&nbsp;<code>x</code>&nbsp;。</p>

<p>请你返回将<em>&nbsp;</em><code>n</code>&nbsp;表示成一些&nbsp;<strong>互不相同</strong>&nbsp;正整数的<em>&nbsp;</em><code>x</code>&nbsp;次幂之和的方案数。换句话说，你需要返回互不相同整数&nbsp;<code>[n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>k</sub>]</code>&nbsp;的集合数目，满足&nbsp;<code>n = n<sub>1</sub><sup>x</sup> + n<sub>2</sub><sup>x</sup> + ... + n<sub>k</sub><sup>x</sup></code>&nbsp;。</p>

<p>由于答案可能非常大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后返回。</p>

<p>比方说，<code>n = 160</code> 且&nbsp;<code>x = 3</code>&nbsp;，一个表示&nbsp;<code>n</code>&nbsp;的方法是&nbsp;<code>n = 2<sup>3</sup> + 3<sup>3</sup> + 5<sup>3</sup></code><sup>&nbsp;</sup>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 10, x = 2
<b>输出：</b>1
<b>解释：</b>我们可以将 n 表示为：n = 3<sup>2</sup> + 1<sup>2</sup> = 10 。
这是唯一将 10 表达成不同整数 2 次方之和的方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 4, x = 1
<b>输出：</b>2
<b>解释：</b>我们可以将 n 按以下方案表示：
- n = 4<sup>1</sup> = 4 。
- n = 3<sup>1</sup> + 1<sup>1</sup> = 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>1 &lt;= x &lt;= 5</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 提示

1. You can use dynamic programming, where dp[k][j] represents the number of ways to express k as the sum of the x-th power of unique positive integers such that the biggest possible number we use is j.
2. To calculate dp[k][j], you can iterate over the numbers smaller than j and try to use each one as a power of x to make our sum k.

## 示例

```
10
2
4
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfWays(int n, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfWays(int n, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
```

### C

```c
int numberOfWays(int n, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfWays(int n, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function(n, x) {
    
};
```

### TypeScript

```typescript
function numberOfWays(n: number, x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $x
     * @return Integer
     */
    function numberOfWays($n, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWays(_ n: Int, _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWays(n: Int, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWays(int n, int x) {
    
  }
}
```

### Go

```golang
func numberOfWays(n int, x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def number_of_ways(n, x)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWays(n: Int, x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-ways n x)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_ways(N :: integer(), X :: integer()) -> integer().
number_of_ways(N, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(n :: integer, x :: integer) :: integer
  def number_of_ways(n, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWays(n: Int64, x: Int64): Int64 {

    }
}
```

