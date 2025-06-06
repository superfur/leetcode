# 1368. 使网格图至少有一条有效路径的最小代价

## 题目描述

<p>给你一个 m x n 的网格图&nbsp;<code>grid</code>&nbsp;。&nbsp;<code>grid</code>&nbsp;中每个格子都有一个数字，对应着从该格子出发下一步走的方向。&nbsp;<code>grid[i][j]</code>&nbsp;中的数字可能为以下几种情况：</p>

<ul>
	<li><strong>1</strong>&nbsp;，下一步往右走，也就是你会从 <code>grid[i][j]</code>&nbsp;走到 <code>grid[i][j + 1]</code></li>
	<li><strong>2</strong>&nbsp;，下一步往左走，也就是你会从 <code>grid[i][j]</code>&nbsp;走到 <code>grid[i][j - 1]</code></li>
	<li><strong>3</strong>&nbsp;，下一步往下走，也就是你会从 <code>grid[i][j]</code>&nbsp;走到 <code>grid[i + 1][j]</code></li>
	<li><strong>4</strong>&nbsp;，下一步往上走，也就是你会从 <code>grid[i][j]</code>&nbsp;走到 <code>grid[i - 1][j]</code></li>
</ul>

<p>注意网格图中可能会有&nbsp;<strong>无效数字</strong>&nbsp;，因为它们可能指向&nbsp;<code>grid</code>&nbsp;以外的区域。</p>

<p>一开始，你会从最左上角的格子&nbsp;<code>(0,0)</code>&nbsp;出发。我们定义一条&nbsp;<strong>有效路径</strong>&nbsp;为从格子&nbsp;<code>(0,0)</code>&nbsp;出发，每一步都顺着数字对应方向走，最终在最右下角的格子&nbsp;<code>(m - 1, n - 1)</code>&nbsp;结束的路径。有效路径&nbsp;<strong>不需要是最短路径</strong>&nbsp;。</p>

<p>你可以花费&nbsp;<code>cost = 1</code>&nbsp;的代价修改一个格子中的数字，但每个格子中的数字&nbsp;<strong>只能修改一次</strong>&nbsp;。</p>

<p>请你返回让网格图至少有一条有效路径的最小代价。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid1.png" style="height: 528px; width: 542px;"></p>

<pre><strong>输入：</strong>grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
<strong>输出：</strong>3
<strong>解释：</strong>你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --&gt; (0, 1) --&gt; (0, 2) --&gt; (0, 3) 花费代价 cost = 1 使方向向下 --&gt; (1, 3) --&gt; (1, 2) --&gt; (1, 1) --&gt; (1, 0) 花费代价 cost = 1 使方向向下 --&gt; (2, 0) --&gt; (2, 1) --&gt; (2, 2) --&gt; (2, 3) 花费代价 cost = 1 使方向向下 --&gt; (3, 3)
总花费为 cost = 3.
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid2.png" style="height: 408px; width: 419px;"></p>

<pre><strong>输入：</strong>grid = [[1,1,3],[3,2,2],[1,1,4]]
<strong>输出：</strong>0
<strong>解释：</strong>不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid3.png" style="height: 302px; width: 314px;"></p>

<pre><strong>输入：</strong>grid = [[1,2],[4,3]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>grid = [[2,2,2],[2,2,2]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>grid = [[4]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
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

1. Build a graph where grid[i][j] is connected to all the four side-adjacent cells with weighted edge. the weight is 0 if the sign is pointing to the adjacent cell or 1 otherwise.
2. Do BFS from (0, 0) visit all edges with weight = 0 first. the answer is the distance to (m -1, n - 1).

## 示例

```
[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
[[1,1,3],[3,2,2],[1,1,4]]
[[1,2],[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minCost(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    
};
```

### TypeScript

```typescript
function minCost(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minCost($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minCost(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_cost(grid)
    
end
```

### Scala

```scala
object Solution {
    def minCost(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Grid :: [[integer()]]) -> integer().
min_cost(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(grid :: [[integer]]) :: integer
  def min_cost(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(grid: Array<Array<Int64>>): Int64 {

    }
}
```

