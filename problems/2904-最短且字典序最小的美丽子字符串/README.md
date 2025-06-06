# 2904. 最短且字典序最小的美丽子字符串

## 题目描述

<p>给你一个二进制字符串 <code>s</code> 和一个正整数 <code>k</code> 。</p>

<p>如果 <code>s</code> 的某个子字符串中 <code>1</code> 的个数恰好等于 <code>k</code> ，则称这个子字符串是一个 <strong>美丽子字符串</strong> 。</p>

<p>令 <code>len</code> 等于 <strong>最短</strong> 美丽子字符串的长度。</p>

<p>返回长度等于 <code>len</code> 且字典序 <strong>最小</strong> 的美丽子字符串。如果 <code>s</code> 中不含美丽子字符串，则返回一个 <strong>空</strong> 字符串。</p>

<p>对于相同长度的两个字符串 <code>a</code> 和 <code>b</code> ，如果在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置上，<code>a</code> 中该位置上的字符严格大于 <code>b</code> 中的对应字符，则认为字符串 <code>a</code> 字典序 <strong>大于</strong> 字符串 <code>b</code> 。</p>

<ul>
	<li>例如，<code>"abcd"</code> 的字典序大于 <code>"abcc"</code> ，因为两个字符串出现不同的第一个位置对应第四个字符，而 <code>d</code> 大于 <code>c</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "100011001", k = 3
<strong>输出：</strong>"11001"
<strong>解释：</strong>示例中共有 7 个美丽子字符串：
1. 子字符串 "<u>100011</u>001" 。
2. 子字符串 "<u>1000110</u>01" 。
3. 子字符串 "<u>10001100</u>1" 。
4. 子字符串 "1<u>00011001</u>" 。
5. 子字符串 "10<u>0011001</u>" 。
6. 子字符串 "100<u>011001</u>" 。
7. 子字符串 "1000<u>11001</u>" 。
最短美丽子字符串的长度是 5 。
长度为 5 且字典序最小的美丽子字符串是子字符串 "11001" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "1011", k = 2
<strong>输出：</strong>"11"
<strong>解释：</strong>示例中共有 3 个美丽子字符串：
1. 子字符串 "<u>101</u>1" 。
2. 子字符串 "1<u>011</u>" 。
3. 子字符串 "10<u>11</u>" 。
最短美丽子字符串的长度是 2 。
长度为 2 且字典序最小的美丽子字符串是子字符串 "11" 。 
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "000", k = 1
<strong>输出：</strong>""
<strong>解释：</strong>示例中不存在美丽子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 滑动窗口

## 提示

1. Notice that if we consider that index <code>i</code> is the leftmost index of a beautiful substring, it has only one candidate <code>j</code>, such that <code>s[i:j]</code> is beautiful and shortest too.
2. We can iterate over all possibilities of leftmost index <code>i</code> take <code>s[i:j]</code> and compare with the shortest and the lexicographically smallest beautiful string we could get before index <code>i</code>.

## 示例

```
"100011001"
3
"1011"
2
"000"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
```

### C

```c
char* shortestBeautifulSubstring(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShortestBeautifulSubstring(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var shortestBeautifulSubstring = function(s, k) {
    
};
```

### TypeScript

```typescript
function shortestBeautifulSubstring(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function shortestBeautifulSubstring($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestBeautifulSubstring(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestBeautifulSubstring(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shortestBeautifulSubstring(String s, int k) {
    
  }
}
```

### Go

```golang
func shortestBeautifulSubstring(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def shortest_beautiful_substring(s, k)
    
end
```

### Scala

```scala
object Solution {
    def shortestBeautifulSubstring(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-beautiful-substring s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec shortest_beautiful_substring(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
shortest_beautiful_substring(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_beautiful_substring(s :: String.t, k :: integer) :: String.t
  def shortest_beautiful_substring(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestBeautifulSubstring(s: String, k: Int64): String {

    }
}
```

