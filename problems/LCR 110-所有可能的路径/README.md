# LCR 110. 所有可能的路径

## 题目描述

<p>给定一个有&nbsp;<code>n</code>&nbsp;个节点的有向无环图，用二维数组&nbsp;<code>graph</code>&nbsp;表示，请找到所有从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的路径并输出（不要求按顺序）。</p>

<p><code>graph</code>&nbsp;的第 <code>i</code> 个数组中的单元都表示有向图中 <code>i</code>&nbsp;号节点所能到达的下一些结点（译者注：有向图是有方向的，即规定了 a&rarr;b 你就不能从 b&rarr;a ），若为空，就是没有下一个节点了。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" style="height: 242px; width: 242px;" /></p>

<pre>
<strong>输入：</strong>graph = [[1,2],[3],[3],[]]
<strong>输出：</strong>[[0,1,3],[0,2,3]]
<strong>解释：</strong>有两条路径 0 -&gt; 1 -&gt; 3 和 0 -&gt; 2 -&gt; 3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" style="height: 301px; width: 423px;" /></p>

<pre>
<strong>输入：</strong>graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>输出：</strong>[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1],[]]
<strong>输出：</strong>[[0,1]]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,2,3],[2],[3],[]]
<strong>输出：</strong>[[0,1,2,3],[0,2,3],[0,3]]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,3],[2],[3],[]]
<strong>输出：</strong>[[0,1,2,3],[0,3]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 15</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; n</code></li>
	<li><code>graph[i][j] != i</code>&nbsp;</li>
	<li>保证输入为有向无环图 <code>(GAD)</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 797&nbsp;题相同：<a href="https://leetcode-cn.com/problems/all-paths-from-source-to-target/">https://leetcode-cn.com/problems/all-paths-from-source-to-target/</a></p>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 回溯

## 示例

```
[[1,2],[3],[3],[]]
[[4,3,1],[3,2,4],[3],[4],[]]
[[1],[]]
[[1,2,3],[2],[3],[]]
[[1,3],[2],[3],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {

    }
}
```

### Python

```python
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {

};
```

### TypeScript

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer[][]
     */
    function allPathsSourceTarget($graph) {

    }
}
```

### Swift

```swift
class Solution {
    func allPathsSourceTarget(_ graph: [[Int]]) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {

    }
}
```

### Go

```golang
func allPathsSourceTarget(graph [][]int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @return {Integer[][]}
def all_paths_source_target(graph)

end
```

### Scala

```scala
object Solution {
    def allPathsSourceTarget(graph: Array[Array[Int]]): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (all-paths-source-target graph)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec all_paths_source_target(Graph :: [[integer()]]) -> [[integer()]].
all_paths_source_target(Graph) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec all_paths_source_target(graph :: [[integer]]) :: [[integer]]
  def all_paths_source_target(graph) do

  end
end
```

