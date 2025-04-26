# 3402. 使每一列严格递增的最少操作次数

## 题目描述

<p>给你一个由&nbsp;<b>非负&nbsp;</b>整数组成的 <code>m x n</code> 矩阵 <code>grid</code>。</p>

<p>在一次操作中，你可以将任意元素 <code>grid[i][j]</code> 的值增加 1。</p>

<p>返回使 <code>grid</code> 的所有列&nbsp;<strong>严格递增&nbsp;</strong>所需的&nbsp;<strong>最少&nbsp;</strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[3,2],[1,3],[3,4],[0,1]]</span></p>

<p><strong>输出:</strong> <span class="example-io">15</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>为了让第 <code>0</code>&nbsp;列严格递增，可以对 <code>grid[1][0]</code> 执行 3 次操作，对 <code>grid[2][0]</code> 执行 2 次操作，对 <code>grid[3][0]</code> 执行 6 次操作。</li>
	<li>为了让第 <code>1</code>&nbsp;列严格递增，可以对 <code>grid[3][1]</code> 执行 4 次操作。</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/firstexample.png" style="width: 200px; height: 347px;" /></div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[3,2,1],[2,1,0],[1,2,3]]</span></p>

<p><strong>输出:</strong> <span class="example-io">12</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>为了让第 <code>0</code>&nbsp;列严格递增，可以对 <code>grid[1][0]</code> 执行 2 次操作，对 <code>grid[2][0]</code> 执行 4 次操作。</li>
	<li>为了让第 <code>1</code>&nbsp;列严格递增，可以对 <code>grid[1][1]</code> 执行 2 次操作，对 <code>grid[2][1]</code> 执行 2 次操作。</li>
	<li>为了让第 <code>2</code>&nbsp;列严格递增，可以对 <code>grid[1][2]</code> 执行 2 次操作。</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/secondexample.png" style="width: 300px; height: 257px;" /></div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt; 2500</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 矩阵

## 提示

1. <code>grid[i + 1][j]</code> must be at least equal to <code>grid[i][j] + 1<code>.
2. Iterate on <code>i</code> in increasing order, and set <code>grid[i + 1][j] = max(grid[i][j]+1, grid[i + 1][j])<code>.

## 示例

```
[[3,2],[1,3],[3,4],[0,1]]
[[3,2,1],[2,1,0],[1,2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperations = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumOperations(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperations($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumOperations(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Grid :: [[integer()]]) -> integer().
minimum_operations(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(grid :: [[integer]]) :: integer
  def minimum_operations(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(grid: Array<Array<Int64>>): Int64 {

    }
}
```

