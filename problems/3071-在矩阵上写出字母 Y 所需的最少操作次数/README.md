# 3071. 在矩阵上写出字母 Y 所需的最少操作次数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>n x n</code> 的矩阵 <code>grid</code> ，其中 <code>n</code> 为奇数，且 <code>grid[r][c]</code> 的值为 <code>0</code> 、<code>1</code> 或 <code>2</code> 。</p>

<p>如果一个单元格属于以下三条线中的任一一条，我们就认为它是字母 <strong>Y</strong> 的一部分：</p>

<ul>
	<li>从左上角单元格开始到矩阵中心单元格结束的对角线。</li>
	<li>从右上角单元格开始到矩阵中心单元格结束的对角线。</li>
	<li>从中心单元格开始到矩阵底部边界结束的垂直线。</li>
</ul>

<p>当且仅当满足以下全部条件时，可以判定矩阵上写有字母 <strong>Y </strong>：</p>

<ul>
	<li>属于 Y 的所有单元格的值相等。</li>
	<li>不属于 Y 的所有单元格的值相等。</li>
	<li>属于 Y 的单元格的值与不属于Y的单元格的值不同。</li>
</ul>

<p>每次操作你可以将任意单元格的值改变为 <code>0</code> 、<code>1</code> 或 <code>2</code> 。返回在矩阵上写出字母 Y 所需的 <strong>最少 </strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/22/y2.png" style="width: 461px; height: 121px;" />
<pre>
<strong>输入：</strong>grid = [[1,2,2],[1,1,0],[0,1,0]]
<strong>输出：</strong>3
<strong>解释：</strong>将在矩阵上写出字母 Y 需要执行的操作用蓝色高亮显示。操作后，所有属于 Y 的单元格（加粗显示）的值都为 1 ，而不属于 Y 的单元格的值都为 0 。
可以证明，写出 Y 至少需要进行 3 次操作。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/22/y3.png" style="width: 701px; height: 201px;" />
<pre>
<strong>输入：</strong>grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
<strong>输出：</strong>12
<strong>解释：</strong>将在矩阵上写出字母 Y 需要执行的操作用蓝色高亮显示。操作后，所有属于 Y 的单元格（加粗显示）的值都为 0 ，而不属于 Y 的单元格的值都为 2 。
可以证明，写出 Y 至少需要进行 12 次操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 49</code></li>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 2</code></li>
	<li><code>n</code> 为奇数。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数
- 矩阵

## 示例

```
[[1,2,2],[1,1,0],[0,1,0]]
[[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperationsToWriteY(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperationsToWriteY(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minimumOperationsToWriteY(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperationsToWriteY(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperationsToWriteY = function(grid) {
    
};
```

### TypeScript

```typescript
function minimumOperationsToWriteY(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperationsToWriteY($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperationsToWriteY(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperationsToWriteY(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperationsToWriteY(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minimumOperationsToWriteY(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations_to_write_y(grid)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperationsToWriteY(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations_to_write_y(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations-to-write-y grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations_to_write_y(Grid :: [[integer()]]) -> integer().
minimum_operations_to_write_y(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations_to_write_y(grid :: [[integer]]) :: integer
  def minimum_operations_to_write_y(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperationsToWriteY(grid: Array<Array<Int64>>): Int64 {

    }
}
```

