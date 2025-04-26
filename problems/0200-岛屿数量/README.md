# 200. 岛屿数量

## 题目描述

<p>给你一个由 <code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 示例

```
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int numIslands(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
```

### C

```c
int numIslands(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumIslands(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    
};
```

### TypeScript

```typescript
function numIslands(grid: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function numIslands($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numIslands(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func numIslands(grid [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
    
end
```

### Scala

```scala
object Solution {
    def numIslands(grid: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-islands grid)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_islands(Grid :: [[char()]]) -> integer().
num_islands(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_islands(grid :: [[char]]) :: integer
  def num_islands(grid) do
    
  end
end
```

