# 63. 不同路径 II

## 题目描述

<p>给定一个&nbsp;<code>m x n</code>&nbsp;的整数数组&nbsp;<code>grid</code>。一个机器人初始位于 <strong>左上角</strong>（即 <code>grid[0][0]</code>）。机器人尝试移动到 <strong>右下角</strong>（即 <code>grid[m - 1][n - 1]</code>）。机器人每次只能向下或者向右移动一步。</p>

<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。机器人的移动路径中不能包含 <strong>任何</strong>&nbsp;有障碍物的方格。</p>

<p>返回机器人能够到达右下角的不同路径数量。</p>

<p>测试用例保证答案小于等于 <code>2 * 10<sup>9</sup></code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" />
<pre>
<strong>输入：</strong>obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>输出：</strong>2
<strong>解释：</strong>3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 <code>2</code> 条不同的路径：
1. 向右 -&gt; 向右 -&gt; 向下 -&gt; 向下
2. 向下 -&gt; 向下 -&gt; 向右 -&gt; 向右
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" />
<pre>
<strong>输入：</strong>obstacleGrid = [[0,1],[0,0]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m ==&nbsp;obstacleGrid.length</code></li>
	<li><code>n ==&nbsp;obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Use dynamic programming since, from each cell, you can move to the right or down.
2. assume dp[i][j] is the number of unique paths to reach (i, j). dp[i][j] = dp[i][j -1] + dp[i - 1][j]. Be careful when you encounter an obstacle. set its value in dp to 0.

## 示例

```
[[0,0,0],[0,1,0],[0,0,0]]
[[0,1],[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
    }
};
```

### Java

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
```

### C

```c
int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    
};
```

### TypeScript

```typescript
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer
     */
    function uniquePathsWithObstacles($obstacleGrid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniquePathsWithObstacles(obstacleGrid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int uniquePathsWithObstacles(List<List<int>> obstacleGrid) {
    
  }
}
```

### Go

```golang
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} obstacle_grid
# @return {Integer}
def unique_paths_with_obstacles(obstacle_grid)
    
end
```

### Scala

```scala
object Solution {
    def uniquePathsWithObstacles(obstacleGrid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unique-paths-with-obstacles obstacleGrid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec unique_paths_with_obstacles(ObstacleGrid :: [[integer()]]) -> integer().
unique_paths_with_obstacles(ObstacleGrid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_paths_with_obstacles(obstacle_grid :: [[integer]]) :: integer
  def unique_paths_with_obstacles(obstacle_grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniquePathsWithObstacles(obstacleGrid: Array<Array<Int64>>): Int64 {

    }
}
```

