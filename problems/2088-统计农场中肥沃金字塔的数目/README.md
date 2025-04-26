# 2088. 统计农场中肥沃金字塔的数目

## 题目描述

<p>有一个 <strong>矩形网格</strong>&nbsp;状的农场，划分为&nbsp;<code>m</code>&nbsp;行&nbsp;<code>n</code>&nbsp;列的单元格。每个格子要么是 <strong>肥沃的</strong>&nbsp;（用 <code>1</code>&nbsp;表示），要么是 <strong>贫瘠</strong>&nbsp;的（用 <code>0</code>&nbsp;表示）。网格图以外的所有与格子都视为贫瘠的。</p>

<p>农场中的&nbsp;<strong>金字塔</strong>&nbsp;区域定义如下：</p>

<ol>
	<li>区域内格子数目 <strong>大于&nbsp;</strong><code>1</code>&nbsp;且所有格子都是 <strong>肥沃的</strong>&nbsp;。</li>
	<li>金字塔 <strong>顶端</strong>&nbsp;是这个金字塔 <strong>最上方</strong>&nbsp;的格子。金字塔的高度是它所覆盖的行数。令&nbsp;<code>(r, c)</code>&nbsp;为金字塔的顶端且高度为 <code>h</code>&nbsp;，那么金字塔区域内包含的任一格子&nbsp;<code>(i, j)</code>&nbsp;需满足&nbsp;<code>r &lt;= i &lt;= r + h - 1</code>&nbsp;<strong>且</strong>&nbsp;<code>c - (i - r) &lt;= j &lt;= c + (i - r)</code>&nbsp;。</li>
</ol>

<p>一个 <strong>倒金字塔</strong>&nbsp;类似定义如下：</p>

<ol>
	<li>区域内格子数目 <strong>大于</strong>&nbsp;<code>1</code>&nbsp;且所有格子都是 <b>肥沃的</b>&nbsp;。</li>
	<li>倒金字塔的 <strong>顶端</strong>&nbsp;是这个倒金字塔 <strong>最下方</strong>&nbsp;的格子。倒金字塔的高度是它所覆盖的行数。令&nbsp;<code>(r, c)</code>&nbsp;为金字塔的顶端且高度为 <code>h</code>&nbsp;，那么金字塔区域内包含的任一格子&nbsp;<code>(i, j)</code>&nbsp;需满足&nbsp;<code>r - h + 1 &lt;= i &lt;= r</code> <strong>且</strong> <code>c - (r - i) &lt;= j &lt;= c + (r - i)</code>&nbsp;。</li>
</ol>

<p>下图展示了部分符合定义和不符合定义的金字塔区域。黑色区域表示肥沃的格子。</p>

<p><img src="https://assets.leetcode.com/uploads/2021/11/08/image.png" style="width: 700px; height: 156px;"></p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始且大小为 <code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>grid</code>&nbsp;，它表示农场，请你返回 <code>grid</code>&nbsp;中金字塔和倒金字塔的&nbsp;<strong>总数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg11.png" style="width: 200px; height: 102px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa12.png" style="width: 200px; height: 102px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa13.png" style="width: 200px; height: 102px;"></p>

<pre><b>输入：</b>grid = [[0,1,1,0],[1,1,1,1]]
<b>输出：</b>2
<strong>解释：</strong>
2 个可能的金字塔区域分别如上图蓝色和红色区域所示。
这个网格图中没有倒金字塔区域。
所以金字塔区域总数为 2 + 0 = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg21.png" style="width: 180px; height: 122px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa22.png" style="width: 180px; height: 122px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa23.png" style="width: 180px; height: 122px;"></p>

<pre><b>输入：</b>grid = [[1,1,1],[1,1,1]]
<b>输出：</b>2
<strong>解释：</strong>
金字塔区域如上图蓝色区域所示，倒金字塔如上图红色区域所示。
所以金字塔区域总数目为 1 + 1 = 2 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg3.png" style="width: 149px; height: 150px;"></p>

<pre><b>输入：</b>grid = [[1,0,1],[0,0,0],[1,0,1]]
<b>输出：</b>0
<strong>解释：</strong>
网格图中没有任何金字塔或倒金字塔区域。
</pre>

<p><strong>示例 4：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg41.png" style="width: 180px; height: 144px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg42.png" style="width: 180px; height: 144px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg43.png" style="width: 180px; height: 144px;">&nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg44.png" style="width: 180px; height: 144px;"></p>

<pre><strong>输入：</strong>grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
<b>输出：</b>13
<strong>解释：</strong>
有 7 个金字塔区域。上图第二和第三张图中展示了它们中的 3 个。
有 6 个倒金字塔区域。上图中最后一张图展示了它们中的 2 个。
所以金字塔区域总数目为 7 + 6 = 13.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;，要么是&nbsp;<code>1</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Think about how dynamic programming can help solve the problem.
2. For any fixed cell (r, c), can you calculate the maximum height of the pyramid for which it is the apex? Let us denote this value as dp[r][c].
3. How will the values at dp[r+1][c-1] and dp[r+1][c+1] help in determining the value at dp[r][c]?
4. For the cell (r, c), is there a relation between the number of pyramids for which it serves as the apex and dp[r][c]? How does it help in calculating the answer?

## 示例

```
[[0,1,1,0],[1,1,1,1]]
[[1,1,1],[1,1,1]]
[[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPyramids(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPyramids(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int countPyramids(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPyramids(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPyramids = function(grid) {
    
};
```

### TypeScript

```typescript
function countPyramids(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPyramids($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPyramids(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPyramids(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPyramids(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func countPyramids(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def count_pyramids(grid)
    
end
```

### Scala

```scala
object Solution {
    def countPyramids(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pyramids(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pyramids grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pyramids(Grid :: [[integer()]]) -> integer().
count_pyramids(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pyramids(grid :: [[integer]]) :: integer
  def count_pyramids(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPyramids(grid: Array<Array<Int64>>): Int64 {

    }
}
```

