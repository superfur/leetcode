# 2373. 矩阵中的局部最大值

## 题目描述

<p>给你一个大小为 <code>n x n</code> 的整数矩阵 <code>grid</code> 。</p>

<p>生成一个大小为&nbsp;<code>(n - 2) x (n - 2)</code> 的整数矩阵&nbsp; <code>maxLocal</code> ，并满足：</p>

<ul>
	<li><code>maxLocal[i][j]</code> 等于 <code>grid</code> 中以 <code>i + 1</code> 行和 <code>j + 1</code> 列为中心的 <code>3 x 3</code> 矩阵中的 <strong>最大值</strong> 。</li>
</ul>

<p>换句话说，我们希望找出 <code>grid</code> 中每个&nbsp;<code>3 x 3</code> 矩阵中的最大值。</p>

<p>返回生成的矩阵。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/21/ex1.png" style="width: 371px; height: 210px;" /></p>

<pre>
<strong>输入：</strong>grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
<strong>输出：</strong>[[9,9],[8,6]]
<strong>解释：</strong>原矩阵和生成的矩阵如上图所示。
注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/07/02/ex2new2.png" style="width: 436px; height: 240px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
<strong>输出：</strong>[[2,2,2],[2,2,2],[2,2,2]]
<strong>解释：</strong>注意，2 包含在 grid 中每个 3 x 3 的矩阵中。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Use nested loops to run through all possible 3 x 3 windows in the matrix.
2. For each 3 x 3 window, iterate through the values to get the maximum value within the window.

## 示例

```
[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
[[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] largestLocal(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** largestLocal(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] LargestLocal(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function(grid) {
    
};
```

### TypeScript

```typescript
function largestLocal(grid: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function largestLocal($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestLocal(_ grid: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestLocal(grid: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> largestLocal(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func largestLocal(grid [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[][]}
def largest_local(grid)
    
end
```

### Scala

```scala
object Solution {
    def largestLocal(grid: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (largest-local grid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec largest_local(Grid :: [[integer()]]) -> [[integer()]].
largest_local(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_local(grid :: [[integer]]) :: [[integer]]
  def largest_local(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestLocal(grid: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

