# 1771. 由子序列构造的最长回文串的长度

## 题目描述

<p>给你两个字符串 <code>word1</code> 和 <code>word2</code> ，请你按下述方法构造一个字符串：</p>

<ul>
	<li>从 <code>word1</code> 中选出某个 <strong>非空</strong> 子序列 <code>subsequence1</code> 。</li>
	<li>从 <code>word2</code> 中选出某个 <strong>非空</strong> 子序列 <code>subsequence2</code> 。</li>
	<li>连接两个子序列 <code>subsequence1 + subsequence2</code> ，得到字符串。</li>
</ul>

<p>返回可按上述方法构造的最长 <strong>回文串</strong> 的 <strong>长度</strong> 。如果无法构造回文串，返回 <code>0</code> 。</p>

<p>字符串 <code>s</code> 的一个 <strong>子序列</strong> 是通过从 <code>s</code> 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。</p>

<p><strong>回文串</strong> 是正着读和反着读结果一致的字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>word1 = "cacb", word2 = "cbba"
<strong>输出：</strong>5
<strong>解释：</strong>从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>word1 = "ab", word2 = "ab"
<strong>输出：</strong>3
<strong>解释：</strong>从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>word1 = "aa", word2 = "bb"
<strong>输出：</strong>0
<strong>解释：</strong>无法按题面所述方法构造回文串，所以返回 0 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 1000</code></li>
	<li><code>word1</code> 和 <code>word2</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Let's ignore the non-empty subsequence constraint. We can concatenate the two strings and find the largest palindromic subsequence with dynamic programming.
2. Iterate through every pair of characters word1[i] and word2[j], and see if some palindrome begins with word1[i] and ends with word2[j]. This ensures that the subsequences are non-empty.

## 示例

```
"cacb"
"cbba"
"ab"
"ab"
"aa"
"bb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestPalindrome(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
```

### C

```c
int longestPalindrome(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestPalindrome(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var longestPalindrome = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function longestPalindrome(word1: string, word2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function longestPalindrome($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPalindrome(_ word1: String, _ word2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPalindrome(word1: String, word2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestPalindrome(String word1, String word2) {
    
  }
}
```

### Go

```golang
func longestPalindrome(word1 string, word2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Integer}
def longest_palindrome(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def longestPalindrome(word1: String, word2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_palindrome(word1: String, word2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-palindrome word1 word2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_palindrome(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
longest_palindrome(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(word1 :: String.t, word2 :: String.t) :: integer
  def longest_palindrome(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPalindrome(word1: String, word2: String): Int64 {

    }
}
```

