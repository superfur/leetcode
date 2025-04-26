# LCR 019. 验证回文串 II

## 题目描述

<p>给定一个非空字符串&nbsp;<code>s</code>，请判断如果&nbsp;<strong>最多 </strong>从字符串中删除一个字符能否得到一个回文字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> s = &quot;aba&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> s = &quot;abca&quot;
<strong>输出:</strong> true
<strong>解释:</strong> 可以删除 &quot;c&quot; 字符 或者 &quot;b&quot; 字符
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> s = &quot;abc&quot;
<strong>输出:</strong> false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 680&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/valid-palindrome-ii/">https://leetcode-cn.com/problems/valid-palindrome-ii/</a></p>


## 难度

Easy

## 标签

- 贪心
- 双指针
- 字符串

## 示例

```
"aba"
"abca"
"abc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validPalindrome(string s) {

    }
};
```

### Java

```java
class Solution {
    public boolean validPalindrome(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def validPalindrome(self, s: str) -> bool:
```

### C

```c


bool validPalindrome(char * s){

}
```

### C#

```csharp
public class Solution {
    public bool ValidPalindrome(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {

};
```

### TypeScript

```typescript
function validPalindrome(s: string): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function validPalindrome($s) {

    }
}
```

### Swift

```swift
class Solution {
    func validPalindrome(_ s: String) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validPalindrome(s: String): Boolean {

    }
}
```

### Go

```golang
func validPalindrome(s string) bool {

}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def valid_palindrome(s)

end
```

### Scala

```scala
object Solution {
    def validPalindrome(s: String): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_palindrome(s: String) -> bool {

    }
}
```

### Racket

```racket
(define/contract (valid-palindrome s)
  (-> string? boolean?)

  )
```

### Erlang

```erlang
-spec valid_palindrome(S :: unicode:unicode_binary()) -> boolean().
valid_palindrome(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_palindrome(s :: String.t) :: boolean
  def valid_palindrome(s) do

  end
end
```

