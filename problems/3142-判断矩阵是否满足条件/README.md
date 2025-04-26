# 3142. 判断矩阵是否满足条件

## 题目描述

<p>给你一个大小为 <code>m x n</code>&nbsp;的二维矩阵&nbsp;<code>grid</code>&nbsp;。你需要判断每一个格子&nbsp;<code>grid[i][j]</code>&nbsp;是否满足：</p>

<ul>
	<li>如果它下面的格子存在，那么它需要等于它下面的格子，也就是&nbsp;<code>grid[i][j] == grid[i + 1][j]</code>&nbsp;。</li>
	<li>如果它右边的格子存在，那么它需要不等于它右边的格子，也就是&nbsp;<code>grid[i][j] != grid[i][j + 1]</code>&nbsp;。</li>
</ul>

<p>如果 <strong>所有</strong>&nbsp;格子都满足以上条件，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,0,2],[1,0,2]]</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>网格图中所有格子都符合条件。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,1,1],[0,0,0]]</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><b>解释：</b></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/03/27/example21.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>同一行中的格子值都相等。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1],[2],[3]]</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/31/changed.png" style="width: 86px; height: 277px;padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>同一列中的格子值不相等。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 9</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Check if each column has same value in each cell.
2. If the previous condition is satisfied, we can simply check the first cells in adjacent columns.

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
    bool satisfiesConditions(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean satisfiesConditions(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        
```

### C

```c
bool satisfiesConditions(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SatisfiesConditions(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var satisfiesConditions = function(grid) {
    
};
```

### TypeScript

```typescript
function satisfiesConditions(grid: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function satisfiesConditions($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func satisfiesConditions(_ grid: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun satisfiesConditions(grid: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool satisfiesConditions(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func satisfiesConditions(grid [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Boolean}
def satisfies_conditions(grid)
    
end
```

### Scala

```scala
object Solution {
    def satisfiesConditions(grid: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (satisfies-conditions grid)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec satisfies_conditions(Grid :: [[integer()]]) -> boolean().
satisfies_conditions(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec satisfies_conditions(grid :: [[integer]]) :: boolean
  def satisfies_conditions(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func satisfiesConditions(grid: Array<Array<Int64>>): Bool {

    }
}
```

