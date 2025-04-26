# 576. 出界的路径数

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的网格和一个球。球的起始坐标为 <code>[startRow, startColumn]</code> 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 <strong>最多</strong> 可以移动 <code>maxMove</code> 次球。</p>

<p>给你五个整数 <code>m</code>、<code>n</code>、<code>maxMove</code>、<code>startRow</code> 以及 <code>startColumn</code> ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 296px;" />
<pre>
<strong>输入：</strong>m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
<strong>输出：</strong>6
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;" />
<pre>
<strong>输入：</strong>m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= maxMove &lt;= 50</code></li>
	<li><code>0 &lt;= startRow &lt; m</code></li>
	<li><code>0 &lt;= startColumn &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 提示

1. Is traversing every path feasible? There are many possible paths for a small matrix. Try to optimize it.
2. Can we use some space to store the number of paths and update them after every move?
3. One obvious thing: the ball will go out of the boundary only by crossing it. Also, there is only one possible way the ball can go out of the boundary from the boundary cell except for corner cells. From the corner cell, the ball can go out in two different ways.

Can you use this thing to solve the problem?

## 示例

```
2
2
2
0
0
1
3
3
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        
    }
};
```

### Java

```java
class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
```

### C

```c
int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function(m, n, maxMove, startRow, startColumn) {
    
};
```

### TypeScript

```typescript
function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $maxMove
     * @param Integer $startRow
     * @param Integer $startColumn
     * @return Integer
     */
    function findPaths($m, $n, $maxMove, $startRow, $startColumn) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPaths(_ m: Int, _ n: Int, _ maxMove: Int, _ startRow: Int, _ startColumn: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    
  }
}
```

### Go

```golang
func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer} max_move
# @param {Integer} start_row
# @param {Integer} start_column
# @return {Integer}
def find_paths(m, n, max_move, start_row, start_column)
    
end
```

### Scala

```scala
object Solution {
    def findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-paths m n maxMove startRow startColumn)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_paths(M :: integer(), N :: integer(), MaxMove :: integer(), StartRow :: integer(), StartColumn :: integer()) -> integer().
find_paths(M, N, MaxMove, StartRow, StartColumn) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_paths(m :: integer, n :: integer, max_move :: integer, start_row :: integer, start_column :: integer) :: integer
  def find_paths(m, n, max_move, start_row, start_column) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPaths(m: Int64, n: Int64, maxMove: Int64, startRow: Int64, startColumn: Int64): Int64 {

    }
}
```

