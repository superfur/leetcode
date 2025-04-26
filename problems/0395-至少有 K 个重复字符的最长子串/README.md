# 395. 至少有 K 个重复字符的最长子串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> ，请你找出 <code>s</code> 中的最长子串，&nbsp;要求该子串中的每一字符出现次数都不少于 <code>k</code> 。返回这一子串的长度。</p>

<p data-pm-slice="1 1 []">如果不存在这样的子字符串，则返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabb", k = 3
<strong>输出：</strong>3
<strong>解释：</strong>最长子串为 "aaa" ，其中 'a' 重复了 3 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ababbc", k = 2
<strong>输出：</strong>5
<strong>解释：</strong>最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 分治
- 滑动窗口

## 示例

```
"aaabb"
3
"ababbc"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubstring(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubstring(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
```

### C

```c
int longestSubstring(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubstring(string s, int k) {
        
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
var longestSubstring = function(s, k) {
    
};
```

### TypeScript

```typescript
function longestSubstring(s: string, k: number): number {
    
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
    function longestSubstring($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubstring(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubstring(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubstring(String s, int k) {
    
  }
}
```

### Go

```golang
func longestSubstring(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_substring(s, k)
    
end
```

### Scala

```scala
object Solution {
    def longestSubstring(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_substring(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-substring s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_substring(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_substring(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_substring(s :: String.t, k :: integer) :: integer
  def longest_substring(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubstring(s: String, k: Int64): Int64 {

    }
}
```

