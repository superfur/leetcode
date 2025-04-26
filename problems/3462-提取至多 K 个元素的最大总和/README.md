# 3462. 提取至多 K 个元素的最大总和

## 题目描述

<p data-pm-slice="1 3 []">给你一个大小为 <code>n x m</code>&nbsp;的二维矩阵&nbsp;<code>grid</code>&nbsp;，以及一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>limits</code>&nbsp;，和一个整数&nbsp;<code>k</code>&nbsp;。你的目标是从矩阵 <code>grid</code> 中提取出&nbsp;<strong>至多</strong> <code>k</code>&nbsp;个元素，并计算这些元素的最大总和，提取时需满足以下限制<b>：</b></p>

<ul data-spread="false">
	<li>
	<p>从 <code>grid</code>&nbsp;的第 <code>i</code> 行提取的元素数量不超过 <code>limits[i]</code> 。</p>
	</li>
</ul>

<p data-pm-slice="1 1 []">返回最大总和。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,2],[3,4]], limits = [1,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>7</span></p>

<p><b>解释：</b></p>

<ul>
	<li>从第 2 行提取至多 2 个元素，取出 4 和 3 。</li>
	<li>至多提取 2 个元素时的最大总和&nbsp;<code>4 + 3 = 7</code>&nbsp;。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">21</span></p>

<p><b>解释：</b></p>

<ul>
	<li>从第 1&nbsp;行提取至多 2 个元素，取出 7 。</li>
	<li>从第 2 行提取至多 2 个元素，取出&nbsp;8 和 6 。</li>
	<li>至多提取 3&nbsp;个元素时的最大总和 <code>7 + 8 + 6 = 21</code>&nbsp;。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>n == grid.length == limits.length</code></li>
	<li><code>m == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 500</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= limits[i] &lt;= m</code></li>
	<li><code>0 &lt;= k &lt;= min(n * m, sum(limits))</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵
- 排序
- 堆（优先队列）

## 提示

1. Sort each row in descending order and extract the top <code>limits[i]</code> elements.
2. Use a max-heap to efficiently pick the largest <code>k</code> elements across all rows.

## 示例

```
[[1,2],[3,4]]
[1,2]
2
[[5,3,7],[8,2,6]]
[2,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxSum(int[][] grid, int[] limits, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
```

### C

```c
long long maxSum(int** grid, int gridSize, int* gridColSize, int* limits, int limitsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxSum(int[][] grid, int[] limits, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[]} limits
 * @param {number} k
 * @return {number}
 */
var maxSum = function(grid, limits, k) {
    
};
```

### TypeScript

```typescript
function maxSum(grid: number[][], limits: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $limits
     * @param Integer $k
     * @return Integer
     */
    function maxSum($grid, $limits, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSum(_ grid: [[Int]], _ limits: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSum(grid: Array<IntArray>, limits: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSum(List<List<int>> grid, List<int> limits, int k) {
    
  }
}
```

### Go

```golang
func maxSum(grid [][]int, limits []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer[]} limits
# @param {Integer} k
# @return {Integer}
def max_sum(grid, limits, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSum(grid: Array[Array[Int]], limits: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>, limits: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum grid limits k)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum(Grid :: [[integer()]], Limits :: [integer()], K :: integer()) -> integer().
max_sum(Grid, Limits, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum(grid :: [[integer]], limits :: [integer], k :: integer) :: integer
  def max_sum(grid, limits, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSum(grid: Array<Array<Int64>>, limits: Array<Int64>, k: Int64): Int64 {

    }
}
```

