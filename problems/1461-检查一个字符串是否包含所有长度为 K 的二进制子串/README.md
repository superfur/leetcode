# 1461. 检查一个字符串是否包含所有长度为 K 的二进制子串

## 题目描述

<p>给你一个二进制字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。如果所有长度为 <code>k</code>&nbsp;的二进制字符串都是 <code>s</code>&nbsp;的子串，请返回 <code>true</code> ，否则请返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "00110110", k = 2
<strong>输出：</strong>true
<strong>解释：</strong>长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", k = 1
<strong>输出：</strong>true
<strong>解释：</strong>长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", k = 2
<strong>输出：</strong>false
<strong>解释：</strong>长度为 2 的二进制串 "00" 没有出现在 s 中。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 不是<code>'0'</code> 就是 <code>'1'</code></li>
	<li><code>1 &lt;= k &lt;= 20</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 哈希函数
- 滚动哈希

## 提示

1. We need only to check all sub-strings of length k.
2. The number of distinct sub-strings should be exactly 2^k.

## 示例

```
"00110110"
2
"0110"
1
"0110"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasAllCodes(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
```

### C

```c
bool hasAllCodes(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasAllCodes(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
    
};
```

### TypeScript

```typescript
function hasAllCodes(s: string, k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function hasAllCodes($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasAllCodes(_ s: String, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasAllCodes(s: String, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasAllCodes(String s, int k) {
    
  }
}
```

### Go

```golang
func hasAllCodes(s string, k int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Boolean}
def has_all_codes(s, k)
    
end
```

### Scala

```scala
object Solution {
    def hasAllCodes(s: String, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-all-codes s k)
  (-> string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec has_all_codes(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
has_all_codes(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_all_codes(s :: String.t, k :: integer) :: boolean
  def has_all_codes(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasAllCodes(s: String, k: Int64): Bool {

    }
}
```

