# 1351. 统计有序矩阵中的负数

## 题目描述

<p>给你一个&nbsp;<code>m&nbsp;* n</code>&nbsp;的矩阵&nbsp;<code>grid</code>，矩阵中的元素无论是按行还是按列，都以非严格递减顺序排列。&nbsp;请你统计并返回&nbsp;<code>grid</code>&nbsp;中 <strong>负数</strong> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>输出：</strong>8
<strong>解释：</strong>矩阵中共有 8 个负数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[3,2],[1,0]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n + m)</code> 的解决方案吗？</p>


## 难度

Easy

## 标签

- 数组
- 二分查找
- 矩阵

## 提示

1. Use binary search for optimization or simply brute force.

## 示例

```
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
[[3,2],[1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int countNegatives(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int countNegatives(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountNegatives(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    
};
```

### TypeScript

```typescript
function countNegatives(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countNegatives($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countNegatives(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countNegatives(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countNegatives(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func countNegatives(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def count_negatives(grid)
    
end
```

### Scala

```scala
object Solution {
    def countNegatives(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-negatives grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_negatives(Grid :: [[integer()]]) -> integer().
count_negatives(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_negatives(grid :: [[integer]]) :: integer
  def count_negatives(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countNegatives(grid: Array<Array<Int64>>): Int64 {

    }
}
```

