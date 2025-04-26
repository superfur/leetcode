# 2000. 反转单词前缀

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>word</code> 和一个字符 <code>ch</code> 。找出 <code>ch</code> 第一次出现的下标 <code>i</code> ，<strong>反转 </strong><code>word</code> 中从下标 <code>0</code> 开始、直到下标 <code>i</code> 结束（含下标 <code>i</code> ）的那段字符。如果 <code>word</code> 中不存在字符 <code>ch</code> ，则无需进行任何操作。</p>

<ul>
	<li>例如，如果 <code>word = "abcdefd"</code> 且 <code>ch = "d"</code> ，那么你应该 <strong>反转</strong> 从下标 0 开始、直到下标 <code>3</code> 结束（含下标 <code>3</code> ）。结果字符串将会是 <code>"<em><strong>dcba</strong></em>efd"</code> 。</li>
</ul>

<p>返回 <strong>结果字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>word = "<em><strong>abcd</strong></em>efd", ch = "d"
<strong>输出：</strong>"<em><strong>dcba</strong></em>efd"
<strong>解释：</strong>"d" 第一次出现在下标 3 。 
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "dcbaefd" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>word = "<em><strong>xyxz</strong></em>xe", ch = "z"
<strong>输出：</strong>"<em><strong>zxyx</strong></em>xe"
<strong>解释：</strong>"z" 第一次也是唯一一次出现是在下标 3 。
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "zxyxxe" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>word = "abcd", ch = "z"
<strong>输出：</strong>"abcd"
<strong>解释：</strong>"z" 不存在于 word 中。
无需执行反转操作，结果字符串是 "abcd" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 250</code></li>
	<li><code>word</code> 由小写英文字母组成</li>
	<li><code>ch</code> 是一个小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 双指针
- 字符串

## 提示

1. Find the first index where ch appears.
2. Find a way to reverse a substring of word.

## 示例

```
"abcdefd"
"d"
"xyxzxe"
"z"
"abcd"
"z"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reversePrefix(string word, char ch) {
        
    }
};
```

### Java

```java
class Solution {
    public String reversePrefix(String word, char ch) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
```

### C

```c
char* reversePrefix(char* word, char ch) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReversePrefix(string word, char ch) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    
};
```

### TypeScript

```typescript
function reversePrefix(word: string, ch: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reversePrefix(_ word: String, _ ch: Character) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reversePrefix(word: String, ch: Char): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reversePrefix(String word, String ch) {
    
  }
}
```

### Go

```golang
func reversePrefix(word string, ch byte) string {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Character} ch
# @return {String}
def reverse_prefix(word, ch)
    
end
```

### Scala

```scala
object Solution {
    def reversePrefix(word: String, ch: Char): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-prefix word ch)
  (-> string? char? string?)
  )
```

### Erlang

```erlang
-spec reverse_prefix(Word :: unicode:unicode_binary(), Ch :: char()) -> unicode:unicode_binary().
reverse_prefix(Word, Ch) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_prefix(word :: String.t, ch :: char) :: String.t
  def reverse_prefix(word, ch) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reversePrefix(word: String, ch: Rune): String {

    }
}
```

