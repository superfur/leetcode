# 1289. 下降路径最小和  II

## 题目描述

<p>给你一个&nbsp;<code>n x n</code> 整数矩阵&nbsp;<code>grid</code>&nbsp;，请你返回 <strong>非零偏移下降路径</strong> 数字和的最小值。</p>

<p><strong>非零偏移下降路径</strong> 定义为：从&nbsp;<code>grid</code> 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/falling-grid.jpg" style="width: 244px; height: 245px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>13
<strong>解释：</strong>
所有非零偏移下降路径包括：
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
下降路径中数字和最小的是&nbsp;[1,5,7] ，所以答案是&nbsp;13 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[7]]
<strong>输出：</strong>7
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-99 &lt;= grid[i][j] &lt;= 99</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Use dynamic programming.
2. Let dp[i][j] be the answer for the first i rows such that column j is chosen from row i.
3. Use the concept of cumulative array to optimize the complexity of the solution.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFallingPathSum(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minFallingPathSum(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFallingPathSum(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFallingPathSum = function(grid) {
    
};
```

### TypeScript

```typescript
function minFallingPathSum(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFallingPathSum($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFallingPathSum(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFallingPathSum(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFallingPathSum(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minFallingPathSum(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_falling_path_sum(grid)
    
end
```

### Scala

```scala
object Solution {
    def minFallingPathSum(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-falling-path-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_falling_path_sum(Grid :: [[integer()]]) -> integer().
min_falling_path_sum(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_falling_path_sum(grid :: [[integer]]) :: integer
  def min_falling_path_sum(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFallingPathSum(grid: Array<Array<Int64>>): Int64 {

    }
}
```

