# 1592. 重新排列单词间的空格

## 题目描述

<p>给你一个字符串 <code>text</code> ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 <code>text</code> <strong>至少包含一个单词</strong> 。</p>

<p>请你重新排列空格，使每对相邻单词之间的空格数目都 <strong>相等</strong> ，并尽可能 <strong>最大化</strong> 该数目。如果不能重新平均分配所有空格，请 <strong>将多余的空格放置在字符串末尾</strong> ，这也意味着返回的字符串应当与原 <code>text</code> 字符串的长度相等。</p>

<p>返回 <strong>重新排列空格后的字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = &quot;  this   is  a sentence &quot;
<strong>输出：</strong>&quot;this   is   a   sentence&quot;
<strong>解释：</strong>总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = &quot; practice   makes   perfect&quot;
<strong>输出：</strong>&quot;practice   makes   perfect &quot;
<strong>解释：</strong>总共有 7 个空格和 3 个单词。7 / (3-1) = 3 个空格加上 1 个多余的空格。多余的空格需要放在字符串的末尾。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>text = &quot;hello   world&quot;
<strong>输出：</strong>&quot;hello   world&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>text = &quot;  walks  udp package   into  bar a&quot;
<strong>输出：</strong>&quot;walks  udp  package  into  bar  a &quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>text = &quot;a&quot;
<strong>输出：</strong>&quot;a&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 100</code></li>
	<li><code>text</code> 由小写英文字母和 <code>&#39; &#39;</code> 组成</li>
	<li><code>text</code> 中至少包含一个单词</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Count the total number of spaces and words. Then use the integer division to determine the numbers of spaces to add between each word and at the end.

## 示例

```
"  this   is  a sentence "
" practice   makes   perfect"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reorderSpaces(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public String reorderSpaces(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reorderSpaces(self, text: str) -> str:
        
```

### C

```c
char* reorderSpaces(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReorderSpaces(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var reorderSpaces = function(text) {
    
};
```

### TypeScript

```typescript
function reorderSpaces(text: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return String
     */
    function reorderSpaces($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reorderSpaces(_ text: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reorderSpaces(text: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reorderSpaces(String text) {
    
  }
}
```

### Go

```golang
func reorderSpaces(text string) string {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {String}
def reorder_spaces(text)
    
end
```

### Scala

```scala
object Solution {
    def reorderSpaces(text: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reorder_spaces(text: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reorder-spaces text)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reorder_spaces(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
reorder_spaces(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reorder_spaces(text :: String.t) :: String.t
  def reorder_spaces(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reorderSpaces(text: String): String {

    }
}
```

