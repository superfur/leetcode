# 3446. 按对角线进行矩阵排序

## 题目描述

<p>给你一个大小为&nbsp;<code>n x n</code> 的整数方阵 <code>grid</code>。返回一个经过如下调整的矩阵：</p>

<ul>
	<li><strong>左下角三角形</strong>（包括中间对角线）的对角线按&nbsp;<strong>非递增顺序&nbsp;</strong>排序。</li>
	<li><strong>右上角三角形&nbsp;</strong>的对角线按&nbsp;<strong>非递减顺序&nbsp;</strong>排序。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,7,3],[9,8,2],[4,5,6]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[[8,2,3],[9,6,7],[4,5,1]]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example1drawio.png" style="width: 461px; height: 181px;" /></p>

<p>标有黑色箭头的对角线（左下角三角形）应按非递增顺序排序：</p>

<ul>
	<li><code>[1, 8, 6]</code> 变为 <code>[8, 6, 1]</code>。</li>
	<li><code>[9, 5]</code> 和 <code>[4]</code> 保持不变。</li>
</ul>

<p>标有蓝色箭头的对角线（右上角三角形）应按非递减顺序排序：</p>

<ul>
	<li><code>[7, 2]</code> 变为 <code>[2, 7]</code>。</li>
	<li><code>[3]</code> 保持不变。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[0,1],[1,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[[2,1],[1,0]]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example2adrawio.png" style="width: 383px; height: 141px;" /></p>

<p>标有黑色箭头的对角线必须按非递增顺序排序，因此 <code>[0, 2]</code> 变为 <code>[2, 0]</code>。其他对角线已经符合要求。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[[1]]</span></p>

<p><strong>解释：</strong></p>

<p>只有一个元素的对角线已经符合要求，因此无需修改。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>grid.length == grid[i].length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>-10<sup>5</sup> &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 排序

## 提示

1. Use a data structure to store all values in each diagonal.
2. Sort and replace them in the matrix.

## 示例

```
[[1,7,3],[9,8,2],[4,5,6]]
[[0,1],[1,2]]
[[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] sortMatrix(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** sortMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] SortMatrix(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var sortMatrix = function(grid) {
    
};
```

### TypeScript

```typescript
function sortMatrix(grid: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function sortMatrix($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortMatrix(_ grid: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortMatrix(grid: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> sortMatrix(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func sortMatrix(grid [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[][]}
def sort_matrix(grid)
    
end
```

### Scala

```scala
object Solution {
    def sortMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (sort-matrix grid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec sort_matrix(Grid :: [[integer()]]) -> [[integer()]].
sort_matrix(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_matrix(grid :: [[integer]]) :: [[integer]]
  def sort_matrix(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortMatrix(grid: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

