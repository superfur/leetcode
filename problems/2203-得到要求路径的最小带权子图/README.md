# 2203. 得到要求路径的最小带权子图

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，它表示一个 <strong>带权有向</strong> 图的节点数，节点编号为&nbsp;<code>0</code> 到&nbsp;<code>n - 1</code>&nbsp;。</p>

<p>同时给你一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, weight<sub>i</sub>]</code>&nbsp;，表示从&nbsp;<code>from<sub>i</sub></code>&nbsp;到&nbsp;<code>to<sub>i</sub></code>&nbsp;有一条边权为&nbsp;<code>weight<sub>i</sub></code>&nbsp;的 <strong>有向</strong> 边。</p>

<p>最后，给你三个 <strong>互不相同</strong>&nbsp;的整数&nbsp;<code>src1</code>&nbsp;，<code>src2</code>&nbsp;和&nbsp;<code>dest</code>&nbsp;，表示图中三个不同的点。</p>

<p>请你从图中选出一个 <b>边权和最小</b>&nbsp;的子图，使得从 <code>src1</code>&nbsp;和 <code>src2</code>&nbsp;出发，在这个子图中，都 <strong>可以</strong>&nbsp;到达 <code>dest</code>&nbsp;。如果这样的子图不存在，请返回 <code>-1</code>&nbsp;。</p>

<p><strong>子图</strong>&nbsp;中的点和边都应该属于原图的一部分。子图的边权和定义为它所包含的所有边的权值之和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/02/17/example1drawio.png" style="width: 263px; height: 250px;" /></p>

<pre>
<b>输入：</b>n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
<b>输出：</b>9
<strong>解释：</strong>
上图为输入的图。
蓝色边为最优子图之一。
注意，子图 [[1,0,3],[0,5,6]] 也能得到最优解，但无法在满足所有限制的前提下，得到更优解。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/02/17/example2-1drawio.png" style="width: 350px; height: 51px;" /></p>

<pre>
<b>输入：</b>n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
<b>输出：</b>-1
<strong>解释：</strong>
上图为输入的图。
可以看到，不存在从节点 1 到节点 2 的路径，所以不存在任何子图满足所有限制。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 3</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub>, src1, src2, dest &lt;= n - 1</code></li>
	<li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
	<li><code>src1</code>&nbsp;，<code>src2</code>&nbsp;和&nbsp;<code>dest</code>&nbsp;两两不同。</li>
	<li><code>1 &lt;= weight[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 最短路

## 提示

1. Consider what the paths from src1 to dest and src2 to dest would look like in the optimal solution.
2. It can be shown that in an optimal solution, the two paths from src1 and src2 will coincide at one node, and the remaining part to dest will be the same for both paths. Now consider how to find the node where the paths will coincide.
3. How can algorithms for finding the shortest path between two nodes help us?

## 示例

```
6
[[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
0
1
5
3
[[0,1,1],[2,1,1]]
0
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
```

### C

```c
long long minimumWeight(int n, int** edges, int edgesSize, int* edgesColSize, int src1, int src2, int dest) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} src1
 * @param {number} src2
 * @param {number} dest
 * @return {number}
 */
var minimumWeight = function(n, edges, src1, src2, dest) {
    
};
```

### TypeScript

```typescript
function minimumWeight(n: number, edges: number[][], src1: number, src2: number, dest: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $src1
     * @param Integer $src2
     * @param Integer $dest
     * @return Integer
     */
    function minimumWeight($n, $edges, $src1, $src2, $dest) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumWeight(_ n: Int, _ edges: [[Int]], _ src1: Int, _ src2: Int, _ dest: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumWeight(n: Int, edges: Array<IntArray>, src1: Int, src2: Int, dest: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumWeight(int n, List<List<int>> edges, int src1, int src2, int dest) {
    
  }
}
```

### Go

```golang
func minimumWeight(n int, edges [][]int, src1 int, src2 int, dest int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} src1
# @param {Integer} src2
# @param {Integer} dest
# @return {Integer}
def minimum_weight(n, edges, src1, src2, dest)
    
end
```

### Scala

```scala
object Solution {
    def minimumWeight(n: Int, edges: Array[Array[Int]], src1: Int, src2: Int, dest: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_weight(n: i32, edges: Vec<Vec<i32>>, src1: i32, src2: i32, dest: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-weight n edges src1 src2 dest)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_weight(N :: integer(), Edges :: [[integer()]], Src1 :: integer(), Src2 :: integer(), Dest :: integer()) -> integer().
minimum_weight(N, Edges, Src1, Src2, Dest) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_weight(n :: integer, edges :: [[integer]], src1 :: integer, src2 :: integer, dest :: integer) :: integer
  def minimum_weight(n, edges, src1, src2, dest) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumWeight(n: Int64, edges: Array<Array<Int64>>, src1: Int64, src2: Int64, dest: Int64): Int64 {

    }
}
```

