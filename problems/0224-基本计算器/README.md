# 224. 基本计算器

## 题目描述

<p>给你一个字符串表达式 <code>s</code> ，请你实现一个基本计算器来计算并返回它的值。</p>

<p>注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 <code>eval()</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1 + 1"
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = " 2-1 + 2 "
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(1+(4+5+2)-3)+(6+8)"
<strong>输出：</strong>23
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3&nbsp;* 10<sup>5</sup></code></li>
	<li><code>s</code> 由数字、<code>'+'</code>、<code>'-'</code>、<code>'('</code>、<code>')'</code>、和 <code>' '</code> 组成</li>
	<li><code>s</code> 表示一个有效的表达式</li>
	<li><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'+'</span></span></font></font> 不能用作一元运算(例如， <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">"+1"</span></span></font></font>&nbsp;和 <code>"+(2 + 3)"</code>&nbsp;无效)</li>
	<li><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'-'</span></span></font></font> 可以用作一元运算(即 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">"-1"</span></span></font></font>&nbsp;和 <code>"-(2 + 3)"</code>&nbsp;是有效的)</li>
	<li>输入中不存在两个连续的操作符</li>
	<li>每个数字和运行的计算将适合于一个有符号的 32位 整数</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 递归
- 数学
- 字符串

## 示例

```
"1 + 1"
" 2-1 + 2 "
"(1+(4+5+2)-3)+(6+8)"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int calculate(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int calculate(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def calculate(self, s: str) -> int:
        
```

### C

```c
int calculate(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int Calculate(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    
};
```

### TypeScript

```typescript
function calculate(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int calculate(String s) {
    
  }
}
```

### Go

```golang
func calculate(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def calculate(s)
    
end
```

### Scala

```scala
object Solution {
    def calculate(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn calculate(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (calculate s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec calculate(S :: unicode:unicode_binary()) -> integer().
calculate(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec calculate(s :: String.t) :: integer
  def calculate(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func calculate(s: String): Int64 {

    }
}
```

