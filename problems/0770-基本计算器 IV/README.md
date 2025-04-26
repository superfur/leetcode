# 770. 基本计算器 IV

## 题目描述

<p>给定一个表达式如&nbsp;<code>expression = "e + 8 - a + 5"</code>&nbsp;和一个求值映射，如&nbsp;<code>{"e": 1}</code>（给定的形式为&nbsp;<code>evalvars = ["e"]</code> 和&nbsp;<code>evalints = [1]</code>），返回表示简化表达式的标记列表，例如 <code>["-1*a","14"]</code></p>

<ul>
	<li>表达式交替使用块和符号，每个块和符号之间有一个空格。</li>
	<li>块要么是括号中的表达式，要么是变量，要么是非负整数。</li>
	<li>变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像&nbsp;<code>"2x"</code>&nbsp;或&nbsp;<code>"-x"</code>&nbsp;这样的前导系数或一元运算符&nbsp;。</li>
</ul>

<p>表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。</p>

<ul>
	<li>例如，<code>expression = "1 + 2 * 3"</code>&nbsp;的答案是 <code>["7"]</code>。</li>
</ul>

<p>输出格式如下：</p>

<ul>
	<li>对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。
	<ul>
		<li>例如，我们永远不会写像 <code>“b*a*c”</code> 这样的项，只写 <code>“a*b*c”</code>。</li>
	</ul>
	</li>
	<li>项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
	<ul>
		<li>例如，<code>"a*a*b*c"</code> 的次数为 4。</li>
	</ul>
	</li>
	<li>项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。</li>
	<li>格式良好的一个示例答案是&nbsp;<code>["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]</code>&nbsp;。</li>
	<li>系数为 <code>0</code> 的项（包括常数项）不包括在内。
	<ul>
		<li>例如，<code>“0”</code> 的表达式输出为&nbsp;<code>[]</code>&nbsp;。</li>
	</ul>
	</li>
</ul>

<p><strong>注意：</strong>你可以假设给定的表达式均有效。所有中间结果都在区间 <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code> 内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
<strong>输出：</strong>["-1*a","14"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>expression = "e - 8 + temperature - pressure",
evalvars = ["e", "temperature"], evalints = [1, 12]
<strong>输出：</strong>["-1*pressure","5"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
<strong>输出：</strong>["1*e*e","-64"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 250</code></li>
	<li><code>expression</code>&nbsp;由小写英文字母，数字&nbsp;<code>'+'</code>,&nbsp;<code>'-'</code>,&nbsp;<code>'*'</code>,&nbsp;<code>'('</code>,&nbsp;<code>')'</code>,&nbsp;<code>' '</code>&nbsp;组成</li>
	<li><code>expression</code>&nbsp;不包含任何前空格或后空格</li>
	<li><code>expression</code>&nbsp;中的所有符号都用一个空格隔开</li>
	<li><code>0 &lt;= evalvars.length &lt;= 100</code></li>
	<li><code>1 &lt;= evalvars[i].length &lt;= 20</code></li>
	<li><code>evalvars[i]</code>&nbsp;由小写英文字母组成</li>
	<li><code>evalints.length == evalvars.length</code></li>
	<li><code>-100 &lt;= evalints[i] &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 递归
- 哈希表
- 数学
- 字符串

## 提示

1. One way is with a Polynomial class.  For example,

* `Poly:add(this, that)` returns the result of `this + that`.
* `Poly:sub(this, that)` returns the result of `this - that`.
* `Poly:mul(this, that)` returns the result of `this * that`.
* `Poly:evaluate(this, evalmap)` returns the polynomial after replacing all free variables with constants as specified by `evalmap`.
* `Poly:toList(this)` returns the polynomial in the correct output format.

* `Solution::combine(left, right, symbol)` returns the result of applying the binary operator represented by `symbol` to `left` and `right`.
* `Solution::make(expr)` makes a new `Poly` represented by either the constant or free variable specified by `expr`.
* `Solution::parse(expr)` parses an expression into a new `Poly`.

## 示例

```
"e + 8 - a + 5"
["e"]
[1]
"e - 8 + temperature - pressure"
["e", "temperature"]
[1, 12]
"(e + 8) * (e - 8)"
[]
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) {
        
    }
}
```

### Python

```python
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** basicCalculatorIV(char* expression, char** evalvars, int evalvarsSize, int* evalints, int evalintsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> BasicCalculatorIV(string expression, string[] evalvars, int[] evalints) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @param {string[]} evalvars
 * @param {number[]} evalints
 * @return {string[]}
 */
var basicCalculatorIV = function(expression, evalvars, evalints) {
    
};
```

### TypeScript

```typescript
function basicCalculatorIV(expression: string, evalvars: string[], evalints: number[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @param String[] $evalvars
     * @param Integer[] $evalints
     * @return String[]
     */
    function basicCalculatorIV($expression, $evalvars, $evalints) {
        
    }
}
```

### Swift

```swift
class Solution {
    func basicCalculatorIV(_ expression: String, _ evalvars: [String], _ evalints: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun basicCalculatorIV(expression: String, evalvars: Array<String>, evalints: IntArray): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> basicCalculatorIV(String expression, List<String> evalvars, List<int> evalints) {
    
  }
}
```

### Go

```golang
func basicCalculatorIV(expression string, evalvars []string, evalints []int) []string {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @param {String[]} evalvars
# @param {Integer[]} evalints
# @return {String[]}
def basic_calculator_iv(expression, evalvars, evalints)
    
end
```

### Scala

```scala
object Solution {
    def basicCalculatorIV(expression: String, evalvars: Array[String], evalints: Array[Int]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn basic_calculator_iv(expression: String, evalvars: Vec<String>, evalints: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (basic-calculator-iv expression evalvars evalints)
  (-> string? (listof string?) (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec basic_calculator_iv(Expression :: unicode:unicode_binary(), Evalvars :: [unicode:unicode_binary()], Evalints :: [integer()]) -> [unicode:unicode_binary()].
basic_calculator_iv(Expression, Evalvars, Evalints) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec basic_calculator_iv(expression :: String.t, evalvars :: [String.t], evalints :: [integer]) :: [String.t]
  def basic_calculator_iv(expression, evalvars, evalints) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func basicCalculatorIV(expression: String, evalvars: Array<String>, evalints: Array<Int64>): ArrayList<String> {

    }
}
```

