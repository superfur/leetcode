# 150. 逆波兰表达式求值

## 题目描述

<p>给你一个字符串数组 <code>tokens</code> ，表示一个根据&nbsp;<a href="https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437" target="_blank">逆波兰表示法</a> 表示的算术表达式。</p>

<p>请你计算该表达式。返回一个表示表达式值的整数。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>有效的算符为 <code>'+'</code>、<code>'-'</code>、<code>'*'</code> 和 <code>'/'</code> 。</li>
	<li>每个操作数（运算对象）都可以是一个整数或者另一个表达式。</li>
	<li>两个整数之间的除法总是 <strong>向零截断</strong> 。</li>
	<li>表达式中不含除零运算。</li>
	<li>输入是一个根据逆波兰表示法表示的算术表达式。</li>
	<li>答案及所有中间计算结果可以用 <strong>32 位</strong> 整数表示。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>tokens = ["2","1","+","3","*"]
<strong>输出：</strong>9
<strong>解释：</strong>该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>tokens = ["4","13","5","/","+"]
<strong>输出：</strong>6
<strong>解释：</strong>该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
<strong>输出：</strong>22
<strong>解释：</strong>该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tokens.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tokens[i]</code>&nbsp;是一个算符（<code>"+"</code>、<code>"-"</code>、<code>"*"</code> 或 <code>"/"</code>），或是在范围 <code>[-200, 200]</code> 内的一个整数</li>
</ul>

<p>&nbsp;</p>

<p><strong>逆波兰表达式：</strong></p>

<p>逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。</p>

<ul>
	<li>平常使用的算式则是一种中缀表达式，如 <code>( 1 + 2 ) * ( 3 + 4 )</code> 。</li>
	<li>该算式的逆波兰表达式写法为 <code>( ( 1 2 + ) ( 3 4 + ) * )</code> 。</li>
</ul>

<p>逆波兰表达式主要有以下两个优点：</p>

<ul>
	<li>去掉括号后表达式无歧义，上式即便写成 <code>1 2 + 3 4 + * </code>也可以依据次序计算出正确结果。</li>
	<li>适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 数学

## 示例

```
["2","1","+","3","*"]
["4","13","5","/","+"]
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
    }
};
```

### Java

```java
class Solution {
    public int evalRPN(String[] tokens) {
        
    }
}
```

### Python

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
```

### C

```c
int evalRPN(char** tokens, int tokensSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EvalRPN(string[] tokens) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    
};
```

### TypeScript

```typescript
function evalRPN(tokens: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $tokens
     * @return Integer
     */
    function evalRPN($tokens) {
        
    }
}
```

### Swift

```swift
class Solution {
    func evalRPN(_ tokens: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int evalRPN(List<String> tokens) {
    
  }
}
```

### Go

```golang
func evalRPN(tokens []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} tokens
# @return {Integer}
def eval_rpn(tokens)
    
end
```

### Scala

```scala
object Solution {
    def evalRPN(tokens: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (eval-rpn tokens)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec eval_rpn(Tokens :: [unicode:unicode_binary()]) -> integer().
eval_rpn(Tokens) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec eval_rpn(tokens :: [String.t]) :: integer
  def eval_rpn(tokens) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func evalRPN(tokens: Array<String>): Int64 {

    }
}
```

