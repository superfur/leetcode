# LCR 105. 岛屿的最大面积

## 题目描述

<p>给定一个由&nbsp;<code>0</code> 和 <code>1</code> 组成的非空二维数组&nbsp;<code>grid</code>&nbsp;，用来表示海洋岛屿地图。</p>

<p>一个&nbsp;<strong>岛屿</strong>&nbsp;是由一些相邻的&nbsp;<code>1</code>&nbsp;(代表土地) 构成的组合，这里的「相邻」要求两个 <code>1</code> 必须在水平或者竖直方向上相邻。你可以假设&nbsp;<code>grid</code> 的四个边缘都被 <code>0</code>（代表水）包围着。</p>

<p>找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1626667010-nSGPXz-image.png" style="width: 452px; " /></p>

<pre>
<strong>输入: </strong>grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>输出: </strong>6
<strong>解释: </strong>对于上面这个给定矩阵应返回&nbsp;<code>6</code>。注意答案不应该是 <code>11</code> ，因为岛屿只能包含水平或垂直的四个方向的 <code>1</code> 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>grid = [[0,0,0,0,0,0,0,0]]
<strong>输出: </strong>0</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j] is either 0 or 1</code></li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 695&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/max-area-of-island/">https://leetcode-cn.com/problems/max-area-of-island/</a></p>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 示例

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
[[0,0,0,0,0,0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {

    }
};
```

### Java

```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {

    }
}
```

### Python

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
```

### C

```c


int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){

}
```

### C#

```csharp
public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {

};
```

### TypeScript

```typescript
function maxAreaOfIsland(grid: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxAreaOfIsland($grid) {

    }
}
```

### Swift

```swift
class Solution {
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func maxAreaOfIsland(grid [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)

end
```

### Scala

```scala
object Solution {
    def maxAreaOfIsland(grid: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (max-area-of-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec max_area_of_island(Grid :: [[integer()]]) -> integer().
max_area_of_island(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_area_of_island(grid :: [[integer]]) :: integer
  def max_area_of_island(grid) do

  end
end
```

