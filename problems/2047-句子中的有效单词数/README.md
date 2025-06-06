# 2047. 句子中的有效单词数

## 题目描述

<p>句子仅由小写字母（<code>'a'</code> 到 <code>'z'</code>）、数字（<code>'0'</code> 到 <code>'9'</code>）、连字符（<code>'-'</code>）、标点符号（<code>'!'</code>、<code>'.'</code> 和 <code>','</code>）以及空格（<code>' '</code>）组成。每个句子可以根据空格分解成 <strong>一个或者多个 token</strong> ，这些 token 之间由一个或者多个空格 <code>' '</code> 分隔。</p>

<p>如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：</p>

<ul>
	<li>仅由小写字母、连字符和/或标点（不含数字）组成。</li>
	<li><strong>至多一个</strong> 连字符 <code>'-'</code> 。如果存在，连字符两侧应当都存在小写字母（<code>"a-b"</code> 是一个有效单词，但 <code>"-ab"</code> 和 <code>"ab-"</code> 不是有效单词）。</li>
	<li><strong>至多一个 </strong>标点符号。如果存在，标点符号应当位于 token 的 <strong>末尾</strong> 。</li>
</ul>

<p>这里给出几个有效单词的例子：<code>"a-b."</code>、<code>"afad"</code>、<code>"ba-c"</code>、<code>"a!"</code> 和 <code>"!"</code> 。</p>

<p>给你一个字符串 <code>sentence</code> ，请你找出并返回<em> </em><code>sentence</code> 中<strong> 有效单词的数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sentence = "<em><strong>cat</strong></em> <em><strong>and</strong></em>  <em><strong>dog</strong></em>"
<strong>输出：</strong>3
<strong>解释：</strong>句子中的有效单词是 "cat"、"and" 和 "dog"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sentence = "!this  1-s b8d!"
<strong>输出：</strong>0
<strong>解释：</strong>句子中没有有效单词
"!this" 不是有效单词，因为它以一个标点开头
"1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>sentence = "<em><strong>alice</strong></em> <em><strong>and</strong></em>  <em><strong>bob</strong></em> <em><strong>are</strong></em> <em><strong>playing</strong></em> stone-game10"
<strong>输出：</strong>5
<strong>解释：</strong>句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"
"stone-game10" 不是有效单词，因为它含有数字
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 1000</code></li>
	<li><code>sentence</code> 由小写英文字母、数字（<code>0-9</code>）、以及字符（<code>' '</code>、<code>'-'</code>、<code>'!'</code>、<code>'.'</code> 和 <code>','</code>）组成</li>
	<li>句子中至少有 <code>1</code> 个 token</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Iterate through the string to split it by spaces.
2. Count the number of characters of each type (letters, numbers, hyphens, and punctuations).

## 示例

```
"cat and  dog"
"!this  1-s b8d!"
"alice and  bob are playing stone-game10"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countValidWords(string sentence) {
        
    }
};
```

### Java

```java
class Solution {
    public int countValidWords(String sentence) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countValidWords(self, sentence: str) -> int:
        
```

### C

```c
int countValidWords(char* sentence) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountValidWords(string sentence) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence
 * @return {number}
 */
var countValidWords = function(sentence) {
    
};
```

### TypeScript

```typescript
function countValidWords(sentence: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence
     * @return Integer
     */
    function countValidWords($sentence) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countValidWords(_ sentence: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countValidWords(sentence: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countValidWords(String sentence) {
    
  }
}
```

### Go

```golang
func countValidWords(sentence string) int {
    
}
```

### Ruby

```ruby
# @param {String} sentence
# @return {Integer}
def count_valid_words(sentence)
    
end
```

### Scala

```scala
object Solution {
    def countValidWords(sentence: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_valid_words(sentence: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-valid-words sentence)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_valid_words(Sentence :: unicode:unicode_binary()) -> integer().
count_valid_words(Sentence) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_valid_words(sentence :: String.t) :: integer
  def count_valid_words(sentence) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countValidWords(sentence: String): Int64 {

    }
}
```

