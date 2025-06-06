# 1451. 重新排列句子中的单词

## 题目描述

<p>「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 <code>text</code> :</p>

<ul>
	<li>句子的首字母大写</li>
	<li><code>text</code> 中的每个单词都用单个空格分隔。</li>
</ul>

<p>请你重新排列 <code>text</code> 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。</p>

<p>请同样按上述格式返回新的句子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = &quot;Leetcode is cool&quot;
<strong>输出：</strong>&quot;Is cool leetcode&quot;
<strong>解释：</strong>句子中共有 3 个单词，长度为 8 的 &quot;Leetcode&quot; ，长度为 2 的 &quot;is&quot; 以及长度为 4 的 &quot;cool&quot; 。
输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = &quot;Keep calm and code on&quot;
<strong>输出：</strong>&quot;On and keep calm code&quot;
<strong>解释：</strong>输出的排序情况如下：
&quot;On&quot; 2 个字母。
&quot;and&quot; 3 个字母。
&quot;keep&quot; 4 个字母，因为存在长度相同的其他单词，所以它们之间需要保留在原句子中的相对顺序。
&quot;calm&quot; 4 个字母。
&quot;code&quot; 4 个字母。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>text = &quot;To be or not to be&quot;
<strong>输出：</strong>&quot;To be or to be not&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>text</code> 以大写字母开头，然后包含若干小写字母以及单词间的单个空格。</li>
	<li><code>1 &lt;= text.length &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 排序

## 提示

1. Store each word and their relative position. Then, sort them by length of words in case of tie by their original order.

## 示例

```
"Leetcode is cool"
"Keep calm and code on"
"To be or not to be"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string arrangeWords(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public String arrangeWords(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def arrangeWords(self, text: str) -> str:
        
```

### C

```c
char* arrangeWords(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public string ArrangeWords(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var arrangeWords = function(text) {
    
};
```

### TypeScript

```typescript
function arrangeWords(text: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return String
     */
    function arrangeWords($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arrangeWords(_ text: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arrangeWords(text: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String arrangeWords(String text) {
    
  }
}
```

### Go

```golang
func arrangeWords(text string) string {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {String}
def arrange_words(text)
    
end
```

### Scala

```scala
object Solution {
    def arrangeWords(text: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn arrange_words(text: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (arrange-words text)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec arrange_words(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
arrange_words(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec arrange_words(text :: String.t) :: String.t
  def arrange_words(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arrangeWords(text: String): String {

    }
}
```

