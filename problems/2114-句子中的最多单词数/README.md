# 2114. 句子中的最多单词数

## 题目描述

<p>一个 <strong>句子</strong>&nbsp;由一些 <strong>单词</strong>&nbsp;以及它们之间的单个空格组成，句子的开头和结尾不会有多余空格。</p>

<p>给你一个字符串数组&nbsp;<code>sentences</code>&nbsp;，其中&nbsp;<code>sentences[i]</code>&nbsp;表示单个 <strong>句子</strong>&nbsp;。</p>

<p>请你返回单个句子里 <strong>单词的最多数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>sentences = ["alice and bob love leetcode", "i think so too", <em><strong>"this is great thanks very much"</strong></em>]
<b>输出：</b>6
<b>解释：</b>
- 第一个句子 "alice and bob love leetcode" 总共有 5 个单词。
- 第二个句子 "i think so too" 总共有 4 个单词。
- 第三个句子 "this is great thanks very much" 总共有 6 个单词。
所以，单个句子中有最多单词数的是第三个句子，总共有 6 个单词。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>sentences = ["please wait", <em><strong>"continue to fight"</strong></em>, <em><strong>"continue to win"</strong></em>]
<b>输出：</b>3
<b>解释：</b>可能有多个句子有相同单词数。
这个例子中，第二个句子和第三个句子（加粗斜体）有相同数目的单词数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentences.length &lt;= 100</code></li>
	<li><code>1 &lt;= sentences[i].length &lt;= 100</code></li>
	<li><code>sentences[i]</code>&nbsp;只包含小写英文字母和&nbsp;<code>' '</code>&nbsp;。</li>
	<li><code>sentences[i]</code>&nbsp;的开头和结尾都没有空格。</li>
	<li><code>sentences[i]</code>&nbsp;中所有单词由单个空格隔开。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Process each sentence separately and count the number of words by looking for the number of space characters in the sentence and adding it by 1.

## 示例

```
["alice and bob love leetcode","i think so too","this is great thanks very much"]
["please wait","continue to fight","continue to win"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        
    }
};
```

### Java

```java
class Solution {
    public int mostWordsFound(String[] sentences) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
```

### C

```c
int mostWordsFound(char** sentences, int sentencesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MostWordsFound(string[] sentences) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    
};
```

### TypeScript

```typescript
function mostWordsFound(sentences: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $sentences
     * @return Integer
     */
    function mostWordsFound($sentences) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostWordsFound(_ sentences: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostWordsFound(sentences: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mostWordsFound(List<String> sentences) {
    
  }
}
```

### Go

```golang
func mostWordsFound(sentences []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} sentences
# @return {Integer}
def most_words_found(sentences)
    
end
```

### Scala

```scala
object Solution {
    def mostWordsFound(sentences: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (most-words-found sentences)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec most_words_found(Sentences :: [unicode:unicode_binary()]) -> integer().
most_words_found(Sentences) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_words_found(sentences :: [String.t]) :: integer
  def most_words_found(sentences) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostWordsFound(sentences: Array<String>): Int64 {

    }
}
```

