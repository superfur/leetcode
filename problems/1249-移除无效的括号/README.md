# 1249. 移除无效的括号

## 题目描述

<p>给你一个由 <code>'('</code>、<code>')'</code> 和小写字母组成的字符串 <code>s</code>。</p>

<p>你需要从字符串中删除最少数目的 <code>'('</code> 或者 <code>')'</code>&nbsp;（可以删除任意位置的括号)，使得剩下的「括号字符串」有效。</p>

<p>请返回任意一个合法字符串。</p>

<p>有效「括号字符串」应当符合以下&nbsp;<strong>任意一条&nbsp;</strong>要求：</p>

<ul>
	<li>空字符串或只包含小写字母的字符串</li>
	<li>可以被写作&nbsp;<code>AB</code>（<code>A</code>&nbsp;连接&nbsp;<code>B</code>）的字符串，其中&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都是有效「括号字符串」</li>
	<li>可以被写作&nbsp;<code>(A)</code>&nbsp;的字符串，其中&nbsp;<code>A</code>&nbsp;是一个有效的「括号字符串」</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "lee(t(c)o)de)"
<strong>输出：</strong>"lee(t(c)o)de"
<strong>解释：</strong>"lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a)b(c)d"
<strong>输出：</strong>"ab(c)d"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "))(("
<strong>输出：</strong>""
<strong>解释：</strong>空字符串也是有效的
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;可能是&nbsp;<code>'('</code>、<code>')'</code>&nbsp;或英文小写字母</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 提示

1. Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.
2. Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.

## 示例

```
"lee(t(c)o)de)"
"a)b(c)d"
"))(("
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String minRemoveToMakeValid(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
```

### C

```c
char* minRemoveToMakeValid(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinRemoveToMakeValid(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    
};
```

### TypeScript

```typescript
function minRemoveToMakeValid(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function minRemoveToMakeValid($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minRemoveToMakeValid(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minRemoveToMakeValid(String s) {
    
  }
}
```

### Go

```golang
func minRemoveToMakeValid(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def min_remove_to_make_valid(s)
    
end
```

### Scala

```scala
object Solution {
    def minRemoveToMakeValid(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (min-remove-to-make-valid s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec min_remove_to_make_valid(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_remove_to_make_valid(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_remove_to_make_valid(s :: String.t) :: String.t
  def min_remove_to_make_valid(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minRemoveToMakeValid(s: String): String {

    }
}
```

