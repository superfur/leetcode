# 2503. 矩阵查询可获得的最大分数

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的整数矩阵 <code>grid</code> 和一个大小为 <code>k</code> 的数组 <code>queries</code> 。</p>

<p>找出一个大小为 <code>k</code> 的数组 <code>answer</code> ，且满足对于每个整数 <code>queries[i]</code> ，你从矩阵 <strong>左上角</strong> 单元格开始，重复以下过程：</p>

<ul>
	<li>如果 <code>queries[i]</code> <strong>严格</strong> 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 <code>4</code> 个方向（上、下、左、右）上任一 <strong>相邻</strong> 单元格。</li>
	<li>否则，你不能获得任何分，并且结束这一过程。</li>
</ul>

<p>在过程结束后，<code>answer[i]</code> 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 <strong>多次</strong> 。</p>

<p>返回结果数组 <code>answer</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/03/15/image1.png" style="width: 571px; height: 152px;" />
<pre>
<strong>输入：</strong>grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
<strong>输出：</strong>[5,8,1]
<strong>解释：</strong>上图展示了每个查询中访问并获得分数的单元格。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/20/yetgriddrawio-2.png" />
<pre>
<strong>输入：</strong>grid = [[5,2,1],[1,1,2]], queries = [3]
<strong>输出：</strong>[0]
<strong>解释：</strong>无法获得分数，因为左上角单元格的值大于等于 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>k == queries.length</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= grid[i][j], queries[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 并查集
- 数组
- 双指针
- 矩阵
- 排序
- 堆（优先队列）

## 提示

1. The queries are all given to you beforehand so you can answer them in any order you want.
2. Sort the queries knowing their original order to be able to build the answer array.
3. Run a BFS on the graph and answer the queries in increasing order.

## 示例

```
[[1,2,3],[2,5,7],[3,5,1]]
[5,6,2]
[[5,2,1],[1,1,2]]
[3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maxPoints(int[][] grid, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxPoints(int** grid, int gridSize, int* gridColSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaxPoints(int[][] grid, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[]} queries
 * @return {number[]}
 */
var maxPoints = function(grid, queries) {
    
};
```

### TypeScript

```typescript
function maxPoints(grid: number[][], queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maxPoints($grid, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPoints(_ grid: [[Int]], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPoints(grid: Array<IntArray>, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxPoints(List<List<int>> grid, List<int> queries) {
    
  }
}
```

### Go

```golang
func maxPoints(grid [][]int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @param {Integer[]} queries
# @return {Integer[]}
def max_points(grid, queries)
    
end
```

### Scala

```scala
object Solution {
    def maxPoints(grid: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-points grid queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_points(Grid :: [[integer()]], Queries :: [integer()]) -> [integer()].
max_points(Grid, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_points(grid :: [[integer]], queries :: [integer]) :: [integer]
  def max_points(grid, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPoints(grid: Array<Array<Int64>>, queries: Array<Int64>): Array<Int64> {

    }
}
```

