# 738. 单调递增的数字

## 题目描述

<p>当且仅当每个相邻位数上的数字&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp;满足&nbsp;<code>x &lt;= y</code>&nbsp;时，我们称这个整数是<strong>单调递增</strong>的。</p>

<p>给定一个整数 <code>n</code> ，返回 <em>小于或等于 <code>n</code> 的最大数字，且数字呈 <strong>单调递增</strong></em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 10
<strong>输出:</strong> 9
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 1234
<strong>输出:</strong> 1234
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> n = 332
<strong>输出:</strong> 299
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. Build the answer digit by digit, adding the largest possible one that would make the number still less than or equal to N.

## 示例

```
10
1234
332
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int monotoneIncreasingDigits(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
```

### C

```c
int monotoneIncreasingDigits(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MonotoneIncreasingDigits(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var monotoneIncreasingDigits = function(n) {
    
};
```

### TypeScript

```typescript
function monotoneIncreasingDigits(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function monotoneIncreasingDigits($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func monotoneIncreasingDigits(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun monotoneIncreasingDigits(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int monotoneIncreasingDigits(int n) {
    
  }
}
```

### Go

```golang
func monotoneIncreasingDigits(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def monotone_increasing_digits(n)
    
end
```

### Scala

```scala
object Solution {
    def monotoneIncreasingDigits(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn monotone_increasing_digits(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (monotone-increasing-digits n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec monotone_increasing_digits(N :: integer()) -> integer().
monotone_increasing_digits(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec monotone_increasing_digits(n :: integer) :: integer
  def monotone_increasing_digits(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func monotoneIncreasingDigits(n: Int64): Int64 {

    }
}
```

