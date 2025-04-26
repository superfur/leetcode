# 847. 访问所有节点的最短路径

## 题目描述

<p>存在一个由 <code>n</code> 个节点组成的无向连通图，图中的节点按从 <code>0</code> 到 <code>n - 1</code> 编号。</p>

<p>给你一个数组 <code>graph</code> 表示这个图。其中，<code>graph[i]</code> 是一个列表，由所有与节点 <code>i</code> 直接相连的节点组成。</p>

<p>返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg" style="width: 222px; height: 183px;" />
<pre>
<strong>输入：</strong>graph = [[1,2,3],[0],[0],[0]]
<strong>输出：</strong>4
<strong>解释：</strong>一种可能的路径为 [1,0,2,0,3]</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg" style="width: 382px; height: 222px;" /></p>

<pre>
<strong>输入：</strong>graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>输出：</strong>4
<strong>解释：</strong>一种可能的路径为 [0,1,4,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;n</code></li>
	<li><code>graph[i]</code> 不包含 <code>i</code></li>
	<li>如果 <code>graph[a]</code> 包含 <code>b</code> ，那么 <code>graph[b]</code> 也包含 <code>a</code></li>
	<li>输入的图总是连通图</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 广度优先搜索
- 图
- 动态规划
- 状态压缩

## 示例

```
[[1,2,3],[0],[0],[0]]
[[1],[0,2,4],[1,3,4],[2],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestPathLength(int[][] graph) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
```

### C

```c
int shortestPathLength(int** graph, int graphSize, int* graphColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestPathLength(int[][] graph) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function(graph) {
    
};
```

### TypeScript

```typescript
function shortestPathLength(graph: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestPathLength(_ graph: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestPathLength(graph: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestPathLength(List<List<int>> graph) {
    
  }
}
```

### Go

```golang
func shortestPathLength(graph [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @return {Integer}
def shortest_path_length(graph)
    
end
```

### Scala

```scala
object Solution {
    def shortestPathLength(graph: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_path_length(graph: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-path-length graph)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_path_length(Graph :: [[integer()]]) -> integer().
shortest_path_length(Graph) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_path_length(graph :: [[integer]]) :: integer
  def shortest_path_length(graph) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestPathLength(graph: Array<Array<Int64>>): Int64 {

    }
}
```

