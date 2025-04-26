# 861. 翻转矩阵后的得分

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的二元矩阵 <code>grid</code> ，矩阵中每个元素的值为 <code>0</code> 或 <code>1</code> 。</p>

<p>一次 <strong>移动</strong> 是指选择任一行或列，并转换该行或列中的每一个值：将所有 <code>0</code> 都更改为 <code>1</code>，将所有 <code>1</code> 都更改为 <code>0</code>。</p>

<p>在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的 <strong>得分</strong> 就是这些数字的总和。</p>

<p>在执行任意次 <strong>移动</strong> 后（含 0 次），返回可能的最高分数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-toogle1.jpg" style="width: 500px; height: 299px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
<strong>输出：</strong>39
<strong>解释：</strong>0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[0]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数组
- 矩阵

## 示例

```
[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
[[0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int matrixScore(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int matrixScore(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MatrixScore(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var matrixScore = function(grid) {
    
};
```

### TypeScript

```typescript
function matrixScore(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function matrixScore($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matrixScore(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matrixScore(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int matrixScore(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func matrixScore(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def matrix_score(grid)
    
end
```

### Scala

```scala
object Solution {
    def matrixScore(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn matrix_score(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (matrix-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec matrix_score(Grid :: [[integer()]]) -> integer().
matrix_score(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec matrix_score(grid :: [[integer]]) :: integer
  def matrix_score(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matrixScore(grid: Array<Array<Int64>>): Int64 {

    }
}
```

