# 65. 有效数字

## 题目描述

<p>给定一个字符串&nbsp;<code>s</code>&nbsp;，返回&nbsp;<code>s</code>&nbsp;是否是一个 <strong>有效数字</strong>。</p>

<p>例如，下面的都是有效数字：<code>"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"</code>，而接下来的不是：<code>"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"</code>。</p>

<p>一般的，一个 <strong>有效数字</strong>&nbsp;可以用以下的规则之一定义：</p>

<ol>
	<li>一个 <strong>整数</strong> 后面跟着一个 <strong>可选指数</strong>。</li>
	<li>一个 <strong>十进制数</strong> 后面跟着一个&nbsp;<strong>可选指数</strong>。</li>
</ol>

<p>一个 <strong>整数</strong> 定义为一个&nbsp;<strong>可选符号</strong>&nbsp;<code>'-'</code>&nbsp;或&nbsp;<code>'+'</code>&nbsp;后面跟着 <strong>数字</strong>。</p>

<p>一个 <strong>十进制数</strong>&nbsp;定义为一个&nbsp;<strong>可选符号&nbsp;</strong><code>'-'</code>&nbsp;或&nbsp;<code>'+'</code>&nbsp;后面跟着下述规则：</p>

<ol>
	<li><strong>数字&nbsp;</strong>后跟着一个 <strong>小数点&nbsp;<code>.</code></strong>。</li>
	<li><strong>数字&nbsp;</strong>后跟着一个 <strong>小数点&nbsp;<code>.</code>&nbsp;</strong>再跟着<strong> 数位</strong>。</li>
	<li>一个 <strong>小数点&nbsp;<code>.</code>&nbsp;</strong>后跟着<strong> 数位</strong>。</li>
</ol>

<p><strong>指数</strong> 定义为指数符号 <code>'e'</code> 或 <code>'E'</code>，后面跟着一个 <b>整数</b>。</p>

<p><strong>数字</strong>&nbsp;定义为一个或多个数位。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "0"</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "e"</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "."</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> 仅含英文字母（大写和小写），数字（<code>0-9</code>），加号 <code>'+'</code> ，减号 <code>'-'</code> ，或者点 <code>'.'</code> 。</li>
</ul>


## 难度

Hard

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
    bool isNumber(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isNumber(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isNumber(self, s: str) -> bool:
        
```

### C

```c
bool isNumber(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsNumber(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    
};
```

### TypeScript

```typescript
function isNumber(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isNumber($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isNumber(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isNumber(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isNumber(String s) {
    
  }
}
```

### Go

```golang
func isNumber(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def is_number(s)
    
end
```

### Scala

```scala
object Solution {
    def isNumber(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_number(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-number s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_number(S :: unicode:unicode_binary()) -> boolean().
is_number(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_number(s :: String.t) :: boolean
  def is_number(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isNumber(s: String): Bool {

    }
}
```

