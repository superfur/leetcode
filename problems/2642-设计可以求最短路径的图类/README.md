# 2642. 设计可以求最短路径的图类

## 题目描述

<p>给你一个有&nbsp;<code>n</code>&nbsp;个节点的&nbsp;<strong>有向带权</strong>&nbsp;图，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。图中的初始边用数组&nbsp;<code>edges</code>&nbsp;表示，其中&nbsp;<code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, edgeCost<sub>i</sub>]</code>&nbsp;表示从&nbsp;<code>from<sub>i</sub></code>&nbsp;到&nbsp;<code>to<sub>i</sub></code>&nbsp;有一条代价为&nbsp;<code>edgeCost<sub>i</sub></code>&nbsp;的边。</p>

<p>请你实现一个&nbsp;<code>Graph</code>&nbsp;类：</p>

<ul>
	<li><code>Graph(int n, int[][] edges)</code>&nbsp;初始化图有&nbsp;<code>n</code>&nbsp;个节点，并输入初始边。</li>
	<li><code>addEdge(int[] edge)</code>&nbsp;向边集中添加一条边，其中<strong>&nbsp;</strong><code>edge = [from, to, edgeCost]</code>&nbsp;。数据保证添加这条边之前对应的两个节点之间没有有向边。</li>
	<li><code>int shortestPath(int node1, int node2)</code>&nbsp;返回从节点&nbsp;<code>node1</code>&nbsp;到&nbsp;<code>node2</code>&nbsp;的路径<strong>&nbsp;最小</strong>&nbsp;代价。如果路径不存在，返回&nbsp;<code>-1</code>&nbsp;。一条路径的代价是路径中所有边代价之和。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/graph3drawio-2.png" style="width: 621px; height: 191px;"></p>

<pre><strong>输入：</strong>
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
<b>输出：</b>
[null, 6, -1, null, 6]

<strong>解释：</strong>
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // 返回 6 。从 3 到 2 的最短路径如第一幅图所示：3 -&gt; 0 -&gt; 1 -&gt; 2 ，总代价为 3 + 2 + 1 = 6 。
g.shortestPath(0, 3); // 返回 -1 。没有从 0 到 3 的路径。
g.addEdge([1, 3, 4]); // 添加一条节点 1 到节点 3 的边，得到第二幅图。
g.shortestPath(0, 3); // 返回 6 。从 0 到 3 的最短路径为 0 -&gt; 1 -&gt; 3 ，总代价为 2 + 4 = 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1)</code></li>
	<li><code>edges[i].length == edge.length == 3</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub>, from, to, node1, node2 &lt;= n - 1</code></li>
	<li><code>1 &lt;= edgeCost<sub>i</sub>, edgeCost &lt;= 10<sup>6</sup></code></li>
	<li>图中任何时候都不会有重边和自环。</li>
	<li>调用 <code>addEdge</code>&nbsp;至多&nbsp;<code>100</code>&nbsp;次。</li>
	<li>调用 <code>shortestPath</code>&nbsp;至多&nbsp;<code>100</code>&nbsp;次。</li>
</ul>


## 难度

Hard

## 标签

- 图
- 设计
- 最短路
- 堆（优先队列）

## 提示

1. After adding each edge, update your graph with the new edge, and you can calculate the shortest path in your graph each time the shortestPath method is called.
2. Use dijkstra’s algorithm to calculate the shortest paths.

## 示例

```
["Graph","shortestPath","shortestPath","addEdge","shortestPath"]
[[4,[[0,2,5],[0,1,2],[1,2,1],[3,0,3]]],[3,2],[0,3],[[1,3,4]],[0,3]]
```

## 示例代码

### C++

```cpp
class Graph {
public:
    Graph(int n, vector<vector<int>>& edges) {
        
    }
    
    void addEdge(vector<int> edge) {
        
    }
    
    int shortestPath(int node1, int node2) {
        
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */
```

### Java

```java
class Graph {

    public Graph(int n, int[][] edges) {
        
    }
    
    public void addEdge(int[] edge) {
        
    }
    
    public int shortestPath(int node1, int node2) {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.addEdge(edge);
 * int param_2 = obj.shortestPath(node1,node2);
 */
```

### Python

```python
class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
```

### Python3

```python3
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        

    def addEdge(self, edge: List[int]) -> None:
        

    def shortestPath(self, node1: int, node2: int) -> int:
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
```

### C

```c



typedef struct {
    
} Graph;


Graph* graphCreate(int n, int** edges, int edgesSize, int* edgesColSize) {
    
}

void graphAddEdge(Graph* obj, int* edge, int edgeSize) {
    
}

int graphShortestPath(Graph* obj, int node1, int node2) {
    
}

void graphFree(Graph* obj) {
    
}

/**
 * Your Graph struct will be instantiated and called as such:
 * Graph* obj = graphCreate(n, edges, edgesSize, edgesColSize);
 * graphAddEdge(obj, edge, edgeSize);
 
 * int param_2 = graphShortestPath(obj, node1, node2);
 
 * graphFree(obj);
*/
```

### C#

```csharp
public class Graph {

    public Graph(int n, int[][] edges) {
        
    }
    
    public void AddEdge(int[] edge) {
        
    }
    
    public int ShortestPath(int node1, int node2) {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.AddEdge(edge);
 * int param_2 = obj.ShortestPath(node1,node2);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 */
var Graph = function(n, edges) {
    
};

/** 
 * @param {number[]} edge
 * @return {void}
 */
Graph.prototype.addEdge = function(edge) {
    
};

/** 
 * @param {number} node1 
 * @param {number} node2
 * @return {number}
 */
Graph.prototype.shortestPath = function(node1, node2) {
    
};

/** 
 * Your Graph object will be instantiated and called as such:
 * var obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

### TypeScript

```typescript
class Graph {
    constructor(n: number, edges: number[][]) {
        
    }

    addEdge(edge: number[]): void {
        
    }

    shortestPath(node1: number, node2: number): number {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * var obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

### PHP

```php
class Graph {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     */
    function __construct($n, $edges) {
        
    }
  
    /**
     * @param Integer[] $edge
     * @return NULL
     */
    function addEdge($edge) {
        
    }
  
    /**
     * @param Integer $node1
     * @param Integer $node2
     * @return Integer
     */
    function shortestPath($node1, $node2) {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * $obj = Graph($n, $edges);
 * $obj->addEdge($edge);
 * $ret_2 = $obj->shortestPath($node1, $node2);
 */
```

### Swift

```swift

class Graph {

    init(_ n: Int, _ edges: [[Int]]) {
        
    }
    
    func addEdge(_ edge: [Int]) {
        
    }
    
    func shortestPath(_ node1: Int, _ node2: Int) -> Int {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * let obj = Graph(n, edges)
 * obj.addEdge(edge)
 * let ret_2: Int = obj.shortestPath(node1, node2)
 */
```

### Kotlin

```kotlin
class Graph(n: Int, edges: Array<IntArray>) {

    fun addEdge(edge: IntArray) {
        
    }

    fun shortestPath(node1: Int, node2: Int): Int {
        
    }

}

/**
 * Your Graph object will be instantiated and called as such:
 * var obj = Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

### Dart

```dart
class Graph {

  Graph(int n, List<List<int>> edges) {
    
  }
  
  void addEdge(List<int> edge) {
    
  }
  
  int shortestPath(int node1, int node2) {
    
  }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = Graph(n, edges);
 * obj.addEdge(edge);
 * int param2 = obj.shortestPath(node1,node2);
 */
```

### Go

```golang
type Graph struct {
    
}


func Constructor(n int, edges [][]int) Graph {
    
}


func (this *Graph) AddEdge(edge []int)  {
    
}


func (this *Graph) ShortestPath(node1 int, node2 int) int {
    
}


/**
 * Your Graph object will be instantiated and called as such:
 * obj := Constructor(n, edges);
 * obj.AddEdge(edge);
 * param_2 := obj.ShortestPath(node1,node2);
 */
```

### Ruby

```ruby
class Graph

=begin
    :type n: Integer
    :type edges: Integer[][]
=end
    def initialize(n, edges)
        
    end


=begin
    :type edge: Integer[]
    :rtype: Void
=end
    def add_edge(edge)
        
    end


=begin
    :type node1: Integer
    :type node2: Integer
    :rtype: Integer
=end
    def shortest_path(node1, node2)
        
    end


end

# Your Graph object will be instantiated and called as such:
# obj = Graph.new(n, edges)
# obj.add_edge(edge)
# param_2 = obj.shortest_path(node1, node2)
```

### Scala

```scala
class Graph(_n: Int, _edges: Array[Array[Int]]) {

    def addEdge(edge: Array[Int]): Unit = {
        
    }

    def shortestPath(node1: Int, node2: Int): Int = {
        
    }

}

/**
 * Your Graph object will be instantiated and called as such:
 * val obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * val param_2 = obj.shortestPath(node1,node2)
 */
```

### Rust

```rust
struct Graph {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Graph {

    fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn add_edge(&self, edge: Vec<i32>) {
        
    }
    
    fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * let obj = Graph::new(n, edges);
 * obj.add_edge(edge);
 * let ret_2: i32 = obj.shortest_path(node1, node2);
 */
```

### Racket

```racket
(define graph%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; edges : (listof (listof exact-integer?))
    (init-field
      n
      edges)
    
    ; add-edge : (listof exact-integer?) -> void?
    (define/public (add-edge edge)
      )
    ; shortest-path : exact-integer? exact-integer? -> exact-integer?
    (define/public (shortest-path node1 node2)
      )))

;; Your graph% object will be instantiated and called as such:
;; (define obj (new graph% [n n] [edges edges]))
;; (send obj add-edge edge)
;; (define param_2 (send obj shortest-path node1 node2))
```

### Erlang

```erlang
-spec graph_init_(N :: integer(), Edges :: [[integer()]]) -> any().
graph_init_(N, Edges) ->
  .

-spec graph_add_edge(Edge :: [integer()]) -> any().
graph_add_edge(Edge) ->
  .

-spec graph_shortest_path(Node1 :: integer(), Node2 :: integer()) -> integer().
graph_shortest_path(Node1, Node2) ->
  .


%% Your functions will be called as such:
%% graph_init_(N, Edges),
%% graph_add_edge(Edge),
%% Param_2 = graph_shortest_path(Node1, Node2),

%% graph_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Graph do
  @spec init_(n :: integer, edges :: [[integer]]) :: any
  def init_(n, edges) do
    
  end

  @spec add_edge(edge :: [integer]) :: any
  def add_edge(edge) do
    
  end

  @spec shortest_path(node1 :: integer, node2 :: integer) :: integer
  def shortest_path(node1, node2) do
    
  end
end

# Your functions will be called as such:
# Graph.init_(n, edges)
# Graph.add_edge(edge)
# param_2 = Graph.shortest_path(node1, node2)

# Graph.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Graph {
    init(n: Int64, edges: Array<Array<Int64>>) {

    }
    
    func addEdge(edge: Array<Int64>): Unit {

    }
    
    func shortestPath(node1: Int64, node2: Int64): Int64 {

    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * let obj: Graph = Graph(n, edges)
 * obj.addEdge(edge)
 * let param_2 = obj.shortestPath(node1,node2)
 */
```

