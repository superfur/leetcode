# 2319. 判断矩阵是否是一个 X 矩阵

## 题目描述

<p>如果一个正方形矩阵满足下述 <strong>全部</strong> 条件，则称之为一个 <strong>X 矩阵</strong> ：</p>

<ol>
	<li>矩阵对角线上的所有元素都 <strong>不是 0</strong></li>
	<li>矩阵中所有其他元素都是 <strong>0</strong></li>
</ol>

<p>给你一个大小为 <code>n x n</code> 的二维整数数组 <code>grid</code> ，表示一个正方形矩阵。如果<em> </em><code>grid</code><em> </em>是一个 <strong>X 矩阵 </strong>，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex1.jpg" style="width: 311px; height: 320px;">
<pre><strong>输入：</strong>grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
<strong>输出：</strong>true
<strong>解释：</strong>矩阵如上图所示。
X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
因此，grid 是一个 X 矩阵。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex2.jpg" style="width: 238px; height: 246px;">
<pre><strong>输入：</strong>grid = [[5,7,0],[0,3,1],[0,5,0]]
<strong>输出：</strong>false
<strong>解释：</strong>矩阵如上图所示。
X 矩阵应该满足：绿色元素（对角线上）都不是 0 ，红色元素都是 0 。
因此，grid 不是一个 X 矩阵。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Assuming a 0-indexed matrix, for a given cell on row i and column j, it is in a diagonal if and only if i == j or i == n - 1 - j.
2. We can then iterate through the elements in the matrix to check if all the elements in the diagonals are non-zero and all other elements are zero.

## 示例

```
[[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
[[5,7,0],[0,3,1],[0,5,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkXMatrix(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
```

### C

```c
bool checkXMatrix(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckXMatrix(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkXMatrix = function(grid) {
    
};
```

### TypeScript

```typescript
function checkXMatrix(grid: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function checkXMatrix($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkXMatrix(_ grid: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkXMatrix(grid: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkXMatrix(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func checkXMatrix(grid [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Boolean}
def check_x_matrix(grid)
    
end
```

### Scala

```scala
object Solution {
    def checkXMatrix(grid: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_x_matrix(grid: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-x-matrix grid)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec check_x_matrix(Grid :: [[integer()]]) -> boolean().
check_x_matrix(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_x_matrix(grid :: [[integer]]) :: boolean
  def check_x_matrix(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkXMatrix(grid: Array<Array<Int64>>): Bool {

    }
}
```

