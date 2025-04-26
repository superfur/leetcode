# 780. 到达终点

## 题目描述

<p>给定四个整数&nbsp;<code>sx</code>&nbsp;,&nbsp;<code>sy</code>&nbsp;，<code>tx</code>&nbsp;和&nbsp;<code>ty</code>，如果通过一系列的<strong>转换</strong>可以从起点&nbsp;<code>(sx, sy)</code>&nbsp;到达终点&nbsp;<code>(tx, ty)</code>，则返回 <code>true</code>，否则返回&nbsp;<code>false</code>。</p>

<p>从点&nbsp;<code>(x, y)</code>&nbsp;可以<strong>转换</strong>到&nbsp;<code>(x, x+y)</code>&nbsp; 或者&nbsp;<code>(x+y, y)</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> sx = 1, sy = 1, tx = 3, ty = 5
<strong>输出:</strong> true
<strong>解释:
</strong>可以通过以下一系列<strong>转换</strong>从起点转换到终点：
(1, 1) -&gt; (1, 2)
(1, 2) -&gt; (3, 2)
(3, 2) -&gt; (3, 5)
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> sx = 1, sy = 1, tx = 2, ty = 2 
<strong>输出:</strong> false
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> sx = 1, sy = 1, tx = 1, ty = 1 
<strong>输出:</strong> true
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= sx, sy, tx, ty &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学

## 示例

```
1
1
3
5
1
1
2
2
1
1
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
```

### C

```c
bool reachingPoints(int sx, int sy, int tx, int ty) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ReachingPoints(int sx, int sy, int tx, int ty) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} tx
 * @param {number} ty
 * @return {boolean}
 */
var reachingPoints = function(sx, sy, tx, ty) {
    
};
```

### TypeScript

```typescript
function reachingPoints(sx: number, sy: number, tx: number, ty: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $tx
     * @param Integer $ty
     * @return Boolean
     */
    function reachingPoints($sx, $sy, $tx, $ty) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reachingPoints(_ sx: Int, _ sy: Int, _ tx: Int, _ ty: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool reachingPoints(int sx, int sy, int tx, int ty) {
    
  }
}
```

### Go

```golang
func reachingPoints(sx int, sy int, tx int, ty int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Boolean}
def reaching_points(sx, sy, tx, ty)
    
end
```

### Scala

```scala
object Solution {
    def reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reaching_points(sx: i32, sy: i32, tx: i32, ty: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (reaching-points sx sy tx ty)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec reaching_points(Sx :: integer(), Sy :: integer(), Tx :: integer(), Ty :: integer()) -> boolean().
reaching_points(Sx, Sy, Tx, Ty) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reaching_points(sx :: integer, sy :: integer, tx :: integer, ty :: integer) :: boolean
  def reaching_points(sx, sy, tx, ty) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reachingPoints(sx: Int64, sy: Int64, tx: Int64, ty: Int64): Bool {

    }
}
```

