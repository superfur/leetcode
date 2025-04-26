# 76. 最小覆盖子串

## 题目描述

<p>给你一个字符串 <code>s</code> 、一个字符串 <code>t</code> 。返回 <code>s</code> 中涵盖 <code>t</code> 所有字符的最小子串。如果 <code>s</code> 中不存在涵盖 <code>t</code> 所有字符的子串，则返回空字符串 <code>""</code> 。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>对于 <code>t</code> 中重复字符，我们寻找的子字符串中该字符数量必须不少于 <code>t</code> 中该字符数量。</li>
	<li>如果 <code>s</code> 中存在这样的子串，我们保证它是唯一的答案。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ADOBECODEBANC", t = "ABC"
<strong>输出：</strong>"BANC"
<strong>解释：</strong>最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a", t = "a"
<strong>输出：</strong>"a"
<strong>解释：</strong>整个字符串 s 是最小覆盖子串。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> s = "a", t = "aa"
<strong>输出:</strong> ""
<strong>解释:</strong> t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code><sup>m == s.length</sup></code></li>
	<li><code><sup>n == t.length</sup></code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<p>&nbsp;</p>
<strong>进阶：</strong>你能设计一个在 <code>o(m+n)</code> 时间内解决此问题的算法吗？

## 难度

Hard

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Use two pointers to create a window of letters in s, which would have all the characters from t.
2. Expand the right pointer until all the characters of t are covered.
3. Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
4. Continue expanding the right and left pointers until you reach the end of s.

## 示例

```
"ADOBECODEBANC"
"ABC"
"a"
"a"
"a"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public String minWindow(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
```

### C

```c
char* minWindow(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinWindow(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    
};
```

### TypeScript

```typescript
function minWindow(s: string, t: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function minWindow($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minWindow(s: String, t: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minWindow(String s, String t) {
    
  }
}
```

### Go

```golang
func minWindow(s string, t string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    
end
```

### Scala

```scala
object Solution {
    def minWindow(s: String, t: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (min-window s t)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec min_window(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_window(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_window(s :: String.t, t :: String.t) :: String.t
  def min_window(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minWindow(s: String, t: String): String {

    }
}
```

