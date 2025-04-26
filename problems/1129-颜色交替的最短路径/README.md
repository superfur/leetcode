# 1129. 颜色交替的最短路径

## 题目描述

<p>给定一个整数 <code>n</code>，即有向图中的节点数，其中节点标记为 <code>0</code> 到 <code>n - 1</code>。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。</p>

<p>给定两个数组&nbsp;<code>redEdges</code>&nbsp;和&nbsp;<code>blueEdges</code>，其中：</p>

<ul>
	<li><code>redEdges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示图中存在一条从节点&nbsp;<code>a<sub>i</sub></code>&nbsp;到节点&nbsp;<code>b<sub>i</sub></code>&nbsp;的红色有向边，</li>
	<li><code>blueEdges[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>&nbsp;表示图中存在一条从节点&nbsp;<code>u<sub>j</sub></code>&nbsp;到节点&nbsp;<code>v<sub>j</sub></code>&nbsp;的蓝色有向边。</li>
</ul>

<p>返回长度为 <code>n</code> 的数组&nbsp;<code>answer</code>，其中&nbsp;<code>answer[X]</code>&nbsp;是从节点&nbsp;<code>0</code>&nbsp;到节点&nbsp;<code>X</code>&nbsp;的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 <code>answer[x] = -1</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
<strong>输出：</strong>[0,1,-1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
<strong>输出：</strong>[0,1,-1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= redEdges.length,&nbsp;blueEdges.length &lt;= 400</code></li>
	<li><code>redEdges[i].length == blueEdges[j].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub>, u<sub>j</sub>, v<sub>j</sub>&nbsp;&lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 图

## 提示

1. Do a breadth-first search, where the "nodes" are actually (Node, color of last edge taken).

## 示例

```
3
[[0,1],[1,2]]
[]
3
[[0,1]]
[[2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestAlternatingPaths(int n, int** redEdges, int redEdgesSize, int* redEdgesColSize, int** blueEdges, int blueEdgesSize, int* blueEdgesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ShortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
var shortestAlternatingPaths = function(n, redEdges, blueEdges) {
    
};
```

### TypeScript

```typescript
function shortestAlternatingPaths(n: number, redEdges: number[][], blueEdges: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $redEdges
     * @param Integer[][] $blueEdges
     * @return Integer[]
     */
    function shortestAlternatingPaths($n, $redEdges, $blueEdges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestAlternatingPaths(_ n: Int, _ redEdges: [[Int]], _ blueEdges: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestAlternatingPaths(n: Int, redEdges: Array<IntArray>, blueEdges: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> shortestAlternatingPaths(int n, List<List<int>> redEdges, List<List<int>> blueEdges) {
    
  }
}
```

### Go

```golang
func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} red_edges
# @param {Integer[][]} blue_edges
# @return {Integer[]}
def shortest_alternating_paths(n, red_edges, blue_edges)
    
end
```

### Scala

```scala
object Solution {
    def shortestAlternatingPaths(n: Int, redEdges: Array[Array[Int]], blueEdges: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_alternating_paths(n: i32, red_edges: Vec<Vec<i32>>, blue_edges: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-alternating-paths n redEdges blueEdges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec shortest_alternating_paths(N :: integer(), RedEdges :: [[integer()]], BlueEdges :: [[integer()]]) -> [integer()].
shortest_alternating_paths(N, RedEdges, BlueEdges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_alternating_paths(n :: integer, red_edges :: [[integer]], blue_edges :: [[integer]]) :: [integer]
  def shortest_alternating_paths(n, red_edges, blue_edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestAlternatingPaths(n: Int64, redEdges: Array<Array<Int64>>, blueEdges: Array<Array<Int64>>): Array<Int64> {

    }
}
```

