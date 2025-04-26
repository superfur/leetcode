# 1143. 最长公共子序列

## 题目描述

<p>给定两个字符串 <code>text1</code> 和 <code>text2</code>，返回这两个字符串的最长 <strong>公共子序列</strong> 的长度。如果不存在 <strong>公共子序列</strong> ，返回 <code>0</code> 。</p>

<p>一个字符串的 <strong>子序列</strong><em> </em>是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。</p>

<ul>
	<li>例如，<code>"ace"</code> 是 <code>"abcde"</code> 的子序列，但 <code>"aec"</code> 不是 <code>"abcde"</code> 的子序列。</li>
</ul>

<p>两个字符串的 <strong>公共子序列</strong> 是这两个字符串所共同拥有的子序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>text1 = "abcde", text2 = "ace" 
<strong>输出：</strong>3  
<strong>解释：</strong>最长公共子序列是 "ace" ，它的长度为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>text1 = "abc", text2 = "abc"
<strong>输出：</strong>3
<strong>解释：</strong>最长公共子序列是 "abc" ，它的长度为 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>text1 = "abc", text2 = "def"
<strong>输出：</strong>0
<strong>解释：</strong>两个字符串没有公共子序列，返回 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= text1.length, text2.length <= 1000</code></li>
	<li><code>text1</code> 和 <code>text2</code> 仅由小写英文字符组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 提示

1. Try dynamic programming. 
DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
2. DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j]
DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

## 示例

```
"abcde"
"ace"
"abc"
"abc"
"abc"
"def"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
```

### C

```c
int longestCommonSubsequence(char* text1, char* text2) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    
};
```

### TypeScript

```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text1
     * @param String $text2
     * @return Integer
     */
    function longestCommonSubsequence($text1, $text2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestCommonSubsequence(text1: String, text2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestCommonSubsequence(String text1, String text2) {
    
  }
}
```

### Go

```golang
func longestCommonSubsequence(text1 string, text2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
    
end
```

### Scala

```scala
object Solution {
    def longestCommonSubsequence(text1: String, text2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-common-subsequence text1 text2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_common_subsequence(Text1 :: unicode:unicode_binary(), Text2 :: unicode:unicode_binary()) -> integer().
longest_common_subsequence(Text1, Text2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_common_subsequence(text1 :: String.t, text2 :: String.t) :: integer
  def longest_common_subsequence(text1, text2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestCommonSubsequence(text1: String, text2: String): Int64 {

    }
}
```

