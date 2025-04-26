# 1137. 第 N 个泰波那契数

## 题目描述

<p>泰波那契序列&nbsp;T<sub>n</sub>&nbsp;定义如下：&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, 且在 n &gt;= 0&nbsp;的条件下 T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub></p>

<p>给你整数&nbsp;<code>n</code>，请返回第 n 个泰波那契数&nbsp;T<sub>n </sub>的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>4
<strong>解释：</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 25
<strong>输出：</strong>1389537
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>答案保证是一个 32 位整数，即&nbsp;<code>answer &lt;= 2^31 - 1</code>。</li>
</ul>


## 难度

Easy

## 标签

- 记忆化搜索
- 数学
- 动态规划

## 提示

1. Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
2. Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].

## 示例

```
4
25
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int tribonacci(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int tribonacci(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def tribonacci(self, n: int) -> int:
        
```

### C

```c
int tribonacci(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int Tribonacci(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    
};
```

### TypeScript

```typescript
function tribonacci(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function tribonacci($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func tribonacci(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun tribonacci(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int tribonacci(int n) {
    
  }
}
```

### Go

```golang
func tribonacci(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    
end
```

### Scala

```scala
object Solution {
    def tribonacci(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (tribonacci n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec tribonacci(N :: integer()) -> integer().
tribonacci(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec tribonacci(n :: integer) :: integer
  def tribonacci(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func tribonacci(n: Int64): Int64 {

    }
}
```

