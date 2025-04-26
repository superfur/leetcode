# LCR 138. 有效数字

## 题目描述

<p><strong>有效数字</strong>（按顺序）可以分成以下几个部分：</p>

<ol>
	<li>若干空格</li>
	<li>一个 <strong>小数</strong> 或者 <strong>整数</strong></li>
	<li>（可选）一个 <code>'e'</code> 或 <code>'E'</code> ，后面跟着一个 <strong>整数</strong></li>
	<li>若干空格</li>
</ol>

<p><strong>小数</strong>（按顺序）可以分成以下几个部分：</p>

<ol>
	<li>（可选）一个符号字符（<code>'+'</code> 或 <code>'-'</code>）</li>
	<li>下述格式之一：
	<ol>
		<li>至少一位数字，后面跟着一个点 <code>'.'</code></li>
		<li>至少一位数字，后面跟着一个点 <code>'.'</code> ，后面再跟着至少一位数字</li>
		<li>一个点 <code>'.'</code> ，后面跟着至少一位数字</li>
	</ol>
	</li>
</ol>

<p><strong>整数</strong>（按顺序）可以分成以下几个部分：</p>

<ol>
	<li>（可选）一个符号字符（<code>'+'</code> 或 <code>'-'</code>）</li>
	<li>至少一位数字</li>
</ol>

<p>部分有效数字列举如下：<code>["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]</code></p>

<p>部分无效数字列举如下：<code>["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]</code></p>

<p>给你一个字符串 <code>s</code> ，如果 <code>s</code> 是一个 <strong>有效数字</strong> ，请返回 <code>true</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "0"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "e"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "."
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> 仅含英文字母（大写和小写），数字（<code>0-9</code>），加号 <code>'+'</code> ，减号 <code>'-'</code> ，空格 <code>' '</code> 或者点 <code>'.'</code> 。</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串

## 示例

```
"0"
"e"
"."
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validNumber(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validNumber(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validNumber(self, s: str) -> bool:
        
```

### C

```c
bool validNumber(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidNumber(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var validNumber = function(s) {
    
};
```

### TypeScript

```typescript
function validNumber(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function validNumber($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validNumber(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validNumber(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validNumber(String s) {
    
  }
}
```

### Go

```golang
func validNumber(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def valid_number(s)
    
end
```

### Scala

```scala
object Solution {
    def validNumber(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_number(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (valid-number s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec valid_number(S :: unicode:unicode_binary()) -> boolean().
valid_number(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_number(s :: String.t) :: boolean
  def valid_number(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validNumber(s: String): Bool {

    }
}
```

