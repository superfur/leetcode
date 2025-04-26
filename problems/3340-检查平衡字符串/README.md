# 3340. 检查平衡字符串

## 题目描述

<p>给你一个仅由数字 0 - 9 组成的字符串 <code>num</code>。如果偶数下标处的数字之和等于奇数下标处的数字之和，则认为该数字字符串是一个 <b>平衡字符串</b>。</p>

<p>如果 <code>num</code> 是一个 <strong>平衡字符串</strong>，则返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>num<span class="example-io"> = "1234"</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>偶数下标处的数字之和为 <code>1 + 3 = 4</code>，奇数下标处的数字之和为 <code>2 + 4 = 6</code>。</li>
	<li>由于 4 不等于 6，<code>num</code> 不是平衡字符串。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>num<span class="example-io"> = "24123"</span></p>

<p><strong>输出：</strong>true</p>

<p><strong>解释：</strong></p>

<ul>
	<li>偶数下标处的数字之和为 <code>2 + 1 + 3 = 6</code>，奇数下标处的数字之和为 <code>4 + 2 = 6</code>。</li>
	<li>由于两者相等，<code>num</code> 是平衡字符串。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 100</code></li>
	<li><code>num</code> 仅由数字 0 - 9 组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 示例

```
"1234"
"24123"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isBalanced(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isBalanced(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isBalanced(self, num: str) -> bool:
        
```

### C

```c
bool isBalanced(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsBalanced(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var isBalanced = function(num) {
    
};
```

### TypeScript

```typescript
function isBalanced(num: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function isBalanced($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isBalanced(_ num: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isBalanced(num: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isBalanced(String num) {
    
  }
}
```

### Go

```golang
func isBalanced(num string) bool {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Boolean}
def is_balanced(num)
    
end
```

### Scala

```scala
object Solution {
    def isBalanced(num: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_balanced(num: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-balanced num)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_balanced(Num :: unicode:unicode_binary()) -> boolean().
is_balanced(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_balanced(num :: String.t) :: boolean
  def is_balanced(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isBalanced(num: String): Bool {

    }
}
```

