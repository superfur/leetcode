# 3148. 矩阵中的最大得分

## 题目描述

<p>给你一个由 <strong>正整数</strong> 组成、大小为 <code>m x n</code> 的矩阵 <code>grid</code>。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 <code>c1</code> 的单元格移动到值为 <code>c2</code> 的单元格的得分为 <code>c2 - c1</code> 。</p>

<p>你可以从<strong> 任一</strong> 单元格开始，并且必须至少移动一次。</p>

<p>返回你能得到的 <strong>最大 </strong>总得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/03/14/grid1.png" style="width: 240px; height: 240px;" />
<div class="example-block">
<p><strong>输入：</strong><span class="example-io">grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]</span></p>

<p><strong>输出：</strong><span class="example-io">9</span></p>

<p><strong>解释：</strong>从单元格 <code>(0, 1)</code> 开始，并执行以下移动：<br />
- 从单元格 <code>(0, 1)</code> 移动到 <code>(2, 1)</code>，得分为 <code>7 - 5 = 2</code> 。<br />
- 从单元格 <code>(2, 1)</code> 移动到 <code>(2, 2)</code>，得分为 <code>14 - 7 = 7</code> 。<br />
总得分为 <code>2 + 7 = 9</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/04/08/moregridsdrawio-1.png" style="width: 180px; height: 116px;" /></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">grid = [[4,3,2],[3,2,1]]</span></p>

<p><strong>输出：</strong><span class="example-io">-1</span></p>

<p><strong>解释：</strong>从单元格 <code>(0, 0)</code> 开始，执行一次移动：从 <code>(0, 0)</code> 到 <code>(0, 1)</code> 。得分为 <code>3 - 4 = -1</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Any path from a cell <code>(x1, y1)</code> to another cell <code>(x2, y2)</code> will always have a score of <code>grid[x2][y2] - grid[x1][y1]</code>.
2. Let’s say we fix the starting cell <code>(x1, y1)</code>, how to the find a cell <code>(x2, y2)</code> such that the value <code>grid[x2][y2] - grid[x1][y1]</code> is the maximum possible?

## 示例

```
[[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
[[4,3,2],[3,2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxScore(List<List<Integer>> grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maxScore(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxScore(IList<IList<int>> grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxScore = function(grid) {
    
};
```

### TypeScript

```typescript
function maxScore(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxScore($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(grid: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maxScore(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_score(grid)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(grid: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(Grid :: [[integer()]]) -> integer().
max_score(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(grid :: [[integer]]) :: integer
  def max_score(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(grid: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

