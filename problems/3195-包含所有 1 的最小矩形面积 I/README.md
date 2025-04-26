# 3195. 包含所有 1 的最小矩形面积 I

## 题目描述

<p>给你一个二维 <strong>二进制 </strong>数组 <code>grid</code>。请你找出一个边在水平方向和竖直方向上、面积 <strong>最小</strong> 的矩形，并且满足 <code>grid</code> 中所有的 1 都在矩形的内部。</p>

<p>返回这个矩形可能的 <strong>最小 </strong>面积。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[0,1,0],[1,0,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">6</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 279px; height: 198px;" /></p>

<p>这个最小矩形的高度为 2，宽度为 3，因此面积为 <code>2 * 3 = 6</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[0,0],[1,0]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 204px; height: 201px;" /></p>

<p>这个最小矩形的高度和宽度都是 1，因此面积为 <code>1 * 1 = 1</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> 是 0 或 1。</li>
	<li>输入保证 <code>grid</code> 中至少有一个 1 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵

## 提示

1. Find the minimum and maximum coordinates of a cell with a value of 1 in both directions.

## 示例

```
[[0,1,0],[1,0,1]]
[[1,0],[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumArea(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumArea(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumArea(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumArea(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumArea($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumArea(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumArea(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumArea(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumArea(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_area(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumArea(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_area(Grid :: [[integer()]]) -> integer().
minimum_area(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_area(grid :: [[integer]]) :: integer
  def minimum_area(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumArea(grid: Array<Array<Int64>>): Int64 {

    }
}
```

