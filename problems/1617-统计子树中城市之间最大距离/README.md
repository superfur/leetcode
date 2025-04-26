# 1617. 统计子树中城市之间最大距离

## 题目描述

<p>给你 <code>n</code> 个城市，编号为从 <code>1</code> 到 <code>n</code> 。同时给你一个大小为 <code>n-1</code> 的数组 <code>edges</code> ，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示城市 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code><sub> </sub>之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 <strong>树</strong> 。</p>

<p>一棵 <strong>子树</strong> 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。</p>

<p>对于 <code>d</code> 从 <code>1</code> 到 <code>n-1</code> ，请你找到城市间 <strong>最大距离</strong> 恰好为 <code>d</code> 的所有子树数目。</p>

<p>请你返回一个大小为 <code>n-1</code> 的数组，其中第<em> </em><code>d</code><em> </em>个元素（<strong>下标从 1 开始</strong>）是城市间 <strong>最大距离</strong> 恰好等于 <code>d</code> 的子树数目。</p>

<p><strong>请注意</strong>，两个城市间距离定义为它们之间需要经过的边的数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/p1.png" style="width: 161px; height: 181px;" /></strong></p>

<pre>
<b>输入：</b>n = 4, edges = [[1,2],[2,3],[2,4]]
<b>输出：</b>[3,4,0]
<strong>解释：
</strong>子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 2, edges = [[1,2]]
<b>输出：</b>[1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 3, edges = [[1,2],[2,3]]
<b>输出：</b>[2,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 15</code></li>
	<li><code>edges.length == n-1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 <= u<sub>i</sub>, v<sub>i</sub> <= n</code></li>
	<li>题目保证 <code>(u<sub>i</sub>, v<sub>i</sub>)</code> 所表示的边互不相同。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 树
- 动态规划
- 状态压缩
- 枚举

## 提示

1. Iterate through every possible subtree by doing a bitmask on which vertices to include. How can you determine if a subtree is valid (all vertices are connected)?
2. To determine connectivity, count the number of reachable vertices starting from any included vertex and only traveling on edges connecting 2 vertices in the subtree. The count should be the same as the number of 1s in the bitmask.
3. The diameter is basically the maximum distance between any two nodes. Root the tree at a vertex. The answer is the max of the heights of the two largest subtrees or the longest diameter in any of the subtrees.

## 示例

```
4
[[1,2],[2,3],[2,4]]
2
[[1,2]]
3
[[1,2],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countSubgraphsForEachDiameter(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countSubgraphsForEachDiameter(int n, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSubgraphsForEachDiameter(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountSubgraphsForEachDiameter(int n, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var countSubgraphsForEachDiameter = function(n, edges) {
    
};
```

### TypeScript

```typescript
function countSubgraphsForEachDiameter(n: number, edges: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function countSubgraphsForEachDiameter($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubgraphsForEachDiameter(_ n: Int, _ edges: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubgraphsForEachDiameter(n: Int, edges: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countSubgraphsForEachDiameter(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def count_subgraphs_for_each_diameter(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def countSubgraphsForEachDiameter(n: Int, edges: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_subgraphs_for_each_diameter(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-subgraphs-for-each-diameter n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_subgraphs_for_each_diameter(N :: integer(), Edges :: [[integer()]]) -> [integer()].
count_subgraphs_for_each_diameter(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_subgraphs_for_each_diameter(n :: integer, edges :: [[integer]]) :: [integer]
  def count_subgraphs_for_each_diameter(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubgraphsForEachDiameter(n: Int64, edges: Array<Array<Int64>>): Array<Int64> {

    }
}
```

