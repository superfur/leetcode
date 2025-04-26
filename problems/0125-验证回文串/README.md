# 125. 验证回文串

## 题目描述

<p>如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 <strong>回文串</strong> 。</p>

<p>字母和数字都属于字母数字字符。</p>

<p>给你一个字符串 <code>s</code>，如果它是 <strong>回文串</strong> ，返回 <code>true</code><em> </em>；否则，返回<em> </em><code>false</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> s = "A man, a plan, a canal: Panama"
<strong>输出：</strong>true
<strong>解释：</strong>"amanaplanacanalpanama" 是回文串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "race a car"
<strong>输出：</strong>false
<strong>解释：</strong>"raceacar" 不是回文串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = " "
<strong>输出：</strong>true
<strong>解释：</strong>在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由可打印的 ASCII 字符组成</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 示例

```
"A man, a plan, a canal: Panama"
"race a car"
" "
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPalindrome(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
```

### C

```c
bool isPalindrome(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPalindrome(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
};
```

### TypeScript

```typescript
function isPalindrome(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isPalindrome($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPalindrome(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPalindrome(String s) {
    
  }
}
```

### Go

```golang
func isPalindrome(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    
end
```

### Scala

```scala
object Solution {
    def isPalindrome(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-palindrome s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_palindrome(S :: unicode:unicode_binary()) -> boolean().
is_palindrome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_palindrome(s :: String.t) :: boolean
  def is_palindrome(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPalindrome(s: String): Bool {

    }
}
```

