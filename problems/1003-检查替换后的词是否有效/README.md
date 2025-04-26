# 1003. 检查替换后的词是否有效

## 题目描述

给你一个字符串 <code>s</code> ，请你判断它是否 <strong>有效</strong> 。
<p>字符串 <code>s</code> <strong>有效</strong> 需要满足：假设开始有一个空字符串 <code>t = ""</code> ，你可以执行 <strong>任意次</strong> 下述操作将<strong> </strong><code>t</code><strong> 转换为 </strong><code>s</code> ：</p>

<ul>
	<li>将字符串 <code>"abc"</code> 插入到 <code>t</code> 中的任意位置。形式上，<code>t</code> 变为 <code>t<sub>left</sub> + "abc" + t<sub>right</sub></code>，其中 <code>t == t<sub>left</sub> + t<sub>right</sub></code> 。注意，<code>t<sub>left</sub></code> 和 <code>t<sub>right</sub></code> 可能为 <strong>空</strong> 。</li>
</ul>

<p>如果字符串 <code>s</code> 有效，则返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aabcbc"
<strong>输出：</strong>true
<strong>解释：</strong>
"" -&gt; "<strong>abc</strong>" -&gt; "a<strong>abc</strong>bc"
因此，"aabcbc" 有效。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcabcababcc"
<strong>输出：</strong>true
<strong>解释：</strong>
"" -&gt; "<strong>abc</strong>" -&gt; "abc<strong>abc</strong>" -&gt; "abcabc<strong>abc</strong>" -&gt; "abcabcab<strong>abc</strong>c"
因此，"abcabcababcc" 有效。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abccba"
<strong>输出：</strong>false
<strong>解释：</strong>执行操作无法得到 "abccba" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由字母 <code>'a'</code>、<code>'b'</code> 和 <code>'c'</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 示例

```
"aabcbc"
"abcabcababcc"
"abccba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isValid(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isValid(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        
```

### C

```c
bool isValid(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsValid(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
};
```

### TypeScript

```typescript
function isValid(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isValid(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isValid(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isValid(String s) {
    
  }
}
```

### Go

```golang
func isValid(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def is_valid(s)
    
end
```

### Scala

```scala
object Solution {
    def isValid(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_valid(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-valid s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_valid(S :: unicode:unicode_binary()) -> boolean().
is_valid(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isValid(s: String): Bool {

    }
}
```

