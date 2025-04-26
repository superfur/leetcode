# 1881. 插入后的最大值

## 题目描述

<p>给你一个非常大的整数 <code>n</code> 和一个整数数字 <code>x</code> ，大整数 <code>n</code> 用一个字符串表示。<code>n</code> 中每一位数字和数字 <code>x</code> 都处于闭区间 <code>[1, 9]</code> 中，且 <code>n</code> 可能表示一个 <strong>负数</strong> 。</p>

<p>你打算通过在 <code>n</code> 的十进制表示的任意位置插入 <code>x</code> 来 <strong>最大化</strong> <code>n</code> 的 <strong>数值</strong> ​​​​​​。但 <strong>不能</strong> 在负号的左边插入 <code>x</code> 。</p>

<ul>
	<li>例如，如果 <code>n = 73</code> 且 <code>x = 6</code> ，那么最佳方案是将 <code>6</code> 插入 <code>7</code> 和 <code>3</code> 之间，使 <code>n = 763</code> 。</li>
	<li>如果 <code>n = -55</code> 且 <code>x = 2</code> ，那么最佳方案是将 <code>2</code> 插在第一个 <code>5</code> 之前，使 <code>n = -255</code> 。</li>
</ul>

<p>返回插入操作后，用字符串表示的 <code>n</code> 的最大值。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = "99", x = 9
<strong>输出：</strong>"999"
<strong>解释：</strong>不管在哪里插入 9 ，结果都是相同的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = "-13", x = 2
<strong>输出：</strong>"-123"
<strong>解释：</strong>向 n 中插入 x 可以得到 -213、-123 或者 -132 ，三者中最大的是 -123 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= x <= 9</code></li>
	<li><code>n</code>​​​ 中每一位的数字都在闭区间 <code>[1, 9]</code> 中。</li>
	<li><code>n</code> 代表一个有效的整数。</li>
	<li>当 <code>n</code> 表示负数时，将会以字符 <code>'-'</code> 开始。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Note that if the number is negative it's the same as positive but you look for the minimum instead.
2. In the case of maximum, if s[i] < x it's optimal that x is put before s[i].
3. In the case of minimum, if s[i] > x it's optimal that x is put before s[i].

## 示例

```
"99"
9
"-13"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string maxValue(string n, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public String maxValue(String n, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
```

### C

```c
char* maxValue(char* n, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public string MaxValue(string n, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    
};
```

### TypeScript

```typescript
function maxValue(n: string, x: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $n
     * @param Integer $x
     * @return String
     */
    function maxValue($n, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValue(_ n: String, _ x: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValue(n: String, x: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String maxValue(String n, int x) {
    
  }
}
```

### Go

```golang
func maxValue(n string, x int) string {
    
}
```

### Ruby

```ruby
# @param {String} n
# @param {Integer} x
# @return {String}
def max_value(n, x)
    
end
```

### Scala

```scala
object Solution {
    def maxValue(n: String, x: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value(n: String, x: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (max-value n x)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec max_value(N :: unicode:unicode_binary(), X :: integer()) -> unicode:unicode_binary().
max_value(N, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value(n :: String.t, x :: integer) :: String.t
  def max_value(n, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValue(n: String, x: Int64): String {

    }
}
```

