# 828. 统计子串中的唯一字符

## 题目描述

<p>我们定义了一个函数 <code>countUniqueChars(s)</code> 来统计字符串 <code>s</code> 中的唯一字符，并返回唯一字符的个数。</p>

<p>例如：<code>s = "LEETCODE"</code> ，则其中 <code>"L"</code>, <code>"T"</code>,<code>"C"</code>,<code>"O"</code>,<code>"D"</code> 都是唯一字符，因为它们只出现一次，所以 <code>countUniqueChars(s) = 5</code> 。</p>

<p>本题将会给你一个字符串 <code>s</code> ，我们需要返回 <code>countUniqueChars(t)</code> 的总和，其中 <code>t</code> 是 <code>s</code> 的子字符串。输入用例保证返回值为&nbsp;32 位整数。</p>

<p>注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 <code>s</code> 的所有子字符串中的唯一字符）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入: </strong>s = "ABC"
<strong>输出: </strong>10
<strong>解释:</strong> 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入: </strong>s = "ABA"
<strong>输出: </strong>8
<strong>解释: </strong>除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "LEETCODE"
<strong>输出：</strong>92
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 只包含大写英文字符</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 动态规划

## 示例

```
"ABC"
"ABA"
"LEETCODE"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniqueLetterString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int uniqueLetterString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
```

### C

```c
int uniqueLetterString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int UniqueLetterString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var uniqueLetterString = function(s) {
    
};
```

### TypeScript

```typescript
function uniqueLetterString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function uniqueLetterString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniqueLetterString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniqueLetterString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int uniqueLetterString(String s) {
    
  }
}
```

### Go

```golang
func uniqueLetterString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def unique_letter_string(s)
    
end
```

### Scala

```scala
object Solution {
    def uniqueLetterString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unique-letter-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec unique_letter_string(S :: unicode:unicode_binary()) -> integer().
unique_letter_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_letter_string(s :: String.t) :: integer
  def unique_letter_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniqueLetterString(s: String): Int64 {

    }
}
```

