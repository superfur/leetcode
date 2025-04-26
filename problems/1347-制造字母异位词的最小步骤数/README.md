# 1347. 制造字母异位词的最小步骤数

## 题目描述

<p>给你两个长度相等的字符串&nbsp;<code>s</code> 和 <code>t</code>。每一个步骤中，你可以选择将&nbsp;<code>t</code>&nbsp;中的 <strong>任一字符</strong> 替换为 <strong>另一个字符</strong>。</p>

<p>返回使&nbsp;<code>t</code>&nbsp;成为&nbsp;<code>s</code>&nbsp;的字母异位词的最小步骤数。</p>

<p><strong>字母异位词</strong> 指字母相同，但排列不同（也可能相同）的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输出：</strong>s = &quot;bab&quot;, t = &quot;aba&quot;
<strong>输出：</strong>1
<strong>提示：</strong>用 &#39;b&#39; 替换 t 中的第一个 &#39;a&#39;，t = &quot;bba&quot; 是 s 的一个字母异位词。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>s = &quot;leetcode&quot;, t = &quot;practice&quot;
<strong>输出：</strong>5
<strong>提示：</strong>用合适的字符替换 t 中的 &#39;p&#39;, &#39;r&#39;, &#39;a&#39;, &#39;i&#39; 和 &#39;c&#39;，使 t 变成 s 的字母异位词。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输出：</strong>s = &quot;anagram&quot;, t = &quot;mangaar&quot;
<strong>输出：</strong>0
<strong>提示：</strong>&quot;anagram&quot; 和 &quot;mangaar&quot; 本身就是一组字母异位词。 
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输出：</strong>s = &quot;xxyyzz&quot;, t = &quot;xxyyzz&quot;
<strong>输出：</strong>0
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输出：</strong>s = &quot;friend&quot;, t = &quot;family&quot;
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50000</code></li>
	<li><code>s.length == t.length</code></li>
	<li><code>s</code> 和 <code>t</code>&nbsp;只包含小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Count the frequency of characters of each string.
2. Loop over all characters if the frequency of a character in t is less than the frequency of the same character in s then add the difference between the frequencies to the answer.

## 示例

```
"bab"
"aba"
"leetcode"
"practice"
"anagram"
"mangaar"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSteps(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSteps(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
```

### C

```c
int minSteps(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSteps(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    
};
```

### TypeScript

```typescript
function minSteps(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minSteps($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSteps(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSteps(String s, String t) {
    
  }
}
```

### Go

```golang
func minSteps(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def min_steps(s, t)
    
end
```

### Scala

```scala
object Solution {
    def minSteps(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-steps s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_steps(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
min_steps(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_steps(s :: String.t, t :: String.t) :: integer
  def min_steps(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSteps(s: String, t: String): Int64 {

    }
}
```

