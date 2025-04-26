# 2368. 受限条件下可到达节点的数目

## 题目描述

<p>现有一棵由 <code>n</code> 个节点组成的无向树，节点编号从 <code>0</code> 到 <code>n - 1</code> ，共有 <code>n - 1</code> 条边。</p>

<p>给你一个二维整数数组 <code>edges</code> ，长度为 <code>n - 1</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条边。另给你一个整数数组 <code>restricted</code> 表示 <strong>受限</strong> 节点。</p>

<p>在不访问受限节点的前提下，返回你可以从节点<em> </em><code>0</code><em> </em>到达的 <strong>最多</strong> 节点数目<em>。</em></p>

<p>注意，节点 <code>0</code> <strong>不</strong> 会标记为受限节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/15/ex1drawio.png" style="width: 402px; height: 322px;">
<pre><strong>输入：</strong>n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
<strong>输出：</strong>4
<strong>解释：</strong>上图所示正是这棵树。
在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/15/ex2drawio.png" style="width: 412px; height: 312px;">
<pre><strong>输入：</strong>n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
<strong>输出：</strong>3
<strong>解释：</strong>上图所示正是这棵树。
在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code> 表示一棵有效的树</li>
	<li><code>1 &lt;= restricted.length &lt; n</code></li>
	<li><code>1 &lt;= restricted[i] &lt; n</code></li>
	<li><code>restricted</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 并查集
- 图
- 数组
- 哈希表

## 提示

1. Can we find all the reachable nodes in a single traversal?
2. Traverse the graph from node 0 while avoiding the nodes in restricted and do not revisit nodes that have been visited.
3. Keep count of how many nodes are visited in total.

## 示例

```
7
[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
[4,5]
7
[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
[4,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        
    }
};
```

### Java

```java
class Solution {
    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
```

### C

```c
int reachableNodes(int n, int** edges, int edgesSize, int* edgesColSize, int* restricted, int restrictedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReachableNodes(int n, int[][] edges, int[] restricted) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function(n, edges, restricted) {
    
};
```

### TypeScript

```typescript
function reachableNodes(n: number, edges: number[][], restricted: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $restricted
     * @return Integer
     */
    function reachableNodes($n, $edges, $restricted) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reachableNodes(_ n: Int, _ edges: [[Int]], _ restricted: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reachableNodes(n: Int, edges: Array<IntArray>, restricted: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reachableNodes(int n, List<List<int>> edges, List<int> restricted) {
    
  }
}
```

### Go

```golang
func reachableNodes(n int, edges [][]int, restricted []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} restricted
# @return {Integer}
def reachable_nodes(n, edges, restricted)
    
end
```

### Scala

```scala
object Solution {
    def reachableNodes(n: Int, edges: Array[Array[Int]], restricted: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reachable_nodes(n: i32, edges: Vec<Vec<i32>>, restricted: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reachable-nodes n edges restricted)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec reachable_nodes(N :: integer(), Edges :: [[integer()]], Restricted :: [integer()]) -> integer().
reachable_nodes(N, Edges, Restricted) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reachable_nodes(n :: integer, edges :: [[integer]], restricted :: [integer]) :: integer
  def reachable_nodes(n, edges, restricted) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reachableNodes(n: Int64, edges: Array<Array<Int64>>, restricted: Array<Int64>): Int64 {

    }
}
```

