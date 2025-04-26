# 1260. 二维网格迁移

## 题目描述

<p>给你一个 <code>m</code> 行 <code>n</code>&nbsp;列的二维网格&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>k</code>。你需要将&nbsp;<code>grid</code>&nbsp;迁移&nbsp;<code>k</code>&nbsp;次。</p>

<p>每次「迁移」操作将会引发下述活动：</p>

<ul>
	<li>位于 <code>grid[i][j]</code>（<code>j &lt; n - 1</code>）的元素将会移动到&nbsp;<code>grid[i][j + 1]</code>。</li>
	<li>位于&nbsp;<code>grid[i][n&nbsp;- 1]</code> 的元素将会移动到&nbsp;<code>grid[i + 1][0]</code>。</li>
	<li>位于 <code>grid[m&nbsp;- 1][n - 1]</code>&nbsp;的元素将会移动到&nbsp;<code>grid[0][0]</code>。</li>
</ul>

<p>请你返回&nbsp;<code>k</code> 次迁移操作后最终得到的 <strong>二维网格</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e1-1.png" style="height: 158px; width: 400px;" /></p>

<pre>
<code><strong>输入：</strong>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>输出：</strong>[[9,1,2],[3,4,5],[6,7,8]]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e2-1.png" style="height: 166px; width: 400px;" /></p>

<pre>
<code><strong>输入：</strong>grid</code> = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
<strong>输出：</strong>[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<code><strong>输入：</strong>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 9
<strong>输出：</strong>[[1,2,3],[4,5,6],[7,8,9]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m ==&nbsp;grid.length</code></li>
	<li><code>n ==&nbsp;grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 50</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>-1000 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 模拟

## 提示

1. Simulate step by step. move grid[i][j] to grid[i][j+1]. handle last column of the grid.
2. Put the matrix row by row to a vector. take k % vector.length and move last k of the vector to the beginning. put the vector to the matrix back the same way.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
1
[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
4
[[1,2,3],[4,5,6],[7,8,9]]
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> ShiftGrid(int[][] grid, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    
};
```

### TypeScript

```typescript
function shiftGrid(grid: number[][], k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shiftGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> shiftGrid(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func shiftGrid(grid [][]int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def shift_grid(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (shift-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec shift_grid(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
shift_grid(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shift_grid(grid :: [[integer]], k :: integer) :: [[integer]]
  def shift_grid(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shiftGrid(grid: Array<Array<Int64>>, k: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

