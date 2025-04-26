# 3240. 最少翻转次数使二进制矩阵回文 II

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二进制矩阵&nbsp;<code>grid</code>&nbsp;。</p>

<p>如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 <strong>回文</strong>&nbsp;的。</p>

<p>你可以将 <code>grid</code>&nbsp;中任意格子的值 <strong>翻转</strong>&nbsp;，也就是将格子里的值从 <code>0</code>&nbsp;变成 <code>1</code>&nbsp;，或者从 <code>1</code>&nbsp;变成 <code>0</code>&nbsp;。</p>

<p>请你返回 <strong>最少</strong>&nbsp;翻转次数，使得矩阵中 <strong>所有</strong>&nbsp;行和列都是 <strong>回文的</strong>&nbsp;，且矩阵中 <code>1</code>&nbsp;的数目可以被 <code>4</code>&nbsp;<strong>整除</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,0,0],[0,1,0],[0,0,1]]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/08/01/image.png" style="width: 400px; height: 105px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[0,1],[0,1],[0,0]]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/08/screenshot-from-2024-07-09-01-37-48.png" style="width: 300px; height: 104px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1],[1]]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/01/screenshot-from-2024-08-01-23-05-26.png" style="width: 200px; height: 70px;" /></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m * n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 矩阵

## 提示

1. For each <code>(x, y)</code>, find <code>(m - 1 - x, y)</code>, <code>(m - 1 - x, n - 1 - y)</code>, and <code>(x, n - 1 - y)</code>; they should be the same.
2. Note that we need to specially handle the middle row (column) if the number of rows (columns) is odd.

## 示例

```
[[1,0,0],[0,1,0],[0,0,1]]
[[0,1],[0,1],[0,0]]
[[1],[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlips(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int minFlips(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlips(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFlips = function(grid) {
    
};
```

### TypeScript

```typescript
function minFlips(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFlips($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlips(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlips(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlips(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func minFlips(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_flips(grid)
    
end
```

### Scala

```scala
object Solution {
    def minFlips(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips(Grid :: [[integer()]]) -> integer().
min_flips(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips(grid :: [[integer]]) :: integer
  def min_flips(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlips(grid: Array<Array<Int64>>): Int64 {

    }
}
```

