# 730. 统计不同回文子序列

## 题目描述

<p>给你一个字符串 <code>s</code> ，返回 <code>s</code>&nbsp;中不同的非空回文子序列个数 。由于答案可能很大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>字符串的子序列可以经由字符串删除 0 个或多个字符获得。</p>

<p>如果一个序列与它反转后的序列一致，那么它是回文序列。</p>

<p>如果存在某个 <code>i</code> , 满足&nbsp;<code>a<sub>i</sub>&nbsp;!= b<sub>i</sub></code><sub>&nbsp;</sub>，则两个序列&nbsp;<code>a<sub>1</sub>, a<sub>2</sub>, ...</code>&nbsp;和&nbsp;<code>b<sub>1</sub>, b<sub>2</sub>, ...</code>&nbsp;不同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = 'bccb'
<strong>输出：</strong>6
<strong>解释：</strong>6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
<strong>输出：</strong>104860361
<strong>解释：</strong>共有 3104860382 个不同的非空回文子序列，104860361 是对 10<sup>9</sup> + 7 取余后的值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code>&nbsp;仅包含&nbsp;<code>'a'</code>,&nbsp;<code>'b'</code>,&nbsp;<code>'c'</code>&nbsp;或&nbsp;<code>'d'</code>&nbsp;</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Let dp(i, j) be the answer for the string T = S[i:j+1] including the empty sequence. The answer is the number of unique characters in T, plus palindromes of the form "a_a", "b_b", "c_c", and "d_d", where "_" represents zero or more characters.

## 示例

```
"bccb"
"abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPalindromicSubsequences(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPalindromicSubsequences(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        
```

### C

```c
int countPalindromicSubsequences(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPalindromicSubsequences(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequences = function(s) {
    
};
```

### TypeScript

```typescript
function countPalindromicSubsequences(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequences($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPalindromicSubsequences(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPalindromicSubsequences(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPalindromicSubsequences(String s) {
    
  }
}
```

### Go

```golang
func countPalindromicSubsequences(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def count_palindromic_subsequences(s)
    
end
```

### Scala

```scala
object Solution {
    def countPalindromicSubsequences(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_palindromic_subsequences(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-palindromic-subsequences s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_palindromic_subsequences(S :: unicode:unicode_binary()) -> integer().
count_palindromic_subsequences(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_palindromic_subsequences(s :: String.t) :: integer
  def count_palindromic_subsequences(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPalindromicSubsequences(s: String): Int64 {

    }
}
```

