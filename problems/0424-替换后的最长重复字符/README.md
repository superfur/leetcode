# 424. 替换后的最长重复字符

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 <code>k</code> 次。</p>

<p>在执行上述操作后，返回 <em>包含相同字母的最长子字符串的长度。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ABAB", k = 2
<strong>输出：</strong>4
<strong>解释：</strong>用两个'A'替换为两个'B',反之亦然。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "AABABBA", k = 1
<strong>输出：</strong>4
<strong>解释：</strong>
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
可能存在其他的方法来得到同样的结果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由大写英文字母组成</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 示例

```
"ABAB"
2
"AABABBA"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int characterReplacement(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
```

### C

```c
int characterReplacement(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CharacterReplacement(string s, int k) {
        
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
var characterReplacement = function(s, k) {
    
};
```

### TypeScript

```typescript
function characterReplacement(s: string, k: number): number {
    
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
    function characterReplacement($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func characterReplacement(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int characterReplacement(String s, int k) {
    
  }
}
```

### Go

```golang
func characterReplacement(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def character_replacement(s, k)
    
end
```

### Scala

```scala
object Solution {
    def characterReplacement(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (character-replacement s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec character_replacement(S :: unicode:unicode_binary(), K :: integer()) -> integer().
character_replacement(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec character_replacement(s :: String.t, k :: integer) :: integer
  def character_replacement(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func characterReplacement(s: String, k: Int64): Int64 {

    }
}
```

