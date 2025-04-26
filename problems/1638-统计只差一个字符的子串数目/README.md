# 1638. 统计只差一个字符的子串数目

## 题目描述

<p>给你两个字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;，请你找出 <code>s</code>&nbsp;中的非空子串的数目，这些子串满足替换 <strong>一个不同字符</strong>&nbsp;以后，是 <code>t</code>&nbsp;串的子串。换言之，请你找到 <code>s</code>&nbsp;和 <code>t</code>&nbsp;串中 <strong>恰好</strong>&nbsp;只有一个字符不同的子字符串对的数目。</p>

<p>比方说，&nbsp;<code>"<u>compute</u>r"</code>&nbsp;and&nbsp;<code>"<u>computa</u>tion"&nbsp;</code>只有一个字符不同：&nbsp;<code>'e'</code>/<code>'a'</code>&nbsp;，所以这一对子字符串会给答案加 1 。</p>

<p>请你返回满足上述条件的不同子字符串对数目。</p>

<p>一个 <strong>子字符串</strong>&nbsp;是一个字符串中连续的字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "aba", t = "baba"
<b>输出：</b>6
<strong>解释：</strong>以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("<strong>a</strong>ba", "<strong>b</strong>aba")
("<strong>a</strong>ba", "ba<strong>b</strong>a")
("ab<strong>a</strong>", "<strong>b</strong>aba")
("ab<strong>a</strong>", "ba<strong>b</strong>a")
("a<strong>b</strong>a", "b<strong>a</strong>ba")
("a<strong>b</strong>a", "bab<strong>a</strong>")
加粗部分分别表示 s 和 t 串选出来的子字符串。
</pre>
<strong>示例 2：</strong>

<pre>
<b>输入：</b>s = "ab", t = "bb"
<b>输出：</b>3
<strong>解释：</strong>以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("<strong>a</strong>b", "<strong>b</strong>b")
("<strong>a</strong>b", "b<strong>b</strong>")
("<strong>ab</strong>", "<strong>bb</strong>")
加粗部分分别表示 s 和 t 串选出来的子字符串。
</pre>
<strong>示例 3：</strong>

<pre>
<b>输入：</b>s = "a", t = "a"
<b>输出：</b>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>s = "abe", t = "bbc"
<b>输出：</b>10
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 100</code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 动态规划
- 枚举

## 提示

1. Take every substring of s, change a character, and see how many substrings of t match that substring.
2. Use a Trie to store all substrings of t as a dictionary.

## 示例

```
"aba"
"baba"
"ab"
"bb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubstrings(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubstrings(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
```

### C

```c
int countSubstrings(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubstrings(string s, string t) {
        
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
var countSubstrings = function(s, t) {
    
};
```

### TypeScript

```typescript
function countSubstrings(s: string, t: string): number {
    
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
    function countSubstrings($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubstrings(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubstrings(String s, String t) {
    
  }
}
```

### Go

```golang
func countSubstrings(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def count_substrings(s, t)
    
end
```

### Scala

```scala
object Solution {
    def countSubstrings(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_substrings(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-substrings s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_substrings(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
count_substrings(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t, t :: String.t) :: integer
  def count_substrings(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubstrings(s: String, t: String): Int64 {

    }
}
```

