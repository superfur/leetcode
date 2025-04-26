# 1807. 替换字符串中的括号内容

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它包含一些括号对，每个括号中包含一个 <strong>非空</strong>&nbsp;的键。</p>

<ul>
	<li>比方说，字符串&nbsp;<code>"(name)is(age)yearsold"</code>&nbsp;中，有&nbsp;<strong>两个</strong>&nbsp;括号对，分别包含键&nbsp;<code>"name"</code> 和&nbsp;<code>"age"</code>&nbsp;。</li>
</ul>

<p>你知道许多键对应的值，这些关系由二维字符串数组&nbsp;<code>knowledge</code>&nbsp;表示，其中&nbsp;<code>knowledge[i] = [key<sub>i</sub>, value<sub>i</sub>]</code>&nbsp;，表示键&nbsp;<code>key<sub>i</sub></code>&nbsp;对应的值为&nbsp;<code>value<sub>i</sub></code><sub>&nbsp;</sub>。</p>

<p>你需要替换 <strong>所有</strong>&nbsp;的括号对。当你替换一个括号对，且它包含的键为&nbsp;<code>key<sub>i</sub></code>&nbsp;时，你需要：</p>

<ul>
	<li>将&nbsp;<code>key<sub>i</sub></code>&nbsp;和括号用对应的值&nbsp;<code>value<sub>i</sub></code>&nbsp;替换。</li>
	<li>如果从 <code>knowledge</code>&nbsp;中无法得知某个键对应的值，你需要将&nbsp;<code>key<sub>i</sub></code>&nbsp;和括号用问号&nbsp;<code>"?"</code>&nbsp;替换（不需要引号）。</li>
</ul>

<p><code>knowledge</code>&nbsp;中每个键最多只会出现一次。<code>s</code>&nbsp;中不会有嵌套的括号。</p>

<p>请你返回替换 <strong>所有</strong>&nbsp;括号对后的结果字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
<b>输出：</b>"bobistwoyearsold"
<strong>解释：</strong>
键 "name" 对应的值为 "bob" ，所以将 "(name)" 替换为 "bob" 。
键 "age" 对应的值为 "two" ，所以将 "(age)" 替换为 "two" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "hi(name)", knowledge = [["a","b"]]
<b>输出：</b>"hi?"
<b>解释：</b>由于不知道键 "name" 对应的值，所以用 "?" 替换 "(name)" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
<b>输出：</b>"yesyesyesaaa"
<b>解释：</b>相同的键在 s 中可能会出现多次。
键 "a" 对应的值为 "yes" ，所以将所有的 "(a)" 替换为 "yes" 。
注意，不在括号里的 "a" 不需要被替换。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= knowledge.length &lt;= 10<sup>5</sup></code></li>
	<li><code>knowledge[i].length == 2</code></li>
	<li><code>1 &lt;= key<sub>i</sub>.length, value<sub>i</sub>.length &lt;= 10</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母和圆括号&nbsp;<code>'('</code>&nbsp;和&nbsp;<code>')'</code>&nbsp;。</li>
	<li><code>s</code>&nbsp;中每一个左圆括号&nbsp;<code>'('</code>&nbsp;都有对应的右圆括号&nbsp;<code>')'</code>&nbsp;。</li>
	<li><code>s</code>&nbsp;中每对括号内的键都不会为空。</li>
	<li><code>s</code>&nbsp;中不会有嵌套括号对。</li>
	<li><code>key<sub>i</sub></code>&nbsp;和&nbsp;<code>value<sub>i</sub></code>&nbsp;只包含小写英文字母。</li>
	<li><code>knowledge</code>&nbsp;中的&nbsp;<code>key<sub>i</sub></code>&nbsp;不会重复。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Process pairs from right to left to handle repeats
2. Keep track of the current enclosed string using another string

## 示例

```
"(name)is(age)yearsold"
[["name","bob"],["age","two"]]
"hi(name)"
[["a","b"]]
"(a)(a)(a)aaa"
[["a","yes"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        
    }
};
```

### Java

```java
class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        
    }
}
```

### Python

```python
class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
```

### C

```c
char* evaluate(char* s, char*** knowledge, int knowledgeSize, int* knowledgeColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[][]} knowledge
 * @return {string}
 */
var evaluate = function(s, knowledge) {
    
};
```

### TypeScript

```typescript
function evaluate(s: string, knowledge: string[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[][] $knowledge
     * @return String
     */
    function evaluate($s, $knowledge) {
        
    }
}
```

### Swift

```swift
class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun evaluate(s: String, knowledge: List<List<String>>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String evaluate(String s, List<List<String>> knowledge) {
    
  }
}
```

### Go

```golang
func evaluate(s string, knowledge [][]string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[][]} knowledge
# @return {String}
def evaluate(s, knowledge)
    
end
```

### Scala

```scala
object Solution {
    def evaluate(s: String, knowledge: List[List[String]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (evaluate s knowledge)
  (-> string? (listof (listof string?)) string?)
  )
```

### Erlang

```erlang
-spec evaluate(S :: unicode:unicode_binary(), Knowledge :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
evaluate(S, Knowledge) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec evaluate(s :: String.t, knowledge :: [[String.t]]) :: String.t
  def evaluate(s, knowledge) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func evaluate(s: String, knowledge: ArrayList<ArrayList<String>>): String {

    }
}
```

