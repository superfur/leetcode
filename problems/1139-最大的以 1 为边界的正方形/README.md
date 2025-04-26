# 1139. 最大的以 1 为边界的正方形

## 题目描述

<p>给你一个由若干 <code>0</code> 和 <code>1</code> 组成的二维网格&nbsp;<code>grid</code>，请你找出边界全部由 <code>1</code> 组成的最大 <strong>正方形</strong> 子网格，并返回该子网格中的元素数量。如果不存在，则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>输出：</strong>9
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>grid = [[1,1,0,0]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length &lt;= 100</code></li>
	<li><code>1 &lt;= grid[0].length &lt;= 100</code></li>
	<li><code>grid[i][j]</code> 为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. For each square, know how many ones are up, left, down, and right of this square. You can find it in O(N^2) using dynamic programming.
2. Now for each square ( O(N^3) ), we can evaluate whether that square is 1-bordered in O(1).

## 示例

```
[[1,1,1],[1,0,1],[1,1,1]]
[[1,1,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int largest1BorderedSquare(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Largest1BorderedSquare(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largest1BorderedSquare = function(grid) {
    
};
```

### TypeScript

```typescript
function largest1BorderedSquare(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largest1BorderedSquare($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largest1BorderedSquare(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largest1BorderedSquare(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largest1BorderedSquare(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func largest1BorderedSquare(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def largest1_bordered_square(grid)
    
end
```

### Scala

```scala
object Solution {
    def largest1BorderedSquare(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest1_bordered_square(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest1-bordered-square grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest1_bordered_square(Grid :: [[integer()]]) -> integer().
largest1_bordered_square(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest1_bordered_square(grid :: [[integer]]) :: integer
  def largest1_bordered_square(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largest1BorderedSquare(grid: Array<Array<Int64>>): Int64 {

    }
}
```

