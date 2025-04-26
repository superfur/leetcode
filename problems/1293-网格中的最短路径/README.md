# 1293. 网格中的最短路径

## 题目描述

<p>给你一个&nbsp;<code>m * n</code>&nbsp;的网格，其中每个单元格不是&nbsp;<code>0</code>（空）就是&nbsp;<code>1</code>（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。</p>

<p>如果您 <strong>最多</strong> 可以消除 <code>k</code> 个障碍物，请找出从左上角 <code>(0, 0)</code> 到右下角 <code>(m-1, n-1)</code> 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://pic.leetcode.cn/1700710956-kcxqcC-img_v3_025f_d55a658c-8f40-464b-800f-22ccd27cc9fg.jpg" style="width: 243px; height: 404px;" /></p>

<pre>
<strong>输入：</strong> grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
<strong>输出：</strong>6
<strong>解释：
</strong>不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 <code>(0,0) -&gt; (0,1) -&gt; (0,2) -&gt; (1,2) -&gt; (2,2) -&gt; <strong>(3,2)</strong> -&gt; (4,2)</code>.
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://pic.leetcode.cn/1700710701-uPqkZe-img_v3_025f_0edd50fb-8a70-4a42-add0-f602caaad35g.jpg" style="width: 243px; height: 244px;" /></p>

<pre>
<strong>输入：</strong>grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
<strong>输出：</strong>-1
<strong>解释：</strong>我们至少需要消除两个障碍才能找到这样的路径。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>grid.length&nbsp;== m</code></li>
	<li><code>grid[0].length&nbsp;== n</code></li>
	<li><code>1 &lt;= m, n &lt;= 40</code></li>
	<li><code>1 &lt;= k &lt;= m*n</code></li>
	<li><code>grid[i][j]</code>&nbsp;是&nbsp;<code>0</code>&nbsp;或<strong>&nbsp;</strong><code>1</code></li>
	<li><code>grid[0][0] == grid[m-1][n-1] == 0</code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Use BFS.
2. BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.

## 示例

```
[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
1
[[0,1,1],[1,1,1],[1,0,0]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestPath(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
```

### C

```c
int shortestPath(int** grid, int gridSize, int* gridColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestPath(int[][] grid, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var shortestPath = function(grid, k) {
    
};
```

### TypeScript

```typescript
function shortestPath(grid: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function shortestPath($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestPath(grid: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestPath(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func shortestPath(grid [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def shortest_path(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def shortestPath(grid: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_path(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-path grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_path(Grid :: [[integer()]], K :: integer()) -> integer().
shortest_path(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_path(grid :: [[integer]], k :: integer) :: integer
  def shortest_path(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestPath(grid: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

