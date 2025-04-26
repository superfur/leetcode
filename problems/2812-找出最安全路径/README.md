# 2812. 找出最安全路径

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>n x n</code> 的二维矩阵 <code>grid</code> ，其中 <code>(r, c)</code> 表示：</p>

<ul>
	<li>如果 <code>grid[r][c] = 1</code> ，则表示一个存在小偷的单元格</li>
	<li>如果 <code>grid[r][c] = 0</code> ，则表示一个空单元格</li>
</ul>

<p>你最开始位于单元格 <code>(0, 0)</code> 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。</p>

<p>矩阵中路径的 <strong>安全系数</strong> 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 <strong>最小</strong> 曼哈顿距离。</p>

<p>返回所有通向单元格<em> </em><code>(n - 1, n - 1)</code> 的路径中的 <strong>最大安全系数</strong> 。</p>

<p>单元格 <code>(r, c)</code> 的某个 <strong>相邻</strong> 单元格，是指在矩阵中存在的 <code>(r, c + 1)</code>、<code>(r, c - 1)</code>、<code>(r + 1, c)</code> 和 <code>(r - 1, c)</code> 之一。</p>

<p>两个单元格 <code>(a, b)</code> 和 <code>(x, y)</code> 之间的 <strong>曼哈顿距离</strong> 等于 <code>| a - x | + | b - y |</code> ，其中 <code>|val|</code> 表示 <code>val</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example1.png" style="width: 362px; height: 242px;" />
<pre>
<strong>输入：</strong>grid = [[1,0,0],[0,0,0],[0,0,1]]
<strong>输出：</strong>0
<strong>解释：</strong>从 (0, 0) 到 (n - 1, n - 1) 的每条路径都经过存在小偷的单元格 (0, 0) 和 (n - 1, n - 1) 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example2.png" style="width: 362px; height: 242px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,1],[0,0,0],[0,0,0]]
<strong>输出：</strong>2
<strong>解释：</strong>
上图所示路径的安全系数为 2：
- 该路径上距离小偷所在单元格（0，2）最近的单元格是（0，0）。它们之间的曼哈顿距离为 | 0 - 0 | + | 0 - 2 | = 2 。
可以证明，不存在安全系数更高的其他路径。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/07/02/example3.png" style="width: 362px; height: 242px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
<strong>输出：</strong>2
<strong>解释：</strong>
上图所示路径的安全系数为 2：
- 该路径上距离小偷所在单元格（0，3）最近的单元格是（1，2）。它们之间的曼哈顿距离为 | 0 - 1 | + | 3 - 2 | = 2 。
- 该路径上距离小偷所在单元格（3，0）最近的单元格是（3，2）。它们之间的曼哈顿距离为 | 3 - 3 | + | 0 - 2 | = 2 。
可以证明，不存在安全系数更高的其他路径。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length == n &lt;= 400</code></li>
	<li><code>grid[i].length == n</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>grid</code> 至少存在一个小偷</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 并查集
- 数组
- 二分查找
- 矩阵
- 堆（优先队列）

## 提示

1. Consider using both BFS and binary search together.
2. Launch a BFS starting from all the cells containing thieves to calculate d[x][y] which is the smallest Manhattan distance from (x, y) to the nearest grid that contains thieves.
3. To check if the bottom-right cell of the grid can be reached through a path of safeness factor v, eliminate all cells (x, y) such that grid[x][y]  < v. if (0, 0) and (n - 1, n - 1) are still connected, there exists a path between (0, 0) and (n - 1, n - 1) of safeness factor v.
4. Binary search over the final safeness factor v.

## 示例

```
[[1,0,0],[0,0,0],[0,0,1]]
[[0,0,1],[0,0,0],[0,0,0]]
[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maximumSafenessFactor(int** grid, int gridSize, int* gridColSize){

}
```

### C#

```csharp
public class Solution {
    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumSafenessFactor = function(grid) {
    
};
```

### TypeScript

```typescript
function maximumSafenessFactor(grid: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumSafenessFactor($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSafenessFactor(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSafenessFactor(grid: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSafenessFactor(List<List<int>> grid) {

  }
}
```

### Go

```golang
func maximumSafenessFactor(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def maximum_safeness_factor(grid)
    
end
```

### Scala

```scala
object Solution {
    def maximumSafenessFactor(grid: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-safeness-factor grid)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec maximum_safeness_factor(Grid :: [[integer()]]) -> integer().
maximum_safeness_factor(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_safeness_factor(grid :: [[integer]]) :: integer
  def maximum_safeness_factor(grid) do

  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSafenessFactor(grid: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

