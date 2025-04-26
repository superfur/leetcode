# 844. 比较含退格的字符串

## 题目描述

<p>给定 <code>s</code> 和 <code>t</code> 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 <code>true</code> 。<code>#</code> 代表退格字符。</p>

<p><strong>注意：</strong>如果对空文本输入退格字符，文本继续为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ab#c", t = "ad#c"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 "ac"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ab##", t = "c#d#"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 ""。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a#c", t = "b"
<strong>输出：</strong>false
<strong>解释：</strong>s 会变成 "c"，但 t 仍然是 "b"。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 200</code></li>
	<li><code>s</code> 和 <code>t</code> 只含有小写字母以及字符 <code>'#'</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以用 <code>O(n)</code> 的时间复杂度和 <code>O(1)</code> 的空间复杂度解决该问题吗？</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 双指针
- 字符串
- 模拟

## 示例

```
"ab#c"
"ad#c"
"ab##"
"c#d#"
"a#c"
"b"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean backspaceCompare(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
```

### C

```c
bool backspaceCompare(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public bool BackspaceCompare(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    
};
```

### TypeScript

```typescript
function backspaceCompare(s: string, t: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function backspaceCompare($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func backspaceCompare(_ s: String, _ t: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun backspaceCompare(s: String, t: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool backspaceCompare(String s, String t) {
    
  }
}
```

### Go

```golang
func backspaceCompare(s string, t string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    
end
```

### Scala

```scala
object Solution {
    def backspaceCompare(s: String, t: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (backspace-compare s t)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec backspace_compare(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
backspace_compare(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec backspace_compare(s :: String.t, t :: String.t) :: boolean
  def backspace_compare(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func backspaceCompare(s: String, t: String): Bool {

    }
}
```

