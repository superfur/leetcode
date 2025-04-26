# 1021. 删除最外层的括号

## 题目描述

<p>有效括号字符串为空 <code>""</code>、<code>"(" + A + ")"</code> 或 <code>A + B</code> ，其中 <code>A</code> 和 <code>B</code> 都是有效的括号字符串，<code>+</code> 代表字符串的连接。</p>

<ul>
	<li>例如，<code>""</code>，<code>"()"</code>，<code>"(())()"</code> 和 <code>"(()(()))"</code> 都是有效的括号字符串。</li>
</ul>

<p>如果有效字符串 <code>s</code> 非空，且不存在将其拆分为 <code>s = A + B</code> 的方法，我们称其为<strong>原语（primitive）</strong>，其中 <code>A</code> 和 <code>B</code> 都是非空有效括号字符串。</p>

<p>给出一个非空有效字符串 <code>s</code>，考虑将其进行原语化分解，使得：<code>s = P_1 + P_2 + ... + P_k</code>，其中 <code>P_i</code> 是有效括号字符串原语。</p>

<p>对 <code>s</code> 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 <code>s</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "(()())(())"
<strong>输出：</strong>"()()()"
<strong>解释：
</strong>输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(()())(())(()(()))"
<strong>输出：</strong>"()()()()(())"
<strong>解释：</strong>
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "()()"
<strong>输出：</strong>""
<strong>解释：</strong>
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'('</code> 或 <code>')'</code></li>
	<li><code>s</code> 是一个有效括号字符串</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串

## 提示

1. Can you find the primitive decomposition?  The number of ( and ) characters must be equal.

## 示例

```
"(()())(())"
"(()())(())(()(()))"
"()()"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeOuterParentheses(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeOuterParentheses(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
```

### C

```c
char* removeOuterParentheses(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveOuterParentheses(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    
};
```

### TypeScript

```typescript
function removeOuterParentheses(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeOuterParentheses($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeOuterParentheses(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeOuterParentheses(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeOuterParentheses(String s) {
    
  }
}
```

### Go

```golang
func removeOuterParentheses(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def remove_outer_parentheses(s)
    
end
```

### Scala

```scala
object Solution {
    def removeOuterParentheses(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-outer-parentheses s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec remove_outer_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_outer_parentheses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_outer_parentheses(s :: String.t) :: String.t
  def remove_outer_parentheses(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeOuterParentheses(s: String): String {

    }
}
```

