# 1960. 两个回文子字符串长度的最大乘积

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;，你需要找到两个 <strong>不重叠</strong><strong>的回文&nbsp;</strong>子字符串，它们的长度都必须为 <strong>奇数</strong>&nbsp;，使得它们长度的乘积最大。</p>

<p>更正式地，你想要选择四个整数&nbsp;<code>i</code>&nbsp;，<code>j</code>&nbsp;，<code>k</code>&nbsp;，<code>l</code>&nbsp;，使得&nbsp;<code>0 &lt;= i &lt;= j &lt; k &lt;= l &lt; s.length</code>&nbsp;，且子字符串&nbsp;<code>s[i...j]</code> 和&nbsp;<code>s[k...l]</code>&nbsp;都是回文串且长度为奇数。<code>s[i...j]</code>&nbsp;表示下标从 <code>i</code>&nbsp;到 <code>j</code>&nbsp;且 <strong>包含</strong>&nbsp;两端下标的子字符串。</p>

<p>请你返回两个不重叠回文子字符串长度的 <strong>最大</strong>&nbsp;乘积。</p>

<p><strong>回文字符串</strong>&nbsp;指的是一个从前往后读和从后往前读一模一样的字符串。<strong>子字符串</strong>&nbsp;指的是一个字符串中一段连续字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "ababbb"
<b>输出：</b>9
<b>解释：</b>子字符串 "aba" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "zaaaxbbby"
<b>输出：</b>9
<b>解释：</b>子字符串 "aaa" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 哈希函数
- 滚动哈希

## 提示

1. You can use Manacher's algorithm to get the maximum palindromic substring centered at each index
2. After using Manacher's for each center use a line sweep from the center to the left and from the center to the right to find for each index the farthest center to it with distance ≤ palin[center]
3. After that, find the maximum palindrome size for each prefix in the string and for each suffix and the answer would be max(prefix[i] * suffix[i + 1])

## 示例

```
"ababbb"
"zaaaxbbby"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxProduct(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxProduct(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProduct(self, s: str) -> int:
        
```

### C

```c
long long maxProduct(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxProduct(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    
};
```

### TypeScript

```typescript
function maxProduct(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProduct(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProduct(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProduct(String s) {
    
  }
}
```

### Go

```golang
func maxProduct(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_product(s)
    
end
```

### Scala

```scala
object Solution {
    def maxProduct(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-product s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_product(S :: unicode:unicode_binary()) -> integer().
max_product(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product(s :: String.t) :: integer
  def max_product(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProduct(s: String): Int64 {

    }
}
```

