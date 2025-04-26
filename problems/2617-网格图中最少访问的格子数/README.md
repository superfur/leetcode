# 2617. 网格图中最少访问的格子数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的&nbsp;<code>m x n</code>&nbsp;整数矩阵&nbsp;<code>grid</code>&nbsp;。你一开始的位置在&nbsp;<strong>左上角</strong>&nbsp;格子&nbsp;<code>(0, 0)</code>&nbsp;。</p>

<p>当你在格子&nbsp;<code>(i, j)</code>&nbsp;的时候，你可以移动到以下格子之一：</p>

<ul>
	<li>满足 <code>j &lt; k &lt;= grid[i][j] + j</code>&nbsp;的格子&nbsp;<code>(i, k)</code>&nbsp;（向右移动），或者</li>
	<li>满足 <code>i &lt; k &lt;= grid[i][j] + i</code>&nbsp;的格子&nbsp;<code>(k, j)</code>&nbsp;（向下移动）。</li>
</ul>

<p>请你返回到达 <strong>右下角</strong>&nbsp;格子&nbsp;<code>(m - 1, n - 1)</code>&nbsp;需要经过的最少移动格子数，如果无法到达右下角格子，请你返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/01/25/ex1.png" style="width: 271px; height: 171px;"></p>

<pre><b>输入：</b>grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
<b>输出：</b>4
<b>解释：</b>上图展示了到达右下角格子经过的 4 个格子。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/01/25/ex2.png" style="width: 271px; height: 171px;"></p>

<pre><b>输入：</b>grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
<b>输出：</b>3
<strong>解释：</strong>上图展示了到达右下角格子经过的 3 个格子。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/01/26/ex3.png" style="width: 181px; height: 81px;"></p>

<pre><b>输入：</b>grid = [[2,1,0],[1,0,0]]
<b>输出：</b>-1
<b>解释：</b>无法到达右下角格子。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt; m * n</code></li>
	<li><code>grid[m - 1][n - 1] == 0</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 广度优先搜索
- 并查集
- 数组
- 动态规划
- 矩阵
- 单调栈
- 堆（优先队列）

## 提示

1. For each cell (i,j), it is critical to find out the minimum number of steps to reach (i,j), denoted dis[i][j], quickly, given the tight constraint.
2. Calculate dis[i][j] going left to right, top to bottom.
3. Suppose we want to calculate dis[i][j], keep track of a priority queue that stores (dis[i][k], i, k) for all k ≤ j, and another priority queue that stores (dis[k][j], k, j) for all k ≤ i.

## 示例

```
[[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
[[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
[[2,1,0],[1,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumVisitedCells(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumVisitedCells(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumVisitedCells(int** grid, int gridSize, int* gridColSize){

}
```

### C#

```csharp
public class Solution {
    public int MinimumVisitedCells(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumVisitedCells = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumVisitedCells(grid: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumVisitedCells($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumVisitedCells(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumVisitedCells(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumVisitedCells(List<List<int>> grid) {

  }
}
```

### Go

```golang
func minimumVisitedCells(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_visited_cells(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumVisitedCells(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_visited_cells(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-visited-cells grid)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec minimum_visited_cells(Grid :: [[integer()]]) -> integer().
minimum_visited_cells(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_visited_cells(grid :: [[integer]]) :: integer
  def minimum_visited_cells(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumVisitedCells(grid: Array<Array<Int64>>): Int64 {

    }
}
```

