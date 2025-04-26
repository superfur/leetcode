# 3212. 统计 X 和 Y 频数相等的子矩阵数量

## 题目描述

<p>给你一个二维字符矩阵 <code>grid</code>，其中 <code>grid[i][j]</code> 可能是 <code>'X'</code>、<code>'Y'</code> 或 <code>'.'</code>，返回满足以下条件的<span data-keyword="submatrix">子矩阵</span>数量：</p>

<ul>
	<li>包含 <code>grid[0][0]</code></li>
	<li><code>'X'</code> 和 <code>'Y'</code> 的频数相等。</li>
	<li>至少包含一个 <code>'X'</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [["X","Y","."],["Y",".","."]]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/07/examplems.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 175px; height: 350px;" /></strong></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [["X","X"],["X","Y"]]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>不存在满足 <code>'X'</code> 和 <code>'Y'</code> 频数相等的子矩阵。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[".","."],[".","."]]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>不存在满足至少包含一个 <code>'X'</code> 的子矩阵。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> 可能是 <code>'X'</code>、<code>'Y'</code> 或 <code>'.'</code>.</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 提示

1. Replace <code>’X’</code> with 1, <code>’Y’</code> with -1 and <code>’.’</code> with 0.
2. You need to find how many submatrices <code>grid[0..x][0..y]</code> have a sum of 0 and at least one <code>’X’</code>.
3. Use prefix sum to calculate submatrices sum.

## 示例

```
[["X","Y","."],["Y",".","."]]
[["X","X"],["X","Y"]]
[[".","."],[".","."]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
```

### C

```c
int numberOfSubmatrices(char** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSubmatrices(char[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numberOfSubmatrices = function(grid) {
    
};
```

### TypeScript

```typescript
function numberOfSubmatrices(grid: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function numberOfSubmatrices($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubmatrices(_ grid: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubmatrices(grid: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubmatrices(List<List<String>> grid) {
    
  }
}
```

### Go

```golang
func numberOfSubmatrices(grid [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} grid
# @return {Integer}
def number_of_submatrices(grid)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubmatrices(grid: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-submatrices grid)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_submatrices(Grid :: [[char()]]) -> integer().
number_of_submatrices(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_submatrices(grid :: [[char]]) :: integer
  def number_of_submatrices(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubmatrices(grid: Array<Array<Rune>>): Int64 {

    }
}
```

