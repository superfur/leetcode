# 面试题 01.09. 字符串轮转

## 题目描述

<p>字符串轮转。给定两个字符串<code>s1</code>和<code>s2</code>，请编写代码检查<code>s2</code>是否为<code>s1</code>旋转而成（比如，<code>waterbottle</code>是<code>erbottlewat</code>旋转后的字符串）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：s1 = "waterbottle", s2 = "erbottlewat"
<strong> 输出</strong>：True
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：s1 = "aa", s2 = "aba"
<strong> 输出</strong>：False
</pre>

<ol>
</ol>

<p><strong>提示：</strong></p>

<ol>
	<li>字符串长度在[0, 100000]范围内。</li>
</ol>

<p><strong>说明:</strong></p>

<ol>
	<li>你能只调用一次检查子串的方法吗？</li>
</ol>


## 难度

Easy

## 标签

- 字符串
- 字符串匹配

## 提示

1. 如果一个字符串是另一个字符串的旋转，那么它就是在某个特定点上的旋转。例如，字符串waterbottle在3处的旋转意味着在第三个字符处切割waterbottle，并在左半部分（wat）之前放置右半部分（erbottle）。
2. 本质上，我们是在寻找是否有一种方式可以把第一个字符串分成两部分，即x和y，如此一来，第一个字符串就是xy，第二个字符串就是yx。例如，x = wat，y = erbottle。那么，第一个字符串xy = waterbottle，第二个字符串yx = erbottlewat。
3. 想想前面的提示。再想想当你将erbottlewat与它本身连接会发生什么。你得到了erbottlewaterbottlewat。

## 示例

```
"waterbottle"
"erbottlewat"
"aa"
"aba"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isFlipedString(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool isFlipedString(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsFlipedString(string s1, string s2) {
        
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
var isFlipedString = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function isFlipedString(s1: string, s2: string): boolean {
    
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
    function isFlipedString($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isFlipedString(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isFlipedString(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isFlipedString(String s1, String s2) {
    
  }
}
```

### Go

```golang
func isFlipedString(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def is_fliped_string(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def isFlipedString(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_fliped_string(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-fliped-string s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_fliped_string(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
is_fliped_string(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_fliped_string(s1 :: String.t, s2 :: String.t) :: boolean
  def is_fliped_string(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isFlipedString(s1: String, s2: String): Bool {

    }
}
```

