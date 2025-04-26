# 1914. 循环轮转矩阵

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>grid</code>​​​ ，其中 <code>m</code> 和 <code>n</code> 都是 <strong>偶数</strong> ；另给你一个整数 <code>k</code> 。</p>

<p>矩阵由若干层组成，如下图所示，每种颜色代表一层：</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png" style="width: 231px; height: 258px;"></p>

<p>矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 <strong>逆时针 </strong>方向的相邻元素。轮转示例如下：</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg" style="width: 500px; height: 268px;">
<p>返回执行 <code>k</code> 次循环轮转操作后的矩阵。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/rod2.png" style="width: 421px; height: 191px;">
<pre><strong>输入：</strong>grid = [[40,10],[30,20]], k = 1
<strong>输出：</strong>[[10,20],[40,30]]
<strong>解释：</strong>上图展示了矩阵在执行循环轮转操作时每一步的状态。</pre>

<p><strong>示例 2：</strong></p>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png" style="width: 231px; height: 262px;"></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png" style="width: 231px; height: 262px;"></strong> <strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png" style="width: 231px; height: 262px;"></strong>

<pre><strong>输入：</strong>grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
<strong>输出：</strong>[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
<strong>解释：</strong>上图展示了矩阵在执行循环轮转操作时每一步的状态。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 50</code></li>
	<li><code>m</code> 和 <code>n</code> 都是 <strong>偶数</strong></li>
	<li><code>1 &lt;= grid[i][j] &lt;=<sup> </sup>5000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 模拟

## 提示

1. First, you need to consider each layer separately as an array.
2. Just cycle this array and then re-assign it.

## 示例

```
[[40,10],[30,20]]
1
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] rotateGrid(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** rotateGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] RotateGrid(int[][] grid, int k) {
        
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
var rotateGrid = function(grid, k) {
    
};
```

### TypeScript

```typescript
function rotateGrid(grid: number[][], k: number): number[][] {
    
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
    function rotateGrid($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rotateGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rotateGrid(grid: Array<IntArray>, k: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> rotateGrid(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func rotateGrid(grid [][]int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def rotate_grid(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def rotateGrid(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rotate_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (rotate-grid grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec rotate_grid(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
rotate_grid(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rotate_grid(grid :: [[integer]], k :: integer) :: [[integer]]
  def rotate_grid(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rotateGrid(grid: Array<Array<Int64>>, k: Int64): Array<Array<Int64>> {

    }
}
```

