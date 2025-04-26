# 1455. 检查单词是否为句中其他单词的前缀

## 题目描述

<p>给你一个字符串 <code>sentence</code> 作为句子并指定检索词为 <code>searchWord</code> ，其中句子由若干用 <strong>单个空格</strong> 分隔的单词组成。请你检查检索词 <code>searchWord</code> 是否为句子 <code>sentence</code> 中任意单词的前缀。</p>

<p>如果&nbsp;<code>searchWord</code> 是某一个单词的前缀，则返回句子&nbsp;<code>sentence</code> 中该单词所对应的下标（<strong>下标从 1 开始</strong>）。如果 <code>searchWord</code> 是多个单词的前缀，则返回匹配的第一个单词的下标（<strong>最小下标</strong>）。如果 <code>searchWord</code> 不是任何单词的前缀，则返回 <code>-1</code><strong> </strong>。</p>

<p>字符串 <code>s</code> 的 <strong>前缀</strong> 是 <code>s</code> 的任何前导连续子字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sentence = "i love eating burger", searchWord = "burg"
<strong>输出：</strong>4
<strong>解释：</strong>"burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sentence = "this problem is an easy problem", searchWord = "pro"
<strong>输出：</strong>2
<strong>解释：</strong>"pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>sentence = "i am tired", searchWord = "you"
<strong>输出：</strong>-1
<strong>解释：</strong>"you" 不是句子中任何单词的前缀。

</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 100</code></li>
	<li><code>1 &lt;= searchWord.length &lt;= 10</code></li>
	<li><code>sentence</code> 由小写英文字母和空格组成。</li>
	<li><code>searchWord</code> 由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串
- 字符串匹配

## 提示

1. First extract the words of the sentence.
2. Check for each word if searchWord occurs at index 0, if so return the index of this word (1-indexed)
3. If searchWord doesn't exist as a prefix of any word return the default value (-1).

## 示例

```
"i love eating burger"
"burg"
"this problem is an easy problem"
"pro"
"i am tired"
"you"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        
    }
};
```

### Java

```java
class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
```

### C

```c
int isPrefixOfWord(char* sentence, char* searchWord) {
    
}
```

### C#

```csharp
public class Solution {
    public int IsPrefixOfWord(string sentence, string searchWord) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence
 * @param {string} searchWord
 * @return {number}
 */
var isPrefixOfWord = function(sentence, searchWord) {
    
};
```

### TypeScript

```typescript
function isPrefixOfWord(sentence: string, searchWord: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence
     * @param String $searchWord
     * @return Integer
     */
    function isPrefixOfWord($sentence, $searchWord) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPrefixOfWord(_ sentence: String, _ searchWord: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPrefixOfWord(sentence: String, searchWord: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int isPrefixOfWord(String sentence, String searchWord) {
    
  }
}
```

### Go

```golang
func isPrefixOfWord(sentence string, searchWord string) int {
    
}
```

### Ruby

```ruby
# @param {String} sentence
# @param {String} search_word
# @return {Integer}
def is_prefix_of_word(sentence, search_word)
    
end
```

### Scala

```scala
object Solution {
    def isPrefixOfWord(sentence: String, searchWord: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (is-prefix-of-word sentence searchWord)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec is_prefix_of_word(Sentence :: unicode:unicode_binary(), SearchWord :: unicode:unicode_binary()) -> integer().
is_prefix_of_word(Sentence, SearchWord) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_prefix_of_word(sentence :: String.t, search_word :: String.t) :: integer
  def is_prefix_of_word(sentence, search_word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPrefixOfWord(sentence: String, searchWord: String): Int64 {

    }
}
```

