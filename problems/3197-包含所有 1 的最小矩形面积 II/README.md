# 3197. 包含所有 1 的最小矩形面积 II

## 题目描述

<p>给你一个二维 <strong>二进制 </strong>数组 <code>grid</code>。你需要找到 3 个<strong> 不重叠</strong>、面积 <strong>非零</strong> 、边在水平方向和竖直方向上的矩形，并且满足 <code>grid</code> 中所有的 1 都在这些矩形的内部。</p>

<p>返回这些矩形面积之和的<strong> 最小 </strong>可能值。</p>

<p><strong>注意</strong>，这些矩形可以相接。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,0,1],[1,1,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example0rect21.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 280px; height: 198px;" /></p>

<ul>
	<li>位于 <code>(0, 0)</code> 和 <code>(1, 0)</code> 的 1 被一个面积为 2 的矩形覆盖。</li>
	<li>位于 <code>(0, 2)</code> 和 <code>(1, 2)</code> 的 1 被一个面积为 2 的矩形覆盖。</li>
	<li>位于 <code>(1, 1)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,0,1,0],[0,1,0,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example1rect2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 356px; height: 198px;" /></p>

<ul>
	<li>位于 <code>(0, 0)</code> 和 <code>(0, 2)</code> 的 1 被一个面积为 3 的矩形覆盖。</li>
	<li>位于 <code>(1, 1)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
	<li>位于 <code>(1, 3)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> 是 0 或 1。</li>
	<li>输入保证 <code>grid</code> 中至少有三个 1 。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 枚举
- 矩阵

## 提示

1. Consider covering using 2 rectangles. As the rectangles don’t overlap, one of the rectangles must either be vertically above or horizontally left to the other.
2. To find the minimum area, check all possible vertical and horizontal splits.
3. For 3 rectangles, extend the idea to first covering using one rectangle, and then try splitting leftover ones both horizontally and vertically.

## 示例

```
[[1,0,1],[1,1,1]]
[[1,0,1,0],[0,1,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSum(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSum(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumSum(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSum(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumSum = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumSum(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumSum($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSum(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSum(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSum(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumSum(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_sum(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumSum(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_sum(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_sum(Grid :: [[integer()]]) -> integer().
minimum_sum(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(grid :: [[integer]]) :: integer
  def minimum_sum(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSum(grid: Array<Array<Int64>>): Int64 {

    }
}
```

