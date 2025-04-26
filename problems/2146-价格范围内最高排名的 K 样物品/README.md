# 2146. 价格范围内最高排名的 K 样物品

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>grid</code>&nbsp;，它的大小为&nbsp;<code>m x n</code>&nbsp;，表示一个商店中物品的分布图。数组中的整数含义为：</p>

<ul>
	<li><code>0</code>&nbsp;表示无法穿越的一堵墙。</li>
	<li><code>1</code>&nbsp;表示可以自由通过的一个空格子。</li>
	<li>所有其他正整数表示该格子内的一样物品的价格。你可以自由经过这些格子。</li>
</ul>

<p>从一个格子走到上下左右相邻格子花费&nbsp;<code>1</code>&nbsp;步。</p>

<p>同时给你一个整数数组&nbsp;<code>pricing</code> 和&nbsp;<code>start</code>&nbsp;，其中&nbsp;<code>pricing = [low, high]</code> 且&nbsp;<code>start = [row, col]</code>&nbsp;，表示你开始位置为&nbsp;<code>(row, col)</code>&nbsp;，同时你只对物品价格在<strong>&nbsp;闭区间</strong>&nbsp;<code>[low, high]</code>&nbsp;之内的物品感兴趣。同时给你一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你想知道给定范围 <strong>内</strong>&nbsp;且 <strong>排名最高</strong>&nbsp;的 <code>k</code>&nbsp;件物品的 <strong>位置</strong>&nbsp;。排名按照优先级从高到低的以下规则制定：</p>

<ol>
	<li>距离：定义为从&nbsp;<code>start</code>&nbsp;到一件物品的最短路径需要的步数（<strong>较近</strong>&nbsp;距离的排名更高）。</li>
	<li>价格：<strong>较低</strong>&nbsp;价格的物品有更高优先级，但只考虑在给定范围之内的价格。</li>
	<li>行坐标：<strong>较小</strong>&nbsp;行坐标的有更高优先级。</li>
	<li>列坐标：<strong>较小</strong>&nbsp;列坐标的有更高优先级。</li>
</ol>

<p>请你返回给定价格内排名最高的 <code>k</code>&nbsp;件物品的坐标，将它们按照排名排序后返回。如果给定价格内少于 <code>k</code>&nbsp;件物品，那么请将它们的坐标&nbsp;<strong>全部</strong>&nbsp;返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/16/example1drawio.png" style="width: 200px; height: 151px;"></p>

<pre><b>输入：</b>grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3
<b>输出：</b>[[0,1],[1,1],[2,1]]
<b>解释：</b>起点为 (0,0) 。
价格范围为 [2,5] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(2,1) 和 (2,2) 。
这些物品的排名为：
- (0,1) 距离为 1
- (1,1) 距离为 2
- (2,1) 距离为 3
- (2,2) 距离为 4
所以，给定价格范围内排名最高的 3 件物品的坐标为 (0,1)，(1,1) 和 (2,1) 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/16/example2drawio1.png" style="width: 200px; height: 151px;"></p>

<pre><b>输入：</b>grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2
<b>输出：</b>[[2,1],[1,2]]
<b>解释：</b>起点为 (2,3) 。
价格范围为 [2,3] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(1,2) 和 (2,1) 。
这些物品的排名为： 
- (2,1) 距离为 2 ，价格为 2
- (1,2) 距离为 2 ，价格为 3
- (1,1) 距离为 3
- (0,1) 距离为 4
所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (1,2) 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/30/example3.png" style="width: 149px; height: 150px;"></p>

<pre><b>输入：</b>grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3
<b>输出：</b>[[2,1],[2,0]]
<b>解释：</b>起点为 (0,0) 。
价格范围为 [2,3] ，我们可以选择的物品坐标为 (2,0) 和 (2,1) 。
这些物品的排名为：
- (2,1) 距离为 5
- (2,0) 距离为 6
所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (2,0) 。
注意，k = 3 但给定价格范围内只有 2 件物品。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>pricing.length == 2</code></li>
	<li><code>2 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code></li>
	<li><code>start.length == 2</code></li>
	<li><code>0 &lt;= row &lt;= m - 1</code></li>
	<li><code>0 &lt;= col &lt;= n - 1</code></li>
	<li><code>grid[row][col] &gt; 0</code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 矩阵
- 排序
- 堆（优先队列）

## 提示

1. Could you determine the rank of every item efficiently?
2. We can perform a breadth-first search from the starting position and know the length of the shortest path from start to every item.
3. Sort all the items according to the conditions listed in the problem, and return the first k (or all if less than k exist) items as the answer.

## 示例

```
[[1,2,0,1],[1,3,0,1],[0,2,5,1]]
[2,5]
[0,0]
3
[[1,2,0,1],[1,3,3,1],[0,2,5,1]]
[2,3]
[2,3]
2
[[1,1,1],[0,0,1],[2,3,4]]
[2,3]
[0,0]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& pricing, vector<int>& start, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> highestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** highestRankedKItems(int** grid, int gridSize, int* gridColSize, int* pricing, int pricingSize, int* start, int startSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> HighestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[]} pricing
 * @param {number[]} start
 * @param {number} k
 * @return {number[][]}
 */
var highestRankedKItems = function(grid, pricing, start, k) {
    
};
```

### TypeScript

```typescript
function highestRankedKItems(grid: number[][], pricing: number[], start: number[], k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $pricing
     * @param Integer[] $start
     * @param Integer $k
     * @return Integer[][]
     */
    function highestRankedKItems($grid, $pricing, $start, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func highestRankedKItems(_ grid: [[Int]], _ pricing: [Int], _ start: [Int], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun highestRankedKItems(grid: Array<IntArray>, pricing: IntArray, start: IntArray, k: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> highestRankedKItems(List<List<int>> grid, List<int> pricing, List<int> start, int k) {
    
  }
}
```

### Go

```golang
func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer[]} pricing
# @param {Integer[]} start
# @param {Integer} k
# @return {Integer[][]}
def highest_ranked_k_items(grid, pricing, start, k)
    
end
```

### Scala

```scala
object Solution {
    def highestRankedKItems(grid: Array[Array[Int]], pricing: Array[Int], start: Array[Int], k: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn highest_ranked_k_items(grid: Vec<Vec<i32>>, pricing: Vec<i32>, start: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (highest-ranked-k-items grid pricing start k)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec highest_ranked_k_items(Grid :: [[integer()]], Pricing :: [integer()], Start :: [integer()], K :: integer()) -> [[integer()]].
highest_ranked_k_items(Grid, Pricing, Start, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec highest_ranked_k_items(grid :: [[integer]], pricing :: [integer], start :: [integer], k :: integer) :: [[integer]]
  def highest_ranked_k_items(grid, pricing, start, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func highestRankedKItems(grid: Array<Array<Int64>>, pricing: Array<Int64>, start: Array<Int64>, k: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

