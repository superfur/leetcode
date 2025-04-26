# 1328. 破坏回文串

## 题目描述

<p>给你一个由小写英文字母组成的回文字符串&nbsp;<code>palindrome</code> ，请你将其中&nbsp;<strong>一个</strong> 字符用任意小写英文字母替换，使得结果字符串的 <strong>字典序最小</strong> ，且&nbsp;<strong>不是</strong>&nbsp;回文串。</p>

<p>请你返回结果字符串。如果无法做到，则返回一个 <strong>空串</strong> 。</p>

<p>如果两个字符串长度相同，那么字符串 <code>a</code> 字典序比字符串 <code>b</code> 小可以这样定义：在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置上，字符串 <code>a</code> 中的字符严格小于 <code>b</code> 中的对应字符。例如，<code>"abcc”</code> 字典序比 <code>"abcd"</code> 小，因为不同的第一个位置是在第四个字符，显然 <code>'c'</code> 比 <code>'d'</code> 小。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>palindrome = "abccba"
<strong>输出：</strong>"aaccba"
<strong>解释：</strong>存在多种方法可以使 "abccba" 不是回文，例如 "<em><strong>z</strong></em>bccba", "a<em><strong>a</strong></em>ccba", 和 "ab<em><strong>a</strong></em>cba" 。
在所有方法中，"aaccba" 的字典序最小。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>palindrome = "a"
<strong>输出：</strong>""
<strong>解释：</strong>不存在替换一个字符使 "a" 变成非回文的方法，所以返回空字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= palindrome.length &lt;= 1000</code></li>
	<li><code>palindrome</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. How to detect if there is impossible to perform the replacement? Only when the length = 1.
2. Change the first non 'a' character to 'a'.
3. What if the string has only 'a'?
4. Change the last character to 'b'.

## 示例

```
"abccba"
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        
    }
};
```

### Java

```java
class Solution {
    public String breakPalindrome(String palindrome) {
        
    }
}
```

### Python

```python
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
```

### C

```c
char* breakPalindrome(char* palindrome) {
    
}
```

### C#

```csharp
public class Solution {
    public string BreakPalindrome(string palindrome) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    
};
```

### TypeScript

```typescript
function breakPalindrome(palindrome: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $palindrome
     * @return String
     */
    function breakPalindrome($palindrome) {
        
    }
}
```

### Swift

```swift
class Solution {
    func breakPalindrome(_ palindrome: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun breakPalindrome(palindrome: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String breakPalindrome(String palindrome) {
    
  }
}
```

### Go

```golang
func breakPalindrome(palindrome string) string {
    
}
```

### Ruby

```ruby
# @param {String} palindrome
# @return {String}
def break_palindrome(palindrome)
    
end
```

### Scala

```scala
object Solution {
    def breakPalindrome(palindrome: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn break_palindrome(palindrome: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (break-palindrome palindrome)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec break_palindrome(Palindrome :: unicode:unicode_binary()) -> unicode:unicode_binary().
break_palindrome(Palindrome) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec break_palindrome(palindrome :: String.t) :: String.t
  def break_palindrome(palindrome) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func breakPalindrome(palindrome: String): String {

    }
}
```

