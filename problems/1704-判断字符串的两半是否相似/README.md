# 1704. 判断字符串的两半是否相似

## 题目描述

<p>给你一个偶数长度的字符串 <code>s</code> 。将其拆分成长度相同的两半，前一半为 <code>a</code> ，后一半为 <code>b</code> 。</p>

<p>两个字符串 <strong>相似</strong> 的前提是它们都含有相同数目的元音（<code>'a'</code>，<code>'e'</code>，<code>'i'</code>，<code>'o'</code>，<code>'u'</code>，<code>'A'</code>，<code>'E'</code>，<code>'I'</code>，<code>'O'</code>，<code>'U'</code>）。注意，<code>s</code> 可能同时含有大写和小写字母。</p>

<p>如果<em> </em><code>a</code><em> </em>和<em> </em><code>b</code> 相似，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "book"
<strong>输出：</strong>true
<strong>解释：</strong>a = "b<strong>o</strong>" 且 b = "<strong>o</strong>k" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "textbook"
<strong>输出：</strong>false
<strong>解释：</strong>a = "t<strong>e</strong>xt" 且 b = "b<strong>oo</strong>k" 。a 中有 1 个元音，b 中有 2 个元音。因此，a 和 b 不相似。
注意，元音 o 在 b 中出现两次，记为 2 个。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s.length</code> 是偶数</li>
	<li><code>s</code> 由 <strong>大写和小写</strong> 字母组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 计数

## 提示

1. Create a function that checks if a character is a vowel, either uppercase or lowercase.

## 示例

```
"book"
"textbook"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool halvesAreAlike(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean halvesAreAlike(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
```

### C

```c
bool halvesAreAlike(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HalvesAreAlike(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    
};
```

### TypeScript

```typescript
function halvesAreAlike(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function halvesAreAlike($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func halvesAreAlike(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun halvesAreAlike(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool halvesAreAlike(String s) {
    
  }
}
```

### Go

```golang
func halvesAreAlike(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def halves_are_alike(s)
    
end
```

### Scala

```scala
object Solution {
    def halvesAreAlike(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (halves-are-alike s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec halves_are_alike(S :: unicode:unicode_binary()) -> boolean().
halves_are_alike(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec halves_are_alike(s :: String.t) :: boolean
  def halves_are_alike(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func halvesAreAlike(s: String): Bool {

    }
}
```

