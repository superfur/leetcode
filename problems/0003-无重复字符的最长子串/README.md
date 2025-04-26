# 3. 无重复字符的最长子串

## 题目描述

<p>给定一个字符串 <code>s</code> ，请你找出其中不含有重复字符的&nbsp;<strong>最长 <span data-keyword="substring-nonempty">子串</span></strong><strong>&nbsp;</strong>的长度。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "abcabcbb"
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code>"abc"</code>，所以其长度为 3。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "bbbbb"
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code>"b"</code>，所以其长度为 1。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>s = "pwwkew"
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是&nbsp;<code>"wke"</code>，所以其长度为 3。
&nbsp;    请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>"pwke"</code>&nbsp;是一个<em>子序列，</em>不是子串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;由英文字母、数字、符号和空格组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.

## 示例

```
"abcabcbb"
"bbbbb"
"pwwkew"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
```

### C

```c
int lengthOfLongestSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function lengthOfLongestSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lengthOfLongestSubstring(String s) {
    
  }
}
```

### Go

```golang
func lengthOfLongestSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (length-of-longest-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec length_of_longest_substring(S :: unicode:unicode_binary()) -> integer().
length_of_longest_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec length_of_longest_substring(s :: String.t) :: integer
  def length_of_longest_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lengthOfLongestSubstring(s: String): Int64 {

    }
}
```

