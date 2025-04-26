# 2272. 最大波动的子字符串

## 题目描述

<p>字符串的 <strong>波动</strong>&nbsp;定义为子字符串中出现次数 <strong>最多</strong>&nbsp;的字符次数与出现次数 <strong>最少</strong>&nbsp;的字符次数之差。</p>

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它只包含小写英文字母。请你返回 <code>s</code>&nbsp;里所有 <strong>子字符串的</strong>&nbsp;<strong>最大波动</strong>&nbsp;值。</p>

<p><strong>子字符串</strong> 是一个字符串的一段连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "aababbb"
<b>输出：</b>3
<strong>解释：</strong>
所有可能的波动值和它们对应的子字符串如以下所示：
- 波动值为 0 的子字符串："a" ，"aa" ，"ab" ，"abab" ，"aababb" ，"ba" ，"b" ，"bb" 和 "bbb" 。
- 波动值为 1 的子字符串："aab" ，"aba" ，"abb" ，"aabab" ，"ababb" ，"aababbb" 和 "bab" 。
- 波动值为 2 的子字符串："aaba" ，"ababbb" ，"abbb" 和 "babb" 。
- 波动值为 3 的子字符串 "babbb" 。
所以，最大可能波动值为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "abcde"
<b>输出：</b>0
<strong>解释：</strong>
s 中没有字母出现超过 1 次，所以 s 中每个子字符串的波动值都是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp; 只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Think about how to solve the problem if the string had only two distinct characters.
2. If we replace all occurrences of the first character by +1 and those of the second character by -1, can we efficiently calculate the largest possible variance of a string with only two distinct characters?
3. Now, try finding the optimal answer by taking all possible pairs of characters into consideration.

## 示例

```
"aababbb"
"abcde"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestVariance(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestVariance(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestVariance(self, s: str) -> int:
        
```

### C

```c
int largestVariance(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestVariance(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var largestVariance = function(s) {
    
};
```

### TypeScript

```typescript
function largestVariance(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function largestVariance($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestVariance(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestVariance(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestVariance(String s) {
    
  }
}
```

### Go

```golang
func largestVariance(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def largest_variance(s)
    
end
```

### Scala

```scala
object Solution {
    def largestVariance(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-variance s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_variance(S :: unicode:unicode_binary()) -> integer().
largest_variance(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_variance(s :: String.t) :: integer
  def largest_variance(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestVariance(s: String): Int64 {

    }
}
```

