# 2663. 字典序最小的美丽字符串

## 题目描述

<p>如果一个字符串满足以下条件，则称其为 <strong>美丽字符串</strong> ：</p>

<ul>
	<li>它由英语小写字母表的前 <code>k</code> 个字母组成。</li>
	<li>它不包含任何长度为 <code>2</code> 或更长的回文子字符串。</li>
</ul>

<p>给你一个长度为 <code>n</code> 的美丽字符串 <code>s</code> 和一个正整数 <code>k</code> 。</p>

<p>请你找出并返回一个长度为 <code>n</code> 的美丽字符串，该字符串还满足：在字典序大于 <code>s</code> 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。</p>

<p>对于长度相同的两个字符串 <code>a</code> 和 <code>b</code> ，如果字符串 <code>a</code> 在与字符串 <code>b</code> 不同的第一个位置上的字符字典序更大，则字符串 <code>a</code> 的字典序大于字符串 <code>b</code> 。</p>

<ul>
	<li>例如，<code>"abcd"</code> 的字典序比 <code>"abcc"</code> 更大，因为在不同的第一个位置（第四个字符）上 <code>d</code> 的字典序大于 <code>c</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcz", k = 26
<strong>输出：</strong>"abda"
<strong>解释：</strong>字符串 "abda" 既是美丽字符串，又满足字典序大于 "abcz" 。
可以证明不存在字符串同时满足字典序大于 "abcz"、美丽字符串、字典序小于 "abda" 这三个条件。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "dc", k = 4
<strong>输出：</strong>""
<strong>解释：</strong>可以证明，不存在既是美丽字符串，又字典序大于 "dc" 的字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>4 &lt;= k &lt;= 26</code></li>
	<li><code>s</code> 是一个美丽字符串</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 字符串

## 提示

1. If the string does not contain any palindromic substrings of lengths 2 and 3, then the string does not contain any palindromic substrings at all.
2. Iterate from right to left and if it is possible to increase character at index i without creating any palindromic substrings of lengths 2 and 3, then increase it.
3. After increasing the character at index i, set every character after index i equal to character a. With this, we will ensure that we have created a lexicographically larger string than s, which does not contain any palindromes before index i and is lexicographically the smallest.
4. Finally, we are just left with a case to fix palindromic substrings, which come after index i. This can be done with a similar method mentioned in the second hint.

## 示例

```
"abcz"
26
"dc"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestBeautifulString(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestBeautifulString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        
```

### C

```c
char* smallestBeautifulString(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestBeautifulString(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var smallestBeautifulString = function(s, k) {
    
};
```

### TypeScript

```typescript
function smallestBeautifulString(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function smallestBeautifulString($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestBeautifulString(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestBeautifulString(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestBeautifulString(String s, int k) {
    
  }
}
```

### Go

```golang
func smallestBeautifulString(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_beautiful_string(s, k)
    
end
```

### Scala

```scala
object Solution {
    def smallestBeautifulString(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_beautiful_string(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-beautiful-string s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec smallest_beautiful_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
smallest_beautiful_string(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_beautiful_string(s :: String.t, k :: integer) :: String.t
  def smallest_beautiful_string(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestBeautifulString(s: String, k: Int64): String {

    }
}
```

