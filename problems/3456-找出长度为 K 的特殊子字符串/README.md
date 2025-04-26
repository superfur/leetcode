# 3456. 找出长度为 K 的特殊子字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>判断是否存在一个长度&nbsp;<strong>恰好&nbsp;</strong>为 <code>k</code> 的子字符串，该子字符串需要满足以下条件：</p>

<ol>
	<li>该子字符串&nbsp;<strong>只包含一个唯一字符</strong>（例如，<code>"aaa"</code> 或 <code>"bbb"</code>）。</li>
	<li>如果该子字符串的&nbsp;<strong>前面&nbsp;</strong>有字符，则该字符必须与子字符串中的字符不同。</li>
	<li>如果该子字符串的&nbsp;<strong>后面&nbsp;</strong>有字符，则该字符也必须与子字符串中的字符不同。</li>
</ol>

<p>如果存在这样的子串，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p><strong>子字符串&nbsp;</strong>是字符串中的连续、非空字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aaabaaa", k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>子字符串 <code>s[4..6] == "aaa"</code> 满足条件：</p>

<ul>
	<li>长度为 3。</li>
	<li>所有字符相同。</li>
	<li>子串 <code>"aaa"</code> 前的字符是 <code>'b'</code>，与 <code>'a'</code> 不同。</li>
	<li>子串 <code>"aaa"</code> 后没有字符。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abc", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>不存在长度为 2 、仅由一个唯一字符组成且满足所有条件的子字符串。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Return <code>true</code> if there is a sequence of consecutive characters of length <code>k</code>

## 示例

```
"aaabaaa"
3
"abc"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasSpecialSubstring(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        
```

### C

```c
bool hasSpecialSubstring(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasSpecialSubstring(string s, int k) {
        
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
var hasSpecialSubstring = function(s, k) {
    
};
```

### TypeScript

```typescript
function hasSpecialSubstring(s: string, k: number): boolean {
    
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
    function hasSpecialSubstring($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasSpecialSubstring(_ s: String, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasSpecialSubstring(s: String, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasSpecialSubstring(String s, int k) {
    
  }
}
```

### Go

```golang
func hasSpecialSubstring(s string, k int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Boolean}
def has_special_substring(s, k)
    
end
```

### Scala

```scala
object Solution {
    def hasSpecialSubstring(s: String, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_special_substring(s: String, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-special-substring s k)
  (-> string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec has_special_substring(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
has_special_substring(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_special_substring(s :: String.t, k :: integer) :: boolean
  def has_special_substring(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasSpecialSubstring(s: String, k: Int64): Bool {

    }
}
```

