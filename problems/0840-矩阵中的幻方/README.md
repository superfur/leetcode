# 840. 矩阵中的幻方

## 题目描述

<p><code>3 x 3</code> 的幻方是一个填充有&nbsp;<strong>从 <code>1</code> 到 <code>9</code>&nbsp;</strong> 的不同数字的 <code>3 x 3</code> 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。</p>

<p>给定一个由整数组成的<code>row x col</code>&nbsp;的 <code>grid</code>，其中有多少个&nbsp;<code>3 × 3</code> 的 “幻方” 子矩阵？</p>

<p>注意：虽然幻方只能包含 1 到 9 的数字，但&nbsp;<code>grid</code> 可以包含最多15的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" /></p>

<pre>
<strong>输入: </strong>grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]
<strong>输出: </strong>1
<strong>解释: </strong>
下面的子矩阵是一个 3 x 3 的幻方：
<img src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" />
而这一个不是：
<img src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" />
总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> grid = [[8]]
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 15</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 矩阵

## 示例

```
[[4,3,8,4],[9,5,1,9],[2,7,6,2]]
[[8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumMagicSquaresInside(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numMagicSquaresInside = function(grid) {
    
};
```

### TypeScript

```typescript
function numMagicSquaresInside(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numMagicSquaresInside($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numMagicSquaresInside(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numMagicSquaresInside(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func numMagicSquaresInside(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def num_magic_squares_inside(grid)
    
end
```

### Scala

```scala
object Solution {
    def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-magic-squares-inside grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_magic_squares_inside(Grid :: [[integer()]]) -> integer().
num_magic_squares_inside(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_magic_squares_inside(grid :: [[integer]]) :: integer
  def num_magic_squares_inside(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numMagicSquaresInside(grid: Array<Array<Int64>>): Int64 {

    }
}
```

