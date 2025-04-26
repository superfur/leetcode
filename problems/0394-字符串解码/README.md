# 394. 字符串解码

## 题目描述

<p>给定一个经过编码的字符串，返回它解码后的字符串。</p>

<p>编码规则为: <code>k[encoded_string]</code>，表示其中方括号内部的 <code>encoded_string</code> 正好重复 <code>k</code> 次。注意 <code>k</code> 保证为正整数。</p>

<p>你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。</p>

<p>此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 <code>k</code> ，例如不会出现像&nbsp;<code>3a</code>&nbsp;或&nbsp;<code>2[4]</code>&nbsp;的输入。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "3[a]2[bc]"
<strong>输出：</strong>"aaabcbc"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "3[a2[c]]"
<strong>输出：</strong>"accaccacc"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "2[abc]3[cd]ef"
<strong>输出：</strong>"abcabccdcdcdef"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "abc3[cd]xyz"
<strong>输出：</strong>"abccdcdcdxyz"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 30</code></li>
	<li><meta charset="UTF-8" /><code>s</code>&nbsp;由小写英文字母、数字和方括号<meta charset="UTF-8" />&nbsp;<code>'[]'</code> 组成</li>
	<li><code>s</code>&nbsp;保证是一个&nbsp;<strong>有效</strong>&nbsp;的输入。</li>
	<li><code>s</code>&nbsp;中所有整数的取值范围为<meta charset="UTF-8" />&nbsp;<code>[1, 300]</code>&nbsp;</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 递归
- 字符串

## 示例

```
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string decodeString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String decodeString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def decodeString(self, s: str) -> str:
        
```

### C

```c
char* decodeString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string DecodeString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    
};
```

### TypeScript

```typescript
function decodeString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function decodeString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decodeString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decodeString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String decodeString(String s) {
    
  }
}
```

### Go

```golang
func decodeString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def decode_string(s)
    
end
```

### Scala

```scala
object Solution {
    def decodeString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decode_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (decode-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec decode_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
decode_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decode_string(s :: String.t) :: String.t
  def decode_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decodeString(s: String): String {

    }
}
```

