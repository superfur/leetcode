# 880. 索引处的解码字符串

## 题目描述

<p>给定一个编码字符串 <code>s</code> 。请你找出<em> </em><strong>解码字符串</strong> 并将其写入磁带。解码时，从编码字符串中<strong> 每次读取一个字符 </strong>，并采取以下步骤：</p>

<ul>
	<li>如果所读的字符是字母，则将该字母写在磁带上。</li>
	<li>如果所读的字符是数字（例如 <code>d</code>），则整个当前磁带总共会被重复写&nbsp;<code>d-1</code> 次。</li>
</ul>

<p>现在，对于给定的编码字符串 <code>s</code> 和索引 <code>k</code>，查找并返回解码字符串中的第 <code>k</code> 个字母。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leet2code3", k = 10
<strong>输出：</strong>"o"
<strong>解释：</strong>
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ha22", k = 5
<strong>输出：</strong>"h"
<strong>解释：</strong>
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a2345678999999999999999", k = 1
<strong>输出：</strong>"a"
<strong>解释：</strong>
解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 只包含小写字母与数字 <code>2</code> 到 <code>9</code> 。</li>
	<li><code>s</code> 以字母开头。</li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li>题目保证 <code>k</code> 小于或等于解码字符串的长度。</li>
	<li>解码后的字符串保证少于&nbsp;<code>2<sup>63</sup></code>&nbsp;个字母。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 示例

```
"leet2code3"
10
"ha22"
5
"a2345678999999999999999"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string decodeAtIndex(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String decodeAtIndex(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
```

### C

```c
char* decodeAtIndex(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string DecodeAtIndex(string s, int k) {
        
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
var decodeAtIndex = function(s, k) {
    
};
```

### TypeScript

```typescript
function decodeAtIndex(s: string, k: number): string {
    
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
    function decodeAtIndex($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decodeAtIndex(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decodeAtIndex(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String decodeAtIndex(String s, int k) {
    
  }
}
```

### Go

```golang
func decodeAtIndex(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def decode_at_index(s, k)
    
end
```

### Scala

```scala
object Solution {
    def decodeAtIndex(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (decode-at-index s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec decode_at_index(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
decode_at_index(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decode_at_index(s :: String.t, k :: integer) :: String.t
  def decode_at_index(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decodeAtIndex(s: String, k: Int64): String {

    }
}
```

