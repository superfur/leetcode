# 3393. 统计异或值为给定值的路径数目

## 题目描述

<p>给你一个大小为 <code>m x n</code>&nbsp;的二维整数数组&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你的任务是统计满足以下 <strong>条件</strong> 且从左上格子&nbsp;<code>(0, 0)</code>&nbsp;出发到达右下格子&nbsp;<code>(m - 1, n - 1)</code>&nbsp;的路径数目：</p>

<ul>
	<li>每一步你可以向右或者向下走，也就是如果格子存在的话，可以从格子&nbsp;<code>(i, j)</code>&nbsp;走到格子&nbsp;<code>(i, j + 1)</code>&nbsp;或者格子&nbsp;<code>(i + 1, j)</code>&nbsp;。</li>
	<li>路径上经过的所有数字&nbsp;<code>XOR</code>&nbsp;异或值必须 <strong>等于</strong>&nbsp;<code>k</code>&nbsp;。</li>
</ul>

<p>请你返回满足上述条件的路径总数。</p>

<p>由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<p>3 条路径分别为：</p>

<ul>
	<li><code>(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)</code></li>
	<li><code>(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)</code></li>
	<li><code>(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)</code></li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<p>5 条路径分别为：</p>

<ul>
	<li><code>(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)</code></li>
	<li><code>(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)</code></li>
	<li><code>(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)</code></li>
	<li><code>(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)</code></li>
	<li><code>(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)</code></li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 300</code></li>
	<li><code>1 &lt;= n == grid[r].length &lt;= 300</code></li>
	<li><code>0 &lt;= grid[r][c] &lt; 16</code></li>
	<li><code>0 &lt;= k &lt; 16</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 矩阵

## 提示

1. Use DP.

## 示例

```
[[2,1,5],[7,10,0],[12,6,4]]
11
[[1,3,3,3],[0,3,3,2],[3,0,1,1]]
2
[[1,1,1,2],[3,0,3,2],[3,0,2,2]]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPathsWithXorValue(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        
```

### C

```c
int countPathsWithXorValue(int** grid, int gridSize, int* gridColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPathsWithXorValue(int[][] grid, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countPathsWithXorValue = function(grid, k) {
    
};
```

### TypeScript

```typescript
function countPathsWithXorValue(grid: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function countPathsWithXorValue($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPathsWithXorValue(_ grid: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPathsWithXorValue(grid: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPathsWithXorValue(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func countPathsWithXorValue(grid [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_paths_with_xor_value(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def countPathsWithXorValue(grid: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_paths_with_xor_value(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-paths-with-xor-value grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_paths_with_xor_value(Grid :: [[integer()]], K :: integer()) -> integer().
count_paths_with_xor_value(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_paths_with_xor_value(grid :: [[integer]], k :: integer) :: integer
  def count_paths_with_xor_value(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPathsWithXorValue(grid: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

