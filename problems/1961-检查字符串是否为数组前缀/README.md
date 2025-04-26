# 1961. 检查字符串是否为数组前缀

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符串数组 <code>words</code> ，请你判断 <code>s</code> 是否为 <code>words</code> 的 <strong>前缀字符串</strong> 。</p>

<p>字符串 <code>s</code> 要成为 <code>words</code> 的 <strong>前缀字符串</strong> ，需要满足：<code>s</code> 可以由 <code>words</code> 中的前 <code>k</code>（<code>k</code> 为 <strong>正数</strong> ）个字符串按顺序相连得到，且 <code>k</code> 不超过 <code>words.length</code> 。</p>

<p>如果 <code>s</code> 是 <code>words</code> 的 <strong>前缀字符串</strong> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "iloveleetcode", words = ["i","love","leetcode","apples"]
<strong>输出：</strong>true
<strong>解释：</strong>
s 可以由 "i"、"love" 和 "leetcode" 相连得到。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "iloveleetcode", words = ["apples","i","love","leetcode"]
<strong>输出：</strong>false
<strong>解释：</strong>
数组的前缀相连无法得到 s 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>words[i]</code> 和 <code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 字符串

## 提示

1. There are only words.length prefix strings.
2. Create all of them and see if s is one of them.

## 示例

```
"iloveleetcode"
["i","love","leetcode","apples"]
"iloveleetcode"
["apples","i","love","leetcode"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPrefixString(String s, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
```

### C

```c
bool isPrefixString(char* s, char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPrefixString(string s, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} words
 * @return {boolean}
 */
var isPrefixString = function(s, words) {
    
};
```

### TypeScript

```typescript
function isPrefixString(s: string, words: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Boolean
     */
    function isPrefixString($s, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPrefixString(_ s: String, _ words: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPrefixString(s: String, words: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPrefixString(String s, List<String> words) {
    
  }
}
```

### Go

```golang
func isPrefixString(s string, words []string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} words
# @return {Boolean}
def is_prefix_string(s, words)
    
end
```

### Scala

```scala
object Solution {
    def isPrefixString(s: String, words: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_prefix_string(s: String, words: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-prefix-string s words)
  (-> string? (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec is_prefix_string(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> boolean().
is_prefix_string(S, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_prefix_string(s :: String.t, words :: [String.t]) :: boolean
  def is_prefix_string(s, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPrefixString(s: String, words: Array<String>): Bool {

    }
}
```

