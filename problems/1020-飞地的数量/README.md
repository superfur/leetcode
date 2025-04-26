# 1020. 飞地的数量

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的二进制矩阵 <code>grid</code> ，其中 <code>0</code> 表示一个海洋单元格、<code>1</code> 表示一个陆地单元格。</p>

<p>一次 <strong>移动</strong> 是指从一个陆地单元格走到另一个相邻（<strong>上、下、左、右</strong>）的陆地单元格或跨过 <code>grid</code> 的边界。</p>

<p>返回网格中<strong> 无法 </strong>在任意次数的移动中离开网格边界的陆地单元格的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg" style="height: 200px; width: 200px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
<strong>输出：</strong>3
<strong>解释：</strong>有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg" style="height: 200px; width: 200px;" />
<pre>
<strong>输入：</strong>grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>所有 1 都在边界上或可以到达边界。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 提示

1. Can you model this problem as a graph problem?  Create n * m + 1 nodes where n * m nodes represents each cell of the map and one extra node to represent the exterior of the map.
2. In the map add edges between neighbors on land cells. And add edges between the exterior and land nodes which are in the boundary.
Return as answer the number of nodes that are not reachable from the exterior node.

## 示例

```
[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int numEnclaves(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int numEnclaves(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumEnclaves(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function(grid) {
    
};
```

### TypeScript

```typescript
function numEnclaves(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numEnclaves($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numEnclaves(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numEnclaves(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numEnclaves(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func numEnclaves(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def num_enclaves(grid)
    
end
```

### Scala

```scala
object Solution {
    def numEnclaves(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_enclaves(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-enclaves grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_enclaves(Grid :: [[integer()]]) -> integer().
num_enclaves(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_enclaves(grid :: [[integer]]) :: integer
  def num_enclaves(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numEnclaves(grid: Array<Array<Int64>>): Int64 {

    }
}
```

