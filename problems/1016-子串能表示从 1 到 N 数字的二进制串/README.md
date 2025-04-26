# 1016. 子串能表示从 1 到 N 数字的二进制串

## 题目描述

<p>给定一个二进制字符串&nbsp;<code>s</code>&nbsp;和一个正整数&nbsp;<code>n</code>，如果对于&nbsp;<code>[1, n]</code>&nbsp;范围内的每个整数，<em>其二进制表示都是&nbsp;<code>s</code> 的 <strong>子字符串</strong> ，就返回 <code>true</code>，否则返回 <code>false</code>&nbsp;</em>。</p>

<p><strong>子字符串</strong>&nbsp;是字符串中连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", n = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", n = 4
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code>&nbsp;不是&nbsp;<code>'0'</code>&nbsp;就是&nbsp;<code>'1'</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 提示

1. We only need to check substrings of length at most 30, because 10^9 has 30 bits.

## 示例

```
"0110"
3
"0110"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool queryString(string s, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean queryString(String s, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
```

### C

```c
bool queryString(char* s, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool QueryString(string s, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} n
 * @return {boolean}
 */
var queryString = function(s, n) {
    
};
```

### TypeScript

```typescript
function queryString(s: string, n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $n
     * @return Boolean
     */
    function queryString($s, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func queryString(_ s: String, _ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun queryString(s: String, n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool queryString(String s, int n) {
    
  }
}
```

### Go

```golang
func queryString(s string, n int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} n
# @return {Boolean}
def query_string(s, n)
    
end
```

### Scala

```scala
object Solution {
    def queryString(s: String, n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn query_string(s: String, n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (query-string s n)
  (-> string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec query_string(S :: unicode:unicode_binary(), N :: integer()) -> boolean().
query_string(S, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec query_string(s :: String.t, n :: integer) :: boolean
  def query_string(s, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func queryString(s: String, n: Int64): Bool {

    }
}
```

