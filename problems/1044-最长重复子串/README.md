# 1044. 最长重复子串

## 题目描述

<p>给你一个字符串 <code>s</code> ，考虑其所有 <em>重复子串</em> ：即&nbsp;<code>s</code> 的（连续）子串，在 <code>s</code> 中出现 2 次或更多次。这些出现之间可能存在重叠。</p>

<p>返回 <strong>任意一个</strong> 可能具有最长长度的重复子串。如果 <code>s</code> 不含重复子串，那么答案为 <code>""</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "banana"
<strong>输出：</strong>"ana"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd"
<strong>输出：</strong>""
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 二分查找
- 后缀数组
- 滑动窗口
- 哈希函数
- 滚动哈希

## 提示

1. Binary search for the length of the answer.  (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
2. To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

## 示例

```
"banana"
"abcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestDupSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestDupSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
```

### C

```c
char* longestDupSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestDupSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestDupSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function longestDupSubstring(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestDupSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestDupSubstring(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestDupSubstring(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestDupSubstring(String s) {
    
  }
}
```

### Go

```golang
func longestDupSubstring(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def longest_dup_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def longestDupSubstring(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_dup_substring(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-dup-substring s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec longest_dup_substring(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
longest_dup_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_dup_substring(s :: String.t) :: String.t
  def longest_dup_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestDupSubstring(s: String): String {

    }
}
```

