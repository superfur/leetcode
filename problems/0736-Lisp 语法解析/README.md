# 736. Lisp 语法解析

## 题目描述

<p>给你一个类似 Lisp 语句的字符串表达式 <code>expression</code>，求出其计算结果。</p>

<p>表达式语法如下所示:</p>

<ul>
	<li>表达式可以为整数，<strong>let</strong> 表达式，<strong>add</strong> 表达式，<strong>mult</strong> 表达式，或赋值的变量。表达式的结果总是一个整数。</li>
	<li>(整数可以是正整数、负整数、0)</li>
	<li><strong>let</strong> 表达式采用&nbsp;<code>"(let v<sub>1</sub> e<sub>1</sub> v<sub>2</sub> e<sub>2</sub> ... v<sub>n</sub> e<sub>n</sub> expr)"</code> 的形式，其中&nbsp;<code>let</code> 总是以字符串&nbsp;<code>"let"</code>来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量&nbsp;<code>v<sub>1</sub></code>被分配为表达式&nbsp;<code>e<sub>1</sub></code>&nbsp;的值，第二个变量&nbsp;<code>v<sub>2</sub></code>&nbsp;被分配为表达式&nbsp;<code>e<sub>2</sub></code>&nbsp;的值，<strong>依次类推</strong>；最终 <code>let</code> 表达式的值为&nbsp;<code>expr</code>表达式的值。</li>
	<li><strong>add </strong>表达式表示为&nbsp;<code>"(add e<sub>1</sub> e<sub>2</sub>)"</code> ，其中&nbsp;<code>add</code> 总是以字符串&nbsp;<code>"add"</code> 来表示，该表达式总是包含两个表达式 <code>e<sub>1</sub></code>、<code>e<sub>2</sub></code> ，最终结果是&nbsp;<code>e<sub>1</sub></code> 表达式的值与&nbsp;<code>e<sub>2</sub></code>&nbsp;表达式的值之 <strong>和 </strong>。</li>
	<li><strong>mult</strong> 表达式表示为&nbsp;<code>"(mult e<sub>1</sub> e<sub>2</sub>)"</code>&nbsp;，其中&nbsp;<code>mult</code> 总是以字符串 <code>"mult"</code> 表示，该表达式总是包含两个表达式 <code>e<sub>1</sub></code>、<code>e<sub>2</sub></code>，最终结果是&nbsp;<code>e<sub>1</sub></code> 表达式的值与&nbsp;<code>e<sub>2</sub></code>&nbsp;表达式的值之<strong> 积 </strong>。</li>
	<li>在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，<code>"add"</code> ，<code>"let"</code> ，<code>"mult"</code> 会被定义为 "关键字" ，不会用作变量名。</li>
	<li>最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。</li>
</ul>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
<strong>输出：</strong>14
<strong>解释：</strong>
计算表达式 (add x y), 在检查变量 x 值时，
在变量的上下文中由最内层作用域依次向外检查。
首先找到 x = 3, 所以此处的 x 值是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>expression = "(let x 3 x 2 x)"
<strong>输出：</strong>2
<strong>解释：</strong>let 语句中的赋值运算按顺序处理即可。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>expression = "(let x 1 y 2 x (add x y) (add x y))"
<strong>输出：</strong>5
<strong>解释：</strong>
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。 
第二个 (add x y) 计算结果是 3 + 2 = 5 。
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 2000</code></li>
	<li><code>exprssion</code> 中不含前导和尾随空格</li>
	<li><code>expressoin</code> 中的不同部分（token）之间用单个空格进行分隔</li>
	<li>答案和所有中间计算结果都符合 <strong>32-bit</strong> 整数范围</li>
	<li>测试用例中的表达式均为合法的且最终结果为整数</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 递归
- 哈希表
- 字符串

## 提示

1. * If the expression starts with a digit or '-', it's an integer: return it.

* If the expression starts with a letter, it's a variable.  Recall it by checking the current scope in reverse order.

* Otherwise, group the tokens (variables or expressions) within this expression by counting the "balance" `bal` of the occurrences of `'('` minus the number of occurrences of `')'`.  When the balance is zero, we have ended a token.  For example, `(add 1 (add 2 3))` should have tokens `'1'` and `'(add 2 3)'`.

* For add and mult expressions, evaluate each token and return the addition or multiplication of them.

* For let expressions, evaluate each expression sequentially and assign it to the variable in the current scope, then return the evaluation of the final expression.

## 示例

```
"(let x 2 (mult x (let x 3 y 4 (add x y))))"
"(let x 3 x 2 x)"
"(let x 1 y 2 x (add x y) (add x y))"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int evaluate(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public int evaluate(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def evaluate(self, expression: str) -> int:
        
```

### C

```c
int evaluate(char* expression) {
    
}
```

### C#

```csharp
public class Solution {
    public int Evaluate(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {number}
 */
var evaluate = function(expression) {
    
};
```

### TypeScript

```typescript
function evaluate(expression: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return Integer
     */
    function evaluate($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func evaluate(_ expression: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun evaluate(expression: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int evaluate(String expression) {
    
  }
}
```

### Go

```golang
func evaluate(expression string) int {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {Integer}
def evaluate(expression)
    
end
```

### Scala

```scala
object Solution {
    def evaluate(expression: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn evaluate(expression: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (evaluate expression)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec evaluate(Expression :: unicode:unicode_binary()) -> integer().
evaluate(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec evaluate(expression :: String.t) :: integer
  def evaluate(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func evaluate(expression: String): Int64 {

    }
}
```

