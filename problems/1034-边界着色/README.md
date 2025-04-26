# 1034. 边界着色

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>grid</code> ，表示一个网格。另给你三个整数&nbsp;<code>row</code>、<code>col</code> 和 <code>color</code> 。网格中的每个值表示该位置处的网格块的颜色。</p>

<p>如果两个方块在任意 4 个方向上相邻，则称它们&nbsp;<strong>相邻 </strong>。</p>

<p>如果两个方块具有相同的颜色且相邻，它们则属于同一个 <strong>连通分量</strong> 。</p>

<p><strong>连通分量的边界</strong><strong> </strong>是指连通分量中满足下述条件之一的所有网格块：</p>

<ul>
	<li>在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻</li>
	<li>在网格的边界上（第一行/列或最后一行/列）</li>
</ul>

<p>请你使用指定颜色&nbsp;<code>color</code> 为所有包含网格块&nbsp;<code>grid[row][col]</code> 的 <strong>连通分量的边界</strong> 进行着色。</p>

<p>并返回最终的网格&nbsp;<code>grid</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
<strong>输出：</strong>[[3,3],[3,2]]</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
<strong>输出：</strong>[[1,3,3],[2,3,3]]</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
<strong>输出：</strong>[[2,2,2],[2,1,2],[2,2,2]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j], color &lt;= 1000</code></li>
	<li><code>0 &lt;= row &lt; m</code></li>
	<li><code>0 &lt;= col &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Use a DFS to find every square in the component.  Then for each square, color it if it has a neighbor that is outside the grid or a different color.

## 示例

```
[[1,1],[1,2]]
0
0
3
[[1,2,2],[2,3,2]]
0
1
3
[[1,1,1],[1,1,1],[1,1,1]]
1
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int row, int col, int color) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        
    }
}
```

### Python

```python
class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** colorBorder(int** grid, int gridSize, int* gridColSize, int row, int col, int color, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ColorBorder(int[][] grid, int row, int col, int color) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
var colorBorder = function(grid, row, col, color) {
    
};
```

### TypeScript

```typescript
function colorBorder(grid: number[][], row: number, col: number, color: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $row
     * @param Integer $col
     * @param Integer $color
     * @return Integer[][]
     */
    function colorBorder($grid, $row, $col, $color) {
        
    }
}
```

### Swift

```swift
class Solution {
    func colorBorder(_ grid: [[Int]], _ row: Int, _ col: Int, _ color: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun colorBorder(grid: Array<IntArray>, row: Int, col: Int, color: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> colorBorder(List<List<int>> grid, int row, int col, int color) {
    
  }
}
```

### Go

```golang
func colorBorder(grid [][]int, row int, col int, color int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} row
# @param {Integer} col
# @param {Integer} color
# @return {Integer[][]}
def color_border(grid, row, col, color)
    
end
```

### Scala

```scala
object Solution {
    def colorBorder(grid: Array[Array[Int]], row: Int, col: Int, color: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn color_border(grid: Vec<Vec<i32>>, row: i32, col: i32, color: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (color-border grid row col color)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec color_border(Grid :: [[integer()]], Row :: integer(), Col :: integer(), Color :: integer()) -> [[integer()]].
color_border(Grid, Row, Col, Color) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec color_border(grid :: [[integer]], row :: integer, col :: integer, color :: integer) :: [[integer]]
  def color_border(grid, row, col, color) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func colorBorder(grid: Array<Array<Int64>>, row: Int64, col: Int64, color: Int64): Array<Array<Int64>> {

    }
}
```

