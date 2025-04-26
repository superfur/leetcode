# 204. 计数质数

## 题目描述

<p>给定整数 <code>n</code> ，返回 <em>所有小于非负整数&nbsp;<code>n</code>&nbsp;的质数的数量</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10
<strong>输出：</strong>4
<strong>解释：</strong>小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 0
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出</strong>：0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 枚举
- 数论

## 提示

1. Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
2. Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
3. Use Sieve of Eratosthenes.

## 示例

```
10
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPrimes(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPrimes(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPrimes(self, n: int) -> int:
        
```

### C

```c
int countPrimes(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPrimes(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    
};
```

### TypeScript

```typescript
function countPrimes(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countPrimes($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPrimes(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPrimes(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPrimes(int n) {
    
  }
}
```

### Go

```golang
func countPrimes(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_primes(n)
    
end
```

### Scala

```scala
object Solution {
    def countPrimes(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-primes n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_primes(N :: integer()) -> integer().
count_primes(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_primes(n :: integer) :: integer
  def count_primes(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPrimes(n: Int64): Int64 {

    }
}
```

