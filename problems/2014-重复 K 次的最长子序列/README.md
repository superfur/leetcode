# 2014. 重复 K 次的最长子序列

## 题目描述

<p>给你一个长度为 <code>n</code> 的字符串 <code>s</code> ，和一个整数 <code>k</code> 。请你找出字符串 <code>s</code> 中 <strong>重复</strong> <code>k</code> 次的 <strong>最长子序列</strong> 。</p>

<p><strong>子序列</strong> 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。</p>

<p>如果&nbsp;<code>seq * k</code> 是 <code>s</code> 的一个子序列，其中 <code>seq * k</code> 表示一个由 <code>seq</code> 串联 <code>k</code>&nbsp;次构造的字符串，那么就称 <code>seq</code><strong> </strong>是字符串 <code>s</code> 中一个 <strong>重复 <code>k</code> 次</strong> 的子序列。</p>

<ul>
	<li>举个例子，<code>"bba"</code> 是字符串 <code>"bababcba"</code> 中的一个重复 <code>2</code> 次的子序列，因为字符串 <code>"bbabba"</code> 是由 <code>"bba"</code> 串联 <code>2</code> 次构造的，而&nbsp;<code>"bbabba"</code> 是字符串 <code>"<em><strong>b</strong></em>a<em><strong>bab</strong></em>c<em><strong>ba</strong></em>"</code> 的一个子序列。</li>
</ul>

<p>返回字符串 <code>s</code> 中 <strong>重复 k 次的最长子序列</strong>&nbsp; 。如果存在多个满足的子序列，则返回 <strong>字典序最大</strong> 的那个。如果不存在这样的子序列，返回一个 <strong>空</strong> 字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="example 1" src="https://assets.leetcode.com/uploads/2021/08/30/longest-subsequence-repeat-k-times.png" style="width: 457px; height: 99px;" /></p>

<pre>
<strong>输入：</strong>s = "letsleetcode", k = 2
<strong>输出：</strong>"let"
<strong>解释：</strong>存在两个最长子序列重复 2 次：let" 和 "ete" 。
"let" 是其中字典序最大的一个。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "bb", k = 2
<strong>输出：</strong>"b"
<strong>解释：</strong>重复 2 次的最长子序列是 "b" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "ab", k = 2
<strong>输出：</strong>""
<strong>解释：</strong>不存在重复 2 次的最长子序列。返回空字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>2 &lt;= k &lt;= 2000</code></li>
	<li><code>2 &lt;= n &lt; k * 8</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 字符串
- 回溯
- 计数
- 枚举

## 提示

1. The length of the longest subsequence does not exceed n/k. Do you know why?
2. Find the characters that could be included in the potential answer. A character occurring more than or equal to k times can be used in the answer up to (count of the character / k) times.
3. Try all possible candidates in reverse lexicographic order, and check the string for the subsequence condition.

## 示例

```
"letsleetcode"
2
"bb"
2
"ab"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestSubsequenceRepeatedK(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
```

### C

```c
char* longestSubsequenceRepeatedK(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestSubsequenceRepeatedK(string s, int k) {
        
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
var longestSubsequenceRepeatedK = function(s, k) {
    
};
```

### TypeScript

```typescript
function longestSubsequenceRepeatedK(s: string, k: number): string {
    
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
    function longestSubsequenceRepeatedK($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubsequenceRepeatedK(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubsequenceRepeatedK(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestSubsequenceRepeatedK(String s, int k) {
    
  }
}
```

### Go

```golang
func longestSubsequenceRepeatedK(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def longest_subsequence_repeated_k(s, k)
    
end
```

### Scala

```scala
object Solution {
    def longestSubsequenceRepeatedK(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subsequence_repeated_k(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subsequence-repeated-k s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec longest_subsequence_repeated_k(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
longest_subsequence_repeated_k(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence_repeated_k(s :: String.t, k :: integer) :: String.t
  def longest_subsequence_repeated_k(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubsequenceRepeatedK(s: String, k: Int64): String {

    }
}
```

