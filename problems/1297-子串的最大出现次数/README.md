# 1297. 子串的最大出现次数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code> ，请你返回满足以下条件且出现次数最大的&nbsp;<strong>任意</strong>&nbsp;子串的出现次数：</p>

<ul>
	<li>子串中不同字母的数目必须小于等于 <code>maxLetters</code> 。</li>
	<li>子串的长度必须大于等于&nbsp;<code>minSize</code> 且小于等于&nbsp;<code>maxSize</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;aababcaab&quot;, maxLetters = 2, minSize = 3, maxSize = 4
<strong>输出：</strong>2
<strong>解释：</strong>子串 &quot;aab&quot; 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaaa&quot;, maxLetters = 1, minSize = 3, maxSize = 3
<strong>输出：</strong>2
<strong>解释：</strong>子串 &quot;aaa&quot; 在原字符串中出现了 2 次，且它们有重叠部分。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;aabcabcab&quot;, maxLetters = 2, minSize = 2, maxSize = 3
<strong>输出：</strong>3
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcde&quot;, maxLetters = 2, minSize = 3, maxSize = 3
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= maxLetters &lt;= 26</code></li>
	<li><code>1 &lt;= minSize &lt;= maxSize &lt;= min(26, s.length)</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Check out the constraints, (maxSize <=26).
2. This means you can explore all substrings in O(n * 26).
3. Find the Maximum Number of Occurrences of a Substring with bruteforce.

## 示例

```
"aababcaab"
2
3
4
"aaaa"
1
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
```

### C

```c
int maxFreq(char* s, int maxLetters, int minSize, int maxSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxFreq(string s, int maxLetters, int minSize, int maxSize) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} maxLetters
 * @param {number} minSize
 * @param {number} maxSize
 * @return {number}
 */
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    
};
```

### TypeScript

```typescript
function maxFreq(s: string, maxLetters: number, minSize: number, maxSize: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $maxLetters
     * @param Integer $minSize
     * @param Integer $maxSize
     * @return Integer
     */
    function maxFreq($s, $maxLetters, $minSize, $maxSize) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxFreq(_ s: String, _ maxLetters: Int, _ minSize: Int, _ maxSize: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
    
  }
}
```

### Go

```golang
func maxFreq(s string, maxLetters int, minSize int, maxSize int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} max_letters
# @param {Integer} min_size
# @param {Integer} max_size
# @return {Integer}
def max_freq(s, max_letters, min_size, max_size)
    
end
```

### Scala

```scala
object Solution {
    def maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_freq(s: String, max_letters: i32, min_size: i32, max_size: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-freq s maxLetters minSize maxSize)
  (-> string? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_freq(S :: unicode:unicode_binary(), MaxLetters :: integer(), MinSize :: integer(), MaxSize :: integer()) -> integer().
max_freq(S, MaxLetters, MinSize, MaxSize) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_freq(s :: String.t, max_letters :: integer, min_size :: integer, max_size :: integer) :: integer
  def max_freq(s, max_letters, min_size, max_size) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxFreq(s: String, maxLetters: Int64, minSize: Int64, maxSize: Int64): Int64 {

    }
}
```

