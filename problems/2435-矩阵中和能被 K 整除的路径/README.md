# 2435. 矩阵中和能被 K 整除的路径

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的&nbsp;<code>m x n</code>&nbsp;整数矩阵&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你从起点&nbsp;<code>(0, 0)</code>&nbsp;出发，每一步只能往 <strong>下</strong>&nbsp;或者往 <strong>右</strong>&nbsp;，你想要到达终点&nbsp;<code>(m - 1, n - 1)</code>&nbsp;。</p>

<p>请你返回路径和能被 <code>k</code>&nbsp;整除的路径数目，由于答案可能很大，返回答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2022/08/13/image-20220813183124-1.png" style="width: 437px; height: 200px;"></p>

<pre><b>输入：</b>grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
<b>输出：</b>2
<b>解释：</b>有两条路径满足路径上元素的和能被 k 整除。
第一条路径为上图中用红色标注的路径，和为 5 + 2 + 4 + 5 + 2 = 18 ，能被 3 整除。
第二条路径为上图中用蓝色标注的路径，和为 5 + 3 + 0 + 5 + 2 = 15 ，能被 3 整除。
</pre>

<p><strong>示例 2：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/17/image-20220817112930-3.png" style="height: 85px; width: 132px;">
<pre><b>输入：</b>grid = [[0,0]], k = 5
<b>输出：</b>1
<b>解释：</b>红色标注的路径和为 0 + 0 = 0 ，能被 5 整除。
</pre>

<p><strong>示例 3：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/08/12/image-20220812224605-3.png" style="width: 257px; height: 200px;">
<pre><b>输入：</b>grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
<b>输出：</b>10
<b>解释：</b>每个数字都能被 1 整除，所以每一条路径的和都能被 k 整除。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. The actual numbers in grid do not matter. What matters are the remainders you get when you divide the numbers by k.
2. We can use dynamic programming to solve this problem. What can we use as states?
3. Let dp[i][j][value] represent the number of paths where the sum of the elements on the path has a remainder of value when divided by k.

## 示例

```
[[5,2,4],[3,0,5],[0,7,2]]
3
[[0,0]]
5
[[7,3,4,9],[2,3,6,2],[2,3,7,0]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
```

### C

```c
int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPaths(int[][] grid, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var numberOfPaths = function(grid, k) {
    
};
```

### TypeScript

```typescript
function numberOfPaths(grid: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function numberOfPaths($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPaths(_ grid: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPaths(grid: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPaths(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func numberOfPaths(grid [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def number_of_paths(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-paths grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_paths(Grid :: [[integer()]], K :: integer()) -> integer().
number_of_paths(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_paths(grid :: [[integer]], k :: integer) :: integer
  def number_of_paths(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPaths(grid: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

