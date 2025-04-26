# 2544. 交替数字和

## 题目描述

<p>给你一个正整数 <code>n</code> 。<code>n</code> 中的每一位数字都会按下述规则分配一个符号：</p>

<ul>
	<li><strong>最高有效位</strong> 上的数字分配到 <strong>正</strong> 号。</li>
	<li>剩余每位上数字的符号都与其相邻数字相反。</li>
</ul>

<p>返回所有数字及其对应符号的和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 521
<strong>输出：</strong>4
<strong>解释：</strong>(+5) + (-2) + (+1) = 4</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 111
<strong>输出：</strong>1
<strong>解释：</strong>(+1) + (-1) + (+1) = 1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 886996
<strong>输出：</strong>0
<strong>解释：</strong>(+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数学

## 提示

1. The first step is to loop over the digits. We can convert the integer into a string, an array of digits, or just loop over its digits.
2. Keep a variable sign that initially equals 1 and a variable answer that initially equals 0.
3. Each time you loop over a digit i, add sign * i to answer, then multiply sign by -1.

## 示例

```
521
111
886996
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int alternateDigitSum(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int alternateDigitSum(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
```

### C

```c
int alternateDigitSum(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int AlternateDigitSum(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var alternateDigitSum = function(n) {
    
};
```

### TypeScript

```typescript
function alternateDigitSum(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function alternateDigitSum($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func alternateDigitSum(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun alternateDigitSum(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int alternateDigitSum(int n) {
    
  }
}
```

### Go

```golang
func alternateDigitSum(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def alternate_digit_sum(n)
    
end
```

### Scala

```scala
object Solution {
    def alternateDigitSum(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn alternate_digit_sum(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (alternate-digit-sum n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec alternate_digit_sum(N :: integer()) -> integer().
alternate_digit_sum(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec alternate_digit_sum(n :: integer) :: integer
  def alternate_digit_sum(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func alternateDigitSum(n: Int64): Int64 {

    }
}
```

