# 2232. 向表达式添加括号后的最小结果

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>expression</code> ，格式为 <code>"&lt;num1&gt;+&lt;num2&gt;"</code> ，其中 <code>&lt;num1&gt;</code> 和 <code>&lt;num2&gt;</code> 表示正整数。</p>

<p>请你向 <code>expression</code> 中添加一对括号，使得在添加之后， <code>expression</code> 仍然是一个有效的数学表达式，并且计算后可以得到 <strong>最小</strong> 可能值。左括号 <strong>必须</strong> 添加在 <code>'+'</code> 的左侧，而右括号必须添加在 <code>'+'</code> 的右侧。</p>

<p>返回添加一对括号后形成的表达式&nbsp;<code>expression</code> ，且满足<em> </em><code>expression</code><em> </em>计算得到 <strong>最小</strong> 可能值<em>。</em>如果存在多个答案都能产生相同结果，返回任意一个答案。</p>

<p>生成的输入满足：<code>expression</code> 的原始值和添加满足要求的任一对括号之后 <code>expression</code> 的值，都符合 32-bit 带符号整数范围。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>expression = "247+38"
<strong>输出：</strong>"2(47+38)"
<strong>解释：</strong>表达式计算得到 2 * (47 + 38) = 2 * 85 = 170 。
注意 "2(4)7+38" 不是有效的结果，因为右括号必须添加在 <code>'+' 的右侧。</code>
可以证明 170 是最小可能值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>expression = "12+34"
<strong>输出：</strong>"1(2+3)4"
<strong>解释：</strong>表达式计算得到 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>expression = "999+999"
<strong>输出：</strong>"(999+999)"
<strong>解释：</strong>表达式计算得到 999 + 999 = 1998 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= expression.length &lt;= 10</code></li>
	<li><code>expression</code> 仅由数字 <code>'1'</code> 到 <code>'9'</code> 和 <code>'+'</code> 组成</li>
	<li><code>expression</code> 由数字开始和结束</li>
	<li><code>expression</code> 恰好仅含有一个 <code>'+'</code>.</li>
	<li><code>expression</code> 的原始值和添加满足要求的任一对括号之后 <code>expression</code> 的值，都符合 32-bit 带符号整数范围</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 枚举

## 提示

1. The maximum length of expression is very low. We can try every possible spot to place the parentheses.
2. Every possibility of expression is of the form a * (b + c) * d where a, b, c, d represent integers. Note the edge cases where a and/or d do not exist, in which case use 1 instead of them.

## 示例

```
"247+38"
"12+34"
"999+999"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minimizeResult(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public String minimizeResult(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minimizeResult(self, expression: str) -> str:
        
```

### C

```c
char* minimizeResult(char* expression) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinimizeResult(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {string}
 */
var minimizeResult = function(expression) {
    
};
```

### TypeScript

```typescript
function minimizeResult(expression: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return String
     */
    function minimizeResult($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeResult(_ expression: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeResult(expression: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minimizeResult(String expression) {
    
  }
}
```

### Go

```golang
func minimizeResult(expression string) string {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {String}
def minimize_result(expression)
    
end
```

### Scala

```scala
object Solution {
    def minimizeResult(expression: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_result(expression: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-result expression)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec minimize_result(Expression :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimize_result(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_result(expression :: String.t) :: String.t
  def minimize_result(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeResult(expression: String): String {

    }
}
```

