# 2697. 字典序最小回文串

## 题目描述

<p>给你一个由 <strong>小写英文字母</strong> 组成的字符串 <code>s</code> ，你可以对其执行一些操作。在一步操作中，你可以用其他小写英文字母 <strong>替换</strong>&nbsp; <code>s</code> 中的一个字符。</p>

<p>请你执行 <strong>尽可能少的操作</strong> ，使 <code>s</code> 变成一个 <strong>回文串</strong> 。如果执行 <strong>最少</strong> 操作次数的方案不止一种，则只需选取 <strong>字典序最小</strong> 的方案。</p>

<p>对于两个长度相同的字符串 <code>a</code> 和 <code>b</code> ，在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置，如果该位置上 <code>a</code> 中对应字母比 <code>b</code> 中对应字母在字母表中出现顺序更早，则认为 <code>a</code> 的字典序比 <code>b</code> 的字典序要小。</p>

<p>返回最终的回文字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "egcfe"
<strong>输出：</strong>"efcfe"
<strong>解释：</strong>将 "egcfe" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "efcfe"，只需将 'g' 改为 'f' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd"
<strong>输出：</strong>"abba"
<strong>解释：</strong>将 "abcd" 变成回文字符串的最小操作次数为 2 ，修改 2 次得到的字典序最小回文字符串是 "abba" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "seven"
<strong>输出：</strong>"neven"
<strong>解释：</strong>将 "seven" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "neven" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 双指针
- 字符串

## 提示

1. We can make any string a palindrome, by simply making any character at index i equal to the character at index length - i - 1 (using 0-based indexing).
2. To make it lexicographically smallest we can change the character with maximum ASCII value to the one with minimum ASCII value.

## 示例

```
"egcfe"
"abcd"
"seven"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string makeSmallestPalindrome(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String makeSmallestPalindrome(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
```

### C

```c
char* makeSmallestPalindrome(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MakeSmallestPalindrome(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeSmallestPalindrome = function(s) {
    
};
```

### TypeScript

```typescript
function makeSmallestPalindrome(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeSmallestPalindrome($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeSmallestPalindrome(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeSmallestPalindrome(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String makeSmallestPalindrome(String s) {
    
  }
}
```

### Go

```golang
func makeSmallestPalindrome(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def make_smallest_palindrome(s)
    
end
```

### Scala

```scala
object Solution {
    def makeSmallestPalindrome(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_smallest_palindrome(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (make-smallest-palindrome s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec make_smallest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_smallest_palindrome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_smallest_palindrome(s :: String.t) :: String.t
  def make_smallest_palindrome(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeSmallestPalindrome(s: String): String {

    }
}
```

