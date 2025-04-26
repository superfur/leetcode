# LCR 018. 验证回文串

## 题目描述

<p>给定一个字符串 <code>s</code> ，验证 <code>s</code>&nbsp;是否是&nbsp;<strong>回文串&nbsp;</strong>，只考虑字母和数字字符，可以忽略字母的大小写。</p>

<p>本题中，将空字符串定义为有效的&nbsp;<strong>回文串&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>s =<strong> </strong>&quot;A man, a plan, a canal: Panama&quot;
<strong>输出:</strong> true
<strong>解释：</strong>&quot;amanaplanacanalpanama&quot; 是回文串</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> s = &quot;race a car&quot;
<strong>输出:</strong> false
<strong>解释：</strong>&quot;raceacar&quot; 不是回文串</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li>字符串 <code>s</code> 由 ASCII 字符组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 125&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/valid-palindrome/">https://leetcode-cn.com/problems/valid-palindrome/</a></p>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 示例

```
"A man, a plan, a canal: Panama"
"race a car"
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


bool isPalindrome(char * s){

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

