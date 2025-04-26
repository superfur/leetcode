# 2414. 最长的字母序连续子字符串的长度

## 题目描述

<p><strong>字母序连续字符串</strong> 是由字母表中连续字母组成的字符串。换句话说，字符串 <code>"abcdefghijklmnopqrstuvwxyz"</code> 的任意子字符串都是 <strong>字母序连续字符串</strong> 。</p>

<ul>
	<li>例如，<code>"abc"</code> 是一个字母序连续字符串，而 <code>"acb"</code> 和 <code>"za"</code> 不是。</li>
</ul>

<p>给你一个仅由小写英文字母组成的字符串 <code>s</code> ，返回其 <strong>最长</strong> 的 字母序连续子字符串 的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "abacaba"
<strong>输出：</strong>2
<strong>解释：</strong>共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
"ab" 是最长的字母序连续子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "abcde"
<strong>输出：</strong>5
<strong>解释：</strong>"abcde" 是最长的字母序连续子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 提示

1. What is the longest possible continuous substring?
2. The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.

## 示例

```
"abacaba"
"abcde"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestContinuousSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestContinuousSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
```

### C

```c
int longestContinuousSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestContinuousSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestContinuousSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function longestContinuousSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestContinuousSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestContinuousSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestContinuousSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestContinuousSubstring(String s) {
    
  }
}
```

### Go

```golang
func longestContinuousSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def longest_continuous_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def longestContinuousSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_continuous_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-continuous-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_continuous_substring(S :: unicode:unicode_binary()) -> integer().
longest_continuous_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_continuous_substring(s :: String.t) :: integer
  def longest_continuous_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestContinuousSubstring(s: String): Int64 {

    }
}
```

