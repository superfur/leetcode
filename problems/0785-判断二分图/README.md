# 785. 判断二分图

## 题目描述

存在一个 <strong>无向图</strong> ，图中有 <code>n</code> 个节点。其中每个节点都有一个介于 <code>0</code> 到 <code>n - 1</code> 之间的唯一编号。给你一个二维数组 <code>graph</code> ，其中 <code>graph[u]</code> 是一个节点数组，由节点 <code>u</code> 的邻接节点组成。形式上，对于 <code>graph[u]</code> 中的每个 <code>v</code> ，都存在一条位于节点 <code>u</code> 和节点 <code>v</code> 之间的无向边。该无向图同时具有以下属性：
<ul>
	<li>不存在自环（<code>graph[u]</code> 不包含 <code>u</code>）。</li>
	<li>不存在平行边（<code>graph[u]</code> 不包含重复值）。</li>
	<li>如果 <code>v</code> 在 <code>graph[u]</code> 内，那么 <code>u</code> 也应该在 <code>graph[v]</code> 内（该图是无向图）</li>
	<li>这个图可能不是连通图，也就是说两个节点 <code>u</code> 和 <code>v</code> 之间可能不存在一条连通彼此的路径。</li>
</ul>

<p><strong>二分图</strong> 定义：如果能将一个图的节点集合分割成两个独立的子集 <code>A</code> 和 <code>B</code> ，并使图中的每一条边的两个节点一个来自 <code>A</code> 集合，一个来自 <code>B</code> 集合，就将这个图称为 <strong>二分图</strong> 。</p>

<p>如果图是二分图，返回 <code>true</code><em> </em>；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>输入：</strong>graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
<strong>输出：</strong>false
<strong>解释：</strong><code>不能将节点分割成两个独立的子集，</code>以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>输入：</strong>graph = [[1,3],[0,2],[1,3],[0,2]]
<strong>输出：</strong>true
<strong>解释：</strong><code>可以将节点分成两组: {0, 2} 和 {1, 3} 。</code></pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>graph.length == n</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>0 <= graph[u].length < n</code></li>
	<li><code>0 <= graph[u][i] <= n - 1</code></li>
	<li><code>graph[u]</code> 不会包含 <code>u</code></li>
	<li><code>graph[u]</code> 的所有值 <strong>互不相同</strong></li>
	<li>如果 <code>graph[u]</code> 包含 <code>v</code>，那么 <code>graph[v]</code> 也会包含 <code>u</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 示例

```
[[1,2,3],[0,2],[0,1,3],[0,2]]
[[1,3],[0,2],[1,3],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isBipartite(int[][] graph) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
```

### C

```c
bool isBipartite(int** graph, int graphSize, int* graphColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsBipartite(int[][] graph) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    
};
```

### TypeScript

```typescript
function isBipartite(graph: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Boolean
     */
    function isBipartite($graph) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isBipartite(_ graph: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isBipartite(graph: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isBipartite(List<List<int>> graph) {
    
  }
}
```

### Go

```golang
func isBipartite(graph [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
    
end
```

### Scala

```scala
object Solution {
    def isBipartite(graph: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-bipartite graph)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_bipartite(Graph :: [[integer()]]) -> boolean().
is_bipartite(Graph) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_bipartite(graph :: [[integer]]) :: boolean
  def is_bipartite(graph) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isBipartite(graph: Array<Array<Int64>>): Bool {

    }
}
```

