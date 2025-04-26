# 5. 最长回文子串

## 题目描述

<p>给你一个字符串 <code>s</code>，找到 <code>s</code> 中最长的 <span data-keyword="palindromic-string">回文</span> <span data-keyword="substring-nonempty">子串</span>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "babad"
<strong>输出：</strong>"bab"
<strong>解释：</strong>"aba" 同样是符合题意的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cbbd"
<strong>输出：</strong>"bb"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅由数字和英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串
- 动态规划

## 提示

1. How can we reuse a previously computed palindrome to compute a larger palindrome?
2. If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
3. Complexity based hint:</br>
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

## 示例

```
"babad"
"cbbd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestPalindrome(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
```

### C

```c
char* longestPalindrome(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestPalindrome(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
};
```

### TypeScript

```typescript
function longestPalindrome(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPalindrome(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPalindrome(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestPalindrome(String s) {
    
  }
}
```

### Go

```golang
func longestPalindrome(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def longest_palindrome(s)
    
end
```

### Scala

```scala
object Solution {
    def longestPalindrome(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-palindrome s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec longest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_palindrome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(s :: String.t) :: String.t
  def longest_palindrome(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPalindrome(s: String): String {

    }
}
```

