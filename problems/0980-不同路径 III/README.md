# 980. 不同路径 III

## 题目描述

<p>在二维网格 <code>grid</code> 上，有 4 种类型的方格：</p>

<ul>
	<li><code>1</code> 表示起始方格。且只有一个起始方格。</li>
	<li><code>2</code> 表示结束方格，且只有一个结束方格。</li>
	<li><code>0</code> 表示我们可以走过的空方格。</li>
	<li><code>-1</code> 表示我们无法跨越的障碍。</li>
</ul>

<p>返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目<strong>。</strong></p>

<p><strong>每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
<strong>输出：</strong>2
<strong>解释：</strong>我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
<strong>输出：</strong>4
<strong>解释：</strong>我们有以下四条路径： 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[[0,1],[2,0]]
<strong>输出：</strong>0
<strong>解释：</strong>
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length * grid[0].length &lt;= 20</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 回溯
- 矩阵

## 示例

```
[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
[[0,1],[2,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int uniquePathsIII(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int uniquePathsIII(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UniquePathsIII(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    
};
```

### TypeScript

```typescript
function uniquePathsIII(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function uniquePathsIII($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniquePathsIII(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniquePathsIII(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int uniquePathsIII(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func uniquePathsIII(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def unique_paths_iii(grid)
    
end
```

### Scala

```scala
object Solution {
    def uniquePathsIII(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_paths_iii(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unique-paths-iii grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec unique_paths_iii(Grid :: [[integer()]]) -> integer().
unique_paths_iii(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_paths_iii(grid :: [[integer]]) :: integer
  def unique_paths_iii(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniquePathsIII(grid: Array<Array<Int64>>): Int64 {

    }
}
```

