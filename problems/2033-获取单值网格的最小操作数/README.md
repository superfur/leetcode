# 2033. 获取单值网格的最小操作数

## 题目描述

<p>给你一个大小为&nbsp;<code>m x n</code> 的二维整数网格 <code>grid</code> 和一个整数 <code>x</code> 。每一次操作，你可以对 <code>grid</code> 中的任一元素 <strong>加</strong> <code>x</code> 或 <strong>减</strong> <code>x</code> 。</p>

<p><strong>单值网格</strong> 是全部元素都相等的网格。</p>

<p>返回使网格化为单值网格所需的 <strong>最小</strong> 操作数。如果不能，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png" style="width: 164px; height: 165px;" /></p>

<pre>
<strong>输入：</strong>grid = [[2,4],[6,8]], x = 2
<strong>输出：</strong>4
<strong>解释：</strong>可以执行下述操作使所有元素都等于 4 ： 
- 2 加 x 一次。
- 6 减 x 一次。
- 8 减 x 两次。
共计 4 次操作。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png" style="width: 164px; height: 165px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,5],[2,3]], x = 1
<strong>输出：</strong>5
<strong>解释：</strong>可以使所有元素都等于 3 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png" style="width: 164px; height: 165px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,2],[3,4]], x = 2
<strong>输出：</strong>-1
<strong>解释：</strong>无法使所有元素相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x, grid[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 矩阵
- 排序

## 提示

1. Is it possible to make two integers a and b equal if they have different remainders dividing by x?
2. If it is possible, which number should you select to minimize the number of operations?
3. What if the elements are sorted?

## 示例

```
[[2,4],[6,8]]
2
[[1,5],[2,3]]
1
[[1,2],[3,4]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[][] grid, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
```

### C

```c
int minOperations(int** grid, int gridSize, int* gridColSize, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[][] grid, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    
};
```

### TypeScript

```typescript
function minOperations(grid: number[][], x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @return Integer
     */
    function minOperations($grid, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ grid: [[Int]], _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(grid: Array<IntArray>, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<List<int>> grid, int x) {
    
  }
}
```

### Go

```golang
func minOperations(grid [][]int, x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} x
# @return {Integer}
def min_operations(grid, x)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(grid: Array[Array[Int]], x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations grid x)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Grid :: [[integer()]], X :: integer()) -> integer().
min_operations(Grid, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(grid :: [[integer]], x :: integer) :: integer
  def min_operations(grid, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(grid: Array<Array<Int64>>, x: Int64): Int64 {

    }
}
```

