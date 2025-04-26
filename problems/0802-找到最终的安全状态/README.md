# 802. 找到最终的安全状态

## 题目描述

<p>有一个有 <code>n</code> 个节点的有向图，节点按 <code>0</code> 到 <code>n - 1</code> 编号。图由一个 <strong>索引从 0 开始</strong> 的 2D 整数数组&nbsp;<code>graph</code>表示，&nbsp;<code>graph[i]</code>是与节点 <code>i</code> 相邻的节点的整数数组，这意味着从节点 <code>i</code> 到&nbsp;<code>graph[i]</code>中的每个节点都有一条边。</p>

<p>如果一个节点没有连出的有向边，则该节点是 <strong>终端节点</strong> 。如果从该节点开始的所有可能路径都通向 <strong>终端节点</strong> ，则该节点为 <strong>终端节点</strong>（或另一个安全节点）。</p>

<p>返回一个由图中所有 <strong>安全节点</strong> 组成的数组作为答案。答案数组中的元素应当按 <strong>升序</strong> 排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" /></p>

<pre>
<strong>输入：</strong>graph = [[1,2],[2,3],[5],[0],[5],[],[]]
<strong>输出：</strong>[2,4,5,6]
<strong>解释：</strong>示意图如上。
节点 5 和节点 6 是终端节点，因为它们都没有出边。
从节点 2、4、5 和 6 开始的所有路径都指向节点 5 或 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
<strong>输出：</strong>[4]
<strong>解释:</strong>
只有节点 4 是终端节点，从节点 4 开始的所有路径都通向节点 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= graph[i].length &lt;= n</code></li>
	<li><code>0 &lt;= graph[i][j] &lt;= n - 1</code></li>
	<li><code>graph[i]</code> 按严格递增顺序排列。</li>
	<li>图中可能包含自环。</li>
	<li>图中边的数目在范围 <code>[1, 4 * 10<sup>4</sup>]</code> 内。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序

## 示例

```
[[1,2],[2,3],[5],[0],[5],[],[]]
[[1,2,3,4],[1,2],[3,4],[0,4],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        
    }
}
```

### Python

```python
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* eventualSafeNodes(int** graph, int graphSize, int* graphColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> EventualSafeNodes(int[][] graph) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {
    
};
```

### TypeScript

```typescript
function eventualSafeNodes(graph: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer[]
     */
    function eventualSafeNodes($graph) {
        
    }
}
```

### Swift

```swift
class Solution {
    func eventualSafeNodes(_ graph: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun eventualSafeNodes(graph: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> eventualSafeNodes(List<List<int>> graph) {
    
  }
}
```

### Go

```golang
func eventualSafeNodes(graph [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @return {Integer[]}
def eventual_safe_nodes(graph)
    
end
```

### Scala

```scala
object Solution {
    def eventualSafeNodes(graph: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (eventual-safe-nodes graph)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec eventual_safe_nodes(Graph :: [[integer()]]) -> [integer()].
eventual_safe_nodes(Graph) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec eventual_safe_nodes(graph :: [[integer]]) :: [integer]
  def eventual_safe_nodes(graph) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func eventualSafeNodes(graph: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

