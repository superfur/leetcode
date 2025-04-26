# 2352. 相等行列对

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>n x n</code> 的整数矩阵 <code>grid</code> ，返回满足 <code>R<sub>i</sub></code><em> </em>行和<em> </em><code>C<sub>j</sub></code><em> </em>列相等的行列对<em> </em><code>(R<sub>i</sub>, C<sub>j</sub>)</code><em> </em>的数目<em>。</em></p>

<p>如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg" style="width: 150px; height: 153px;" /></p>

<pre>
<strong>输入：</strong>grid = [[3,2,1],[1,7,6],[2,7,7]]
<strong>输出：</strong>1
<strong>解释：</strong>存在一对相等行列对：
- (第 2 行，第 1 列)：[2,7,7]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg" style="width: 200px; height: 209px;" /></p>

<pre>
<strong>输入：</strong>grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
<strong>输出：</strong>3
<strong>解释：</strong>存在三对相等行列对：
- (第 0 行，第 0 列)：[3,1,2,2]
- (第 2 行, 第 2 列)：[2,4,2,2]
- (第 3 行, 第 2 列)：[2,4,2,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 矩阵
- 模拟

## 提示

1. We can use nested loops to compare every row against every column.
2. Another loop is necessary to compare the row and column element by element.
3. It is also possible to hash the arrays and compare the hashed values instead.

## 示例

```
[[3,2,1],[1,7,6],[2,7,7]]
[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int equalPairs(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int equalPairs(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EqualPairs(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    
};
```

### TypeScript

```typescript
function equalPairs(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function equalPairs($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func equalPairs(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun equalPairs(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int equalPairs(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func equalPairs(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def equal_pairs(grid)
    
end
```

### Scala

```scala
object Solution {
    def equalPairs(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (equal-pairs grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec equal_pairs(Grid :: [[integer()]]) -> integer().
equal_pairs(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec equal_pairs(grid :: [[integer]]) :: integer
  def equal_pairs(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func equalPairs(grid: Array<Array<Int64>>): Int64 {

    }
}
```

