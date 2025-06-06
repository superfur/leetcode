# 3417. 跳过交替单元格的之字形遍历

## 题目描述

<p>给你一个 <code>m x n</code> 的二维数组 <code>grid</code>，数组由&nbsp;<strong>正整数</strong> 组成。</p>

<p>你的任务是以&nbsp;<strong>之字形&nbsp;</strong>遍历 <code>grid</code>，同时跳过每个&nbsp;<strong>交替&nbsp;</strong>的单元格。</p>

<p>之字形遍历的定义如下：</p>

<ul>
	<li>从左上角的单元格 <code>(0, 0)</code> 开始。</li>
	<li>在当前行中向 <strong>右</strong> 移动，直到到达该行的末尾。</li>
	<li>下移到下一行，然后在该行中向&nbsp;<strong>左</strong><em>&nbsp;</em>移动，直到到达该行的开头。</li>
	<li>继续在行间交替向右和向左移动，直到所有行都被遍历完。</li>
</ul>

<p><strong>注意：</strong>在遍历过程中，必须跳过每个&nbsp;<strong>交替&nbsp;</strong>的单元格。</p>

<p>返回一个整数数组 <code>result</code>，其中包含按&nbsp;<strong>顺序&nbsp;</strong>记录的、且跳过交替单元格后的之字形遍历中访问到的单元格值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,2],[3,4]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,4]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example0.png" style="width: 200px; height: 200px;" /></strong></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[2,1],[2,1],[2,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,1,2]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example1.png" style="width: 200px; height: 240px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,2,3],[4,5,6],[7,8,9]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,3,5,7,9]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example2.png" style="width: 260px; height: 250px;" /></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == grid.length &lt;= 50</code></li>
	<li><code>2 &lt;= m == grid[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 2500</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 模拟

## 示例

```
[[1,2],[3,4]]
[[2,1],[2,1],[2,1]]
[[1,2,3],[4,5,6],[7,8,9]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> zigzagTraversal(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* zigzagTraversal(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> ZigzagTraversal(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var zigzagTraversal = function(grid) {
    
};
```

### TypeScript

```typescript
function zigzagTraversal(grid: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function zigzagTraversal($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func zigzagTraversal(_ grid: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun zigzagTraversal(grid: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> zigzagTraversal(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func zigzagTraversal(grid [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[]}
def zigzag_traversal(grid)
    
end
```

### Scala

```scala
object Solution {
    def zigzagTraversal(grid: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn zigzag_traversal(grid: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (zigzag-traversal grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec zigzag_traversal(Grid :: [[integer()]]) -> [integer()].
zigzag_traversal(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec zigzag_traversal(grid :: [[integer]]) :: [integer]
  def zigzag_traversal(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func zigzagTraversal(grid: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

