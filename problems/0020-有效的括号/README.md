# 20. 有效的括号

## 题目描述

<p>给定一个只包括 <code>'('</code>，<code>')'</code>，<code>'{'</code>，<code>'}'</code>，<code>'['</code>，<code>']'</code>&nbsp;的字符串 <code>s</code> ，判断字符串是否有效。</p>

<p>有效字符串需满足：</p>

<ol>
	<li>左括号必须用相同类型的右括号闭合。</li>
	<li>左括号必须以正确的顺序闭合。</li>
	<li>每个右括号都有一个对应的相同类型的左括号。</li>
</ol>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "()"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "()[]{}"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "(]"</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "([])"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由括号 <code>'()[]{}'</code> 组成</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串

## 提示

1. Use a stack of characters.
2. When you encounter an opening bracket, push it to the top of the stack.
3. When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

## 示例

```
"()"
"()[]{}"
"(]"
"([])"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isValid(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isValid(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        
```

### C

```c
bool isValid(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsValid(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
};
```

### TypeScript

```typescript
function isValid(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isValid(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isValid(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isValid(String s) {
    
  }
}
```

### Go

```golang
func isValid(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def is_valid(s)
    
end
```

### Scala

```scala
object Solution {
    def isValid(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_valid(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-valid s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_valid(S :: unicode:unicode_binary()) -> boolean().
is_valid(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isValid(s: String): Bool {

    }
}
```

