# 2131. 连接两字母单词得到的最长回文串

## 题目描述

<p>给你一个字符串数组&nbsp;<code>words</code>&nbsp;。<code>words</code>&nbsp;中每个元素都是一个包含 <strong>两个</strong>&nbsp;小写英文字母的单词。</p>

<p>请你从 <code>words</code>&nbsp;中选择一些元素并按 <b>任意顺序</b>&nbsp;连接它们，并得到一个 <strong>尽可能长的回文串</strong>&nbsp;。每个元素 <strong>至多</strong>&nbsp;只能使用一次。</p>

<p>请你返回你能得到的最长回文串的 <strong>长度</strong>&nbsp;。如果没办法得到任何一个回文串，请你返回 <code>0</code>&nbsp;。</p>

<p><strong>回文串</strong>&nbsp;指的是从前往后和从后往前读一样的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>words = ["lc","cl","gg"]
<b>输出：</b>6
<b>解释：</b>一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。
"clgglc" 是另一个可以得到的最长回文串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>words = ["ab","ty","yt","lc","cl","ab"]
<b>输出：</b>8
<strong>解释：</strong>最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。
"lcyttycl" 是另一个可以得到的最长回文串。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>words = ["cc","ll","xx"]
<b>输出：</b>2
<b>解释：</b>最长回文串是 "cc" ，长度为 2 。
"ll" 是另一个可以得到的最长回文串。"xx" 也是。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>words[i].length == 2</code></li>
	<li><code>words[i]</code>&nbsp;仅包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. A palindrome must be mirrored over the center. Suppose we have a palindrome. If we prepend the word "ab" on the left, what must we append on the right to keep it a palindrome?
2. We must append "ba" on the right. The number of times we can do this is the minimum of (occurrences of "ab") and (occurrences of "ba").
3. For words that are already palindromes, e.g. "aa", we can prepend and append these in pairs as described in the previous hint. We can also use exactly one in the middle to form an even longer palindrome.

## 示例

```
["lc","cl","gg"]
["ab","ty","yt","lc","cl","ab"]
["cc","ll","xx"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestPalindrome(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
```

### C

```c
int longestPalindrome(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestPalindrome(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var longestPalindrome = function(words) {
    
};
```

### TypeScript

```typescript
function longestPalindrome(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function longestPalindrome($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPalindrome(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPalindrome(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestPalindrome(List<String> words) {
    
  }
}
```

### Go

```golang
func longestPalindrome(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def longest_palindrome(words)
    
end
```

### Scala

```scala
object Solution {
    def longestPalindrome(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-palindrome words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_palindrome(Words :: [unicode:unicode_binary()]) -> integer().
longest_palindrome(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(words :: [String.t]) :: integer
  def longest_palindrome(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPalindrome(words: Array<String>): Int64 {

    }
}
```

