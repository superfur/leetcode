# 2849. 判断能否在给定时间到达单元格

## 题目描述

<p>给你四个整数 <code>sx</code>、<code>sy</code>、<code>fx</code>、<code>fy</code>&nbsp; 以及一个 <strong>非负整数</strong> <code>t</code> 。</p>

<p>在一个无限的二维网格中，你从单元格 <code>(sx, sy)</code> 开始出发。每一秒，你 <strong>必须</strong> 移动到任一与之前所处单元格相邻的单元格中。</p>

<p>如果你能在 <strong>恰好 </strong><code>t</code><strong> 秒</strong> 后到达单元格<em> </em><code>(fx, fy)</code> ，返回 <code>true</code> ；否则，返回&nbsp; <code>false</code> 。</p>

<p>单元格的 <strong>相邻单元格</strong> 是指该单元格周围与其至少共享一个角的 8 个单元格。你可以多次访问同一个单元格。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/05/example2.svg" style="width: 443px; height: 243px;" />
<pre>
<strong>输入：</strong>sx = 2, sy = 4, fx = 7, fy = 7, t = 6
<strong>输出：</strong>true
<strong>解释：</strong>从单元格 (2, 4) 开始出发，穿过上图标注的单元格，可以在恰好 6 秒后到达单元格 (7, 7) 。 
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/05/example1.svg" style="width: 383px; height: 202px;" />
<pre>
<strong>输入：</strong>sx = 3, sy = 1, fx = 7, fy = 3, t = 3
<strong>输出：</strong>false
<strong>解释：</strong>从单元格 (3, 1) 开始出发，穿过上图标注的单元格，至少需要 4 秒后到达单元格 (7, 3) 。 因此，无法在 3 秒后到达单元格 (7, 3) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sx, sy, fx, fy &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= t &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Minimum time to reach the cell should be less than or equal to given time.
2. The answer is true if <code>t</code> is greater or equal than the Chebyshev distance from <code>(sx, sy)</code> to <code>(fx, fy)</code>. However, there is one more edge case to be considered.
3. The answer is false If <code>sx == fx</code> and <code>sy == fy</code>

## 示例

```
2
4
7
7
6
3
1
7
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
```

### C

```c
bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} fx
 * @param {number} fy
 * @param {number} t
 * @return {boolean}
 */
var isReachableAtTime = function(sx, sy, fx, fy, t) {
    
};
```

### TypeScript

```typescript
function isReachableAtTime(sx: number, sy: number, fx: number, fy: number, t: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $fx
     * @param Integer $fy
     * @param Integer $t
     * @return Boolean
     */
    function isReachableAtTime($sx, $sy, $fx, $fy, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isReachableAtTime(_ sx: Int, _ sy: Int, _ fx: Int, _ fy: Int, _ t: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    
  }
}
```

### Go

```golang
func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} fx
# @param {Integer} fy
# @param {Integer} t
# @return {Boolean}
def is_reachable_at_time(sx, sy, fx, fy, t)
    
end
```

### Scala

```scala
object Solution {
    def isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-reachable-at-time sx sy fx fy t)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_reachable_at_time(Sx :: integer(), Sy :: integer(), Fx :: integer(), Fy :: integer(), T :: integer()) -> boolean().
is_reachable_at_time(Sx, Sy, Fx, Fy, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_reachable_at_time(sx :: integer, sy :: integer, fx :: integer, fy :: integer, t :: integer) :: boolean
  def is_reachable_at_time(sx, sy, fx, fy, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isReachableAtTime(sx: Int64, sy: Int64, fx: Int64, fy: Int64, t: Int64): Bool {

    }
}
```

