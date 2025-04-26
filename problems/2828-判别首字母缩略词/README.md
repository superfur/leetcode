# 2828. 判别首字母缩略词

## 题目描述

<p>给你一个字符串数组&nbsp;<code>words</code> 和一个字符串 <code>s</code> ，请你判断 <code>s</code> 是不是 <code>words</code> 的 <strong>首字母缩略词</strong> 。</p>

<p>如果可以按顺序串联 <code>words</code> 中每个字符串的第一个字符形成字符串 <code>s</code> ，则认为 <code>s</code> 是 <code>words</code> 的首字母缩略词。例如，<code>"ab"</code> 可以由 <code>["apple", "banana"]</code> 形成，但是无法从 <code>["bear", "aardvark"]</code> 形成。</p>

<p>如果 <code>s</code> 是 <code>words</code> 的首字母缩略词，返回 <code>true</code><em> </em>；否则，返回<em> </em><code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["alice","bob","charlie"], s = "abc"
<strong>输出：</strong>true
<strong>解释：</strong>words 中 "alice"、"bob" 和 "charlie" 的第一个字符分别是 'a'、'b' 和 'c'。因此，s = "abc" 是首字母缩略词。 
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["an","apple"], s = "a"
<strong>输出：</strong>false
<strong>解释：</strong>words 中 "an" 和 "apple" 的第一个字符分别是 'a' 和 'a'。
串联这些字符形成的首字母缩略词是 "aa" 。
因此，s = "a" 不是首字母缩略词。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["never","gonna","give","up","on","you"], s = "ngguoy"
<strong>输出：</strong>true
<strong>解释：</strong>串联数组 words 中每个字符串的第一个字符，得到字符串 "ngguoy" 。
因此，s = "ngguoy" 是首字母缩略词。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>words[i]</code> 和 <code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. <div class="_1l1MA">Concatenate the first characters of the strings in <code>words</code>, and compare the resulting concatenation to <code>s</code>.</div>

## 示例

```
["alice","bob","charlie"]
"abc"
["an","apple"]
"a"
["never","gonna","give","up","on","you"]
"ngguoy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isAcronym(List<String> words, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
```

### C

```c
bool isAcronym(char** words, int wordsSize, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsAcronym(IList<string> words, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    
};
```

### TypeScript

```typescript
function isAcronym(words: string[], s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $s
     * @return Boolean
     */
    function isAcronym($words, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isAcronym(_ words: [String], _ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isAcronym(words: List<String>, s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isAcronym(List<String> words, String s) {
    
  }
}
```

### Go

```golang
func isAcronym(words []string, s string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} s
# @return {Boolean}
def is_acronym(words, s)
    
end
```

### Scala

```scala
object Solution {
    def isAcronym(words: List[String], s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-acronym words s)
  (-> (listof string?) string? boolean?)
  )
```

### Erlang

```erlang
-spec is_acronym(Words :: [unicode:unicode_binary()], S :: unicode:unicode_binary()) -> boolean().
is_acronym(Words, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_acronym(words :: [String.t], s :: String.t) :: boolean
  def is_acronym(words, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isAcronym(words: ArrayList<String>, s: String): Bool {

    }
}
```

