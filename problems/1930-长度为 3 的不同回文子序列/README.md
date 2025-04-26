# 1930. 长度为 3 的不同回文子序列

## 题目描述

<p>给你一个字符串 <code>s</code> ，返回 <code>s</code> 中 <strong>长度为 3 </strong>的<strong>不同回文子序列</strong> 的个数。</p>

<p>即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。</p>

<p><strong>回文</strong> 是正着读和反着读一样的字符串。</p>

<p><strong>子序列</strong> 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。</p>

<ul>
	<li>例如，<code>"ace"</code> 是 <code>"<strong><em>a</em></strong>b<strong><em>c</em></strong>d<strong><em>e</em></strong>"</code> 的一个子序列。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aabca"
<strong>输出：</strong>3
<strong>解释：</strong>长度为 3 的 3 个回文子序列分别是：
- "aba" ("<strong><em>a</em></strong>a<strong><em>b</em></strong>c<strong><em>a</em></strong>" 的子序列)
- "aaa" ("<strong><em>aa</em></strong>bc<strong><em>a</em></strong>" 的子序列)
- "aca" ("<strong><em>a</em></strong>ab<strong><em>ca</em></strong>" 的子序列)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "adc"
<strong>输出：</strong>0
<strong>解释：</strong>"adc" 不存在长度为 3 的回文子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "bbcbaba"
<strong>输出：</strong>4
<strong>解释：</strong>长度为 3 的 4 个回文子序列分别是：
- "bbb" ("<strong><em>bb</em></strong>c<strong><em>b</em></strong>aba" 的子序列)
- "bcb" ("<strong><em>b</em></strong>b<strong><em>cb</em></strong>aba" 的子序列)
- "bab" ("<strong><em>b</em></strong>bcb<strong><em>ab</em></strong>a" 的子序列)
- "aba" ("bbcb<strong><em>aba</em></strong>" 的子序列)
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 前缀和

## 提示

1. What is the maximum number of length-3 palindromic strings?
2. How can we keep track of the characters that appeared to the left of a given position?

## 示例

```
"aabca"
"adc"
"bbcbaba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPalindromicSubsequence(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
```

### C

```c
int countPalindromicSubsequence(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPalindromicSubsequence(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    
};
```

### TypeScript

```typescript
function countPalindromicSubsequence(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPalindromicSubsequence(String s) {
    
  }
}
```

### Go

```golang
func countPalindromicSubsequence(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_palindromic_subsequence(s)
    
end
```

### Scala

```scala
object Solution {
    def countPalindromicSubsequence(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-palindromic-subsequence s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_palindromic_subsequence(S :: unicode:unicode_binary()) -> integer().
count_palindromic_subsequence(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPalindromicSubsequence(s: String): Int64 {

    }
}
```

