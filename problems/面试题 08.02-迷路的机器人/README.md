# 面试题 08.02. 迷路的机器人

## 题目描述

<p>设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png" style="height: 183px; width: 400px;" /></p>

<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。</p>

<p>返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：
</strong>[
&nbsp; [<strong>0</strong>,<strong>0</strong>,<strong>0</strong>],
&nbsp; [0,1,<strong>0</strong>],
&nbsp; [0,0,<strong>0</strong>]
]
<strong>输出：</strong>[[0,0],[0,1],[0,2],[1,2],[2,2]]
<strong>解释：
</strong>输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -&gt; 0行1列 -&gt; 0行2列 -&gt; 1行2列 -&gt; 2行2列（右下角）</pre>

<p><strong>说明：</strong><em>r</em>&nbsp;和 <em>c </em>的值均不超过 100。</p>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 回溯
- 矩阵

## 提示

1. 为了让机器人到最后一个格子，必须找出到倒数第二个格子的路径。为了到倒数第二个格子，必须找出到倒数第三个格子的路径。
2. 首先明确是否有路径，以便稍微简化这个问题。然后，修改你的算法跟踪路径。
3. 再考虑一下你算法的效率。你能优化它吗？

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> pathWithObstacles(int[][] obstacleGrid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pathWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> PathWithObstacles(int[][] obstacleGrid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} obstacleGrid
 * @return {number[][]}
 */
var pathWithObstacles = function(obstacleGrid) {
    
};
```

### TypeScript

```typescript
function pathWithObstacles(obstacleGrid: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer[][]
     */
    function pathWithObstacles($obstacleGrid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pathWithObstacles(_ obstacleGrid: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pathWithObstacles(obstacleGrid: Array<IntArray>): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> pathWithObstacles(List<List<int>> obstacleGrid) {
    
  }
}
```

### Go

```golang
func pathWithObstacles(obstacleGrid [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} obstacle_grid
# @return {Integer[][]}
def path_with_obstacles(obstacle_grid)
    
end
```

### Scala

```scala
object Solution {
    def pathWithObstacles(obstacleGrid: Array[Array[Int]]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn path_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (path-with-obstacles obstacleGrid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec path_with_obstacles(ObstacleGrid :: [[integer()]]) -> [[integer()]].
path_with_obstacles(ObstacleGrid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec path_with_obstacles(obstacle_grid :: [[integer]]) :: [[integer]]
  def path_with_obstacles(obstacle_grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pathWithObstacles(obstacleGrid: Array<Array<Int64>>): ArrayList<ArrayList<Int64>> {

    }
}
```

