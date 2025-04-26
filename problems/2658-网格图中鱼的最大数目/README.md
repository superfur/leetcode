# 2658. 网格图中鱼的最大数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始大小为 <code>m x n</code>&nbsp;的二维整数数组&nbsp;<code>grid</code>&nbsp;，其中下标在&nbsp;<code>(r, c)</code>&nbsp;处的整数表示：</p>

<ul>
	<li>如果&nbsp;<code>grid[r][c] = 0</code>&nbsp;，那么它是一块 <strong>陆地</strong>&nbsp;。</li>
	<li>如果&nbsp;<code>grid[r][c] &gt; 0</code>&nbsp;，那么它是一块&nbsp;<strong>水域</strong>&nbsp;，且包含&nbsp;<code>grid[r][c]</code>&nbsp;条鱼。</li>
</ul>

<p>一位渔夫可以从任意 <strong>水域</strong>&nbsp;格子&nbsp;<code>(r, c)</code>&nbsp;出发，然后执行以下操作任意次：</p>

<ul>
	<li>捕捞格子&nbsp;<code>(r, c)</code>&nbsp;处所有的鱼，或者</li>
	<li>移动到相邻的 <strong>水域</strong>&nbsp;格子。</li>
</ul>

<p>请你返回渔夫最优策略下，&nbsp;<strong>最多</strong>&nbsp;可以捕捞多少条鱼。如果没有水域格子，请你返回 <code>0</code>&nbsp;。</p>

<p>格子&nbsp;<code>(r, c)</code>&nbsp;<strong>相邻</strong>&nbsp;的格子为&nbsp;<code>(r, c + 1)</code>&nbsp;，<code>(r, c - 1)</code>&nbsp;，<code>(r + 1, c)</code> 和&nbsp;<code>(r - 1, c)</code>&nbsp;，前提是相邻格子在网格图内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/03/29/example.png" style="width: 241px; height: 161px;"></p>

<pre><b>输入：</b>grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
<b>输出：</b>7
<b>解释：</b>渔夫可以从格子 <code>(1,3)</code> 出发，捕捞 3 条鱼，然后移动到格子 <code>(2,3)</code>&nbsp;，捕捞 4 条鱼。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/03/29/example2.png"></p>

<pre><b>输入：</b>grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
<b>输出：</b>1
<b>解释：</b>渔夫可以从格子 (0,0) 或者 (3,3) ，捕捞 1 条鱼。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 提示

1. Run DFS from each non-zero cell.
2. Each time you pick a cell to start from, add up the number of fish contained in the cells you visit.

## 示例

```
[[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaxFish(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int findMaxFish(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaxFish(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var findMaxFish = function(grid) {
    
};
```

### TypeScript

```typescript
function findMaxFish(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function findMaxFish($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxFish(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxFish(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaxFish(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func findMaxFish(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def find_max_fish(grid)
    
end
```

### Scala

```scala
object Solution {
    def findMaxFish(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_fish(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-fish grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_max_fish(Grid :: [[integer()]]) -> integer().
find_max_fish(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_fish(grid :: [[integer]]) :: integer
  def find_max_fish(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxFish(grid: Array<Array<Int64>>): Int64 {

    }
}
```

