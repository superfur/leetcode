# 2906. 构造乘积矩阵

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>n * m</code> 的二维整数矩阵 <code><font face="monospace">grid</font></code><font face="monospace"> ，定义一个下标从 <strong>0</strong> 开始、大小为 <code>n * m</code> 的的二维矩阵</font> <code>p</code>。如果满足以下条件，则称 <code>p</code> 为 <code>grid</code> 的 <strong>乘积矩阵</strong> ：</p>

<ul>
	<li>对于每个元素 <code>p[i][j]</code> ，它的值等于除了 <code>grid[i][j]</code> 外所有元素的乘积。乘积对 <code>12345</code> 取余数。</li>
</ul>

<p>返回 <code>grid</code> 的乘积矩阵。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2],[3,4]]
<strong>输出：</strong>[[24,12],[8,6]]
<strong>解释：</strong>p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
所以答案是 [[24,12],[8,6]] 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[12345],[2],[1]]
<strong>输出：</strong>[[2],[0],[0]]
<strong>解释：</strong>p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0 ，所以 p[0][1] = 0
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0 ，所以 p[0][2] = 0
所以答案是 [[2],[0],[0]] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == grid[i].length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n * m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. Try to solve this without using the <code>'/'</code> (division operation).
2. Create two 2D arrays for <b>suffix</b> and <b>prefix</b> product, and use them to find the product for each position.

## 示例

```
[[1,2],[3,4]]
[[12345],[2],[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** constructProductMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ConstructProductMatrix(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var constructProductMatrix = function(grid) {
    
};
```

### TypeScript

```typescript
function constructProductMatrix(grid: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function constructProductMatrix($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constructProductMatrix(_ grid: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constructProductMatrix(grid: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> constructProductMatrix(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func constructProductMatrix(grid [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[][]}
def construct_product_matrix(grid)
    
end
```

### Scala

```scala
object Solution {
    def constructProductMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (construct-product-matrix grid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec construct_product_matrix(Grid :: [[integer()]]) -> [[integer()]].
construct_product_matrix(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct_product_matrix(grid :: [[integer]]) :: [[integer]]
  def construct_product_matrix(grid) do
    
  end
end
```

