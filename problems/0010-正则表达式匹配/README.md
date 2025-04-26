# 10. 正则表达式匹配

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个字符规律&nbsp;<code>p</code>，请你来实现一个支持 <code>'.'</code>&nbsp;和&nbsp;<code>'*'</code>&nbsp;的正则表达式匹配。</p>

<ul>
	<li><code>'.'</code> 匹配任意单个字符</li>
	<li><code>'*'</code> 匹配零个或多个前面的那一个元素</li>
</ul>

<p>所谓匹配，是要涵盖&nbsp;<strong>整个&nbsp;</strong>字符串&nbsp;<code>s</code> 的，而不是部分字符串。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "a"
<strong>输出：</strong>false
<strong>解释：</strong>"a" 无法匹配 "aa" 整个字符串。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "a*"
<strong>输出：</strong>true
<strong>解释：</strong>因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>s = "ab", p = ".*"
<strong>输出：</strong>true
<strong>解释：</strong>".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li><code>1 &lt;= p.length&nbsp;&lt;= 20</code></li>
	<li><code>s</code>&nbsp;只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母。</li>
	<li><code>p</code>&nbsp;只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母，以及字符&nbsp;<code>.</code>&nbsp;和&nbsp;<code>*</code>。</li>
	<li>保证每次出现字符&nbsp;<code>*</code> 时，前面都匹配到有效的字符</li>
</ul>


## 难度

Hard

## 标签

- 递归
- 字符串
- 动态规划

## 示例

```
"aa"
"a"
"aa"
"a*"
"ab"
".*"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isMatch(String s, String p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
```

### C

```c
bool isMatch(char* s, char* p) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsMatch(string s, string p) {
        
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
var isMatch = function(s, p) {
    
};
```

### TypeScript

```typescript
function isMatch(s: string, p: string): boolean {
    
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
    function isMatch($s, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isMatch(s: String, p: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isMatch(String s, String p) {
    
  }
}
```

### Go

```golang
func isMatch(s string, p string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    
end
```

### Scala

```scala
object Solution {
    def isMatch(s: String, p: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-match s p)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
is_match(S, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_match(s :: String.t, p :: String.t) :: boolean
  def is_match(s, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isMatch(s: String, p: String): Bool {

    }
}
```

