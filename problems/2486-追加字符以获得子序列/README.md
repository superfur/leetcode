# 2486. 追加字符以获得子序列

## 题目描述

<p>给你两个仅由小写英文字母组成的字符串 <code>s</code> 和 <code>t</code> 。</p>

<p>现在需要通过向 <code>s</code> 末尾追加字符的方式使 <code>t</code> 变成 <code>s</code> 的一个 <strong>子序列</strong> ，返回需要追加的最少字符数。</p>

<p>子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "coaching", t = "coding"
<strong>输出：</strong>4
<strong>解释：</strong>向 s 末尾追加字符串 "ding" ，s = "coachingding" 。
现在，t 是 s ("<em><strong>co</strong></em>aching<em><strong>ding</strong></em>") 的一个子序列。
可以证明向 s 末尾追加任何 3 个字符都无法使 t 成为 s 的一个子序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcde", t = "a"
<strong>输出：</strong>0
<strong>解释：</strong>t 已经是 s ("<em><strong>a</strong></em>bcde") 的一个子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "z", t = "abcde"
<strong>输出：</strong>5
<strong>解释：</strong>向 s 末尾追加字符串 "abcde" ，s = "zabcde" 。
现在，t 是 s ("z<em><strong>abcde</strong></em>") 的一个子序列。 
可以证明向 s 末尾追加任何 4 个字符都无法使 t 成为 s 的一个子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 双指针
- 字符串

## 提示

1. Find the longest prefix of t that is a subsequence of s.
2. Use two variables to keep track of your location in s and t. If the characters match, increment both variables. Otherwise, only increment the variable for s.
3. The remaining characters in t must be appended to the end of s.

## 示例

```
"coaching"
"coding"
"abcde"
"a"
"z"
"abcde"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int appendCharacters(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int appendCharacters(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
```

### C

```c
int appendCharacters(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int AppendCharacters(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    
};
```

### TypeScript

```typescript
function appendCharacters(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function appendCharacters($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func appendCharacters(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun appendCharacters(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int appendCharacters(String s, String t) {
    
  }
}
```

### Go

```golang
func appendCharacters(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def append_characters(s, t)
    
end
```

### Scala

```scala
object Solution {
    def appendCharacters(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (append-characters s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec append_characters(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
append_characters(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec append_characters(s :: String.t, t :: String.t) :: integer
  def append_characters(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func appendCharacters(s: String, t: String): Int64 {

    }
}
```

