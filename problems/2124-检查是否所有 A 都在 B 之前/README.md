# 2124. 检查是否所有 A 都在 B 之前

## 题目描述

<p>给你一个 <strong>仅</strong> 由字符 <code>'a'</code> 和 <code>'b'</code> 组成的字符串&nbsp; <code>s</code> 。如果字符串中 <strong>每个</strong> <em> </em><code>'a'</code> 都出现在 <strong>每个</strong><em> </em><code>'b'</code><em> </em>之前，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "aaabbb"
<strong>输出：</strong>true
<strong>解释：</strong>
'a' 位于下标 0、1 和 2 ；而 'b' 位于下标 3、4 和 5 。
因此，每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "abab"
<strong>输出：</strong>false
<strong>解释：</strong>
存在一个 'a' 位于下标 2 ，而一个 'b' 位于下标 1 。
因此，不能满足每个 'a' 都出现在每个 'b' 之前，所以返回 false 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = "bbb"
<strong>输出：</strong>true
<strong>解释：</strong>
不存在 'a' ，因此可以视作每个 'a' 都出现在每个 'b' 之前，所以返回 true 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> 为 <code>'a'</code> 或 <code>'b'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. You can check the opposite: check if there is a ‘b’ before an ‘a’. Then, negate and return that answer.
2. s should not have any occurrences of “ba” as a substring.

## 示例

```
"aaabbb"
"abab"
"bbb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkString(self, s: str) -> bool:
        
```

### C

```c
bool checkString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkString = function(s) {
    
};
```

### TypeScript

```typescript
function checkString(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkString(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkString(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkString(String s) {
    
  }
}
```

### Go

```golang
func checkString(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_string(s)
    
end
```

### Scala

```scala
object Solution {
    def checkString(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_string(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-string s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_string(S :: unicode:unicode_binary()) -> boolean().
check_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_string(s :: String.t) :: boolean
  def check_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkString(s: String): Bool {

    }
}
```

