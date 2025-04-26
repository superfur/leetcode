# 463. 岛屿的周长

## 题目描述

<p>给定一个 <code>row x col</code> 的二维网格地图 <code>grid</code> ，其中：<code>grid[i][j] = 1</code> 表示陆地， <code>grid[i][j] = 0</code> 表示水域。</p>

<p>网格中的格子 <strong>水平和垂直</strong> 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。</p>

<p>岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/island.png" /></p>

<pre>
<strong>输入：</strong>grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>输出：</strong>16
<strong>解释：</strong>它的周长是上面图片中的 16 个黄色的边</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,0]]
<strong>输出：</strong>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 <= row, col <= 100</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 示例

```
[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
[[1]]
[[1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int islandPerimeter(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int IslandPerimeter(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    
};
```

### TypeScript

```typescript
function islandPerimeter(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function islandPerimeter($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func islandPerimeter(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int islandPerimeter(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func islandPerimeter(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def island_perimeter(grid)
    
end
```

### Scala

```scala
object Solution {
    def islandPerimeter(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (island-perimeter grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec island_perimeter(Grid :: [[integer()]]) -> integer().
island_perimeter(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec island_perimeter(grid :: [[integer]]) :: integer
  def island_perimeter(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func islandPerimeter(grid: Array<Array<Int64>>): Int64 {

    }
}
```

