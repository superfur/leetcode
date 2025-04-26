# 1910. 删除一个字符串中所有出现的给定子字符串

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>part</code> ，请你对 <code>s</code> 反复执行以下操作直到 <b>所有</b> 子字符串 <code>part</code> 都被删除：</p>

<ul>
	<li>找到 <code>s</code> 中 <strong>最左边</strong> 的子字符串 <code>part</code> ，并将它从 <code>s</code> 中删除。</li>
</ul>

<p>请你返回从 <code>s</code> 中删除所有 <code>part</code> 子字符串以后得到的剩余字符串。</p>

<p>一个 <strong>子字符串</strong> 是一个字符串中连续的字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "daabcbaabcbc", part = "abc"
<b>输出：</b>"dab"
<b>解释：</b>以下操作按顺序执行：
- s = "da<strong>abc</strong>baabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。
- s = "daba<strong>abc</strong>bc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。
- s = "dab<strong>abc</strong>" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。
此时 s 中不再含有子字符串 "abc" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "axxxxyyyyb", part = "xy"
<b>输出：</b>"ab"
<b>解释：</b>以下操作按顺序执行：
- s = "axxx<strong>xy</strong>yyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。
- s = "axx<strong>xy</strong>yyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。
- s = "ax<strong>xy</strong>yb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。
- s = "a<strong>xy</strong>b" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。
此时 s 中不再含有子字符串 "xy" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= part.length &lt;= 1000</code></li>
	<li><code>s</code>​​​​​​ 和 <code>part</code> 只包小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串
- 模拟

## 提示

1. Note that a new occurrence of pattern can appear if you remove an old one, For example, s = "ababcc" and pattern = "abc".
2. You can maintain a stack of characters and if the last character of the pattern size in the stack match the pattern remove them

## 示例

```
"daabcbaabcbc"
"abc"
"axxxxyyyyb"
"xy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeOccurrences(string s, string part) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeOccurrences(String s, String part) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
```

### C

```c
char* removeOccurrences(char* s, char* part) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveOccurrences(string s, string part) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    
};
```

### TypeScript

```typescript
function removeOccurrences(s: string, part: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $part
     * @return String
     */
    function removeOccurrences($s, $part) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeOccurrences(_ s: String, _ part: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeOccurrences(s: String, part: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeOccurrences(String s, String part) {
    
  }
}
```

### Go

```golang
func removeOccurrences(s string, part string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} part
# @return {String}
def remove_occurrences(s, part)
    
end
```

### Scala

```scala
object Solution {
    def removeOccurrences(s: String, part: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-occurrences s part)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec remove_occurrences(S :: unicode:unicode_binary(), Part :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_occurrences(S, Part) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_occurrences(s :: String.t, part :: String.t) :: String.t
  def remove_occurrences(s, part) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeOccurrences(s: String, part: String): String {

    }
}
```

