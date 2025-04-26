# 761. 特殊的二进制序列

## 题目描述

<p>特殊的二进制序列是具有以下两个性质的二进制序列：</p>

<ul>
	<li>0 的数量与 1 的数量相等。</li>
	<li>二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。</li>
</ul>

<p>给定一个特殊的二进制序列&nbsp;<code>S</code>，以字符串形式表示。定义一个<em>操作 </em>为首先选择&nbsp;<code>S</code>&nbsp;的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)</p>

<p>在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> S = &quot;11011000&quot;
<strong>输出:</strong> &quot;11100100&quot;
<strong>解释:</strong>
将子串 &quot;10&quot; （在S[1]出现） 和 &quot;1100&quot; （在S[3]出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>S</code>&nbsp;的长度不超过&nbsp;<code>50</code>。</li>
	<li><code>S</code>&nbsp;保证为一个满足上述定义的<em>特殊 </em>的二进制序列。</li>
</ol>


## 难度

Hard

## 标签

- 递归
- 字符串

## 提示

1. Draw a line from (x, y) to (x+1, y+1) if we see a "1", else to (x+1, y-1).
A special substring is just a line that starts and ends at the same y-coordinate, and that is the lowest y-coordinate reached.
Call a mountain a special substring with no special prefixes - ie. only at the beginning and end is the lowest y-coordinate reached.
If F is the answer function, and S has mountain decomposition M1,M2,M3,...,Mk,  then the answer is:
reverse_sorted(F(M1), F(M2), ..., F(Mk)).
However, you'll also need to deal with the case that S is a mountain, such as 11011000 -> 11100100.

## 示例

```
"11011000"
"10"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string makeLargestSpecial(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String makeLargestSpecial(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
```

### C

```c
char* makeLargestSpecial(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MakeLargestSpecial(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeLargestSpecial = function(s) {
    
};
```

### TypeScript

```typescript
function makeLargestSpecial(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeLargestSpecial($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeLargestSpecial(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeLargestSpecial(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String makeLargestSpecial(String s) {
    
  }
}
```

### Go

```golang
func makeLargestSpecial(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def make_largest_special(s)
    
end
```

### Scala

```scala
object Solution {
    def makeLargestSpecial(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_largest_special(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (make-largest-special s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec make_largest_special(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_largest_special(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_largest_special(s :: String.t) :: String.t
  def make_largest_special(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeLargestSpecial(s: String): String {

    }
}
```

