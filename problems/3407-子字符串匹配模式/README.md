# 3407. 子字符串匹配模式

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个模式字符串&nbsp;<code>p</code>&nbsp;，其中&nbsp;<code>p</code> <strong>恰好</strong>&nbsp;包含 <strong>一个</strong>&nbsp;<code>'*'</code>&nbsp;符号。</p>

<p><code>p</code>&nbsp;中的 <code>'*'</code>&nbsp;符号可以被替换为零个或多个字符组成的任意字符序列。</p>

<p>如果 <code>p</code>&nbsp;可以变成 <code>s</code>&nbsp;的 <span data-keyword="substring-nonempty">子字符串</span>，那么返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "leetcode", p = "ee*e"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><b>解释：</b></p>

<p>将&nbsp;<code>'*'</code>&nbsp;替换为&nbsp;<code>"tcod"</code>&nbsp;，子字符串&nbsp;<code>"eetcode"</code>&nbsp;匹配模式串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "car", p = "c*v"</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><strong>解释：</strong></p>

<p>不存在匹配模式串的子字符串。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "luck", p = "u*"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><b>解释：</b></p>

<p>子字符串&nbsp;<code>"u"</code>&nbsp;，<code>"uc"</code>&nbsp;和&nbsp;<code>"uck"</code>&nbsp;都匹配模式串。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= p.length &lt;= 50 </code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>p</code>&nbsp;只包含小写英文字母和一个&nbsp;<code>'*'</code> 符号。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 字符串匹配

## 提示

1. Divide the pattern in two strings and search in the string.

## 示例

```
"leetcode"
"ee*e"
"car"
"c*v"
"luck"
"u*"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasMatch(string s, string p) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasMatch(String s, String p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        
```

### C

```c
bool hasMatch(char* s, char* p) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasMatch(string s, string p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var hasMatch = function(s, p) {
    
};
```

### TypeScript

```typescript
function hasMatch(s: string, p: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function hasMatch($s, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasMatch(_ s: String, _ p: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasMatch(s: String, p: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasMatch(String s, String p) {
    
  }
}
```

### Go

```golang
func hasMatch(s string, p string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @return {Boolean}
def has_match(s, p)
    
end
```

### Scala

```scala
object Solution {
    def hasMatch(s: String, p: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_match(s: String, p: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-match s p)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec has_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
has_match(S, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_match(s :: String.t, p :: String.t) :: boolean
  def has_match(s, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasMatch(s: String, p: String): Bool {

    }
}
```

