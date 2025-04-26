# 827. 最大人工岛

## 题目描述

<p>给你一个大小为 <code>n x n</code> 二进制矩阵 <code>grid</code> 。<strong>最多</strong> 只能将一格&nbsp;<code>0</code> 变成&nbsp;<code>1</code> 。</p>

<p>返回执行此操作后，<code>grid</code> 中最大的岛屿面积是多少？</p>

<p><strong>岛屿</strong> 由一组上、下、左、右四个方向相连的&nbsp;<code>1</code> 形成。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入: </strong>grid = [[1, 0], [0, 1]]
<strong>输出:</strong> 3
<strong>解释:</strong> 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入: </strong>grid =<strong> </strong>[[1, 1], [1, 0]]
<strong>输出:</strong> 4
<strong>解释:</strong> 将一格0变成1，岛屿的面积扩大为 4。</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入: </strong>grid = [[1, 1], [1, 1]]
<strong>输出:</strong> 4
<strong>解释:</strong> 没有0可以让我们变成1，面积依然为 4。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 示例

```
[[1,0],[0,1]]
[[1,1],[1,0]]
[[1,1],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestIsland(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int largestIsland(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestIsland(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestIsland = function(grid) {
    
};
```

### TypeScript

```typescript
function largestIsland(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestIsland($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestIsland(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestIsland(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func largestIsland(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def largest_island(grid)
    
end
```

### Scala

```scala
object Solution {
    def largestIsland(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_island(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_island(Grid :: [[integer()]]) -> integer().
largest_island(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_island(grid :: [[integer]]) :: integer
  def largest_island(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestIsland(grid: Array<Array<Int64>>): Int64 {

    }
}
```

