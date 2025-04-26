# 316. 去除重复字母

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 <strong>返回结果的<span data-keyword="lexicographically-smaller-string-alien">字典序</span>最小</strong>（要求不能打乱其他字符的相对位置）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>s = "bcabc"</code>
<strong>输出<code>：</code></strong><code>"abc"</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>s = "cbacdcbc"</code>
<strong>输出：</strong><code>"acdb"</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>该题与 1081 <a href="https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters">https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters</a> 相同</p>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串
- 单调栈

## 提示

1. Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

## 示例

```
"bcabc"
"cbacdcbc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeDuplicateLetters(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
```

### C

```c
char* removeDuplicateLetters(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveDuplicateLetters(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    
};
```

### TypeScript

```typescript
function removeDuplicateLetters(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeDuplicateLetters($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeDuplicateLetters(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeDuplicateLetters(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeDuplicateLetters(String s) {
    
  }
}
```

### Go

```golang
func removeDuplicateLetters(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def remove_duplicate_letters(s)
    
end
```

### Scala

```scala
object Solution {
    def removeDuplicateLetters(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-duplicate-letters s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec remove_duplicate_letters(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_duplicate_letters(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_duplicate_letters(s :: String.t) :: String.t
  def remove_duplicate_letters(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeDuplicateLetters(s: String): String {

    }
}
```

