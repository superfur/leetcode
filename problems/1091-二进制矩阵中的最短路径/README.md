# 1091. 二进制矩阵中的最短路径

## 题目描述

<p>给你一个 <code>n x n</code> 的二进制矩阵 <code>grid</code> 中，返回矩阵中最短 <strong>畅通路径</strong> 的长度。如果不存在这样的路径，返回 <code>-1</code> 。</p>

<p>二进制矩阵中的 畅通路径 是一条从 <strong>左上角</strong> 单元格（即，<code>(0, 0)</code>）到 右下角 单元格（即，<code>(n - 1, n - 1)</code>）的路径，该路径同时满足下述要求：</p>

<ul>
	<li>路径途经的所有单元格的值都是 <code>0</code> 。</li>
	<li>路径中所有相邻的单元格应当在 <strong>8 个方向之一</strong> 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。</li>
</ul>

<p><strong>畅通路径的长度</strong> 是该路径途经的单元格总数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example1_1.png" style="width: 500px; height: 234px;" />
<pre>
<strong>输入：</strong>grid = [[0,1],[1,0]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example2_1.png" style="height: 216px; width: 500px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,0],[1,1,0],[1,1,0]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,0,0],[1,1,0],[1,1,0]]
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Do a breadth first search to find the shortest path.

## 示例

```
[[0,1],[1,0]]
[[0,0,0],[1,1,0],[1,1,0]]
[[1,0,0],[1,1,0],[1,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int shortestPathBinaryMatrix(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestPathBinaryMatrix(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    
};
```

### TypeScript

```typescript
function shortestPathBinaryMatrix(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestPathBinaryMatrix($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestPathBinaryMatrix(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestPathBinaryMatrix(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func shortestPathBinaryMatrix(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def shortest_path_binary_matrix(grid)
    
end
```

### Scala

```scala
object Solution {
    def shortestPathBinaryMatrix(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-path-binary-matrix grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_path_binary_matrix(Grid :: [[integer()]]) -> integer().
shortest_path_binary_matrix(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_path_binary_matrix(grid :: [[integer]]) :: integer
  def shortest_path_binary_matrix(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestPathBinaryMatrix(grid: Array<Array<Int64>>): Int64 {

    }
}
```

