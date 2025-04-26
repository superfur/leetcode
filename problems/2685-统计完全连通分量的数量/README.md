# 2685. 统计完全连通分量的数量

## 题目描述

<p>给你一个整数 <code>n</code> 。现有一个包含 <code>n</code> 个顶点的 <strong>无向</strong> 图，顶点按从 <code>0</code> 到 <code>n - 1</code> 编号。给你一个二维整数数组 <code>edges</code> 其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示顶点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条 <strong>无向</strong> 边。</p>

<p>返回图中 <strong>完全连通分量</strong> 的数量。</p>

<p>如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 <strong>连通分量</strong> 。</p>

<p>如果连通分量中每对节点之间都存在一条边，则称其为 <strong>完全连通分量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
<strong>输出：</strong>3
<strong>解释：</strong>如上图所示，可以看到此图所有分量都是完全连通分量。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
<strong>输出：</strong>1
<strong>解释：</strong>包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
因此，在图中完全连接分量的数量是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>不存在重复的边</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 提示

1. Find the connected components of an undirected graph using depth-first search (DFS) or breadth-first search (BFS).
2. For each connected component, count the number of nodes and edges in the component.
3. A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.

## 示例

```
6
[[0,1],[0,2],[1,2],[3,4]]
6
[[0,1],[0,2],[1,2],[3,4],[3,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
```

### C

```c
int countCompleteComponents(int n, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCompleteComponents(int n, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    
};
```

### TypeScript

```typescript
function countCompleteComponents(n: number, edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countCompleteComponents($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCompleteComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCompleteComponents(n: Int, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCompleteComponents(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func countCompleteComponents(n int, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_complete_components(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def countCompleteComponents(n: Int, edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-complete-components n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_complete_components(N :: integer(), Edges :: [[integer()]]) -> integer().
count_complete_components(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_complete_components(n :: integer, edges :: [[integer]]) :: integer
  def count_complete_components(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCompleteComponents(n: Int64, edges: Array<Array<Int64>>): Int64 {

    }
}
```

