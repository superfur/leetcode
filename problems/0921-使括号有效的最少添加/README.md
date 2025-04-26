# 921. 使括号有效的最少添加

## 题目描述

<p>只有满足下面几点之一，括号字符串才是有效的：</p>

<ul>
	<li>它是一个空字符串，或者</li>
	<li>它可以被写成&nbsp;<code>AB</code>&nbsp;（<code>A</code>&nbsp;与&nbsp;<code>B</code>&nbsp;连接）, 其中&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是有效字符串，或者</li>
	<li>它可以被写作&nbsp;<code>(A)</code>，其中&nbsp;<code>A</code>&nbsp;是有效字符串。</li>
</ul>

<p>给定一个括号字符串 <code>s</code> ，在每一次操作中，你都可以在字符串的任何位置插入一个括号</p>

<ul>
	<li>例如，如果 <code>s = "()))"</code> ，你可以插入一个开始括号为 <code>"(()))"</code> 或结束括号为 <code>"())))"</code> 。</li>
</ul>

<p>返回 <em>为使结果字符串 <code>s</code> 有效而必须添加的最少括号数</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "())"
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "((("
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 只包含&nbsp;<code>'('</code> 和&nbsp;<code>')'</code>&nbsp;字符。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串

## 示例

```
"())"
"((("
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minAddToMakeValid(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
```

### C

```c
int minAddToMakeValid(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinAddToMakeValid(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    
};
```

### TypeScript

```typescript
function minAddToMakeValid(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minAddToMakeValid($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAddToMakeValid(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minAddToMakeValid(String s) {
    
  }
}
```

### Go

```golang
func minAddToMakeValid(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_add_to_make_valid(s)
    
end
```

### Scala

```scala
object Solution {
    def minAddToMakeValid(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-add-to-make-valid s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_add_to_make_valid(S :: unicode:unicode_binary()) -> integer().
min_add_to_make_valid(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_add_to_make_valid(s :: String.t) :: integer
  def min_add_to_make_valid(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAddToMakeValid(s: String): Int64 {

    }
}
```

