# 2490. 回环句

## 题目描述

<p><strong>句子</strong> 是由单个空格分隔的一组单词，且不含前导或尾随空格。</p>

<ul>
	<li>例如，<code>"Hello World"</code>、<code>"HELLO"</code>、<code>"hello world hello world"</code> 都是符合要求的句子。</li>
</ul>

<p>单词 <strong>仅</strong> 由大写和小写英文字母组成。且大写和小写字母会视作不同字符。</p>

<p>如果句子满足下述全部条件，则认为它是一个 <strong>回环句</strong> ：</p>

<ul>
	<li>句子中每个单词的最后一个字符等于下一个单词的第一个字符。</li>
	<li>最后一个单词的最后一个字符和第一个单词的第一个字符相等。</li>
</ul>

<p>例如，<code>"leetcode exercises sound delightful"</code>、<code>"eetcode"</code>、<code>"leetcode eats soul"</code> 都是回环句。然而，<code>"Leetcode is cool"</code>、<code>"happy Leetcode"</code>、<code>"Leetcode"</code> 和 <code>"I like Leetcode"</code> 都 <strong>不</strong> 是回环句。</p>

<p>给你一个字符串 <code>sentence</code> ，请你判断它是不是一个回环句。如果是，返回 <code>true</code><em> </em>；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sentence = "leetcode exercises sound delightful"
<strong>输出：</strong>true
<strong>解释：</strong>句子中的单词是 ["leetcode", "exercises", "sound", "delightful"] 。
- leetcod<strong><em>e</em></strong> 的最后一个字符和 <strong><em>e</em></strong>xercises 的第一个字符相等。
- exercise<em><strong>s</strong></em> 的最后一个字符和 <em><strong>s</strong></em>ound 的第一个字符相等。
- <em><strong>s</strong></em>ound 的最后一个字符和 delightfu<em><strong>l</strong></em> 的第一个字符相等。
- delightfu<em><strong>l</strong></em> 的最后一个字符和 <em><strong>l</strong></em>eetcode 的第一个字符相等。
这个句子是回环句。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sentence = "eetcode"
<strong>输出：</strong>true
<strong>解释：</strong>句子中的单词是 ["eetcode"] 。
- eetcod<em><strong>e</strong></em> 的最后一个字符和 <em><strong>e</strong></em>etcod<em>e</em> 的第一个字符相等。
这个句子是回环句。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>sentence = "Leetcode is cool"
<strong>输出：</strong>false
<strong>解释：</strong>句子中的单词是 ["Leetcode", "is", "cool"] 。
- Leetcod<em><strong>e</strong></em>&nbsp;的最后一个字符和 <em><strong>i</strong></em>s 的第一个字符 <strong>不</strong> 相等。 
这个句子 <strong>不</strong> 是回环句。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 500</code></li>
	<li><code>sentence</code> 仅由大小写英文字母和空格组成</li>
	<li><code>sentence</code> 中的单词由单个空格进行分隔</li>
	<li>不含任何前导或尾随空格</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Check the character before the empty space and the character after the empty space.
2. Check the first character and the last character of the sentence.

## 示例

```
"leetcode exercises sound delightful"
"eetcode"
"Leetcode is cool"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isCircularSentence(string sentence) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isCircularSentence(String sentence) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
```

### C

```c
bool isCircularSentence(char* sentence) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsCircularSentence(string sentence) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    
};
```

### TypeScript

```typescript
function isCircularSentence(sentence: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence
     * @return Boolean
     */
    function isCircularSentence($sentence) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isCircularSentence(_ sentence: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isCircularSentence(sentence: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isCircularSentence(String sentence) {
    
  }
}
```

### Go

```golang
func isCircularSentence(sentence string) bool {
    
}
```

### Ruby

```ruby
# @param {String} sentence
# @return {Boolean}
def is_circular_sentence(sentence)
    
end
```

### Scala

```scala
object Solution {
    def isCircularSentence(sentence: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-circular-sentence sentence)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_circular_sentence(Sentence :: unicode:unicode_binary()) -> boolean().
is_circular_sentence(Sentence) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_circular_sentence(sentence :: String.t) :: boolean
  def is_circular_sentence(sentence) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isCircularSentence(sentence: String): Bool {

    }
}
```

