# 2245. 转角路径的乘积中最多能有几个尾随零

## 题目描述

<p>给你一个二维整数数组 <code>grid</code> ，大小为 <code>m x n</code>，其中每个单元格都含一个正整数。</p>

<p><strong>转角路径</strong> 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 <strong>向水平方向</strong> 或者 <strong>向竖直方向</strong> 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 <strong>另一个</strong> 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。</p>

<p>一条路径的 <strong>乘积</strong> 定义为：路径上所有值的乘积。</p>

<p>请你从 <code>grid</code> 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。</p>

<p>注意：</p>

<ul>
	<li><strong>水平</strong> 移动是指向左或右移动。</li>
	<li><strong>竖直 </strong>移动是指向上或下移动。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/23/ex1new2.jpg" style="width: 577px; height: 190px;" /></p>

<pre>
<strong>输入：</strong>grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
<strong>输出：</strong>3
<strong>解释：</strong>左侧的图展示了一条有效的转角路径。
其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。
可以证明在这条转角路径的乘积中尾随零数目最多。

中间的图不是一条有效的转角路径，因为它有不止一个弯。
右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/ex2.jpg" style="width: 150px; height: 157px;" /></p>

<pre>
<strong>输入：</strong>grid = [[4,3,2],[7,6,1],[8,8,8]]
<strong>输出：</strong>0
<strong>解释：</strong>网格如上图所示。
不存在乘积含尾随零的转角路径。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. What actually tells us the trailing zeros of the product of a path?
2. It is the sum of the exponents of 2 and sum of the exponents of 5 of the prime factorizations of the numbers on that path. The smaller of the two is the answer for that path.
3. We can then treat each cell as the elbow point and calculate the largest minimum (sum of 2 exponents, sum of 5 exponents) from the combination of top-left, top-right, bottom-left and bottom-right.
4. To do this efficiently, we should use the prefix sum technique.

## 示例

```
[[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
[[4,3,2],[7,6,1],[8,8,8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTrailingZeros(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTrailingZeros(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maxTrailingZeros(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTrailingZeros(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxTrailingZeros = function(grid) {
    
};
```

### TypeScript

```typescript
function maxTrailingZeros(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxTrailingZeros($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTrailingZeros(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTrailingZeros(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTrailingZeros(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maxTrailingZeros(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_trailing_zeros(grid)
    
end
```

### Scala

```scala
object Solution {
    def maxTrailingZeros(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_trailing_zeros(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-trailing-zeros grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_trailing_zeros(Grid :: [[integer()]]) -> integer().
max_trailing_zeros(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_trailing_zeros(grid :: [[integer]]) :: integer
  def max_trailing_zeros(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTrailingZeros(grid: Array<Array<Int64>>): Int64 {

    }
}
```

