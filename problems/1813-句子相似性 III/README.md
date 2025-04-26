# 1813. 句子相似性 III

## 题目描述

<p>给定两个字符串&nbsp;<code>sentence1</code>&nbsp;和&nbsp;<code>sentence2</code>，每个表示由一些单词组成的一个句子。句子是一系列由&nbsp;<strong>单个 </strong>空格分隔的&nbsp;<strong>单词</strong>，且开头和结尾没有多余空格。每个单词都只包含大写和小写英文字母。</p>

<p>如果两个句子&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 <strong>相似的</strong>&nbsp;。<strong>注意</strong>，插入的句子必须与现有单词用空白隔开。&nbsp;</p>

<p>比方说，</p>

<ul>
	<li><code>s1 = "Hello Jane"</code> 与&nbsp;<code>s2 = "Hello my name is Jane"</code>，我们可以往 <code>s1</code>&nbsp;中&nbsp;<code>"Hello"</code> 和&nbsp;<code>"Jane"</code>&nbsp;之间插入&nbsp;<code>"my name is"</code>&nbsp;得到 <code>s2</code>&nbsp;。</li>
	<li><code>s1 = "Frog cool"</code>&nbsp;与 <code>s2 = "Frogs are cool"</code>&nbsp;不是相似的，因为尽管往&nbsp;<code>s1</code>&nbsp;中插入&nbsp;<code>"s are"</code>，它没有与&nbsp;<code>"Frog"</code>&nbsp;用空格隔开。</li>
</ul>

<p>给你两个句子&nbsp;<code>sentence1</code> 和&nbsp;<code>sentence2</code>&nbsp;，如果<em>&nbsp;</em><code>sentence1</code> 和<em>&nbsp;</em><code>sentence2</code> 是 <strong>相似</strong> 的，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block"><b>输入：</b>sentence1 = "My name is Haley", sentence2 = "My Haley"</div>

<div class="example-block"><b>输出：</b>true</div>

<div class="example-block"><b>解释：</b>可以往 <code>sentence2</code> 中 "My" 和 "Haley" 之间插入 "name is" ，得到 <code>sentence1</code> 。</div>

<div class="example-block">&nbsp;</div>

<p><strong>示例 2：</strong></p>

<div class="example-block"><b>输入：</b>sentence1 = "of", sentence2 = "A lot of words"</div>

<div class="example-block"><b>输出：</b>false</div>

<div class="example-block"><strong>解释：</strong>没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。</div>

<div class="example-block">&nbsp;</div>

<p><strong>示例 3：</strong></p>

<div class="example-block"><b>输入：</b>sentence1 = "Eating right now", sentence2 = "Eating"</div>

<div class="example-block"><b>输出：</b>true</div>

<div class="example-block"><b>解释：</b>可以往 <code>sentence2</code> 的结尾插入 "right now" 得到 <code>sentence1</code> 。</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentence1.length, sentence2.length &lt;= 100</code></li>
	<li><code>sentence1</code>&nbsp;和&nbsp;<code>sentence2</code>&nbsp;都只包含大小写英文字母和空格。</li>
	<li><code>sentence1</code>&nbsp;和&nbsp;<code>sentence2</code>&nbsp;中的单词都只由单个空格隔开。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 字符串

## 提示

1. One way to look at it is to find one sentence as a concatenation of a prefix and suffix from the other sentence.
2. Get the longest common prefix between them and the longest common suffix.

## 示例

```
"My name is Haley"
"My Haley"
"of"
"A lot of words"
"Eating right now"
"Eating"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
```

### C

```c
bool areSentencesSimilar(char* sentence1, char* sentence2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool AreSentencesSimilar(string sentence1, string sentence2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    
};
```

### TypeScript

```typescript
function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence1
     * @param String $sentence2
     * @return Boolean
     */
    function areSentencesSimilar($sentence1, $sentence2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func areSentencesSimilar(_ sentence1: String, _ sentence2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun areSentencesSimilar(sentence1: String, sentence2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool areSentencesSimilar(String sentence1, String sentence2) {
    
  }
}
```

### Go

```golang
func areSentencesSimilar(sentence1 string, sentence2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} sentence1
# @param {String} sentence2
# @return {Boolean}
def are_sentences_similar(sentence1, sentence2)
    
end
```

### Scala

```scala
object Solution {
    def areSentencesSimilar(sentence1: String, sentence2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn are_sentences_similar(sentence1: String, sentence2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (are-sentences-similar sentence1 sentence2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec are_sentences_similar(Sentence1 :: unicode:unicode_binary(), Sentence2 :: unicode:unicode_binary()) -> boolean().
are_sentences_similar(Sentence1, Sentence2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec are_sentences_similar(sentence1 :: String.t, sentence2 :: String.t) :: boolean
  def are_sentences_similar(sentence1, sentence2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func areSentencesSimilar(sentence1: String, sentence2: String): Bool {

    }
}
```

