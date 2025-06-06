# 2730. 找到最长的半重复子字符串

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;，这个字符串只包含&nbsp;<code>0</code>&nbsp;到&nbsp;<code>9</code>&nbsp;的数字字符。</p>

<p>如果一个字符串&nbsp;<code>t</code>&nbsp;中至多有一对相邻字符是相等的，那么称这个字符串 <code>t</code> 是 <strong>半重复的</strong>&nbsp;。例如，<code>"0010"</code>&nbsp;、<code>"002020"</code>&nbsp;、<code>"0123"</code>&nbsp;、<code>"2002"</code>&nbsp;和 <code>"54944"</code>&nbsp;是半重复字符串，而 <code>"00101022"</code>&nbsp;（相邻的相同数字对是 00 和 22）和 <code>"1101234883"</code>&nbsp;（相邻的相同数字对是 11 和 88）不是半重复字符串。</p>

<p>请你返回 <code>s</code>&nbsp;中最长 <strong>半重复</strong>&nbsp;<span data-keyword="substring-nonempty">子字符串</span> 的长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "52233"</span></p>

<p><strong>输出：</strong><span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "5494"</span></p>

<p><strong>输出：</strong><span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code>&nbsp;是一个半重复字符串。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "1111111"</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>'0' &lt;= s[i] &lt;= '9'</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 滑动窗口

## 提示

1. Since n is small, we can just check every substring, and if the substring is semi-repetitive, maximize the answer with its length.

## 示例

```
"52233"
"5494"
"1111111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
```

### C

```c
int longestSemiRepetitiveSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSemiRepetitiveSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestSemiRepetitiveSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function longestSemiRepetitiveSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestSemiRepetitiveSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSemiRepetitiveSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSemiRepetitiveSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSemiRepetitiveSubstring(String s) {
    
  }
}
```

### Go

```golang
func longestSemiRepetitiveSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def longest_semi_repetitive_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def longestSemiRepetitiveSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_semi_repetitive_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-semi-repetitive-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_semi_repetitive_substring(S :: unicode:unicode_binary()) -> integer().
longest_semi_repetitive_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_semi_repetitive_substring(s :: String.t) :: integer
  def longest_semi_repetitive_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSemiRepetitiveSubstring(s: String): Int64 {

    }
}
```

