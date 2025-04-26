# 2497. 图中最大星和

## 题目描述

<p>给你一个&nbsp;<code>n</code>&nbsp;个点的无向图，节点从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;编号。给你一个长度为 <code>n</code>&nbsp;下标从&nbsp;<strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>vals</code>&nbsp;，其中&nbsp;<code>vals[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个节点的值。</p>

<p>同时给你一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条双向边。</p>

<p><strong>星图</strong>&nbsp;是给定图中的一个子图，它包含一个中心节点和&nbsp;<code>0</code>&nbsp;个或更多个邻居。换言之，星图是给定图中一个边的子集，且这些边都有一个公共节点。</p>

<p>下图分别展示了有 <code>3</code>&nbsp;个和 <code>4</code>&nbsp;个邻居的星图，蓝色节点为中心节点。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/07/max-star-sum-descdrawio.png" style="width: 400px; height: 179px;"></p>

<p><strong>星和</strong> 定义为星图中所有节点值的和。</p>

<p>给你一个整数&nbsp;<code>k</code>&nbsp;，请你返回 <strong>至多</strong>&nbsp;包含 <code>k</code>&nbsp;条边的星图中的 <strong>最大星和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/07/max-star-sum-example1drawio.png" style="width: 300px; height: 291px;"></p>

<pre><b>输入：</b>vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2
<b>输出：</b>16
<b>解释：</b>上图展示了输入示例。
最大星和对应的星图在上图中用蓝色标出。中心节点是 3 ，星图中还包含邻居 1 和 4 。
无法得到一个和大于 16 且边数不超过 2 的星图。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>vals = [-5], edges = [], k = 0
<b>输出：</b>-5
<b>解释：</b>只有一个星图，就是节点 0 自己。
所以我们返回 -5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == vals.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= vals[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= min(n * (n - 1) / 2</code><code>, 10<sup>5</sup>)</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 图
- 数组
- 排序
- 堆（优先队列）

## 提示

1. A star graph doesn’t necessarily include all of its neighbors.
2. For each node, sort its neighbors in descending order and take k max valued neighbors.

## 示例

```
[1,2,3,4,10,-10,-20]
[[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
2
[-5]
[]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxStarSum(vector<int>& vals, vector<vector<int>>& edges, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxStarSum(int[] vals, int[][] edges, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
```

### C

```c
int maxStarSum(int* vals, int valsSize, int** edges, int edgesSize, int* edgesColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxStarSum(int[] vals, int[][] edges, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStarSum = function(vals, edges, k) {
    
};
```

### TypeScript

```typescript
function maxStarSum(vals: number[], edges: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $vals
     * @param Integer[][] $edges
     * @param Integer $k
     * @return Integer
     */
    function maxStarSum($vals, $edges, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxStarSum(_ vals: [Int], _ edges: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxStarSum(vals: IntArray, edges: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxStarSum(List<int> vals, List<List<int>> edges, int k) {
    
  }
}
```

### Go

```golang
func maxStarSum(vals []int, edges [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} vals
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def max_star_sum(vals, edges, k)
    
end
```

### Scala

```scala
object Solution {
    def maxStarSum(vals: Array[Int], edges: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_star_sum(vals: Vec<i32>, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-star-sum vals edges k)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_star_sum(Vals :: [integer()], Edges :: [[integer()]], K :: integer()) -> integer().
max_star_sum(Vals, Edges, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_star_sum(vals :: [integer], edges :: [[integer]], k :: integer) :: integer
  def max_star_sum(vals, edges, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxStarSum(vals: Array<Int64>, edges: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

