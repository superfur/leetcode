# 1071. 字符串的最大公因子

## 题目描述

<p>对于字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>，只有在&nbsp;<code>s = t + t + t + ... + t + t</code>（<code>t</code> 自身连接 1 次或多次）时，我们才认定&nbsp;“<code>t</code> 能除尽 <code>s</code>”。</p>

<p>给定两个字符串&nbsp;<code>str1</code>&nbsp;和&nbsp;<code>str2</code>&nbsp;。返回 <em>最长字符串&nbsp;<code>x</code>，要求满足&nbsp;<code>x</code> 能除尽 <code>str1</code> 且 <code>x</code> 能除尽 <code>str2</code></em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>str1 = "ABCABC", str2 = "ABC"
<strong>输出：</strong>"ABC"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>str1 = "ABABAB", str2 = "ABAB"
<strong>输出：</strong>"AB"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>str1 = "LEET", str2 = "CODE"
<strong>输出：</strong>""
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code>&nbsp;和&nbsp;<code>str2</code>&nbsp;由大写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 提示

1. The greatest common divisor must be a prefix of each string, so we can try all prefixes.

## 示例

```
"ABCABC"
"ABC"
"ABABAB"
"ABAB"
"LEET"
"CODE"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        
    }
};
```

### Java

```java
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
```

### C

```c
char* gcdOfStrings(char* str1, char* str2) {
    
}
```

### C#

```csharp
public class Solution {
    public string GcdOfStrings(string str1, string str2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    
};
```

### TypeScript

```typescript
function gcdOfStrings(str1: string, str2: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function gcdOfStrings($str1, $str2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func gcdOfStrings(_ str1: String, _ str2: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun gcdOfStrings(str1: String, str2: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String gcdOfStrings(String str1, String str2) {
    
  }
}
```

### Go

```golang
func gcdOfStrings(str1 string, str2 string) string {
    
}
```

### Ruby

```ruby
# @param {String} str1
# @param {String} str2
# @return {String}
def gcd_of_strings(str1, str2)
    
end
```

### Scala

```scala
object Solution {
    def gcdOfStrings(str1: String, str2: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (gcd-of-strings str1 str2)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec gcd_of_strings(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
gcd_of_strings(Str1, Str2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec gcd_of_strings(str1 :: String.t, str2 :: String.t) :: String.t
  def gcd_of_strings(str1, str2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func gcdOfStrings(str1: String, str2: String): String {

    }
}
```

