# 2577. 在网格图中访问一个格子的最少时间

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的矩阵&nbsp;<code>grid</code>&nbsp;，每个元素都为 <strong>非负</strong>&nbsp;整数，其中&nbsp;<code>grid[row][col]</code>&nbsp;表示可以访问格子&nbsp;<code>(row, col)</code>&nbsp;的&nbsp;<strong>最早</strong>&nbsp;时间。也就是说当你访问格子&nbsp;<code>(row, col)</code>&nbsp;时，最少已经经过的时间为&nbsp;<code>grid[row][col]</code>&nbsp;。</p>

<p>你从 <strong>最左上角</strong>&nbsp;出发，出发时刻为 <code>0</code>&nbsp;，你必须一直移动到上下左右相邻四个格子中的 <strong>任意</strong>&nbsp;一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。</p>

<p>请你返回 <strong>最早</strong>&nbsp;到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-8.png" /></p>

<pre>
<b>输入：</b>grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
<b>输出：</b>7
<b>解释：</b>一条可行的路径为：
- 时刻 t = 0 ，我们在格子 (0,0) 。
- 时刻 t = 1 ，我们移动到格子 (0,1) ，可以移动的原因是 grid[0][1] &lt;= 1 。
- 时刻 t = 2 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] &lt;= 2 。
- 时刻 t = 3 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] &lt;= 3 。
- 时刻 t = 4 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] &lt;= 4 。
- 时刻 t = 5 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] &lt;= 5 。
- 时刻 t = 6 ，我们移动到格子 (1,3) ，可以移动的原因是 grid[1][3] &lt;= 6 。
- 时刻 t = 7 ，我们移动到格子 (2,3) ，可以移动的原因是 grid[2][3] &lt;= 7 。
最终到达时刻为 7 。这是最早可以到达的时间。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-9.png" style="width: 151px; height: 151px;" /></p>

<pre>
<b>输入：</b>grid = [[0,2,4],[3,2,1],[1,0,4]]
<b>输出：</b>-1
<b>解释：</b>没法从左上角按题目规定走到右下角。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[0][0] == 0</code></li>
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

1. Try using some algorithm that can find the shortest paths on a graph.
2. Consider the case where you have to go back and forth between two cells of the matrix to unlock some other cells.

## 示例

```
[[0,1,3,2],[5,1,2,5],[4,3,8,6]]
[[0,2,4],[3,2,1],[1,0,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTime(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumTime(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTime(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumTime = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumTime(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumTime($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTime(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTime(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTime(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumTime(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_time(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumTime(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time(Grid :: [[integer()]]) -> integer().
minimum_time(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time(grid :: [[integer]]) :: integer
  def minimum_time(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTime(grid: Array<Array<Int64>>): Int64 {

    }
}
```

