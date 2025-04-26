# 1190. 反转每对括号间的子串

## 题目描述

<p>给出一个字符串&nbsp;<code>s</code>（仅含有小写英文字母和括号）。</p>

<p>请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。</p>

<p>注意，您的结果中 <strong>不应</strong> 包含任何括号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "(abcd)"
<strong>输出：</strong>"dcba"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(u(love)i)"
<strong>输出：</strong>"iloveu"
<strong>解释：</strong>先反转子字符串 "love" ，然后反转整个字符串。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "(ed(et(oc))el)"
<strong>输出：</strong>"leetcode"
<strong>解释：</strong>先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> 中只有小写英文字母和括号</li>
	<li>题目测试用例确保所有括号都是成对出现的</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 提示

1. Find all brackets in the string.
2. Does the order of the reverse matter ?
3. The order does not matter.

## 示例

```
"(abcd)"
"(u(love)i)"
"(ed(et(oc))el)"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reverseParentheses(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String reverseParentheses(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
```

### C

```c
char* reverseParentheses(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReverseParentheses(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function(s) {
    
};
```

### TypeScript

```typescript
function reverseParentheses(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseParentheses($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseParentheses(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseParentheses(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reverseParentheses(String s) {
    
  }
}
```

### Go

```golang
func reverseParentheses(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_parentheses(s)
    
end
```

### Scala

```scala
object Solution {
    def reverseParentheses(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-parentheses s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reverse_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_parentheses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_parentheses(s :: String.t) :: String.t
  def reverse_parentheses(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseParentheses(s: String): String {

    }
}
```

