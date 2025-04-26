# 2596. 检查骑士巡视方案

## 题目描述

<p>骑士在一张 <code>n x n</code> 的棋盘上巡视。在&nbsp;<strong>有效&nbsp;</strong>的巡视方案中，骑士会从棋盘的 <strong>左上角</strong> 出发，并且访问棋盘上的每个格子 <strong>恰好一次</strong> 。</p>

<p>给你一个 <code>n x n</code> 的整数矩阵 <code>grid</code> ，由范围 <code>[0, n * n - 1]</code> 内的不同整数组成，其中 <code>grid[row][col]</code> 表示单元格 <code>(row, col)</code> 是骑士访问的第 <code>grid[row][col]</code> 个单元格。骑士的行动是从下标 <strong>0</strong> 开始的。</p>

<p>如果 <code>grid</code> 表示了骑士的有效巡视方案，返回 <code>true</code>；否则返回 <code>false</code>。</p>

<p><strong>注意</strong>，骑士行动时可以垂直移动两个格子且水平移动一个格子，或水平移动两个格子且垂直移动一个格子。下图展示了骑士从某个格子出发可能的八种行动路线。<br />
<img alt="" src="https://pic.leetcode.cn/1694590028-CTMBQL-image.png" style="width: 350px; height: 350px;" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1694590044-AmhkRb-image.png" style="width: 251px; height: 251px;" />
<pre>
<strong>输入：</strong>grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
<strong>输出：</strong>true
<strong>解释：</strong>grid 如上图所示，可以证明这是一个有效的巡视方案。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1694590057-FIMBAG-image.png" style="width: 151px; height: 151px;" />
<pre>
<strong>输入：</strong>grid = [[0,3,6],[5,8,1],[2,7,4]]
<strong>输出：</strong>false
<strong>解释：</strong>grid 如上图所示，考虑到骑士第 7 次行动后的位置，第 8 次行动是无效的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 &lt;= n &lt;= 7</code></li>
	<li><code>0 &lt;= grid[row][col] &lt; n * n</code></li>
	<li><code>grid</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵
- 模拟

## 提示

1. It is enough to check if each move of the knight is valid.
2. Try all cases of the knight's movements to check if a move is valid.

## 示例

```
[[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
[[0,3,6],[5,8,1],[2,7,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkValidGrid(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkValidGrid(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        
```

### C

```c
bool checkValidGrid(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckValidGrid(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkValidGrid = function(grid) {
    
};
```

### TypeScript

```typescript
function checkValidGrid(grid: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function checkValidGrid($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkValidGrid(_ grid: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkValidGrid(grid: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkValidGrid(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func checkValidGrid(grid [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Boolean}
def check_valid_grid(grid)
    
end
```

### Scala

```scala
object Solution {
    def checkValidGrid(grid: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_valid_grid(grid: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-valid-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec check_valid_grid(Grid :: [[integer()]]) -> boolean().
check_valid_grid(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_valid_grid(grid :: [[integer]]) :: boolean
  def check_valid_grid(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkValidGrid(grid: Array<Array<Int64>>): Bool {

    }
}
```

