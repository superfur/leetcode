# 1234. 替换子串得到平衡字符串

## 题目描述

<p>有一个只含有&nbsp;<code>'Q', 'W', 'E',&nbsp;'R'</code>&nbsp;四种字符，且长度为 <code>n</code>&nbsp;的字符串。</p>

<p>假如在该字符串中，这四个字符都恰好出现&nbsp;<code>n/4</code>&nbsp;次，那么它就是一个「平衡字符串」。</p>

<p>&nbsp;</p>

<p>给你一个这样的字符串 <code>s</code>，请通过「替换一个子串」的方式，使原字符串 <code>s</code> 变成一个「平衡字符串」。</p>

<p>你可以用和「待替换子串」长度相同的&nbsp;<strong>任何</strong> 其他字符串来完成替换。</p>

<p>请返回待替换子串的最小可能长度。</p>

<p>如果原字符串自身就是一个平衡字符串，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "QWER"
<strong>输出：</strong>0
<strong>解释：</strong>s 已经是平衡的了。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "QQWE"
<strong>输出：</strong>1
<strong>解释：</strong>我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "QQQW"
<strong>输出：</strong>2
<strong>解释：</strong>我们可以把前面的 "QQ" 替换成 "ER"。 
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "QQQQ"
<strong>输出：</strong>3
<strong>解释：</strong>我们可以替换后 3 个 'Q'，使 s = "QWER"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s.length</code>&nbsp;是&nbsp;<code>4</code>&nbsp;的倍数</li>
	<li><code>s</code>&nbsp;中只含有&nbsp;<code>'Q'</code>, <code>'W'</code>, <code>'E'</code>,&nbsp;<code>'R'</code>&nbsp;四种字符</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 滑动窗口

## 提示

1. Use 2-pointers algorithm to make sure all amount of characters outside the 2 pointers are smaller or equal to n/4.
2. That means you need to count the amount of each letter and make sure the amount is enough.

## 示例

```
"QWER"
"QQWE"
"QQQW"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int balancedString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int balancedString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def balancedString(self, s: str) -> int:
        
```

### C

```c
int balancedString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int BalancedString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var balancedString = function(s) {
    
};
```

### TypeScript

```typescript
function balancedString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function balancedString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func balancedString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun balancedString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int balancedString(String s) {
    
  }
}
```

### Go

```golang
func balancedString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def balanced_string(s)
    
end
```

### Scala

```scala
object Solution {
    def balancedString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn balanced_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (balanced-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec balanced_string(S :: unicode:unicode_binary()) -> integer().
balanced_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec balanced_string(s :: String.t) :: integer
  def balanced_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func balancedString(s: String): Int64 {

    }
}
```

