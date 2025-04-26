# 1895. 最大的幻方

## 题目描述

<p>一个 <code>k x k</code> 的<strong> 幻方</strong> 指的是一个 <code>k x k</code> 填满整数的方格阵，且每一行、每一列以及两条对角线的和 <strong>全部</strong><strong>相等</strong> 。幻方中的整数 <strong>不需要互不相同</strong> 。显然，每个 <code>1 x 1</code> 的方格都是一个幻方。</p>

<p>给你一个 <code>m x n</code> 的整数矩阵 <code>grid</code> ，请你返回矩阵中 <strong>最大幻方</strong> 的 <strong>尺寸</strong> （即边长 <code>k</code>）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg" style="width: 413px; height: 335px;">
<pre><b>输入：</b>grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
<b>输出：</b>3
<b>解释：</b>最大幻方尺寸为 3 。
每一行，每一列以及两条对角线的和都等于 12 。
- 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12
- 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12
- 对角线的和：5+4+3 = 6+4+2 = 12
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg" style="width: 333px; height: 255px;">
<pre><b>输入：</b>grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
<b>输出：</b>2
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. Check all squares in the matrix and find the largest one.

## 示例

```
[[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
[[5,1,3,1],[9,3,3,1],[1,3,3,8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestMagicSquare(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int largestMagicSquare(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestMagicSquare(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestMagicSquare = function(grid) {
    
};
```

### TypeScript

```typescript
function largestMagicSquare(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestMagicSquare($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestMagicSquare(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestMagicSquare(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestMagicSquare(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func largestMagicSquare(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def largest_magic_square(grid)
    
end
```

### Scala

```scala
object Solution {
    def largestMagicSquare(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-magic-square grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_magic_square(Grid :: [[integer()]]) -> integer().
largest_magic_square(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_magic_square(grid :: [[integer]]) :: integer
  def largest_magic_square(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestMagicSquare(grid: Array<Array<Int64>>): Int64 {

    }
}
```

