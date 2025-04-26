# 1896. 反转表达式值的最少操作次数

## 题目描述

<p>给你一个 <strong>有效的</strong> 布尔表达式，用字符串 <code>expression</code> 表示。这个字符串包含字符 <code>'1'</code>，<code>'0'</code>，<code>'&amp;'</code>（按位 <strong>与</strong> 运算），<code>'|'</code>（按位 <strong>或</strong> 运算），<code>'('</code> 和 <code>')'</code> 。</p>

<ul>
	<li>比方说，<code>"()1|1"</code> 和 <code>"(1)&amp;()"</code> <strong>不是有效</strong> 布尔表达式。而 <code>"1"</code>， <code>"(((1))|(0))"</code> 和 <code>"1|(0&amp;(1))"</code> 是 <strong>有效</strong> 布尔表达式。</li>
</ul>

<p>你的目标是将布尔表达式的 <strong>值</strong> <strong>反转 </strong>（也就是将 <code>0</code> 变为 <code>1</code> ，或者将 <code>1</code> 变为 <code>0</code>），请你返回达成目标需要的 <strong>最少操作</strong> 次数。</p>

<ul>
	<li>比方说，如果表达式 <code>expression = "1|1|(0&amp;0)&amp;1"</code> ，它的 <strong>值</strong> 为 <code>1|1|(0&amp;0)&amp;1 = 1|1|0&amp;1 = 1|0&amp;1 = 1&amp;1 = 1</code> 。我们想要执行操作将 <strong>新的</strong> 表达式的值变成 <code>0</code> 。</li>
</ul>

<p>可执行的 <strong>操作</strong> 如下：</p>

<ul>
	<li>将一个 <code>'1'</code> 变成一个 <code>'0'</code> 。</li>
	<li>将一个 <code>'0'</code> 变成一个 <code>'1'</code> 。</li>
	<li>将一个 <code>'&amp;'</code> 变成一个 <code>'|'</code> 。</li>
	<li>将一个 <code>'|'</code> 变成一个 <code>'&amp;'</code> 。</li>
</ul>

<p><strong>注意：</strong><code>'&amp;'</code> 的 <strong>运算优先级</strong> 与 <code>'|'</code> <strong>相同</strong> 。计算表达式时，括号优先级 <strong>最高</strong> ，然后按照 <strong>从左到右</strong> 的顺序运算。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>expression = "1&amp;(0|1)"
<b>输出：</b>1
<b>解释：</b>我们可以将 "1&amp;(0<strong>|</strong>1)" 变成 "1&amp;(0<strong>&amp;</strong>1)" ，执行的操作为将一个 '|' 变成一个 '&amp;' ，执行了 1 次操作。
新表达式的值为 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>expression = "(0&amp;0)&amp;(0&amp;0&amp;0)"
<b>输出：</b>3
<b>解释：</b>我们可以将 "(0<strong>&amp;0</strong>)<strong>&amp;</strong>(0&amp;0&amp;0)" 变成 "(0<strong>|1</strong>)<strong>|</strong>(0&amp;0&amp;0)" ，执行了 3 次操作。
新表达式的值为 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>expression = "(0|(1|0&amp;1))"
<b>输出：</b>1
<b>解释：</b>我们可以将 "(0|(<strong>1</strong>|0&amp;1))" 变成 "(0|(<strong>0</strong>|0&amp;1))" ，执行了 1 次操作。
新表达式的值为 0 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 10<sup>5</sup></code></li>
	<li><code>expression</code> 只包含 <code>'1'</code>，<code>'0'</code>，<code>'&amp;'</code>，<code>'|'</code>，<code>'('</code> 和 <code>')'</code></li>
	<li>所有括号都有与之匹配的对应括号。</li>
	<li>不会有空的括号（也就是说 <code>"()"</code> 不是 <code>expression</code> 的子字符串）。</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数学
- 字符串
- 动态规划

## 提示

1. How many possible states are there for a given expression?
2. Is there a data structure that we can use to solve the problem optimally?

## 示例

```
"1&(0|1)"
"(0&0)&(0&0&0)"
"(0|(1|0&1))"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperationsToFlip(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperationsToFlip(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        
```

### C

```c
int minOperationsToFlip(char* expression) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperationsToFlip(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {number}
 */
var minOperationsToFlip = function(expression) {
    
};
```

### TypeScript

```typescript
function minOperationsToFlip(expression: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return Integer
     */
    function minOperationsToFlip($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperationsToFlip(_ expression: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperationsToFlip(expression: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperationsToFlip(String expression) {
    
  }
}
```

### Go

```golang
func minOperationsToFlip(expression string) int {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {Integer}
def min_operations_to_flip(expression)
    
end
```

### Scala

```scala
object Solution {
    def minOperationsToFlip(expression: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations_to_flip(expression: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations-to-flip expression)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations_to_flip(Expression :: unicode:unicode_binary()) -> integer().
min_operations_to_flip(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations_to_flip(expression :: String.t) :: integer
  def min_operations_to_flip(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperationsToFlip(expression: String): Int64 {

    }
}
```

