# 1568. 使陆地分离的最少天数

## 题目描述

<p>给你一个大小为 <code>m x n</code> ，由若干 <code>0</code> 和 <code>1</code> 组成的二维网格 <code>grid</code> ，其中 <code>1</code> 表示陆地， <code>0</code> 表示水。<strong>岛屿</strong> 由水平方向或竖直方向上相邻的 <code>1</code> （陆地）连接形成。</p>

<p>如果 <strong>恰好只有一座岛屿 </strong>，则认为陆地是 <strong>连通的</strong> ；否则，陆地就是 <strong>分离的</strong> 。</p>

<p>一天内，可以将 <strong>任何单个</strong> 陆地单元（<code>1</code>）更改为水单元（<code>0</code>）。</p>

<p>返回使陆地分离的最少天数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/land1.jpg" style="width: 500px; height: 169px;" />
<pre>
<strong>输入：</strong>grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
<strong>输出：</strong>2
<strong>解释：</strong>至少需要 2 天才能得到分离的陆地。
将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/land2.jpg" style="width: 404px; height: 85px;" />
<pre>
<strong>输入：</strong>grid = [[1,1]]
<strong>输出：</strong>2
<strong>解释：</strong>如果网格中都是水，也认为是分离的 ([[1,1]] -&gt; [[0,0]])，0 岛屿。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 30</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵
- 强连通分量

## 提示

1. Return 0 if the grid is already disconnected.
2. Return 1 if changing a single land to water disconnect the island.
3. Otherwise return 2.
4. We can disconnect the grid within at most 2 days.

## 示例

```
[[0,1,1,0],[0,1,1,0],[0,0,0,0]]
[[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDays(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minDays(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDays(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minDays = function(grid) {
    
};
```

### TypeScript

```typescript
function minDays(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minDays($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDays(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDays(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDays(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minDays(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_days(grid)
    
end
```

### Scala

```scala
object Solution {
    def minDays(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_days(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-days grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_days(Grid :: [[integer()]]) -> integer().
min_days(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_days(grid :: [[integer]]) :: integer
  def min_days(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDays(grid: Array<Array<Int64>>): Int64 {

    }
}
```

