# 1208. 尽可能使字符串相等

## 题目描述

<p>给你两个长度相同的字符串，<code>s</code> 和 <code>t</code>。</p>

<p>将 <code>s</code> 中的第 <code>i</code> 个字符变到 <code>t</code> 中的第 <code>i</code> 个字符需要 <code>|s[i] - t[i]|</code> 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。</p>

<p>用于变更字符串的最大预算是 <code>maxCost</code>。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。</p>

<p>如果你可以将 <code>s</code> 的子字符串转化为它在 <code>t</code> 中对应的子字符串，则返回可以转化的最大长度。</p>

<p>如果 <code>s</code> 中没有子字符串可以转化成 <code>t</code> 中对应的子字符串，则返回 <code>0</code>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", t = "bcdf", maxCost = 3
<strong>输出：</strong>3
<strong>解释：</strong>s<strong> </strong>中的<strong> </strong>"abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", t = "cdef", maxCost = 3
<strong>输出：</strong>1
<strong>解释：</strong>s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为<code> 1。</code>
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", t = "acde", maxCost = 0
<strong>输出：</strong>1
<strong>解释：</strong>a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length, t.length <= 10^5</code></li>
	<li><code>0 <= maxCost <= 10^6</code></li>
	<li><code>s</code> 和 <code>t</code> 都只含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. Calculate the differences between s[i] and t[i].
2. Use a sliding window to track the longest valid substring.

## 示例

```
"abcd"
"bcdf"
3
"abcd"
"cdef"
3
"abcd"
"acde"
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        
    }
};
```

### Java

```java
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
```

### C

```c
int equalSubstring(char* s, char* t, int maxCost) {
    
}
```

### C#

```csharp
public class Solution {
    public int EqualSubstring(string s, string t, int maxCost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    
};
```

### TypeScript

```typescript
function equalSubstring(s: string, t: string, maxCost: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $maxCost
     * @return Integer
     */
    function equalSubstring($s, $t, $maxCost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func equalSubstring(_ s: String, _ t: String, _ maxCost: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun equalSubstring(s: String, t: String, maxCost: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int equalSubstring(String s, String t, int maxCost) {
    
  }
}
```

### Go

```golang
func equalSubstring(s string, t string, maxCost int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @param {Integer} max_cost
# @return {Integer}
def equal_substring(s, t, max_cost)
    
end
```

### Scala

```scala
object Solution {
    def equalSubstring(s: String, t: String, maxCost: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (equal-substring s t maxCost)
  (-> string? string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec equal_substring(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), MaxCost :: integer()) -> integer().
equal_substring(S, T, MaxCost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec equal_substring(s :: String.t, t :: String.t, max_cost :: integer) :: integer
  def equal_substring(s, t, max_cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func equalSubstring(s: String, t: String, maxCost: Int64): Int64 {

    }
}
```

