# 290. 单词规律

## 题目描述

<p>给定一种规律 <code>pattern</code>&nbsp;和一个字符串&nbsp;<code>s</code>&nbsp;，判断 <code>s</code>&nbsp;是否遵循相同的规律。</p>

<p>这里的&nbsp;<strong>遵循&nbsp;</strong>指完全匹配，例如，&nbsp;<code>pattern</code>&nbsp;里的每个字母和字符串&nbsp;<code>s</code><strong>&nbsp;</strong>中的每个非空单词之间存在着双向连接的对应规律。</p>

<p>&nbsp;</p>

<p><strong class="example">示例1:</strong></p>

<pre>
<strong>输入:</strong> pattern = <code>"abba"</code>, s = <code>"dog cat cat dog"</code>
<strong>输出:</strong> true</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong>pattern = <code>"abba"</code>, s = <code>"dog cat cat fish"</code>
<strong>输出:</strong> false</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> pattern = <code>"aaaa"</code>, s = <code>"dog cat cat dog"</code>
<strong>输出:</strong> false</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt;= 300</code></li>
	<li><code>pattern</code>&nbsp;只包含小写英文字母</li>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母和&nbsp;<code>' '</code></li>
	<li><code>s</code>&nbsp;<strong>不包含</strong> 任何前导或尾随对空格</li>
	<li><code>s</code>&nbsp;中每个单词都被 <strong>单个空格 </strong>分隔</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 示例

```
"abba"
"dog cat cat dog"
"abba"
"dog cat cat fish"
"aaaa"
"dog cat cat dog"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
```

### C

```c
bool wordPattern(char* pattern, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool WordPattern(string pattern, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    
};
```

### TypeScript

```typescript
function wordPattern(pattern: string, s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPattern($pattern, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordPattern(_ pattern: String, _ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool wordPattern(String pattern, String s) {
    
  }
}
```

### Go

```golang
func wordPattern(pattern string, s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} pattern
# @param {String} s
# @return {Boolean}
def word_pattern(pattern, s)
    
end
```

### Scala

```scala
object Solution {
    def wordPattern(pattern: String, s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (word-pattern pattern s)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec word_pattern(Pattern :: unicode:unicode_binary(), S :: unicode:unicode_binary()) -> boolean().
word_pattern(Pattern, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_pattern(pattern :: String.t, s :: String.t) :: boolean
  def word_pattern(pattern, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordPattern(pattern: String, s: String): Bool {

    }
}
```

