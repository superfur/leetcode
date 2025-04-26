# LCR 099. 最小路径和

## 题目描述

<p>给定一个包含非负整数的 <code><em>m</em>&nbsp;x&nbsp;<em>n</em></code>&nbsp;网格&nbsp;<code>grid</code> ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>

<p><strong>说明：</strong>一个机器人每次只能向下或者向右移动一步。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>输出：</strong>7
<strong>解释：</strong>因为路径 1&rarr;3&rarr;1&rarr;1&rarr;1 的总和最小。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2,3],[4,5,6]]
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 64&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/minimum-path-sum/">https://leetcode-cn.com/problems/minimum-path-sum/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 示例

```
[[1,3,1],[1,5,1],[4,2,1]]
[[1,2,3],[4,5,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {

    }
};
```

### Java

```java
class Solution {
    public int minPathSum(int[][] grid) {

    }
}
```

### Python

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
```

### C

```c


int minPathSum(int** grid, int gridSize, int* gridColSize){

}
```

### C#

```csharp
public class Solution {
    public int MinPathSum(int[][] grid) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {

};
```

### TypeScript

```typescript
function minPathSum(grid: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minPathSum($grid) {

    }
}
```

### Swift

```swift
class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minPathSum(grid: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func minPathSum(grid [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)

end
```

### Scala

```scala
object Solution {
    def minPathSum(grid: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (min-path-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec min_path_sum(Grid :: [[integer()]]) -> integer().
min_path_sum(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_path_sum(grid :: [[integer]]) :: integer
  def min_path_sum(grid) do

  end
end
```

