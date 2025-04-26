# 1106. 解析布尔表达式

## 题目描述

<p><strong>布尔表达式</strong> 是计算结果不是 <code>true</code> 就是 <code>false</code> 的表达式。有效的表达式需遵循以下约定：</p>

<ul>
	<li><code>'t'</code>，运算结果为 <code>true</code></li>
	<li><code>'f'</code>，运算结果为 <code>false</code></li>
	<li><code>'!(subExpr)'</code>，运算过程为对内部表达式 <code>subExpr</code> 进行 <strong>逻辑非</strong>（NOT）运算</li>
	<li><code>'&amp;(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code>，运算过程为对 2 个或以上内部表达式 <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> 进行 <strong>逻辑与</strong>（AND）运算</li>
	<li><code>'|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code>，运算过程为对 2 个或以上内部表达式 <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> 进行 <strong>逻辑或</strong>（OR）运算</li>
</ul>

<p>给你一个以字符串形式表述的&nbsp;<a href="https://baike.baidu.com/item/%E5%B8%83%E5%B0%94%E8%A1%A8%E8%BE%BE%E5%BC%8F/1574380?fr=aladdin" target="_blank">布尔表达式</a> <code>expression</code>，返回该式的运算结果。</p>

<p>题目测试用例所给出的表达式均为有效的布尔表达式，遵循上述约定。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>expression = "&amp;(|(f))"
<strong>输出：</strong>false
<strong>解释：</strong>
首先，计算 |(f) --&gt; f ，表达式变为 "&amp;(f)" 。
接着，计算 &amp;(f) --&gt; f ，表达式变为 "f" 。
最后，返回 false 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>expression = "|(f,f,f,t)"
<strong>输出：</strong>true
<strong>解释：</strong>计算 (false OR false OR false OR true) ，结果为 true 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>expression = "!(&amp;(f,t))"
<strong>输出：</strong>true
<strong>解释：</strong>
首先，计算 &amp;(f,t) --&gt; (false AND true) --&gt; false --&gt; f ，表达式变为 "!(f)" 。
接着，计算 !(f) --&gt; NOT false --&gt; true ，返回 true 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>expression[i]</code> 为 <code>'('</code>、<code>')'</code>、<code>'&amp;'</code>、<code>'|'</code>、<code>'!'</code>、<code>'t'</code>、<code>'f'</code> 和 <code>','</code> 之一</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 递归
- 字符串

## 提示

1. Write a function "parse" which calls helper functions "parse_or", "parse_and", "parse_not".

## 示例

```
"&(|(f))"
"|(f,f,f,t)"
"!(&(f,t))"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool parseBoolExpr(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean parseBoolExpr(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
```

### C

```c
bool parseBoolExpr(char* expression) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ParseBoolExpr(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {boolean}
 */
var parseBoolExpr = function(expression) {
    
};
```

### TypeScript

```typescript
function parseBoolExpr(expression: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return Boolean
     */
    function parseBoolExpr($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func parseBoolExpr(_ expression: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun parseBoolExpr(expression: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool parseBoolExpr(String expression) {
    
  }
}
```

### Go

```golang
func parseBoolExpr(expression string) bool {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {Boolean}
def parse_bool_expr(expression)
    
end
```

### Scala

```scala
object Solution {
    def parseBoolExpr(expression: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn parse_bool_expr(expression: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (parse-bool-expr expression)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec parse_bool_expr(Expression :: unicode:unicode_binary()) -> boolean().
parse_bool_expr(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec parse_bool_expr(expression :: String.t) :: boolean
  def parse_bool_expr(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func parseBoolExpr(expression: String): Bool {

    }
}
```

