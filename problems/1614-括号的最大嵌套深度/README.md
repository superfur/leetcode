# 1614. 括号的最大嵌套深度

## 题目描述

<p>给定 <strong>有效括号字符串</strong> <code>s</code>，返回 <code>s</code> 的 <strong>嵌套深度</strong>。嵌套深度是嵌套括号的 <strong>最大</strong> 数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1+(2*3)+((<strong>8</strong>)/4))+1"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 8 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1)+((2))+(((<strong>3</strong>)))"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 3 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "()(())((()()))"</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由数字 <code>0-9</code> 和字符 <code>'+'</code>、<code>'-'</code>、<code>'*'</code>、<code>'/'</code>、<code>'('</code>、<code>')'</code> 组成</li>
	<li>题目数据保证括号字符串&nbsp;<code>s</code> 是 <strong>有效的括号字符串</strong></li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串

## 提示

1. The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )

## 示例

```
"(1+(2*3)+((8)/4))+1"
"(1)+((2))+(((3)))"
"()(())((()()))"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDepth(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDepth(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDepth(self, s: str) -> int:
        
```

### C

```c
int maxDepth(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDepth(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    
};
```

### TypeScript

```typescript
function maxDepth(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxDepth($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDepth(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDepth(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDepth(String s) {
    
  }
}
```

### Go

```golang
func maxDepth(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_depth(s)
    
end
```

### Scala

```scala
object Solution {
    def maxDepth(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_depth(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-depth s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_depth(S :: unicode:unicode_binary()) -> integer().
max_depth(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_depth(s :: String.t) :: integer
  def max_depth(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDepth(s: String): Int64 {

    }
}
```

