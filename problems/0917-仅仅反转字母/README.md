# 917. 仅仅反转字母

## 题目描述

<p>给你一个字符串 <code>s</code> ，根据下述规则反转字符串：</p>

<ul>
	<li>所有非英文字母保留在原有位置。</li>
	<li>所有英文字母（小写或大写）位置反转。</li>
</ul>

<p>返回反转后的 <code>s</code><em> 。</em></p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ab-cd"
<strong>输出：</strong>"dc-ba"
</pre>

<ol>
</ol>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a-bC-dEf-ghIj"
<strong>输出：</strong>"j-Ih-gfE-dCba"
</pre>

<ol>
</ol>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "Test1ng-Leet=code-Q!"
<strong>输出：</strong>"Qedo1ct-eeLg=ntse-T!"
</pre>

<p>&nbsp;</p>

<p><strong>提示</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由 ASCII 值在范围 <code>[33, 122]</code> 的字符组成</li>
	<li><code>s</code> 不含 <code>'\"'</code> 或 <code>'\\'</code></li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 提示

1. This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.

## 示例

```
"ab-cd"
"a-bC-dEf-ghIj"
"Test1ng-Leet=code-Q!"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reverseOnlyLetters(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String reverseOnlyLetters(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
```

### C

```c
char* reverseOnlyLetters(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReverseOnlyLetters(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    
};
```

### TypeScript

```typescript
function reverseOnlyLetters(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseOnlyLetters($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseOnlyLetters(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseOnlyLetters(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reverseOnlyLetters(String s) {
    
  }
}
```

### Go

```golang
func reverseOnlyLetters(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_only_letters(s)
    
end
```

### Scala

```scala
object Solution {
    def reverseOnlyLetters(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_only_letters(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-only-letters s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reverse_only_letters(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_only_letters(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_only_letters(s :: String.t) :: String.t
  def reverse_only_letters(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseOnlyLetters(s: String): String {

    }
}
```

