# 3276. 选择矩阵中单元格的最大得分

## 题目描述

<p>给你一个由正整数构成的二维矩阵 <code>grid</code>。</p>

<p>你需要从矩阵中选择<strong> 一个或多个 </strong>单元格，选中的单元格应满足以下条件：</p>

<ul>
	<li>所选单元格中的任意两个单元格都不会处于矩阵的 <strong>同一行</strong>。</li>
	<li>所选单元格的值 <strong>互不相同</strong>。</li>
</ul>

<p>你的得分为所选单元格值的<strong>总和</strong>。</p>

<p>返回你能获得的<strong> 最大 </strong>得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,2,3],[4,3,2],[1,1,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">8</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/29/grid1drawio.png" /></p>

<p>选择上图中用彩色标记的单元格，对应的值分别为 1、3 和 4 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[8,7,6],[8,3,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/29/grid8_8drawio.png" style="width: 170px; height: 114px;" /></p>

<p>选择上图中用彩色标记的单元格，对应的值分别为 7 和 8 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩
- 矩阵

## 提示

1. Sort all the cells in the grid by their values and keep track of their original positions.
2. Try dynamic programming with the following states: the current cell that we might select and a bitmask representing all the rows from which we have already selected a cell so far.

## 示例

```
[[1,2,3],[4,3,2],[1,1,1]]
[[8,7,6],[8,3,2]]
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

