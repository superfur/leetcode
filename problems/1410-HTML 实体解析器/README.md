# 1410. HTML 实体解析器

## 题目描述

<p>「HTML&nbsp;实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。</p>

<p>HTML 里这些特殊字符和它们对应的字符实体包括：</p>

<ul>
	<li><strong>双引号：</strong>字符实体为&nbsp;<code>&amp;quot;</code>&nbsp;，对应的字符是&nbsp;<code>&quot;</code>&nbsp;。</li>
	<li><strong>单引号：</strong>字符实体为&nbsp;<code>&amp;apos;</code>&nbsp;，对应的字符是&nbsp;<code>&#39;</code>&nbsp;。</li>
	<li><strong>与符号：</strong>字符实体为&nbsp;<code>&amp;amp;</code>&nbsp;，对应对的字符是&nbsp;<code>&amp;</code>&nbsp;。</li>
	<li><strong>大于号：</strong>字符实体为&nbsp;<code>&amp;gt;</code>&nbsp;，对应的字符是&nbsp;<code>&gt;</code>&nbsp;。</li>
	<li><strong>小于号：</strong>字符实体为&nbsp;<code>&amp;lt;</code>&nbsp;，对应的字符是&nbsp;<code>&lt;</code>&nbsp;。</li>
	<li><strong>斜线号：</strong>字符实体为&nbsp;<code>&amp;frasl;</code>&nbsp;，对应的字符是&nbsp;<code>/</code>&nbsp;。</li>
</ul>

<p>给你输入字符串&nbsp;<code>text</code>&nbsp;，请你实现一个 HTML&nbsp;实体解析器，返回解析器解析后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;&amp;amp; is an HTML entity but &amp;ambassador; is not.&quot;
<strong>输出：</strong>&quot;&amp; is an HTML entity but &amp;ambassador; is not.&quot;
<strong>解释：</strong>解析器把字符实体 &amp;amp; 用 &amp; 替换
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;and I quote: &amp;quot;...&amp;quot;&quot;
<strong>输出：</strong>&quot;and I quote: \&quot;...\&quot;&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;Stay home! Practice on Leetcode :)&quot;
<strong>输出：</strong>&quot;Stay home! Practice on Leetcode :)&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false&quot;
<strong>输出：</strong>&quot;x &gt; y &amp;&amp; x &lt; y is always false&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;leetcode.com&amp;frasl;problemset&amp;frasl;all&quot;
<strong>输出：</strong>&quot;leetcode.com/problemset/all&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10^5</code></li>
	<li>字符串可能包含 256 个ASCII 字符中的任意字符。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串

## 提示

1. Search the string for all the occurrences of the character '&'.
2. For every '&' check if it matches an HTML entity by checking the ';' character and if entity found replace it in the answer.

## 示例

```
"&amp; is an HTML entity but &ambassador; is not."
"and I quote: &quot;...&quot;"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string entityParser(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public String entityParser(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def entityParser(self, text: str) -> str:
        
```

### C

```c
char* entityParser(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public string EntityParser(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var entityParser = function(text) {
    
};
```

### TypeScript

```typescript
function entityParser(text: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return String
     */
    function entityParser($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func entityParser(_ text: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun entityParser(text: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String entityParser(String text) {
    
  }
}
```

### Go

```golang
func entityParser(text string) string {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {String}
def entity_parser(text)
    
end
```

### Scala

```scala
object Solution {
    def entityParser(text: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn entity_parser(text: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (entity-parser text)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec entity_parser(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
entity_parser(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec entity_parser(text :: String.t) :: String.t
  def entity_parser(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func entityParser(text: String): String {

    }
}
```

