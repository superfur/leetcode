# 2328. 网格图中递增路径的数目

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的整数网格图&nbsp;<code>grid</code>&nbsp;，你可以从一个格子移动到&nbsp;<code>4</code>&nbsp;个方向相邻的任意一个格子。</p>

<p>请你返回在网格图中从 <strong>任意</strong>&nbsp;格子出发，达到 <strong>任意</strong>&nbsp;格子，且路径中的数字是 <strong>严格递增</strong>&nbsp;的路径数目。由于答案可能会很大，请将结果对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/10/griddrawio-4.png" style="width: 181px; height: 121px;"></p>

<pre><b>输入：</b>grid = [[1,1],[3,4]]
<b>输出：</b>8
<b>解释：</b>严格递增路径包括：
- 长度为 1 的路径：[1]，[1]，[3]，[4] 。
- 长度为 2 的路径：[1 -&gt; 3]，[1 -&gt; 4]，[3 -&gt; 4] 。
- 长度为 3 的路径：[1 -&gt; 3 -&gt; 4] 。
路径数目为 4 + 3 + 1 = 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>grid = [[1],[2]]
<b>输出：</b>3
<b>解释：</b>严格递增路径包括：
- 长度为 1 的路径：[1]，[2] 。
- 长度为 2 的路径：[1 -&gt; 2] 。
路径数目为 2 + 1 = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序
- 记忆化搜索
- 数组
- 动态规划
- 矩阵

## 提示

1. How can you calculate the number of increasing paths that start from a cell (i, j)? Think about dynamic programming.
2. Define f(i, j) as the number of increasing paths starting from cell (i, j). Try to find how f(i, j) is related to each of f(i, j+1), f(i, j-1), f(i+1, j) and f(i-1, j).

## 示例

```
[[1,1],[3,4]]
[[1],[2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPaths(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int countPaths(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPaths(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPaths = function(grid) {
    
};
```

### TypeScript

```typescript
function countPaths(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPaths($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPaths(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPaths(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPaths(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func countPaths(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def count_paths(grid)
    
end
```

### Scala

```scala
object Solution {
    def countPaths(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_paths(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-paths grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_paths(Grid :: [[integer()]]) -> integer().
count_paths(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_paths(grid :: [[integer]]) :: integer
  def count_paths(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPaths(grid: Array<Array<Int64>>): Int64 {

    }
}
```

