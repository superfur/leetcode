# 807. 保持城市天际线

## 题目描述

<p>给你一座由 <code>n x n</code> 个街区组成的城市，每个街区都包含一座立方体建筑。给你一个下标从 <strong>0</strong> 开始的 <code>n x n</code> 整数矩阵 <code>grid</code> ，其中 <code>grid[r][c]</code> 表示坐落于 <code>r</code> 行 <code>c</code> 列的建筑物的 <strong>高度</strong> 。</p>

<p>城市的 <strong>天际线</strong> 是从远处观察城市时，所有建筑物形成的外部轮廓。从东、南、西、北四个主要方向观测到的 <strong>天际线</strong> 可能不同。</p>

<p>我们被允许为 <strong>任意数量的建筑物 </strong>的高度增加<strong> 任意增量（不同建筑物的增量可能不同）</strong> 。 高度为 <code>0</code> 的建筑物的高度也可以增加。然而，增加的建筑物高度 <strong>不能影响</strong> 从任何主要方向观察城市得到的 <strong>天际线</strong> 。</p>

<p>在 <strong>不改变</strong> 从任何主要方向观测到的城市 <strong>天际线</strong> 的前提下，返回建筑物可以增加的 <strong>最大高度增量总和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/21/807-ex1.png" style="width: 700px; height: 603px;" />
<pre>
<strong>输入：</strong>grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>输出：</strong>35
<strong>解释：</strong>建筑物的高度如上图中心所示。
用红色绘制从不同方向观看得到的天际线。
在不影响天际线的情况下，增加建筑物的高度：
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[0,0,0],[0,0,0],[0,0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>增加任何建筑物的高度都会导致天际线的变化。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[r].length</code></li>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[r][c] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵

## 示例

```
[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
[[0,0,0],[0,0,0],[0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxIncreaseKeepingSkyline(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    
};
```

### TypeScript

```typescript
function maxIncreaseKeepingSkyline(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxIncreaseKeepingSkyline($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxIncreaseKeepingSkyline(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxIncreaseKeepingSkyline(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxIncreaseKeepingSkyline(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maxIncreaseKeepingSkyline(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
    
end
```

### Scala

```scala
object Solution {
    def maxIncreaseKeepingSkyline(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-increase-keeping-skyline grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_increase_keeping_skyline(Grid :: [[integer()]]) -> integer().
max_increase_keeping_skyline(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_increase_keeping_skyline(grid :: [[integer]]) :: integer
  def max_increase_keeping_skyline(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxIncreaseKeepingSkyline(grid: Array<Array<Int64>>): Int64 {

    }
}
```

