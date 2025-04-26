# 1616. 分割两个字符串得到回文串

## 题目描述

<p>给你两个字符串&nbsp;<code>a</code> 和&nbsp;<code>b</code>&nbsp;，它们长度相同。请你选择一个下标，将两个字符串都在&nbsp;<strong>相同的下标 </strong>分割开。由&nbsp;<code>a</code>&nbsp;可以得到两个字符串：&nbsp;<code>a<sub>prefix</sub></code>&nbsp;和&nbsp;<code>a<sub>suffix</sub></code>&nbsp;，满足&nbsp;<code>a = a<sub>prefix</sub> + a<sub>suffix</sub></code><sub>&nbsp;</sub>，同理，由&nbsp;<code>b</code> 可以得到两个字符串&nbsp;<code>b<sub>prefix</sub></code> 和&nbsp;<code>b<sub>suffix</sub></code>&nbsp;，满足&nbsp;<code>b = b<sub>prefix</sub> + b<sub>suffix</sub></code>&nbsp;。请你判断&nbsp;<code>a<sub>prefix</sub> + b<sub>suffix</sub></code> 或者&nbsp;<code>b<sub>prefix</sub> + a<sub>suffix</sub></code>&nbsp;能否构成回文串。</p>

<p>当你将一个字符串&nbsp;<code>s</code>&nbsp;分割成&nbsp;<code>s<sub>prefix</sub></code> 和&nbsp;<code>s<sub>suffix</sub></code>&nbsp;时，&nbsp;<code>s<sub>suffix</sub></code> 或者&nbsp;<code>s<sub>prefix</sub></code> 可以为空。比方说，&nbsp;<code>s = "abc"</code>&nbsp;那么&nbsp;<code>"" + "abc"</code>&nbsp;，&nbsp;<code>"a" + "bc"&nbsp;</code>，&nbsp;<code>"ab" + "c"</code>&nbsp;和&nbsp;<code>"abc" + ""</code>&nbsp;都是合法分割。</p>

<p>如果 <strong>能构成回文字符串</strong> ，那么请返回&nbsp;<code>true</code>，否则返回<em>&nbsp;</em><code>false</code>&nbsp;。</p>

<p><strong>注意</strong>，&nbsp;<code>x + y</code>&nbsp;表示连接字符串&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>a = "x", b = "y"
<b>输出：</b>true
<b>解释：</b>如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
a<sub>prefix</sub> = "", a<sub>suffix</sub> = "x"
b<sub>prefix</sub> = "", b<sub>suffix</sub> = "y"
那么 a<sub>prefix</sub> + b<sub>suffix</sub> = "" + "y" = "y" 是回文串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = "xbdef", b = "xecab"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>a = "ulacfd", b = "jizalu"
<b>输出：</b>true
<b>解释：</b>在下标为 3 处分割：
a<sub>prefix</sub> = "ula", a<sub>suffix</sub> = "cfd"
b<sub>prefix</sub> = "jiz", b<sub>suffix</sub> = "alu"
那么 a<sub>prefix</sub> + b<sub>suffix</sub> = "ula" + "alu" = "ulaalu" 是回文串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>a.length == b.length</code></li>
	<li><code>a</code> 和&nbsp;<code>b</code>&nbsp;都只包含小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. Try finding the largest prefix from a that matches a suffix in b
2. Try string matching

## 示例

```
"x"
"y"
"xbdef"
"xecab"
"ulacfd"
"jizalu"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkPalindromeFormation(string a, string b) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkPalindromeFormation(String a, String b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
```

### C

```c
bool checkPalindromeFormation(char* a, char* b) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckPalindromeFormation(string a, string b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {boolean}
 */
var checkPalindromeFormation = function(a, b) {
    
};
```

### TypeScript

```typescript
function checkPalindromeFormation(a: string, b: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Boolean
     */
    function checkPalindromeFormation($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkPalindromeFormation(_ a: String, _ b: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkPalindromeFormation(a: String, b: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkPalindromeFormation(String a, String b) {
    
  }
}
```

### Go

```golang
func checkPalindromeFormation(a string, b string) bool {
    
}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {Boolean}
def check_palindrome_formation(a, b)
    
end
```

### Scala

```scala
object Solution {
    def checkPalindromeFormation(a: String, b: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_palindrome_formation(a: String, b: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-palindrome-formation a b)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_palindrome_formation(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> boolean().
check_palindrome_formation(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_palindrome_formation(a :: String.t, b :: String.t) :: boolean
  def check_palindrome_formation(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkPalindromeFormation(a: String, b: String): Bool {

    }
}
```

