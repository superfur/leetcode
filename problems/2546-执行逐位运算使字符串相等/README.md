# 2546. 执行逐位运算使字符串相等

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的 <strong>二元</strong> 字符串 <code>s</code> 和 <code>target</code> ，两个字符串的长度均为 <code>n</code> 。你可以对 <code>s</code> 执行下述操作 <strong>任意</strong> 次：</p>

<ul>
	<li>选择两个 <strong>不同</strong> 的下标 <code>i</code> 和 <code>j</code> ，其中 <code>0 &lt;= i, j &lt; n</code> 。</li>
	<li>同时，将 <code>s[i]</code> 替换为 (<code>s[i]</code> <strong>OR</strong> <code>s[j]</code>) ，<code>s[j]</code> 替换为 (<code>s[i]</code> <strong>XOR</strong> <code>s[j]</code>) 。</li>
</ul>

<p>例如，如果 <code>s = "0110"</code> ，你可以选择 <code>i = 0</code> 和 <code>j = 2</code>，然后同时将 <code>s[0]</code> 替换为 (<code>s[0]</code> <strong>OR</strong> <code>s[2]</code> = <code>0</code> <strong>OR</strong> <code>1</code> = <code>1</code>)，并将 <code>s[2]</code> 替换为 (<code>s[0]</code> <strong>XOR</strong> <code>s[2]</code> = <code>0</code> <strong>XOR</strong> <code>1</code> = <code>1</code>)，最终得到 <code>s = "1110"</code> 。</p>

<p>如果可以使 <code>s</code> 等于 <code>target</code> ，返回 <code>true</code> ，否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "1010", target = "0110"
<strong>输出：</strong>true
<strong>解释：</strong>可以执行下述操作：
- 选择 i = 2 和 j = 0 ，得到 s = "<em><strong>0</strong></em>0<em><strong>1</strong></em>0".
- 选择 i = 2 和 j = 1 ，得到 s = "0<em><strong>11</strong></em>0".
可以使 s 等于 target ，返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "11", target = "00"
<strong>输出：</strong>false
<strong>解释：</strong>执行任意次操作都无法使 s 等于 target 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s.length == target.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>target</code> 仅由数字 <code>0</code> 和 <code>1</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 字符串

## 提示

1. Think of when it is impossible to convert the string to the target.
2. If exactly one of the strings is having all 0’s, then it is impossible. And it is possible in all other cases. Why is that true?

## 示例

```
"1010"
"0110"
"11"
"00"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool makeStringsEqual(string s, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean makeStringsEqual(String s, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        
```

### C

```c
bool makeStringsEqual(char* s, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool MakeStringsEqual(string s, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} target
 * @return {boolean}
 */
var makeStringsEqual = function(s, target) {
    
};
```

### TypeScript

```typescript
function makeStringsEqual(s: string, target: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $target
     * @return Boolean
     */
    function makeStringsEqual($s, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeStringsEqual(_ s: String, _ target: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeStringsEqual(s: String, target: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool makeStringsEqual(String s, String target) {
    
  }
}
```

### Go

```golang
func makeStringsEqual(s string, target string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} target
# @return {Boolean}
def make_strings_equal(s, target)
    
end
```

### Scala

```scala
object Solution {
    def makeStringsEqual(s: String, target: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_strings_equal(s: String, target: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (make-strings-equal s target)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec make_strings_equal(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> boolean().
make_strings_equal(S, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_strings_equal(s :: String.t, target :: String.t) :: boolean
  def make_strings_equal(s, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeStringsEqual(s: String, target: String): Bool {

    }
}
```

