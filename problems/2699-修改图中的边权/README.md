# 2699. 修改图中的边权

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的 <strong>无向带权连通</strong>&nbsp;图，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，再给你一个整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, w<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边权为&nbsp;<code>w<sub>i</sub></code>&nbsp;的边。</p>

<p>部分边的边权为&nbsp;<code>-1</code>（<code>w<sub>i</sub> = -1</code>），其他边的边权都为 <strong>正</strong>&nbsp;数（<code>w<sub>i</sub> &gt; 0</code>）。</p>

<p>你需要将所有边权为 <code>-1</code>&nbsp;的边都修改为范围&nbsp;<code>[1, 2 * 10<sup>9</sup>]</code>&nbsp;中的 <strong>正整数</strong>&nbsp;，使得从节点&nbsp;<code>source</code>&nbsp;到节点&nbsp;<code>destination</code>&nbsp;的 <strong>最短距离</strong>&nbsp;为整数&nbsp;<code>target</code>&nbsp;。如果有 <strong>多种</strong>&nbsp;修改方案可以使&nbsp;<code>source</code> 和&nbsp;<code>destination</code>&nbsp;之间的最短距离等于&nbsp;<code>target</code>&nbsp;，你可以返回任意一种方案。</p>

<p>如果存在使 <code>source</code>&nbsp;到 <code>destination</code>&nbsp;最短距离为 <code>target</code>&nbsp;的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 <strong>空数组</strong>&nbsp;。</p>

<p><strong>注意：</strong>你不能修改一开始边权为正数的边。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/18/graph.png" style="width: 300px; height: 300px;" /></strong></p>

<pre>
<b>输入：</b>n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
<b>输出：</b>[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
<b>解释：</b>上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/18/graph-2.png" style="width: 300px; height: 300px;" /></strong></p>

<pre>
<b>输入：</b>n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
<b>输出：</b>[]
<b>解释：</b>上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/19/graph-3.png" style="width: 300px; height: 300px;" /></strong></p>

<pre>
<b>输入：</b>n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
<b>输出：</b>[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
<b>解释：</b>上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= edges.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>edges[i].length == 3</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i&nbsp;</sub>&lt;&nbsp;n</code></li>
	<li><code>w<sub>i</sub>&nbsp;= -1</code> 或者 <code>1 &lt;= w<sub>i&nbsp;</sub>&lt;= 10<sup><span style="">7</span></sup></code></li>
	<li><code>a<sub>i&nbsp;</sub>!=&nbsp;b<sub>i</sub></code></li>
	<li><code>0 &lt;= source, destination &lt; n</code></li>
	<li><code>source != destination</code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li>输入的图是连通图，且没有自环和重边。</li>
</ul>


## 难度

Hard

## 标签

- 图
- 最短路
- 堆（优先队列）

## 提示

1. Firstly, check that it’s actually possible to make the shortest path from source to destination equal to the target.
2. If the shortest path from source to destination without the edges to be modified, is less than the target, then it is not possible.
3. If the shortest path from source to destination including the edges to be modified and assigning them a temporary weight of 1, is greater than the target, then it is also not possible.
4. Suppose we can find a modifiable edge (u, v) such that the length of the shortest path from source to u (dis1) plus the length of the shortest path from v to destination (dis2) is less than target (dis1 + dis2 < target), then we can change its weight to “target - dis1 - dis2”.
5. For all the other edges that still have the weight “-1”, change the weights into sufficient large number (target, target + 1 or 200000000 etc.).

## 示例

```
5
[[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
0
1
5
3
[[0,1,-1],[0,2,5]]
0
2
6
4
[[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
0
2
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] modifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** modifiedGraphEdges(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination, int target, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ModifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @param {number} target
 * @return {number[][]}
 */
var modifiedGraphEdges = function(n, edges, source, destination, target) {
    
};
```

### TypeScript

```typescript
function modifiedGraphEdges(n: number, edges: number[][], source: number, destination: number, target: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @param Integer $target
     * @return Integer[][]
     */
    function modifiedGraphEdges($n, $edges, $source, $destination, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func modifiedGraphEdges(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int, _ target: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun modifiedGraphEdges(n: Int, edges: Array<IntArray>, source: Int, destination: Int, target: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> modifiedGraphEdges(int n, List<List<int>> edges, int source, int destination, int target) {
    
  }
}
```

### Go

```golang
func modifiedGraphEdges(n int, edges [][]int, source int, destination int, target int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @param {Integer} target
# @return {Integer[][]}
def modified_graph_edges(n, edges, source, destination, target)
    
end
```

### Scala

```scala
object Solution {
    def modifiedGraphEdges(n: Int, edges: Array[Array[Int]], source: Int, destination: Int, target: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn modified_graph_edges(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32, target: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (modified-graph-edges n edges source destination target)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec modified_graph_edges(N :: integer(), Edges :: [[integer()]], Source :: integer(), Destination :: integer(), Target :: integer()) -> [[integer()]].
modified_graph_edges(N, Edges, Source, Destination, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec modified_graph_edges(n :: integer, edges :: [[integer]], source :: integer, destination :: integer, target :: integer) :: [[integer]]
  def modified_graph_edges(n, edges, source, destination, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func modifiedGraphEdges(n: Int64, edges: Array<Array<Int64>>, source: Int64, destination: Int64, target: Int64): Array<Array<Int64>> {

    }
}
```

