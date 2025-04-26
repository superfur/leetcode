# 882. 细分图中的可到达节点

## 题目描述

<p>给你一个无向图（<strong>原始图</strong>），图中有 <code>n</code> 个节点，编号从 <code>0</code> 到 <code>n - 1</code> 。你决定将图中的每条边 <strong>细分</strong> 为一条节点链，每条边之间的新节点数各不相同。</p>

<p>图用由边组成的二维数组 <code>edges</code> 表示，其中&nbsp;<code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, cnt<sub>i</sub>]</code> 表示原始图中节点&nbsp;<code>u<sub>i</sub></code> 和&nbsp;<code>v<sub>i</sub></code> 之间存在一条边，<code>cnt<sub>i</sub></code> 是将边 <strong>细分</strong> 后的新节点总数。注意，<code>cnt<sub>i</sub> == 0</code> 表示边不可细分。</p>

<p>要 <strong>细分</strong> 边 <code>[ui, vi]</code> ，需要将其替换为 <code>(cnt<sub>i</sub> + 1)</code> 条新边，和&nbsp;<code>cnt<sub>i</sub></code> 个新节点。新节点为 <code>x<sub>1</sub></code>, <code>x<sub>2</sub></code>, ..., <code>x<sub>cnt<sub>i</sub></sub></code> ，新边为 <code>[u<sub>i</sub>, x<sub>1</sub>]</code>, <code>[x<sub>1</sub>, x<sub>2</sub>]</code>, <code>[x<sub>2</sub>, x<sub>3</sub>]</code>, ..., <code>[x<sub>cnt<sub>i</sub>-1</sub>, x<sub>cnt<sub>i</sub></sub>]</code>, <code>[x<sub>cnt<sub>i</sub></sub>, v<sub>i</sub>]</code> 。</p>

<p>现在得到一个&nbsp;<strong>新的细分图</strong> ，请你计算从节点 <code>0</code> 出发，可以到达多少个节点？如果节点间距离是 <code>maxMoves</code> 或更少，则视为 <strong>可以到达</strong> 。</p>

<p>给你原始图和 <code>maxMoves</code> ，返回 <em>新的细分图中从节点 <code>0</code> 出发</em><strong><em> 可到达的节点数</em></strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png" style="height: 247px; width: 600px;" />
<pre>
<strong>输入：</strong>edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
<strong>输出：</strong>13
<strong>解释：</strong>边的细分情况如上图所示。
可以到达的节点已经用黄色标注出来。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
<strong>输出：</strong>23
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
<strong>输出：</strong>1
<strong>解释：</strong>节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= edges.length &lt;= min(n * (n - 1) / 2, 10<sup>4</sup>)</code></li>
	<li><code>edges[i].length == 3</code></li>
	<li><code>0 &lt;= u<sub>i</sub> &lt; v<sub>i</sub> &lt; n</code></li>
	<li>图中 <strong>不存在平行边</strong></li>
	<li><code>0 &lt;= cnt<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= maxMoves &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= n &lt;= 3000</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 最短路
- 堆（优先队列）

## 示例

```
[[0,1,10],[0,2,1],[1,2,2]]
6
3
[[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
10
4
[[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
17
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int reachableNodes(int[][] edges, int maxMoves, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
```

### C

```c
int reachableNodes(int** edges, int edgesSize, int* edgesColSize, int maxMoves, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReachableNodes(int[][] edges, int maxMoves, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} maxMoves
 * @param {number} n
 * @return {number}
 */
var reachableNodes = function(edges, maxMoves, n) {
    
};
```

### TypeScript

```typescript
function reachableNodes(edges: number[][], maxMoves: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $maxMoves
     * @param Integer $n
     * @return Integer
     */
    function reachableNodes($edges, $maxMoves, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reachableNodes(_ edges: [[Int]], _ maxMoves: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reachableNodes(edges: Array<IntArray>, maxMoves: Int, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reachableNodes(List<List<int>> edges, int maxMoves, int n) {
    
  }
}
```

### Go

```golang
func reachableNodes(edges [][]int, maxMoves int, n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer} max_moves
# @param {Integer} n
# @return {Integer}
def reachable_nodes(edges, max_moves, n)
    
end
```

### Scala

```scala
object Solution {
    def reachableNodes(edges: Array[Array[Int]], maxMoves: Int, n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reachable_nodes(edges: Vec<Vec<i32>>, max_moves: i32, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reachable-nodes edges maxMoves n)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec reachable_nodes(Edges :: [[integer()]], MaxMoves :: integer(), N :: integer()) -> integer().
reachable_nodes(Edges, MaxMoves, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reachable_nodes(edges :: [[integer]], max_moves :: integer, n :: integer) :: integer
  def reachable_nodes(edges, max_moves, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reachableNodes(edges: Array<Array<Int64>>, maxMoves: Int64, n: Int64): Int64 {

    }
}
```

