# 934. 最短的桥

## 题目描述

<p>给你一个大小为 <code>n x n</code> 的二元矩阵 <code>grid</code> ，其中 <code>1</code> 表示陆地，<code>0</code> 表示水域。</p>

<p><strong>岛</strong> 是由四面相连的 <code>1</code> 形成的一个最大组，即不会与非组内的任何其他 <code>1</code> 相连。<code>grid</code> 中 <strong>恰好存在两座岛</strong> 。</p>

<div class="original__bRMd">
<div>
<p>你可以将任意数量的 <code>0</code> 变为 <code>1</code> ，以使两座岛连接起来，变成 <strong>一座岛</strong> 。</p>

<p>返回必须翻转的 <code>0</code> 的最小数目。</p>
</div>
</div>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[0,1],[1,0]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[0,1,0],[0,0,0],[0,0,1]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>grid</code> 中恰有两个岛</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵

## 示例

```
[[0,1],[1,0]]
[[0,1,0],[0,0,0],[0,0,1]]
[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestBridge(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int shortestBridge(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestBridge(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    
};
```

### TypeScript

```typescript
function shortestBridge(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestBridge($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestBridge(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestBridge(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestBridge(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func shortestBridge(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def shortest_bridge(grid)
    
end
```

### Scala

```scala
object Solution {
    def shortestBridge(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_bridge(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-bridge grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_bridge(Grid :: [[integer()]]) -> integer().
shortest_bridge(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_bridge(grid :: [[integer]]) :: integer
  def shortest_bridge(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestBridge(grid: Array<Array<Int64>>): Int64 {

    }
}
```

