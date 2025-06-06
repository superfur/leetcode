# 1175. 质数排列

## 题目描述

<p>请你帮忙给从 <code>1</code> 到 <code>n</code>&nbsp;的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。</p>

<p>让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。</p>

<p>由于答案可能会很大，所以请你返回答案 <strong>模 mod&nbsp;<code>10^9 + 7</code></strong>&nbsp;之后的结果即可。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>12
<strong>解释：</strong>举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 100
<strong>输出：</strong>682289015
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Solve the problem for prime numbers and composite numbers separately.
2. Multiply the number of permutations of prime numbers over prime indices with the number of permutations of composite numbers over composite indices.
3. The number of permutations equals the factorial.

## 示例

```
5
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numPrimeArrangements(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int numPrimeArrangements(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
```

### C

```c
int numPrimeArrangements(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumPrimeArrangements(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numPrimeArrangements = function(n) {
    
};
```

### TypeScript

```typescript
function numPrimeArrangements(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numPrimeArrangements($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numPrimeArrangements(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numPrimeArrangements(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numPrimeArrangements(int n) {
    
  }
}
```

### Go

```golang
func numPrimeArrangements(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def num_prime_arrangements(n)
    
end
```

### Scala

```scala
object Solution {
    def numPrimeArrangements(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_prime_arrangements(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-prime-arrangements n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_prime_arrangements(N :: integer()) -> integer().
num_prime_arrangements(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_prime_arrangements(n :: integer) :: integer
  def num_prime_arrangements(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numPrimeArrangements(n: Int64): Int64 {

    }
}
```

