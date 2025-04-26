# 3070. 元素和小于等于 k 的子矩阵的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数矩阵 <code>grid</code> 和一个整数 <code>k</code>。</p>

<p>返回包含 <code>grid</code> 左上角元素、元素和小于或等于 <code>k</code> 的 <strong><span data-keyword="submatrix">子矩阵</span></strong>的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example1.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,6,3],[6,6,1]], k = 18
<strong>输出：</strong>4
<strong>解释：</strong>如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example21.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
<strong>输出：</strong>6
<strong>解释：</strong>如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length </code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000 </code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 前缀和

## 示例

```
[[7,6,3],[6,6,1]]
18
[[7,2,9],[1,5,0],[2,6,6]]
20
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
```

### C

```c
int countSubmatrices(int** grid, int gridSize, int* gridColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubmatrices(int[][] grid, int k) {
        
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
var countSubmatrices = function(grid, k) {
    
};
```

### TypeScript

```typescript
function countSubmatrices(grid: number[][], k: number): number {
    
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
    function countSubmatrices($grid, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubmatrices(_ grid: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubmatrices(grid: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubmatrices(List<List<int>> grid, int k) {
    
  }
}
```

### Go

```golang
func countSubmatrices(grid [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_submatrices(grid, k)
    
end
```

### Scala

```scala
object Solution {
    def countSubmatrices(grid: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-submatrices grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_submatrices(Grid :: [[integer()]], K :: integer()) -> integer().
count_submatrices(Grid, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_submatrices(grid :: [[integer]], k :: integer) :: integer
  def count_submatrices(grid, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubmatrices(grid: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

