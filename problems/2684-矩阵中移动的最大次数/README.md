# 2684. 矩阵中移动的最大次数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的矩阵 <code>grid</code> ，矩阵由若干 <strong>正</strong> 整数组成。</p>

<p>你可以从矩阵第一列中的 <strong>任一</strong> 单元格出发，按以下方式遍历&nbsp;<code>grid</code> ：</p>

<ul>
	<li>从单元格 <code>(row, col)</code> 可以移动到&nbsp;<code>(row - 1, col + 1)</code>、<code>(row, col + 1)</code> 和 <code>(row + 1, col + 1)</code> 三个单元格中任一满足值 <strong>严格</strong> 大于当前单元格的单元格。</li>
</ul>

<p>返回你在矩阵中能够 <strong>移动</strong> 的 <strong>最大</strong> 次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/yetgriddrawio-10.png" style="width: 201px; height: 201px;">
<pre><strong>输入：</strong>grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
<strong>输出：</strong>3
<strong>解释：</strong>可以从单元格 (0, 0) 开始并且按下面的路径移动：
- (0, 0) -&gt; (0, 1).
- (0, 1) -&gt; (1, 2).
- (1, 2) -&gt; (2, 3).
可以证明这是能够移动的最大次数。</pre>

<p><strong>示例 2：</strong></p>

<pre><img alt="" src="https://assets.leetcode.com/uploads/2023/04/12/yetgrid4drawio.png">
<strong>输入：</strong>grid = [[3,2,4],[2,1,9],[1,1,7]]
<strong>输出：</strong>0
<strong>解释：</strong>从第一列的任一单元格开始都无法移动。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Consider using dynamic programming to find the maximum number of moves that can be made from each cell.
2. The final answer will be the maximum value in cells of the first column.

## 示例

```
[[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
[[3,2,4],[2,1,9],[1,1,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxMoves(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maxMoves(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxMoves(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxMoves = function(grid) {
    
};
```

### TypeScript

```typescript
function maxMoves(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxMoves($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxMoves(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxMoves(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxMoves(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maxMoves(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_moves(grid)
    
end
```

### Scala

```scala
object Solution {
    def maxMoves(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_moves(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-moves grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_moves(Grid :: [[integer()]]) -> integer().
max_moves(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_moves(grid :: [[integer]]) :: integer
  def max_moves(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxMoves(grid: Array<Array<Int64>>): Int64 {

    }
}
```

