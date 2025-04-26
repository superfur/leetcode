# 3459. 最长 V 形对角线段的长度

## 题目描述

<p>给你一个大小为 <code>n x m</code> 的二维整数矩阵 <code>grid</code>，其中每个元素的值为 <code>0</code>、<code>1</code> 或 <code>2</code>。</p>

<p><strong>V 形对角线段</strong> 定义如下：</p>

<ul>
	<li>线段从&nbsp;<code>1</code> 开始。</li>
	<li>后续元素按照以下无限序列的模式排列：<code>2, 0, 2, 0, ...</code>。</li>
	<li>该线段：
	<ul>
		<li>起始于某个对角方向（左上到右下、右下到左上、右上到左下或左下到右上）。</li>
		<li>沿着相同的对角方向继续，保持&nbsp;<strong>序列模式&nbsp;</strong>。</li>
		<li>在保持&nbsp;<strong>序列模式&nbsp;</strong>的前提下，最多允许&nbsp;<strong>一次顺时针 90 度转向&nbsp;</strong>另一个对角方向。</li>
	</ul>
	</li>
</ul>

<p><img alt="" src="https://pic.leetcode.cn/1739609732-jHpPma-length_of_longest3.jpg" style="width: 481px; height: 202px;" /></p>

<p>返回最长的&nbsp;<strong>V 形对角线段&nbsp;</strong>的&nbsp;<strong>长度&nbsp;</strong>。如果不存在有效的线段，则返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609768-rhePxN-matrix_1-2.jpg" style="width: 201px; height: 192px;" /></p>

<p>最长的 V 形对角线段长度为 5，路径如下：<code>(0,2) → (1,3) → (2,4)</code>，在 <code>(2,4)</code> 处进行&nbsp;<strong>顺时针 90 度转向&nbsp;</strong>，继续路径为 <code>(3,3) → (4,2)</code>。</p>
</div>

<p><strong>示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609774-nYJElV-matrix_2.jpg" style="width: 201px; height: 201px;" /></p>

<p>最长的 V 形对角线段长度为 4，路径如下：<code>(2,3) → (3,2)</code>，在 <code>(3,2)</code> 处进行&nbsp;<strong>顺时针 90 度转向&nbsp;</strong>，继续路径为 <code>(2,1) → (1,0)</code>。</p>
</div>

<p><strong>示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1739609780-tlkdUW-matrix_3.jpg" style="width: 201px; height: 201px;" /></p>

<p>最长的 V 形对角线段长度为 5，路径如下：<code>(0,0) → (1,1) → (2,2) → (3,3) → (4,4)</code>。</p>
</div>

<p><strong>示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>最长的 V 形对角线段长度为 1，路径如下：<code>(0,0)</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>m == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 500</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>0</code>、<code>1</code> 或 <code>2</code>。</li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 动态规划
- 矩阵

## 提示

1. Use dynamic programming to determine the best point to make a 90-degree rotation in the diagonal path while maintaining the required sequence.
2. Represent dynamic programming states as <code>(row, col, currentDirection, hasMadeTurnYet)</code>. Track the current position, direction of traversal, and whether a turn has already been made, and take transitions accordingly to find the longest V-shaped diagonal segment.

## 示例

```
[[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
[[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
[[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
[[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int lenOfVDiagonal(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int lenOfVDiagonal(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LenOfVDiagonal(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var lenOfVDiagonal = function(grid) {
    
};
```

### TypeScript

```typescript
function lenOfVDiagonal(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function lenOfVDiagonal($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lenOfVDiagonal(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lenOfVDiagonal(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lenOfVDiagonal(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func lenOfVDiagonal(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def len_of_v_diagonal(grid)
    
end
```

### Scala

```scala
object Solution {
    def lenOfVDiagonal(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn len_of_v_diagonal(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (len-of-v-diagonal grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec len_of_v_diagonal(Grid :: [[integer()]]) -> integer().
len_of_v_diagonal(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec len_of_v_diagonal(grid :: [[integer]]) :: integer
  def len_of_v_diagonal(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lenOfVDiagonal(grid: Array<Array<Int64>>): Int64 {

    }
}
```

