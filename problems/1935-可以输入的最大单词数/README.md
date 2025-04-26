# 1935. 可以输入的最大单词数

## 题目描述

<p>键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。</p>

<p>给你一个由若干单词组成的字符串 <code>text</code> ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 <code>brokenLetters</code> ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 <code>text</code> 中单词的数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>text = "hello world", brokenLetters = "ad"
<strong>输出：</strong>1
<strong>解释：</strong>无法输入 "world" ，因为字母键 'd' 已损坏。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>text = "leet code", brokenLetters = "lt"
<strong>输出：</strong>1
<strong>解释：</strong>无法输入 "leet" ，因为字母键 'l' 和 't' 已损坏。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>text = "leet code", brokenLetters = "e"
<strong>输出：</strong>0
<strong>解释：</strong>无法输入任何单词，因为字母键 'e' 已损坏。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= brokenLetters.length &lt;= 26</code></li>
	<li><code>text</code> 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格</li>
	<li>每个单词仅由小写英文字母组成</li>
	<li><code>brokenLetters</code> 由 <strong>互不相同</strong> 的小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Check each word separately if it can be typed.
2. A word can be typed if all its letters are not broken.

## 示例

```
"hello world"
"ad"
"leet code"
"lt"
"leet code"
"e"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        
    }
};
```

### Java

```java
class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
```

### C

```c
int canBeTypedWords(char* text, char* brokenLetters) {
    
}
```

### C#

```csharp
public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    
};
```

### TypeScript

```typescript
function canBeTypedWords(text: string, brokenLetters: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @param String $brokenLetters
     * @return Integer
     */
    function canBeTypedWords($text, $brokenLetters) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canBeTypedWords(_ text: String, _ brokenLetters: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canBeTypedWords(text: String, brokenLetters: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int canBeTypedWords(String text, String brokenLetters) {
    
  }
}
```

### Go

```golang
func canBeTypedWords(text string, brokenLetters string) int {
    
}
```

### Ruby

```ruby
# @param {String} text
# @param {String} broken_letters
# @return {Integer}
def can_be_typed_words(text, broken_letters)
    
end
```

### Scala

```scala
object Solution {
    def canBeTypedWords(text: String, brokenLetters: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (can-be-typed-words text brokenLetters)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec can_be_typed_words(Text :: unicode:unicode_binary(), BrokenLetters :: unicode:unicode_binary()) -> integer().
can_be_typed_words(Text, BrokenLetters) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_be_typed_words(text :: String.t, broken_letters :: String.t) :: integer
  def can_be_typed_words(text, broken_letters) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canBeTypedWords(text: String, brokenLetters: String): Int64 {

    }
}
```

