# 3249. 统计好节点的数目

## 题目描述

<p>现有一棵 <strong>无向</strong> 树，树中包含 <code>n</code> 个节点，按从 <code>0</code> 到 <code>n - 1</code> 标记。树的根节点是节点 <code>0</code> 。给你一个长度为 <code>n - 1</code> 的二维整数数组 <code>edges</code>，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 与节点 <code>b<sub>i</sub></code> 之间存在一条边。</p>

<p>如果一个节点的所有子节点为根的&nbsp;<span data-keyword="subtree">子树</span>&nbsp;包含的节点数相同，则认为该节点是一个 <strong>好节点</strong>。</p>

<p>返回给定树中<strong> 好节点 </strong>的数量。</p>

<p><strong>子树</strong>&nbsp;指的是一个节点以及它所有后代节点构成的一棵树。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]</span></p>

<p><strong>输出：</strong><span class="example-io">7</span></p>

<p><strong>说明：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/26/tree1.png" style="width: 360px; height: 158px;" />
<p>树的所有节点都是好节点。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]</span></p>

<p><strong>输出：</strong><span class="example-io">6</span></p>

<p><strong>说明：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-2024-06-03-193552.png" style="width: 360px; height: 303px;" />
<p>树中有 6 个好节点。上图中已将这些节点着色。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]</span></p>

<p><span class="example-io"><b>输出：</b>12</span></p>

<p><strong>解释：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/08/rob.jpg" style="width: 450px; height: 277px;" />
<p>除了节点 9 以外其他所有节点都是好节点。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li>输入确保 <code>edges</code> 总表示一棵有效的树。</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索

## 提示

1. Use DFS.

## 示例

```
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
[[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodNodes(vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodNodes(int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        
```

### C

```c
int countGoodNodes(int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodNodes(int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @return {number}
 */
var countGoodNodes = function(edges) {
    
};
```

### TypeScript

```typescript
function countGoodNodes(edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function countGoodNodes($edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodNodes(_ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodNodes(edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodNodes(List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func countGoodNodes(edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @return {Integer}
def count_good_nodes(edges)
    
end
```

### Scala

```scala
object Solution {
    def countGoodNodes(edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_nodes(edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-nodes edges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_nodes(Edges :: [[integer()]]) -> integer().
count_good_nodes(Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_nodes(edges :: [[integer]]) :: integer
  def count_good_nodes(edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodNodes(edges: Array<Array<Int64>>): Int64 {

    }
}
```

