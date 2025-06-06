# 3122. 使矩阵满足条件的最少操作次数

## 题目描述

<p>给你一个大小为 <code>m x n</code>&nbsp;的二维矩形&nbsp;<code>grid</code>&nbsp;。每次 <strong>操作</strong>&nbsp;中，你可以将 <strong>任一</strong> 格子的值修改为 <strong>任意</strong>&nbsp;非负整数。完成所有操作后，你需要确保每个格子&nbsp;<code>grid[i][j]</code>&nbsp;的值满足：</p>

<ul>
	<li>如果下面相邻格子存在的话，它们的值相等，也就是&nbsp;<code>grid[i][j] == grid[i + 1][j]</code>（如果存在）。</li>
	<li>如果右边相邻格子存在的话，它们的值不相等，也就是&nbsp;<code>grid[i][j] != grid[i][j + 1]</code>（如果存在）。</li>
</ul>

<p>请你返回需要的 <strong>最少</strong>&nbsp;操作数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,0,2],[1,0,2]]</span></p>

<p><b>输出：</b>0</p>

<p><b>解释：</b></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>矩阵中所有格子已经满足要求。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,1,1],[0,0,0]]</span></p>

<p><b>输出：</b>3</p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/03/27/example21.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>将矩阵变成&nbsp;<code>[[1,0,1],[1,0,1]]</code>&nbsp;，它满足所有要求，需要 3 次操作：</p>

<ul>
	<li>将&nbsp;<code>grid[1][0]</code>&nbsp;变为 1 。</li>
	<li>将&nbsp;<code>grid[0][1]</code> 变为 0 。</li>
	<li>将&nbsp;<code>grid[1][2]</code>&nbsp;变为 1 。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1],[2],[3]]</span></p>

<p><b>输出：</b>2</p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/31/changed.png" style="width: 86px; height: 277px;padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>这个矩阵只有一列，我们可以通过 2 次操作将所有格子里的值变为 1 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 示例

```
[[1,0,2],[1,0,2]]
[[1,1,1],[0,0,0]]
[[1],[2],[3]]
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

