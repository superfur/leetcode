# 541. 反转字符串 II

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个整数 <code>k</code>，从字符串开头算起，每计数至 <code>2k</code> 个字符，就反转这 <code>2k</code> 字符中的前 <code>k</code> 个字符。</p>

<ul>
	<li>如果剩余字符少于 <code>k</code> 个，则将剩余字符全部反转。</li>
	<li>如果剩余字符小于 <code>2k</code> 但大于或等于 <code>k</code> 个，则反转前 <code>k</code> 个字符，其余字符保持原样。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcdefg", k = 2
<strong>输出：</strong>"bacdfeg"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", k = 2
<strong>输出：</strong>"bacd"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文组成</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 示例

```
"abcdefg"
2
"abcd"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reverseStr(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String reverseStr(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
```

### C

```c
char* reverseStr(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReverseStr(string s, int k) {
        
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
var reverseStr = function(s, k) {
    
};
```

### TypeScript

```typescript
function reverseStr(s: string, k: number): string {
    
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
    function reverseStr($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseStr(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseStr(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reverseStr(String s, int k) {
    
  }
}
```

### Go

```golang
func reverseStr(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def reverse_str(s, k)
    
end
```

### Scala

```scala
object Solution {
    def reverseStr(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_str(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-str s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec reverse_str(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
reverse_str(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_str(s :: String.t, k :: integer) :: String.t
  def reverse_str(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseStr(s: String, k: Int64): String {

    }
}
```

