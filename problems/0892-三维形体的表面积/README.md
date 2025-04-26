# 892. 三维形体的表面积

## 题目描述

<p>给你一个 <code>n * n</code> 的网格&nbsp;<code>grid</code> ，上面放置着一些&nbsp;<code>1 x 1 x 1</code>&nbsp;的正方体。每个值&nbsp;<code>v = grid[i][j]</code>&nbsp;表示&nbsp;<code>v</code>&nbsp;个正方体叠放在对应单元格&nbsp;<code>(i, j)</code>&nbsp;上。</p>

<p>放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。</p>

<p>请你返回最终这些形体的总表面积。</p>

<p><strong>注意：</strong>每个形体的底面也需要计入表面积中。</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg" style="height: 80px; width: 80px;" />
<pre>
<strong>输入：</strong>grid = [[1,2],[3,4]]
<strong>输出：</strong>34
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg" style="height: 100px; width: 100px;" />
<pre>
<strong>输入：</strong>grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>输出：</strong>32
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg" style="height: 100px; width: 100px;" />
<pre>
<strong>输入：</strong>grid = [[2,2,2],[2,1,2],[2,2,2]]
<strong>输出：</strong>46
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数组
- 数学
- 矩阵

## 示例

```
[[1,2],[3,4]]
[[1,1,1],[1,0,1],[1,1,1]]
[[2,2,2],[2,1,2],[2,2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int surfaceArea(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int surfaceArea(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SurfaceArea(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var surfaceArea = function(grid) {
    
};
```

### TypeScript

```typescript
function surfaceArea(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function surfaceArea($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func surfaceArea(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun surfaceArea(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int surfaceArea(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func surfaceArea(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def surface_area(grid)
    
end
```

### Scala

```scala
object Solution {
    def surfaceArea(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (surface-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec surface_area(Grid :: [[integer()]]) -> integer().
surface_area(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec surface_area(grid :: [[integer]]) :: integer
  def surface_area(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func surfaceArea(grid: Array<Array<Int64>>): Int64 {

    }
}
```

