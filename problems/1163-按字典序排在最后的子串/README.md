# 1163. 按字典序排在最后的子串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，找出它的所有子串并按字典序排列，返回排在最后的那个子串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abab"
<strong>输出：</strong>"bab"
<strong>解释：</strong>我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>s = "leetcode"
<strong>输出：</strong>"tcode"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅含有小写英文字符。</li>
</ul>


## 难度

Hard

## 标签

- 双指针
- 字符串

## 提示

1. Assume that the answer is a sub-string from index i to j. If you add the character at index j+1 you get a better answer.
2. The answer is always a suffix of the given string.
3. Since the limits are high, we need an efficient data structure.
4. Use suffix array.

## 示例

```
"abab"
"leetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string lastSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String lastSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def lastSubstring(self, s: str) -> str:
        
```

### C

```c
char* lastSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string LastSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var lastSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function lastSubstring(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function lastSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lastSubstring(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lastSubstring(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String lastSubstring(String s) {
    
  }
}
```

### Go

```golang
func lastSubstring(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def last_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def lastSubstring(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn last_substring(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (last-substring s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec last_substring(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
last_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec last_substring(s :: String.t) :: String.t
  def last_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lastSubstring(s: String): String {

    }
}
```

