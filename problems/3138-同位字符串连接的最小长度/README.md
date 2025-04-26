# 3138. 同位字符串连接的最小长度

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它由某个字符串&nbsp;<code>t</code>&nbsp;和若干&nbsp;<code>t</code>&nbsp; 的&nbsp;<strong>同位字符串</strong>&nbsp;连接而成。</p>

<p>请你返回字符串 <code>t</code>&nbsp;的 <strong>最小</strong>&nbsp;可能长度。</p>

<p><strong>同位字符串</strong>&nbsp;指的是重新排列一个字符串的字母得到的另外一个字符串。例如，"aab"，"aba" 和 "baa" 是 "aab" 的同位字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abba"</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>一个可能的字符串&nbsp;<code>t</code>&nbsp;为&nbsp;<code>"ba"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "cdef"</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>一个可能的字符串&nbsp;<code>t</code>&nbsp;为&nbsp;<code>"cdef"</code>&nbsp;，注意&nbsp;<code>t</code>&nbsp;可能等于&nbsp;<code>s</code>&nbsp;。</p>

<p><strong class="example">示例</strong><strong>&nbsp;3：</strong></p>

<p><strong>输入：</strong>s = "abcbcacabbaccba"</p>

<p><b>输出：</b>3</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. The answer should be a divisor of <code>s.length</code>.
2. Check each candidate naively.

## 示例

```
"abba"
"cdef"
"abcbcacabbaccba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minAnagramLength(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minAnagramLength(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minAnagramLength(self, s: str) -> int:
        
```

### C

```c
int minAnagramLength(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinAnagramLength(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minAnagramLength = function(s) {
    
};
```

### TypeScript

```typescript
function minAnagramLength(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minAnagramLength($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAnagramLength(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAnagramLength(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minAnagramLength(String s) {
    
  }
}
```

### Go

```golang
func minAnagramLength(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_anagram_length(s)
    
end
```

### Scala

```scala
object Solution {
    def minAnagramLength(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_anagram_length(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-anagram-length s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_anagram_length(S :: unicode:unicode_binary()) -> integer().
min_anagram_length(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_anagram_length(s :: String.t) :: integer
  def min_anagram_length(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAnagramLength(s: String): Int64 {

    }
}
```

