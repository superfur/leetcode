# 2800. 包含三个字符串的最短字符串

## 题目描述

给你三个字符串&nbsp;<code>a</code>&nbsp;，<code>b</code>&nbsp;和&nbsp;<code>c</code>&nbsp;， 你的任务是找到长度&nbsp;<strong>最短</strong>&nbsp;的字符串，且这三个字符串都是它的 <strong>子字符串</strong>&nbsp;。
<p>如果有多个这样的字符串，请你返回 <strong>字典序最小</strong>&nbsp;的一个。</p>

<p>请你返回满足题目要求的字符串。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>两个长度相同的字符串 <code>a</code>&nbsp;和 <code>b</code>&nbsp;，如果在第一个不相同的字符处，<code>a</code>&nbsp;的字母在字母表中比 <code>b</code>&nbsp;的字母 <strong>靠前</strong>&nbsp;，那么字符串&nbsp;<code>a</code>&nbsp;比字符串&nbsp;<code>b</code> <strong>字典序小</strong>&nbsp;。</li>
	<li><strong>子字符串</strong>&nbsp;是一个字符串中一段连续的字符序列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><code><span style=""><b>输入：</b></span>a</code> = "abc", <code>b</code> = "bca", <code>c</code> = "aaa"
<b>输出：</b>"aaabca"
<b>解释：</b>字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2] 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。</pre>

<p><strong>示例 2：</strong></p>

<pre><code><span style=""><b>输入：</b></span>a</code> = "ab", <code>b</code> = "ba", <code>c</code> = "aba"
<b>输出：</b>"aba"
<strong>解释：</strong>字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length, c.length &lt;= 100</code></li>
	<li><code>a</code>&nbsp;，<code>b</code>&nbsp;，<code>c</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 枚举

## 提示

1. Think about how you can generate all possible strings that contain all three input strings as substrings. Can you come up with an efficient algorithm to do this?
2. Check all permutations of the words a, b, and c. For each permutation, begin by appending some letters to the end of the first word to form the second word. Then, proceed to add more letters to generate the third word.

## 示例

```
"abc"
"bca"
"aaa"
"ab"
"ba"
"aba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minimumString(string a, string b, string c) {
        
    }
};
```

### Java

```java
class Solution {
    public String minimumString(String a, String b, String c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
```

### C

```c
char* minimumString(char* a, char* b, char* c) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinimumString(string a, string b, string c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @param {string} c
 * @return {string}
 */
var minimumString = function(a, b, c) {
    
};
```

### TypeScript

```typescript
function minimumString(a: string, b: string, c: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @param String $c
     * @return String
     */
    function minimumString($a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumString(_ a: String, _ b: String, _ c: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumString(a: String, b: String, c: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minimumString(String a, String b, String c) {
    
  }
}
```

### Go

```golang
func minimumString(a string, b string, c string) string {
    
}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @param {String} c
# @return {String}
def minimum_string(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def minimumString(a: String, b: String, c: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_string(a: String, b: String, c: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-string a b c)
  (-> string? string? string? string?)
  )
```

### Erlang

```erlang
-spec minimum_string(A :: unicode:unicode_binary(), B :: unicode:unicode_binary(), C :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimum_string(A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_string(a :: String.t, b :: String.t, c :: String.t) :: String.t
  def minimum_string(a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumString(a: String, b: String, c: String): String {

    }
}
```

