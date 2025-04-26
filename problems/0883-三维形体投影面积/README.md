# 883. 三维形体投影面积

## 题目描述

<p>在<meta charset="UTF-8" />&nbsp;<code>n x n</code>&nbsp;的网格<meta charset="UTF-8" />&nbsp;<code>grid</code>&nbsp;中，我们放置了一些与 x，y，z 三轴对齐的<meta charset="UTF-8" />&nbsp;<code>1 x 1 x 1</code>&nbsp;立方体。</p>

<p>每个值&nbsp;<code>v = grid[i][j]</code>&nbsp;表示 <code>v</code>&nbsp;个正方体叠放在单元格&nbsp;<code>(i, j)</code>&nbsp;上。</p>

<p>现在，我们查看这些立方体在 <code>xy</code>&nbsp;、<code>yz</code>&nbsp;和 <code>zx</code>&nbsp;平面上的<em>投影</em>。</p>

<p><strong>投影</strong>&nbsp;就像影子，将 <strong>三维</strong> 形体映射到一个 <strong>二维</strong> 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。</p>

<p>返回 <em>所有三个投影的总面积</em> 。</p>

<p>&nbsp;</p>

<ul>
</ul>

<ul>
</ul>

<ul>
</ul>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="height: 214px; width: 800px;" /></p>

<pre>
<strong>输入：</strong>[[1,2],[3,4]]
<strong>输出：</strong>17
<strong>解释：</strong>这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入：</strong>grid = [[2]]
<strong>输出：</strong>5
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>[[1,0],[0,2]]
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
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
[[2]]
[[1,0],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int projectionArea(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int projectionArea(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ProjectionArea(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var projectionArea = function(grid) {
    
};
```

### TypeScript

```typescript
function projectionArea(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function projectionArea($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func projectionArea(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun projectionArea(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int projectionArea(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func projectionArea(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def projection_area(grid)
    
end
```

### Scala

```scala
object Solution {
    def projectionArea(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn projection_area(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (projection-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec projection_area(Grid :: [[integer()]]) -> integer().
projection_area(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec projection_area(grid :: [[integer]]) :: integer
  def projection_area(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func projectionArea(grid: Array<Array<Int64>>): Int64 {

    }
}
```

