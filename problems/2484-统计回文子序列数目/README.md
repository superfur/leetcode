# 2484. 统计回文子序列数目

## 题目描述

<p>给你数字字符串&nbsp;<code>s</code>&nbsp;，请你返回&nbsp;<code>s</code>&nbsp;中长度为&nbsp;<code>5</code>&nbsp;的 <b>回文子序列</b>&nbsp;数目。由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p><strong>提示：</strong></p>

<ul>
	<li>如果一个字符串从前往后和从后往前读相同，那么它是 <strong>回文字符串</strong>&nbsp;。</li>
	<li>子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "103301"
<b>输出：</b>2
<b>解释：</b>
总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
它们中有两个（都是 "10301"）是回文的。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "0000000"
<b>输出：</b>21
<b>解释：</b>所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "9999900000"
<b>输出：</b>2
<b>解释：</b>仅有的两个回文子序列是 "99999" 和 "00000" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;只包含数字字符。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. There are 100 possibilities for the first two characters of the palindrome.
2. Iterate over all characters, letting the current character be the center of the palindrome.

## 示例

```
"103301"
"0000000"
"9999900000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPalindromes(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPalindromes(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPalindromes(self, s: str) -> int:
        
```

### C

```c
int countPalindromes(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPalindromes(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromes = function(s) {
    
};
```

### TypeScript

```typescript
function countPalindromes(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromes($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPalindromes(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPalindromes(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPalindromes(String s) {
    
  }
}
```

### Go

```golang
func countPalindromes(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_palindromes(s)
    
end
```

### Scala

```scala
object Solution {
    def countPalindromes(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_palindromes(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-palindromes s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_palindromes(S :: unicode:unicode_binary()) -> integer().
count_palindromes(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_palindromes(s :: String.t) :: integer
  def count_palindromes(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPalindromes(s: String): Int64 {

    }
}
```

