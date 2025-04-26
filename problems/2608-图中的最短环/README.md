# 2608. 图中的最短环

## 题目描述

<p>现有一个含 <code>n</code> 个顶点的 <strong>双向</strong> 图，每个顶点按从 <code>0</code> 到 <code>n - 1</code> 标记。图中的边由二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示顶点 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code> 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。</p>

<p>返回图中 <strong>最短</strong> 环的长度。如果不存在环，则返回 <code>-1</code> 。</p>

<p><strong>环</strong> 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/04/cropped.png" style="width: 387px; height: 331px;">
<pre><strong>输入：</strong>n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
<strong>输出：</strong>3
<strong>解释：</strong>长度最小的循环是：0 -&gt; 1 -&gt; 2 -&gt; 0 
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/04/croppedagin.png" style="width: 307px; height: 307px;">
<pre><strong>输入：</strong>n = 4, edges = [[0,1],[0,2]]
<strong>输出：</strong>-1
<strong>解释：</strong>图中不存在循环
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= edges.length &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li>不存在重复的边</li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 图

## 提示

1. How can BFS be used?
2. For each vertex u, calculate the length of the shortest cycle that contains vertex u using BFS

## 示例

```
7
[[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
4
[[0,1],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int findShortestCycle(int n, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
```

### C

```c
int findShortestCycle(int n, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindShortestCycle(int n, int[][] edges) {
        
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
var findShortestCycle = function(n, edges) {
    
};
```

### TypeScript

```typescript
function findShortestCycle(n: number, edges: number[][]): number {
    
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
    function findShortestCycle($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findShortestCycle(_ n: Int, _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findShortestCycle(n: Int, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findShortestCycle(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func findShortestCycle(n int, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_shortest_cycle(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def findShortestCycle(n: Int, edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-shortest-cycle n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_shortest_cycle(N :: integer(), Edges :: [[integer()]]) -> integer().
find_shortest_cycle(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_shortest_cycle(n :: integer, edges :: [[integer]]) :: integer
  def find_shortest_cycle(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findShortestCycle(n: Int64, edges: Array<Array<Int64>>): Int64 {

    }
}
```

