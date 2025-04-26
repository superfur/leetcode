# 205. 同构字符串

## 题目描述

<p>给定两个字符串&nbsp;<code>s</code>&nbsp;和&nbsp;<code>t</code>&nbsp;，判断它们是否是同构的。</p>

<p>如果&nbsp;<code>s</code>&nbsp;中的字符可以按某种映射关系替换得到&nbsp;<code>t</code>&nbsp;，那么这两个字符串是同构的。</p>

<p>每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>s = <code>"egg"</code>, t = <code>"add"</code>
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = <code>"foo"</code>, t = <code>"bar"</code>
<strong>输出：</strong>false</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = <code>"paper"</code>, t = <code>"title"</code>
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>t.length == s.length</code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>t</code>&nbsp;由任意有效的 ASCII 字符组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 示例

```
"egg"
"add"
"foo"
"bar"
"paper"
"title"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
```

### C

```c
bool isIsomorphic(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsIsomorphic(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    
};
```

### TypeScript

```typescript
function isIsomorphic(s: string, t: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isIsomorphic($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isIsomorphic(String s, String t) {
    
  }
}
```

### Go

```golang
func isIsomorphic(s string, t string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
    
end
```

### Scala

```scala
object Solution {
    def isIsomorphic(s: String, t: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-isomorphic s t)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_isomorphic(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_isomorphic(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_isomorphic(s :: String.t, t :: String.t) :: boolean
  def is_isomorphic(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isIsomorphic(s: String, t: String): Bool {

    }
}
```

