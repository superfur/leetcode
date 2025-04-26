# 29. 两数相除

## 题目描述

<p>给你两个整数，被除数&nbsp;<code>dividend</code>&nbsp;和除数&nbsp;<code>divisor</code>。将两数相除，要求 <strong>不使用</strong> 乘法、除法和取余运算。</p>

<p>整数除法应该向零截断，也就是截去（<code>truncate</code>）其小数部分。例如，<code>8.345</code> 将被截断为 <code>8</code> ，<code>-2.7335</code> 将被截断至 <code>-2</code> 。</p>

<p>返回被除数&nbsp;<code>dividend</code>&nbsp;除以除数&nbsp;<code>divisor</code>&nbsp;得到的 <strong>商</strong> 。</p>

<p><strong>注意：</strong>假设我们的环境只能存储 <strong>32 位</strong> 有符号整数，其数值范围是 <code>[−2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>− 1]</code> 。本题中，如果商 <strong>严格大于</strong> <code>2<sup>31&nbsp;</sup>− 1</code> ，则返回 <code>2<sup>31&nbsp;</sup>− 1</code> ；如果商 <strong>严格小于</strong> <code>-2<sup>31</sup></code> ，则返回 <code>-2<sup>31</sup></code><sup> </sup>。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> dividend = 10, divisor = 3
<strong>输出:</strong> 3
<strong>解释: </strong>10/3 = 3.33333.. ，向零截断后得到 3 。</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> dividend = 7, divisor = -3
<strong>输出:</strong> -2
<strong>解释:</strong> 7/-3 = -2.33333.. ，向零截断后得到 -2 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= dividend, divisor &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>divisor != 0</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数学

## 示例

```
10
3
7
-3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        
    }
};
```

### Java

```java
class Solution {
    public int divide(int dividend, int divisor) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
```

### C

```c
int divide(int dividend, int divisor) {
    
}
```

### C#

```csharp
public class Solution {
    public int Divide(int dividend, int divisor) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    
};
```

### TypeScript

```typescript
function divide(dividend: number, divisor: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $dividend
     * @param Integer $divisor
     * @return Integer
     */
    function divide($dividend, $divisor) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divide(dividend: Int, divisor: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int divide(int dividend, int divisor) {
    
  }
}
```

### Go

```golang
func divide(dividend int, divisor int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
def divide(dividend, divisor)
    
end
```

### Scala

```scala
object Solution {
    def divide(dividend: Int, divisor: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (divide dividend divisor)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec divide(Dividend :: integer(), Divisor :: integer()) -> integer().
divide(Dividend, Divisor) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide(dividend :: integer, divisor :: integer) :: integer
  def divide(dividend, divisor) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divide(dividend: Int64, divisor: Int64): Int64 {

    }
}
```

