# 2609. 最长平衡子字符串

## 题目描述

<p>给你一个仅由 <code>0</code> 和 <code>1</code> 组成的二进制字符串 <code>s</code> 。<span style="">&nbsp;</span><span style="">&nbsp;</span></p>

<p>如果子字符串中 <strong>所有的<span style=""> </span></strong><code><span style="">0</span></code><strong><span style=""> </span>都在 </strong><code>1</code><strong> 之前</strong> 且其中 <code>0</code> 的数量等于 <code>1</code> 的数量，则认为 <code>s</code> 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。<span style="">&nbsp;</span></p>

<p>返回&nbsp;<span style=""> </span><code>s</code> 中最长的平衡子字符串长度。</p>

<p>子字符串是字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "01000111"
<strong>输出：</strong>6
<strong>解释：</strong>最长的平衡子字符串是 "000111" ，长度为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "00111"
<strong>输出：</strong>4
<strong>解释：</strong>最长的平衡子字符串是 "0011" ，长度为 <span style="">&nbsp;</span>4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "111"
<strong>输出：</strong>0
<strong>解释：</strong>除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>'0' &lt;= s[i] &lt;= '1'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Consider iterating over each subarray and checking if it’s balanced or not.
2. Among all balanced subarrays, the answer is the longest one of them.

## 示例

```
"01000111"
"00111"
"111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
```

### C

```c
int findTheLongestBalancedSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindTheLongestBalancedSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestBalancedSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function findTheLongestBalancedSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function findTheLongestBalancedSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTheLongestBalancedSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTheLongestBalancedSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findTheLongestBalancedSubstring(String s) {
    
  }
}
```

### Go

```golang
func findTheLongestBalancedSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def find_the_longest_balanced_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def findTheLongestBalancedSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_the_longest_balanced_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-the-longest-balanced-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_the_longest_balanced_substring(S :: unicode:unicode_binary()) -> integer().
find_the_longest_balanced_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_the_longest_balanced_substring(s :: String.t) :: integer
  def find_the_longest_balanced_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTheLongestBalancedSubstring(s: String): Int64 {

    }
}
```

