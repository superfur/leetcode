# 2571. 将整数减少到零需要的最少操作数

## 题目描述

<p>给你一个正整数 <code>n</code> ，你可以执行下述操作 <strong>任意</strong> 次：</p>

<ul>
	<li><code>n</code> 加上或减去 <code>2</code> 的某个 <strong>幂</strong></li>
</ul>

<p>返回使 <code>n</code> 等于 <code>0</code> 需要执行的 <strong>最少</strong> 操作数。</p>

<p>如果 <code>x == 2<sup>i</sup></code> 且其中 <code>i &gt;= 0</code> ，则数字 <code>x</code> 是 <code>2</code> 的幂。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 39
<strong>输出：</strong>3
<strong>解释：</strong>我们可以执行下述操作：
- n 加上 2<sup>0</sup> = 1 ，得到 n = 40 。
- n 减去 2<sup>3</sup> = 8 ，得到 n = 32 。
- n 减去 2<sup>5</sup> = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 54
<strong>输出：</strong>3
<strong>解释：</strong>我们可以执行下述操作：
- n 加上 2<sup>1</sup> = 2 ，得到 n = 56 。
- n 加上 2<sup>3</sup> = 8 ，得到 n = 64 。
- n 减去 2<sup>6</sup> = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 动态规划

## 提示

1. Can we set/unset the bits in binary representation?
2. If there are multiple adjacent ones, how can we optimally add and subtract in 2 operations such that all ones get unset?
3. Bonus: Try to solve the problem with higher constraints: n ≤ 10^18.

## 示例

```
39
54
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, n: int) -> int:
        
```

### C

```c
int minOperations(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    
};
```

### TypeScript

```typescript
function minOperations(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minOperations($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(int n) {
    
  }
}
```

### Go

```golang
func minOperations(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def min_operations(n)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(N :: integer()) -> integer().
min_operations(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(n :: integer) :: integer
  def min_operations(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(n: Int64): Int64 {

    }
}
```

