# 720. 词典中最长的单词

## 题目描述

<p>给出一个字符串数组&nbsp;<code>words</code> 组成的一本英语词典。返回&nbsp;<code>words</code> 中最长的一个单词，该单词是由&nbsp;<code>words</code>&nbsp;词典中其他单词逐步添加一个字母组成。</p>

<p>若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。</p>

<p>请注意，单词应该从左到右构建，每个额外的字符都添加到前一个单词的结尾。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["w","wo","wor","worl", "world"]
<strong>输出：</strong>"world"
<strong>解释：</strong> 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
<strong>输出：</strong>"apple"
<strong>解释：</strong>"apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li>所有输入的字符串&nbsp;<code>words[i]</code>&nbsp;都只包含小写字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. For every word in the input list, we can check whether all prefixes of that word are in the input list by using a Set.

## 示例

```
["w","wo","wor","worl","world"]
["a","banana","app","appl","ap","apply","apple"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestWord(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
```

### C

```c
char* longestWord(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestWord(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    
};
```

### TypeScript

```typescript
function longestWord(words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function longestWord($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestWord(_ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestWord(words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestWord(List<String> words) {
    
  }
}
```

### Go

```golang
func longestWord(words []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def longest_word(words)
    
end
```

### Scala

```scala
object Solution {
    def longestWord(words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-word words)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec longest_word(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
longest_word(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_word(words :: [String.t]) :: String.t
  def longest_word(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestWord(words: Array<String>): String {

    }
}
```

