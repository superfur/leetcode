# 1392. 最长快乐前缀

## 题目描述

<p><strong>「快乐前缀」</strong>&nbsp;是在原字符串中既是&nbsp;<strong>非空</strong> 前缀也是后缀（不包括原字符串自身）的字符串。</p>

<p>给你一个字符串 <code>s</code>，请你返回它的 <strong>最长快乐前缀</strong>。如果不存在满足题意的前缀，则返回一个空字符串<meta charset="UTF-8" />&nbsp;<code>""</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "level"
<strong>输出：</strong>"l"
<strong>解释：</strong>不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ababab"
<strong>输出：</strong>"abab"
<strong>解释：</strong>"abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 只含有小写英文字母</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. Use Longest Prefix Suffix (KMP-table) or String Hashing.

## 示例

```
"level"
"ababab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestPrefix(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestPrefix(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestPrefix(self, s: str) -> str:
        
```

### C

```c
char* longestPrefix(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestPrefix(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestPrefix = function(s) {
    
};
```

### TypeScript

```typescript
function longestPrefix(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPrefix($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPrefix(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPrefix(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestPrefix(String s) {
    
  }
}
```

### Go

```golang
func longestPrefix(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def longest_prefix(s)
    
end
```

### Scala

```scala
object Solution {
    def longestPrefix(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_prefix(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-prefix s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec longest_prefix(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_prefix(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_prefix(s :: String.t) :: String.t
  def longest_prefix(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPrefix(s: String): String {

    }
}
```

