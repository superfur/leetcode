# 2290. 到达角落需要移除障碍物的最小数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>grid</code> ，数组大小为 <code>m x n</code> 。每个单元格都是两个值之一：</p>

<ul>
	<li><code>0</code> 表示一个 <strong>空</strong> 单元格，</li>
	<li><code>1</code> 表示一个可以移除的 <strong>障碍物</strong> 。</li>
</ul>

<p>你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。</p>

<p>现在你需要从左上角&nbsp;<code>(0, 0)</code> 移动到右下角 <code>(m - 1, n - 1)</code> ，返回需要移除的障碍物的 <strong>最小</strong> 数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/06/example1drawio-1.png" style="width: 605px; height: 246px;" /></p>

<pre>
<strong>输入：</strong>grid = [[0,1,1],[1,1,0],[1,1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>可以移除位于 (0, 1) 和 (0, 2) 的障碍物来创建从 (0, 0) 到 (2, 2) 的路径。
可以证明我们至少需要移除两个障碍物，所以返回 2 。
注意，可能存在其他方式来移除 2 个障碍物，创建出可行的路径。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/06/example1drawio.png" style="width: 405px; height: 246px;" /></p>

<pre>
<strong>输入：</strong>grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
<strong>输出：</strong>0
<strong>解释：</strong>不移除任何障碍物就能从 (0, 0) 到 (2, 4) ，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> <strong>或</strong> <code>1</code></li>
	<li><code>grid[0][0] == grid[m - 1][n - 1] == 0</code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 图
- 数组
- 矩阵
- 最短路
- 堆（优先队列）

## 提示

1. Model the grid as a graph where cells are nodes and edges are between adjacent cells. Edges to cells with obstacles have a cost of 1 and all other edges have a cost of 0.
2. Could you use 0-1 Breadth-First Search or Dijkstra’s algorithm?

## 示例

```
[[0,1,1],[1,1,0],[1,1,0]]
[[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumObstacles(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumObstacles(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumObstacles(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumObstacles = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumObstacles(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumObstacles($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumObstacles(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumObstacles(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumObstacles(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumObstacles(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_obstacles(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumObstacles(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-obstacles grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_obstacles(Grid :: [[integer()]]) -> integer().
minimum_obstacles(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_obstacles(grid :: [[integer]]) :: integer
  def minimum_obstacles(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumObstacles(grid: Array<Array<Int64>>): Int64 {

    }
}
```

