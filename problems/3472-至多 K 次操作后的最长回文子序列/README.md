# 3472. 至多 K 次操作后的最长回文子序列

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>在一次操作中，你可以将任意位置的字符替换为字母表中相邻的字符（字母表是循环的，因此&nbsp;<code>'z'</code>&nbsp;的下一个字母是&nbsp;<code>'a'</code>）。例如，将 <code>'a'</code> 替换为下一个字母结果是 <code>'b'</code>，将 <code>'a'</code> 替换为上一个字母结果是 <code>'z'</code>；同样，将 <code>'z'</code> 替换为下一个字母结果是 <code>'a'</code>，替换为上一个字母结果是 <code>'y'</code>。</p>

<p>返回在进行&nbsp;<strong>最多</strong> <code>k</code> 次操作后，<code>s</code> 的&nbsp;<strong>最长回文子序列&nbsp;</strong>的长度。</p>

<p><strong>子序列&nbsp;</strong>是一个&nbsp;<strong>非空&nbsp;</strong>字符串，可以通过删除原字符串中的某些字符（或不删除任何字符）并保持剩余字符的相对顺序得到。</p>

<p><strong>回文&nbsp;</strong>是正着读和反着读都相同的字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "abced", k = 2</span></p>

<p><strong>输出:</strong> <span class="example-io">3</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>将 <code>s[1]</code> 替换为下一个字母，得到 <code>"acced"</code>。</li>
	<li>将 <code>s[4]</code> 替换为上一个字母，得到 <code>"accec"</code>。</li>
</ul>

<p>子序列 <code>"ccc"</code> 形成一个长度为 3 的回文，这是最长的回文子序列。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "aaazzz", k = 4</span></p>

<p><strong>输出:</strong> 6</p>

<p><strong>解释:</strong></p>

<ul>
	<li>将 <code>s[0]</code> 替换为上一个字母，得到 <code>"zaazzz"</code>。</li>
	<li>将 <code>s[4]</code> 替换为下一个字母，得到 <code>"zaazaz"</code>。</li>
	<li>将 <code>s[3]</code> 替换为下一个字母，得到 <code>"zaaaaz"</code>。</li>
</ul>

<p>整个字符串形成一个长度为 6 的回文。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= 200</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 提示

1. Use dynamic programming.
2. <code>dp[i][j][k]</code> is the length of the longest palindromic subsequence in substring <code>[i..j]</code> with cost at most <code>k</code>.
3. <code>dp[i][j][k] = max(dp[i + 1][j][k], dp[i][j - 1][k], dp[i + 1][j - 1][k - dist(s[i], s[j])] + 2)</code>, where <code>dist(x, y)</code> is the minimum cyclic distance between <code>x</code> and <code>y</code>.

## 示例

```
"abced"
2
"aaazzz"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestPalindromicSubsequence(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestPalindromicSubsequence(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        
```

### C

```c
int longestPalindromicSubsequence(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestPalindromicSubsequence(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestPalindromicSubsequence = function(s, k) {
    
};
```

### TypeScript

```typescript
function longestPalindromicSubsequence(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function longestPalindromicSubsequence($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPalindromicSubsequence(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPalindromicSubsequence(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestPalindromicSubsequence(String s, int k) {
    
  }
}
```

### Go

```golang
func longestPalindromicSubsequence(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_palindromic_subsequence(s, k)
    
end
```

### Scala

```scala
object Solution {
    def longestPalindromicSubsequence(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_palindromic_subsequence(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-palindromic-subsequence s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_palindromic_subsequence(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_palindromic_subsequence(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_palindromic_subsequence(s :: String.t, k :: integer) :: integer
  def longest_palindromic_subsequence(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPalindromicSubsequence(s: String, k: Int64): Int64 {

    }
}
```

