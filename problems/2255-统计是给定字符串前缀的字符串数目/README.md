# 2255. 统计是给定字符串前缀的字符串数目

## 题目描述

<p>给你一个字符串数组&nbsp;<code>words</code>&nbsp;和一个字符串&nbsp;<code>s</code>&nbsp;，其中&nbsp;<code>words[i]</code> 和&nbsp;<code>s</code>&nbsp;只包含 <strong>小写英文字母</strong>&nbsp;。</p>

<p>请你返回 <code>words</code>&nbsp;中是字符串 <code>s</code>&nbsp;<strong>前缀&nbsp;</strong>的 <strong>字符串数目</strong>&nbsp;。</p>

<p>一个字符串的 <strong>前缀</strong>&nbsp;是出现在字符串开头的子字符串。<strong>子字符串</strong>&nbsp;是一个字符串中的连续一段字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>words = ["a","b","c","ab","bc","abc"], s = "abc"
<b>输出：</b>3
<strong>解释：</strong>
words 中是 s = "abc" 前缀的字符串为：
"a" ，"ab" 和 "abc" 。
所以 words 中是字符串 s 前缀的字符串数目为 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>words = ["a","a"], s = "aa"
<b>输出：</b>2
<strong>解释：
</strong>两个字符串都是 s 的前缀。
注意，相同的字符串可能在 words 中出现多次，它们应该被计数多次。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length, s.length &lt;= 10</code></li>
	<li><code>words[i]</code> 和&nbsp;<code>s</code>&nbsp;<strong>只</strong>&nbsp;包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. For each string in words, check if it is a prefix of s. If true, increment the answer by 1.

## 示例

```
["a","b","c","ab","bc","abc"]
"abc"
["a","a"]
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPrefixes(String[] words, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
```

### C

```c
int countPrefixes(char** words, int wordsSize, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPrefixes(string[] words, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} s
 * @return {number}
 */
var countPrefixes = function(words, s) {
    
};
```

### TypeScript

```typescript
function countPrefixes(words: string[], s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $s
     * @return Integer
     */
    function countPrefixes($words, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPrefixes(_ words: [String], _ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPrefixes(words: Array<String>, s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPrefixes(List<String> words, String s) {
    
  }
}
```

### Go

```golang
func countPrefixes(words []string, s string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} s
# @return {Integer}
def count_prefixes(words, s)
    
end
```

### Scala

```scala
object Solution {
    def countPrefixes(words: Array[String], s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_prefixes(words: Vec<String>, s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-prefixes words s)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_prefixes(Words :: [unicode:unicode_binary()], S :: unicode:unicode_binary()) -> integer().
count_prefixes(Words, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_prefixes(words :: [String.t], s :: String.t) :: integer
  def count_prefixes(words, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPrefixes(words: Array<String>, s: String): Int64 {

    }
}
```

