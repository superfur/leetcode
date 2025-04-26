# 2030. 含特定字母的最小子序列

## 题目描述

<p>给你一个字符串 <code>s</code> ，一个整数 <code>k</code> ，一个字母 <code>letter</code> 以及另一个整数 <code>repetition</code> 。</p>

<p>返回 <code>s</code> 中长度为 <code>k</code> 且 <strong>字典序最小</strong> 的子序列，该子序列同时应满足字母 <code>letter</code> 出现<strong> 至少</strong> <code>repetition</code> 次。生成的测试用例满足 <code>letter</code> 在 <code>s</code> 中出现 <strong>至少</strong> <code>repetition</code> 次。</p>

<p><strong>子序列</strong> 是由原字符串删除一些（或不删除）字符且不改变剩余字符顺序得到的剩余字符串。</p>

<p>字符串 <code>a</code> 字典序比字符串 <code>b</code> 小的定义为：在 <code>a</code> 和 <code>b</code> 出现不同字符的第一个位置上，字符串 <code>a</code> 的字符在字母表中的顺序早于字符串 <code>b</code>&nbsp;的字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leet", k = 3, letter = "e", repetition = 1
<strong>输出：</strong>"eet"
<strong>解释：</strong>存在 4 个长度为 3 ，且满足字母 'e' 出现至少 1 次的子序列：
- "lee"（"<em><strong>lee</strong></em>t"）
- "let"（"<em><strong>le</strong></em>e<em><strong>t</strong></em>"）
- "let"（"<em><strong>l</strong></em>e<em><strong>et</strong></em>"）
- "eet"（"l<em><strong>eet</strong></em>"）
其中字典序最小的子序列是 "eet" 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="example-2" src="https://assets.leetcode.com/uploads/2021/09/13/smallest-k-length-subsequence.png" style="width: 339px; height: 67px;" /></p>

<pre>
<strong>输入：</strong>s = "leetcode", k = 4, letter = "e", repetition = 2
<strong>输出：</strong>"ecde"
<strong>解释：</strong>"ecde" 是长度为 4 且满足字母 "e" 出现至少 2 次的字典序最小的子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "bb", k = 2, letter = "b", repetition = 2
<strong>输出：</strong>"bb"
<strong>解释：</strong>"bb" 是唯一一个长度为 2 且满足字母 "b" 出现至少 2 次的子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= repetition &lt;= k &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>letter</code> 是一个小写英文字母，在 <code>s</code>&nbsp;中至少出现 <code>repetition</code> 次</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 字符串
- 单调栈

## 提示

1. Use stack. For every character to be appended, decide how many character(s) from the stack needs to get popped based on the stack length and the count of the required character.
2. Pop the extra characters out from the stack and return the characters in the stack (reversed).

## 示例

```
"leet"
3
"e"
1
"leetcode"
4
"e"
2
"bb"
2
"b"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestSubsequence(string s, int k, char letter, int repetition) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestSubsequence(String s, int k, char letter, int repetition) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        
```

### C

```c
char* smallestSubsequence(char* s, int k, char letter, int repetition) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestSubsequence(string s, int k, char letter, int repetition) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {character} letter
 * @param {number} repetition
 * @return {string}
 */
var smallestSubsequence = function(s, k, letter, repetition) {
    
};
```

### TypeScript

```typescript
function smallestSubsequence(s: string, k: number, letter: string, repetition: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param String $letter
     * @param Integer $repetition
     * @return String
     */
    function smallestSubsequence($s, $k, $letter, $repetition) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestSubsequence(_ s: String, _ k: Int, _ letter: Character, _ repetition: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestSubsequence(String s, int k, String letter, int repetition) {
    
  }
}
```

### Go

```golang
func smallestSubsequence(s string, k int, letter byte, repetition int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @param {Character} letter
# @param {Integer} repetition
# @return {String}
def smallest_subsequence(s, k, letter, repetition)
    
end
```

### Scala

```scala
object Solution {
    def smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_subsequence(s: String, k: i32, letter: char, repetition: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-subsequence s k letter repetition)
  (-> string? exact-integer? char? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec smallest_subsequence(S :: unicode:unicode_binary(), K :: integer(), Letter :: char(), Repetition :: integer()) -> unicode:unicode_binary().
smallest_subsequence(S, K, Letter, Repetition) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_subsequence(s :: String.t, k :: integer, letter :: char, repetition :: integer) :: String.t
  def smallest_subsequence(s, k, letter, repetition) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestSubsequence(s: String, k: Int64, letter: Rune, repetition: Int64): String {

    }
}
```

