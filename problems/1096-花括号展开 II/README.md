# 1096. 花括号展开 II

## 题目描述

<p>如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。</p>

<p>花括号展开的表达式可以看作一个由 <strong>花括号</strong>、<strong>逗号</strong> 和 <strong>小写英文字母</strong> 组成的字符串，定义下面几条语法规则：</p>

<ul>
	<li>如果只给出单一的元素&nbsp;<code>x</code>，那么表达式表示的字符串就只有&nbsp;<code>"x"</code>。<code>R(x) = {x}</code>

	<ul>
		<li>例如，表达式 <code>"a"</code> 表示字符串 <code>"a"</code>。</li>
		<li>而表达式 <code>"w"</code> 就表示字符串 <code>"w"</code>。</li>
	</ul>
	</li>
	<li>当两个或多个表达式并列，以逗号分隔，我们取这些表达式中元素的并集。<code>R({e_1,e_2,...}) = R(e_1)&nbsp;∪ R(e_2)&nbsp;∪ ...</code>
	<ul>
		<li>例如，表达式 <code>"{a,b,c}"</code> 表示字符串&nbsp;<code>"a","b","c"</code>。</li>
		<li>而表达式 <code>"{{a,b},{b,c}}"</code> 也可以表示字符串&nbsp;<code>"a","b","c"</code>。</li>
	</ul>
	</li>
	<li>要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。<code>R(e_1 + e_2) = {a + b for (a, b) in&nbsp;R(e_1)&nbsp;× R(e_2)}</code>
	<ul>
		<li>例如，表达式 <code>"{a,b}{c,d}"</code> 表示字符串&nbsp;<code>"ac","ad","bc","bd"</code>。</li>
	</ul>
	</li>
	<li>表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
	<ul>
		<li>例如，表达式 <code>"a{b,c,d}"</code> 表示字符串&nbsp;<code>"ab","ac","ad"​​​​​​</code>。</li>
		<li>例如，表达式 <code>"a{b,c}{d,e}f{g,h}"</code> 可以表示字符串&nbsp;<code>"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"</code>。</li>
	</ul>
	</li>
</ul>

<p>给出表示基于给定语法规则的表达式&nbsp;<code>expression</code>，返回它所表示的所有字符串组成的有序列表。</p>

<p>假如你希望以「集合」的概念了解此题，也可以通过点击 “<strong>显示英文描述</strong>” 获取详情。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>expression = "{a,b}{c,{d,e}}"
<strong>输出：</strong>["ac","ad","ae","bc","bd","be"]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>expression = "{{a,z},a{b,c},{ab,z}}"
<strong>输出：</strong>["a","ab","ac","z"]
<strong>解释：</strong>输出中 <strong>不应 </strong>出现重复的组合结果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 60</code></li>
	<li><code>expression[i]</code> 由 <code>'{'</code>，<code>'}'</code>，<code>','</code>&nbsp;或小写英文字母组成</li>
	<li>给出的表达式&nbsp;<code>expression</code>&nbsp;用以表示一组基于题目描述中语法构造的字符串</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 广度优先搜索
- 字符串
- 回溯

## 提示

1. You can write helper methods to parse the next "chunk" of the expression.  If you see eg. "a", the answer is just the set {a}.  If you see "{", you parse until you complete the "}" (the number of { and } seen are equal) and that becomes a chunk that you find where the appropriate commas are, and parse each individual expression between the commas.

## 示例

```
"{a,b}{c,{d,e}}"
"{{a,z},a{b,c},{ab,z}}"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> braceExpansionII(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** braceExpansionII(char* expression, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> BraceExpansionII(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    
};
```

### TypeScript

```typescript
function braceExpansionII(expression: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return String[]
     */
    function braceExpansionII($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func braceExpansionII(_ expression: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun braceExpansionII(expression: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> braceExpansionII(String expression) {
    
  }
}
```

### Go

```golang
func braceExpansionII(expression string) []string {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {String[]}
def brace_expansion_ii(expression)
    
end
```

### Scala

```scala
object Solution {
    def braceExpansionII(expression: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (brace-expansion-ii expression)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec brace_expansion_ii(Expression :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
brace_expansion_ii(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec brace_expansion_ii(expression :: String.t) :: [String.t]
  def brace_expansion_ii(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func braceExpansionII(expression: String): ArrayList<String> {

    }
}
```

