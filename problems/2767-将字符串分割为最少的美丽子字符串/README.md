# 2767. 将字符串分割为最少的美丽子字符串

## 题目描述

<p>给你一个二进制字符串&nbsp;<code>s</code>&nbsp;，你需要将字符串分割成一个或者多个&nbsp;<strong>子字符串</strong>&nbsp;&nbsp;，使每个子字符串都是 <strong>美丽</strong>&nbsp;的。</p>

<p>如果一个字符串满足以下条件，我们称它是 <strong>美丽</strong>&nbsp;的：</p>

<ul>
	<li>它不包含前导 0 。</li>
	<li>它是 <code>5</code>&nbsp;的幂的 <strong>二进制</strong>&nbsp;表示。</li>
</ul>

<p>请你返回分割后的子字符串的 <strong>最少</strong>&nbsp;数目。如果无法将字符串&nbsp;<code>s</code>&nbsp;分割成美丽子字符串，请你返回 <code>-1</code>&nbsp;。</p>

<p>子字符串是一个字符串中一段连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "1011"
<b>输出：</b>2
<b>解释：</b>我们可以将输入字符串分成 ["101", "1"] 。
- 字符串 "101" 不包含前导 0 ，且它是整数 5<sup>1</sup> = 5 的二进制表示。
- 字符串 "1" 不包含前导 0 ，且它是整数 5<sup>0</sup> = 1 的二进制表示。
最少可以将 s 分成 2 个美丽子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "111"
<b>输出：</b>3
<b>解释：</b>我们可以将输入字符串分成 ["1", "1", "1"] 。
- 字符串 "1" 不包含前导 0 ，且它是整数 5<sup>0</sup> = 1 的二进制表示。
最少可以将 s 分成 3 个美丽子字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "0"
<b>输出：</b>-1
<b>解释：</b>无法将给定字符串分成任何美丽子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'0'</code>&nbsp;要么是&nbsp;<code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 动态规划
- 回溯

## 提示

1. To check if number x is a power of 5 or not, we will divide x by 5 while x > 1 and x mod 5 == 0. After iteration if x == 1, then it was a power of 5.
2. Since the constraint of s.length is small, we can use recursion to find all the partitions.

## 示例

```
"1011"
"111"
"0"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumBeautifulSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        
```

### C

```c
int minimumBeautifulSubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumBeautifulSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumBeautifulSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function minimumBeautifulSubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumBeautifulSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumBeautifulSubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumBeautifulSubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumBeautifulSubstrings(String s) {
    
  }
}
```

### Go

```golang
func minimumBeautifulSubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_beautiful_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumBeautifulSubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_beautiful_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-beautiful-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_beautiful_substrings(S :: unicode:unicode_binary()) -> integer().
minimum_beautiful_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_beautiful_substrings(s :: String.t) :: integer
  def minimum_beautiful_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumBeautifulSubstrings(s: String): Int64 {

    }
}
```

