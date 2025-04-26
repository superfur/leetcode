# 2472. 不重叠回文子字符串的最大数目

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个 <strong>正</strong> 整数 <code>k</code> 。</p>

<p>从字符串 <code>s</code> 中选出一组满足下述条件且 <strong>不重叠</strong> 的子字符串：</p>

<ul>
	<li>每个子字符串的长度 <strong>至少</strong> 为 <code>k</code> 。</li>
	<li>每个子字符串是一个 <strong>回文串</strong> 。</li>
</ul>

<p>返回最优方案中能选择的子字符串的 <strong>最大</strong> 数目。</p>

<p><strong>子字符串</strong> 是字符串中一个连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre>
<strong>输入：</strong>s = "abaccdbbd", k = 3
<strong>输出：</strong>2
<strong>解释：</strong>可以选择 s = "<em><strong>aba</strong></em>cc<em><strong>dbbd</strong></em>" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<strong>输入：</strong>s = "adbcda", k = 2
<strong>输出：</strong>0
<strong>解释：</strong>字符串中不存在长度至少为 2 的回文子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 双指针
- 字符串
- 动态规划

## 提示

1. Try to use dynamic programming to solve the problem.
2. let dp[i] be the answer for the prefix s[0…i].
3. The final answer to the problem will be dp[n-1]. How do you compute this dp?

## 示例

```
"abaccdbbd"
3
"adbcda"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPalindromes(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPalindromes(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
```

### C

```c
int maxPalindromes(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPalindromes(string s, int k) {
        
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
var maxPalindromes = function(s, k) {
    
};
```

### TypeScript

```typescript
function maxPalindromes(s: string, k: number): number {
    
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
    function maxPalindromes($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPalindromes(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPalindromes(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPalindromes(String s, int k) {
    
  }
}
```

### Go

```golang
func maxPalindromes(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_palindromes(s, k)
    
end
```

### Scala

```scala
object Solution {
    def maxPalindromes(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_palindromes(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-palindromes s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_palindromes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_palindromes(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_palindromes(s :: String.t, k :: integer) :: integer
  def max_palindromes(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPalindromes(s: String, k: Int64): Int64 {

    }
}
```

