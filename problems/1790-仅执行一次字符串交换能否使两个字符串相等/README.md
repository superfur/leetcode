# 1790. 仅执行一次字符串交换能否使两个字符串相等

## 题目描述

<p>给你长度相等的两个字符串 <code>s1</code> 和 <code>s2</code> 。一次<strong> 字符串交换 </strong>操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。</p>

<p>如果对 <strong>其中一个字符串</strong> 执行 <strong>最多一次字符串交换</strong> 就可以使两个字符串相等，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s1 = "bank", s2 = "kanb"
<strong>输出：</strong>true
<strong>解释：</strong>例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s1 = "attack", s2 = "defend"
<strong>输出：</strong>false
<strong>解释：</strong>一次字符串交换无法使两个字符串相等
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s1 = "kelb", s2 = "kelb"
<strong>输出：</strong>true
<strong>解释：</strong>两个字符串已经相等，所以不需要进行字符串交换
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s1 = "abcd", s2 = "dcba"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1</code> 和 <code>s2</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
2. Check that these positions have the same set of characters.

## 示例

```
"bank"
"kanb"
"attack"
"defend"
"kelb"
"kelb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool areAlmostEqual(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool AreAlmostEqual(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function areAlmostEqual(s1: string, s2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function areAlmostEqual($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func areAlmostEqual(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun areAlmostEqual(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool areAlmostEqual(String s1, String s2) {
    
  }
}
```

### Go

```golang
func areAlmostEqual(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def are_almost_equal(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def areAlmostEqual(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (are-almost-equal s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec are_almost_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
are_almost_equal(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec are_almost_equal(s1 :: String.t, s2 :: String.t) :: boolean
  def are_almost_equal(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func areAlmostEqual(s1: String, s2: String): Bool {

    }
}
```

