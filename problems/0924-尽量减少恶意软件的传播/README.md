# 924. 尽量减少恶意软件的传播

## 题目描述

<p>给出了一个由 <code>n</code> 个节点组成的网络，用 <code>n × n</code> 个邻接矩阵图<meta charset="UTF-8" />&nbsp;<code>graph</code>&nbsp;表示。在节点网络中，当 <code>graph[i][j] = 1</code>&nbsp;时，表示节点&nbsp;<code>i</code>&nbsp;能够直接连接到另一个节点 <code>j</code>。&nbsp;</p>

<p>一些节点&nbsp;<code>initial</code>&nbsp;最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。</p>

<p>假设 <code>M(initial)</code> 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。</p>

<p>如果从&nbsp;<code>initial</code>&nbsp;中<strong>移除某一节点</strong>能够最小化 <code>M(initial)</code>， 返回该节点。如果有多个节点满足条件，就返回<strong>索引最小</strong>的节点。</p>

<p>请注意，如果某个节点已从受感染节点的列表 <code>initial</code> 中删除，它以后仍有可能因恶意软件传播而受到感染。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
<strong>输出：</strong>0
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
<strong>输出：</strong>0
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>n == graph[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 300</code></li>
	<li><code>graph[i][j]&nbsp;==&nbsp;0</code>&nbsp;或&nbsp;<code>1</code>.</li>
	<li><code>graph[i][j] == graph[j][i]</code></li>
	<li><code>graph[i][i] == 1</code></li>
	<li><code>1 &lt;= initial.length &lt;= n</code></li>
	<li><code>0 &lt;= initial[i] &lt;= n - 1</code></li>
	<li><code>initial</code>&nbsp;中所有整数均<strong>不重复</strong></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图
- 数组
- 哈希表

## 示例

```
[[1,1,0],[1,1,0],[0,0,1]]
[0,1]
[[1,0,0],[0,1,0],[0,0,1]]
[0,2]
[[1,1,1],[1,1,1],[1,1,1]]
[1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMalwareSpread(vector<vector<int>>& graph, vector<int>& initial) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMalwareSpread(int[][] graph, int[] initial) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        
```

### C

```c
int minMalwareSpread(int** graph, int graphSize, int* graphColSize, int* initial, int initialSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMalwareSpread(int[][] graph, int[] initial) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @param {number[]} initial
 * @return {number}
 */
var minMalwareSpread = function(graph, initial) {
    
};
```

### TypeScript

```typescript
function minMalwareSpread(graph: number[][], initial: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @param Integer[] $initial
     * @return Integer
     */
    function minMalwareSpread($graph, $initial) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMalwareSpread(_ graph: [[Int]], _ initial: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMalwareSpread(graph: Array<IntArray>, initial: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMalwareSpread(List<List<int>> graph, List<int> initial) {
    
  }
}
```

### Go

```golang
func minMalwareSpread(graph [][]int, initial []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @param {Integer[]} initial
# @return {Integer}
def min_malware_spread(graph, initial)
    
end
```

### Scala

```scala
object Solution {
    def minMalwareSpread(graph: Array[Array[Int]], initial: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_malware_spread(graph: Vec<Vec<i32>>, initial: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-malware-spread graph initial)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_malware_spread(Graph :: [[integer()]], Initial :: [integer()]) -> integer().
min_malware_spread(Graph, Initial) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_malware_spread(graph :: [[integer]], initial :: [integer]) :: integer
  def min_malware_spread(graph, initial) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMalwareSpread(graph: Array<Array<Int64>>, initial: Array<Int64>): Int64 {

    }
}
```

