# 2299. 强密码检验器 II

## 题目描述

<p>如果一个密码满足以下所有条件，我们称它是一个 <strong>强</strong>&nbsp;密码：</p>

<ul>
	<li>它有至少 <code>8</code>&nbsp;个字符。</li>
	<li>至少包含 <strong>一个小写英文</strong>&nbsp;字母。</li>
	<li>至少包含 <strong>一个大写英文</strong>&nbsp;字母。</li>
	<li>至少包含 <strong>一个数字</strong>&nbsp;。</li>
	<li>至少包含 <strong>一个特殊字符</strong>&nbsp;。特殊字符为：<code>"!@#$%^&amp;*()-+"</code>&nbsp;中的一个。</li>
	<li>它 <strong>不</strong>&nbsp;包含&nbsp;<code>2</code>&nbsp;个连续相同的字符（比方说&nbsp;<code>"aab"</code>&nbsp;不符合该条件，但是&nbsp;<code>"aba"</code>&nbsp;符合该条件）。</li>
</ul>

<p>给你一个字符串&nbsp;<code>password</code>&nbsp;，如果它是一个&nbsp;<strong>强</strong>&nbsp;密码，返回&nbsp;<code>true</code>，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>password = "IloveLe3tcode!"
<b>输出：</b>true
<b>解释：</b>密码满足所有的要求，所以我们返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>password = "Me+You--IsMyDream"
<b>输出：</b>false
<b>解释：</b>密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>password = "1aB!"
<b>输出：</b>false
<b>解释：</b>密码不符合长度要求。所以我们返回 false 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= password.length &lt;= 100</code></li>
	<li><code>password</code>&nbsp;包含字母，数字和&nbsp;<code>"!@#$%^&amp;*()-+"</code>&nbsp;这些特殊字符。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. You can use a boolean flag to define certain types of characters seen in the string.
2. In the end, check if all boolean flags have ended up True, and do not forget to check the "adjacent" and "length" criteria.

## 示例

```
"IloveLe3tcode!"
"Me+You--IsMyDream"
"1aB!"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean strongPasswordCheckerII(String password) {
        
    }
}
```

### Python

```python
class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
```

### C

```c
bool strongPasswordCheckerII(char* password) {
    
}
```

### C#

```csharp
public class Solution {
    public bool StrongPasswordCheckerII(string password) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} password
 * @return {boolean}
 */
var strongPasswordCheckerII = function(password) {
    
};
```

### TypeScript

```typescript
function strongPasswordCheckerII(password: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $password
     * @return Boolean
     */
    function strongPasswordCheckerII($password) {
        
    }
}
```

### Swift

```swift
class Solution {
    func strongPasswordCheckerII(_ password: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun strongPasswordCheckerII(password: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool strongPasswordCheckerII(String password) {
    
  }
}
```

### Go

```golang
func strongPasswordCheckerII(password string) bool {
    
}
```

### Ruby

```ruby
# @param {String} password
# @return {Boolean}
def strong_password_checker_ii(password)
    
end
```

### Scala

```scala
object Solution {
    def strongPasswordCheckerII(password: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn strong_password_checker_ii(password: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (strong-password-checker-ii password)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec strong_password_checker_ii(Password :: unicode:unicode_binary()) -> boolean().
strong_password_checker_ii(Password) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec strong_password_checker_ii(password :: String.t) :: boolean
  def strong_password_checker_ii(password) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func strongPasswordCheckerII(password: String): Bool {

    }
}
```

