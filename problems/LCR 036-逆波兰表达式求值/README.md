# LCR 036. 逆波兰表达式求值

## 题目描述

<p>根据<a href="https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437" target="_blank"> 逆波兰表示法</a>，求该后缀表达式的计算结果。</p>

<p>有效的算符包括&nbsp;<code>+</code>、<code>-</code>、<code>*</code>、<code>/</code>&nbsp;。每个运算对象可以是整数，也可以是另一个逆波兰表达式。</p>

<p>&nbsp;</p>

<p><strong>说明：</strong></p>

<ul>
	<li>整数除法只保留整数部分。</li>
	<li>给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>tokens = [&quot;2&quot;,&quot;1&quot;,&quot;+&quot;,&quot;3&quot;,&quot;*&quot;]
<strong>输出：</strong>9
<strong>解释：</strong>该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>tokens = [&quot;4&quot;,&quot;13&quot;,&quot;5&quot;,&quot;/&quot;,&quot;+&quot;]
<strong>输出：</strong>6
<strong>解释：</strong>该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>tokens = [&quot;10&quot;,&quot;6&quot;,&quot;9&quot;,&quot;3&quot;,&quot;+&quot;,&quot;-11&quot;,&quot;*&quot;,&quot;/&quot;,&quot;*&quot;,&quot;17&quot;,&quot;+&quot;,&quot;5&quot;,&quot;+&quot;]
<strong>输出：</strong>22
<strong>解释：</strong>
该算式转化为常见的中缀算术表达式为：
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
	<li><code>tokens[i]</code> 要么是一个算符（<code>&quot;+&quot;</code>、<code>&quot;-&quot;</code>、<code>&quot;*&quot;</code> 或 <code>&quot;/&quot;</code>），要么是一个在范围 <code>[-200, 200]</code> 内的整数</li>
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
	<li>适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 150&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/">https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/</a></p>


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


int evalRPN(char ** tokens, int tokensSize){

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

