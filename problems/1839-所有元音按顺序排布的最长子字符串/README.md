# 1839. 所有元音按顺序排布的最长子字符串

## 题目描述

<p>当一个字符串满足如下条件时，我们称它是 <b>美丽的</b> ：</p>

<ul>
	<li>所有 5 个英文元音字母（<code>'a'</code> ，<code>'e'</code> ，<code>'i'</code> ，<code>'o'</code> ，<code>'u'</code>）都必须 <strong>至少</strong> 出现一次。</li>
	<li>这些元音字母的顺序都必须按照 <strong>字典序</strong> 升序排布（也就是说所有的 <code>'a'</code> 都在 <code>'e'</code> 前面，所有的 <code>'e'</code> 都在 <code>'i'</code> 前面，以此类推）</li>
</ul>

<p>比方说，字符串 <code>"aeiou"</code> 和 <code>"aaaaaaeiiiioou"</code> 都是 <strong>美丽的</strong> ，但是 <code>"uaeio"</code> ，<code>"aeoiu"</code> 和 <code>"aaaeeeooo"</code> <strong>不是美丽的</strong> 。</p>

<p>给你一个只包含英文元音字母的字符串 <code>word</code> ，请你返回 <code>word</code> 中 <strong>最长美丽子字符串的长度</strong> 。如果不存在这样的子字符串，请返回 <code>0</code> 。</p>

<p><strong>子字符串</strong> 是字符串中一个连续的字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>word = "aeiaaio<strong>aaaaeiiiiouuu</strong>ooaauuaeiu"
<b>输出：</b>13
<b>解释：</b>最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>word = "aeeeiiiioooauuu<strong>aeiou</strong>"
<b>输出：</b>5
<b>解释：</b>最长子字符串是 "aeiou" ，长度为 5 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>word = "a"
<b>输出：</b>0
<b>解释：</b>没有美丽子字符串，所以返回 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word.length <= 5 * 10<sup>5</sup></code></li>
	<li><code>word</code> 只包含字符 <code>'a'</code>，<code>'e'</code>，<code>'i'</code>，<code>'o'</code> 和 <code>'u'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 滑动窗口

## 提示

1. Start from each 'a' and find the longest beautiful substring starting at that index.
2. Based on the current character decide if you should include the next character in the beautiful substring.

## 示例

```
"aeiaaioaaaaeiiiiouuuooaauuaeiu"
"aeeeiiiioooauuuaeiou"
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestBeautifulSubstring(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestBeautifulSubstring(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
```

### C

```c
int longestBeautifulSubstring(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestBeautifulSubstring(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var longestBeautifulSubstring = function(word) {
    
};
```

### TypeScript

```typescript
function longestBeautifulSubstring(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function longestBeautifulSubstring($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestBeautifulSubstring(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestBeautifulSubstring(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestBeautifulSubstring(String word) {
    
  }
}
```

### Go

```golang
func longestBeautifulSubstring(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def longest_beautiful_substring(word)
    
end
```

### Scala

```scala
object Solution {
    def longestBeautifulSubstring(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_beautiful_substring(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-beautiful-substring word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_beautiful_substring(Word :: unicode:unicode_binary()) -> integer().
longest_beautiful_substring(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_beautiful_substring(word :: String.t) :: integer
  def longest_beautiful_substring(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestBeautifulSubstring(word: String): Int64 {

    }
}
```

