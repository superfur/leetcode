# 3225. 网格图操作后的最大分数

## 题目描述

<p>给你一个大小为 <code>n x n</code>&nbsp;的二维矩阵&nbsp;<code>grid</code>&nbsp;，一开始所有格子都是白色的。一次操作中，你可以选择任意下标为&nbsp;<code>(i, j)</code>&nbsp;的格子，并将第&nbsp;<code>j</code>&nbsp;列中从最上面到第&nbsp;<code>i</code>&nbsp;行所有格子改成黑色。</p>

<p>如果格子 <code>(i, j)</code>&nbsp;为白色，且左边或者右边的格子至少一个格子为黑色，那么我们将 <code>grid[i][j]</code>&nbsp;加到最后网格图的总分中去。</p>

<p>请你返回执行任意次操作以后，最终网格图的 <strong>最大</strong>&nbsp;总分数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]</span></p>

<p><span class="example-io"><b>输出：</b>11</span></p>

<p><strong>解释：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/11/one.png" style="width: 300px; height: 200px;" />
<p>第一次操作中，我们将第 1 列中，最上面的格子到第 3 行的格子染成黑色。第二次操作中，我们将第 4 列中，最上面的格子到最后一行的格子染成黑色。最后网格图总分为&nbsp;<code>grid[3][0] + grid[1][2] + grid[3][3]</code>&nbsp;等于 11 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]</span></p>

<p><span class="example-io"><b>输出：</b>94</span></p>

<p><strong>解释：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/11/two-1.png" style="width: 300px; height: 200px;" />
<p>我们对第 1 ，2 ，3 列分别从上往下染黑色到第 1 ，4， 0 行。最后网格图总分为&nbsp;<code>grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4]</code>&nbsp;等于 94 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;n == grid.length &lt;= 100</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵
- 前缀和

## 提示

1. Use dynamic programming.
2. Solve the problem in O(N^4) using a 3-states dp.
3. Let <code>dp[i][lastHeight][beforeLastHeight]</code> denote the maximum score if the grid was limited to column <code>i</code>, and the height of column <code>i - 1</code> is <code>lastHeight</code> and the height of column <code>i - 2</code> is <code>beforeLastHeight</code>.
4. The third state, <code>beforeLastHeight</code>, is used to determine which values of column <code>i - 1</code> will be added to the score.  We can replace this state with another state that only takes two values 0 or 1.
5. Let <code>dp[i][lastHeight][isBigger]</code> denote the maximum score if the grid was limited to column <code>i</code>, and where the height of column <code>i - 1</code> is <code>lastHeight</code>. Additionally, if <code>isBigger == 1</code>, the number of black cells in column <code>i</code> is assumed to be larger than the number of black cells in column <code>i - 2</code>, and vice versa. Note that if our assumption is wrong, it would lead to a suboptimal score and, therefore, it would not be considered as the final answer.

## 示例

```
[[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
[[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumScore(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        
```

### C

```c
long long maximumScore(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumScore(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumScore = function(grid) {
    
};
```

### TypeScript

```typescript
function maximumScore(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumScore($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(grid: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maximumScore(grid [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def maximum_score(grid)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(grid: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(Grid :: [[integer()]]) -> integer().
maximum_score(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(grid :: [[integer]]) :: integer
  def maximum_score(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(grid: Array<Array<Int64>>): Int64 {

    }
}
```

