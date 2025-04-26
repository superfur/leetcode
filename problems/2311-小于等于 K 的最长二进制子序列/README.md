# 2311. 小于等于 K 的最长二进制子序列

## 题目描述

<p>给你一个二进制字符串&nbsp;<code>s</code>&nbsp;和一个正整数&nbsp;<code>k</code>&nbsp;。</p>

<p>请你返回 <code>s</code>&nbsp;的 <strong>最长</strong>&nbsp;子序列，且该子序列对应的 <strong>二进制</strong>&nbsp;数字小于等于 <code>k</code>&nbsp;。</p>

<p>注意：</p>

<ul>
	<li>子序列可以有 <strong>前导 0</strong>&nbsp;。</li>
	<li>空字符串视为&nbsp;<code>0</code>&nbsp;。</li>
	<li><strong>子序列</strong>&nbsp;是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "1001010", k = 5
<b>输出：</b>5
<b>解释：</b>s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
最长子序列的长度为 5 ，所以返回 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "00101001", k = 1
<b>输出：</b>6
<b>解释：</b>"000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
最长子序列的长度为 6 ，所以返回 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> 要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code> 。</li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 记忆化搜索
- 字符串
- 动态规划

## 提示

1. Choosing a subsequence from the string is equivalent to deleting all the other digits.
2. If you were to remove a digit, which one should you remove to reduce the value of the string?

## 示例

```
"1001010"
5
"00101001"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubsequence(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubsequence(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
```

### C

```c
int longestSubsequence(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubsequence(string s, int k) {
        
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
var longestSubsequence = function(s, k) {
    
};
```

### TypeScript

```typescript
function longestSubsequence(s: string, k: number): number {
    
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
    function longestSubsequence($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubsequence(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubsequence(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubsequence(String s, int k) {
    
  }
}
```

### Go

```golang
func longestSubsequence(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_subsequence(s, k)
    
end
```

### Scala

```scala
object Solution {
    def longestSubsequence(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subsequence(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subsequence s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_subsequence(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_subsequence(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence(s :: String.t, k :: integer) :: integer
  def longest_subsequence(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubsequence(s: String, k: Int64): Int64 {

    }
}
```

