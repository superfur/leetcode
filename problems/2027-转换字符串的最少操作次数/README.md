# 2027. 转换字符串的最少操作次数

## 题目描述

<p>给你一个字符串 <code>s</code> ，由 <code>n</code> 个字符组成，每个字符不是 <code>'X'</code> 就是 <code>'O'</code> 。</p>

<p>一次<strong> 操作</strong> 定义为从 <code>s</code> 中选出 <strong>三个连续字符 </strong>并将选中的每个字符都转换为 <code>'O'</code> 。注意，如果字符已经是 <code>'O'</code> ，只需要保持 <strong>不变</strong> 。</p>

<p>返回将 <code>s</code> 中所有字符均转换为 <code>'O'</code> 需要执行的&nbsp;<strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "XXX"
<strong>输出：</strong>1
<strong>解释：<em>XXX</em></strong> -&gt; OOO
一次操作，选中全部 3 个字符，并将它们转换为 <code>'O' 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "XXOX"
<strong>输出：</strong>2
<strong>解释：<em>XXO</em></strong>X -&gt; O<em><strong>OOX</strong></em> -&gt; OOOO
第一次操作，选择前 3 个字符，并将这些字符转换为 <code>'O'</code> 。
然后，选中后 3 个字符，并执行转换。最终得到的字符串全由字符 <code>'O'</code> 组成。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "OOOO"
<strong>输出：</strong>0
<strong>解释：</strong>s 中不存在需要转换的 <code>'X' 。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> 为 <code>'X'</code> 或 <code>'O'</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串

## 提示

1. Find the smallest substring you need to consider at a time.
2. Try delaying a move as long as possible.

## 示例

```
"XXX"
"XXOX"
"OOOO"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumMoves(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumMoves(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumMoves(self, s: str) -> int:
        
```

### C

```c
int minimumMoves(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumMoves(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumMoves = function(s) {
    
};
```

### TypeScript

```typescript
function minimumMoves(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumMoves($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumMoves(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumMoves(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumMoves(String s) {
    
  }
}
```

### Go

```golang
func minimumMoves(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_moves(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumMoves(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_moves(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-moves s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_moves(S :: unicode:unicode_binary()) -> integer().
minimum_moves(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_moves(s :: String.t) :: integer
  def minimum_moves(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumMoves(s: String): Int64 {

    }
}
```

