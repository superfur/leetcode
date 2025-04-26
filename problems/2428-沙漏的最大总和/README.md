# 2428. 沙漏的最大总和

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>grid</code> 。</p>

<p>按以下形式将矩阵的一部分定义为一个 <strong>沙漏</strong> ：</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/img.jpg" style="width: 243px; height: 243px;">
<p>返回沙漏中元素的 <strong>最大</strong> 总和。</p>

<p><strong>注意：</strong>沙漏无法旋转且必须整个包含在矩阵中。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/1.jpg" style="width: 323px; height: 323px;">
<pre><strong>输入：</strong>grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
<strong>输出：</strong>30
<strong>解释：</strong>上图中的单元格表示元素总和最大的沙漏：6 + 2 + 1 + 2 + 9 + 2 + 8 = 30 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/2.jpg" style="width: 243px; height: 243px;">
<pre><strong>输入：</strong>grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>35
<strong>解释：</strong>上图中的单元格表示元素总和最大的沙漏：1 + 2 + 3 + 5 + 7 + 8 + 9 = 35 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>3 &lt;= m, n &lt;= 150</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. Each 3x3 submatrix has exactly one hourglass.
2. Find the sum of each hourglass in the matrix and return the largest of these values.

## 示例

```
[[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
[[1,2,3],[4,5,6],[7,8,9]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSum(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int maxSum(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSum(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxSum = function(grid) {
    
};
```

### TypeScript

```typescript
function maxSum(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxSum($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSum(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSum(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSum(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func maxSum(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_sum(grid)
    
end
```

### Scala

```scala
object Solution {
    def maxSum(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum(Grid :: [[integer()]]) -> integer().
max_sum(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum(grid :: [[integer]]) :: integer
  def max_sum(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSum(grid: Array<Array<Int64>>): Int64 {

    }
}
```

