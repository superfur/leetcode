# 2781. 最长合法子字符串的长度

## 题目描述

<p>给你一个字符串&nbsp;<code>word</code>&nbsp;和一个字符串数组&nbsp;<code>forbidden</code>&nbsp;。</p>

<p>如果一个字符串不包含&nbsp;<code>forbidden</code>&nbsp;中的任何字符串，我们称这个字符串是&nbsp;<strong>合法</strong>&nbsp;的。</p>

<p>请你返回字符串 <code>word</code>&nbsp;的一个 <strong>最长合法子字符串</strong>&nbsp;的长度。</p>

<p><strong>子字符串</strong> 指的是一个字符串中一段连续的字符，它可以为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>word = "cbaaaabc", forbidden = ["aaa","cb"]
<b>输出：</b>4
<b>解释：</b>总共有 11 个合法子字符串："c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" 和 "aabc"。最长合法子字符串的长度为 4 。
其他子字符串都要么包含 "aaa" ，要么包含 "cb" 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>word = "leetcode", forbidden = ["de","le","e"]
<strong>输出：</strong>4
<b>解释：</b>总共有 11 个合法子字符串："l" ，"t" ，"c" ，"o" ，"d" ，"tc" ，"co" ，"od" ，"tco" ，"cod" 和 "tcod" 。最长合法子字符串的长度为 4 。
所有其他子字符串都至少包含 "de" ，"le" 和 "e" 之一。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= forbidden.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= forbidden[i].length &lt;= 10</code></li>
	<li><code>forbidden[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 字符串
- 滑动窗口

## 示例

```
"cbaaaabc"
["aaa","cb"]
"leetcode"
["de","le","e"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestValidSubstring(string word, vector<string>& forbidden) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
```

### C

```c
int longestValidSubstring(char* word, char** forbidden, int forbiddenSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestValidSubstring(string word, IList<string> forbidden) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {string[]} forbidden
 * @return {number}
 */
var longestValidSubstring = function(word, forbidden) {
    
};
```

### TypeScript

```typescript
function longestValidSubstring(word: string, forbidden: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param String[] $forbidden
     * @return Integer
     */
    function longestValidSubstring($word, $forbidden) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestValidSubstring(_ word: String, _ forbidden: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestValidSubstring(word: String, forbidden: List<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestValidSubstring(String word, List<String> forbidden) {
    
  }
}
```

### Go

```golang
func longestValidSubstring(word string, forbidden []string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {String[]} forbidden
# @return {Integer}
def longest_valid_substring(word, forbidden)
    
end
```

### Scala

```scala
object Solution {
    def longestValidSubstring(word: String, forbidden: List[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_valid_substring(word: String, forbidden: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-valid-substring word forbidden)
  (-> string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_valid_substring(Word :: unicode:unicode_binary(), Forbidden :: [unicode:unicode_binary()]) -> integer().
longest_valid_substring(Word, Forbidden) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_valid_substring(word :: String.t, forbidden :: [String.t]) :: integer
  def longest_valid_substring(word, forbidden) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestValidSubstring(word: String, forbidden: ArrayList<String>): Int64 {

    }
}
```

