# 2182. 构造限制重复的字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>repeatLimit</code> ，用 <code>s</code> 中的字符构造一个新字符串 <code>repeatLimitedString</code> ，使任何字母 <strong>连续</strong> 出现的次数都不超过 <code>repeatLimit</code> 次。你不必使用 <code>s</code> 中的全部字符。</p>

<p>返回 <strong>字典序最大的</strong><em> </em><code>repeatLimitedString</code> 。</p>

<p>如果在字符串 <code>a</code> 和 <code>b</code> 不同的第一个位置，字符串 <code>a</code> 中的字母在字母表中出现时间比字符串 <code>b</code> 对应的字母晚，则认为字符串 <code>a</code> 比字符串 <code>b</code> <strong>字典序更大</strong> 。如果字符串中前 <code>min(a.length, b.length)</code> 个字符都相同，那么较长的字符串字典序更大。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "cczazcc", repeatLimit = 3
<strong>输出：</strong>"zzcccac"
<strong>解释：</strong>使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "aababab", repeatLimit = 2
<strong>输出：</strong>"bbabaa"
<strong>解释：</strong>
使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
字母 'a' 连续出现至多 2 次。 
字母 'b' 连续出现至多 2 次。 
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= repeatLimit &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 计数
- 堆（优先队列）

## 提示

1. Start constructing the string in descending order of characters.
2. When repeatLimit is reached, pick the next largest character.

## 示例

```
"cczazcc"
3
"aababab"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        
    }
};
```

### Java

```java
class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
```

### C

```c
char* repeatLimitedString(char* s, int repeatLimit) {
    
}
```

### C#

```csharp
public class Solution {
    public string RepeatLimitedString(string s, int repeatLimit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} repeatLimit
 * @return {string}
 */
var repeatLimitedString = function(s, repeatLimit) {
    
};
```

### TypeScript

```typescript
function repeatLimitedString(s: string, repeatLimit: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $repeatLimit
     * @return String
     */
    function repeatLimitedString($s, $repeatLimit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func repeatLimitedString(_ s: String, _ repeatLimit: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun repeatLimitedString(s: String, repeatLimit: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String repeatLimitedString(String s, int repeatLimit) {
    
  }
}
```

### Go

```golang
func repeatLimitedString(s string, repeatLimit int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} repeat_limit
# @return {String}
def repeat_limited_string(s, repeat_limit)
    
end
```

### Scala

```scala
object Solution {
    def repeatLimitedString(s: String, repeatLimit: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn repeat_limited_string(s: String, repeat_limit: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (repeat-limited-string s repeatLimit)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec repeat_limited_string(S :: unicode:unicode_binary(), RepeatLimit :: integer()) -> unicode:unicode_binary().
repeat_limited_string(S, RepeatLimit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec repeat_limited_string(s :: String.t, repeat_limit :: integer) :: String.t
  def repeat_limited_string(s, repeat_limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func repeatLimitedString(s: String, repeatLimit: Int64): String {

    }
}
```

