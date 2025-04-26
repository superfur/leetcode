# 3108. 带权图里旅途的最小代价

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的带权无向图，节点编号为 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;。</p>

<p>给你一个整数 <code>n</code>&nbsp;和一个数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>u<sub>i</sub></code> 和&nbsp;<code>v<sub>i</sub></code>&nbsp;之间有一条权值为&nbsp;<code>w<sub>i</sub></code>&nbsp;的无向边。</p>

<p>在图中，一趟旅途包含一系列节点和边。旅途开始和结束点都是图中的节点，且图中存在连接旅途中相邻节点的边。注意，一趟旅途可能访问同一条边或者同一个节点多次。</p>

<p>如果旅途开始于节点 <code>u</code>&nbsp;，结束于节点 <code>v</code>&nbsp;，我们定义这一趟旅途的 <strong>代价</strong>&nbsp;是经过的边权按位与 <code>AND</code>&nbsp;的结果。换句话说，如果经过的边对应的边权为&nbsp;<code>w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>k</sub></code>&nbsp;，那么代价为<code>w<sub>0</sub> &amp; w<sub>1</sub> &amp; w<sub>2</sub> &amp; ... &amp; w<sub>k</sub></code>&nbsp;，其中&nbsp;<code>&amp;</code>&nbsp;表示按位与&nbsp;<code>AND</code>&nbsp;操作。</p>

<p>给你一个二维数组&nbsp;<code>query</code>&nbsp;，其中&nbsp;<code>query[i] = [s<sub>i</sub>, t<sub>i</sub>]</code>&nbsp;。对于每一个查询，你需要找出从节点开始&nbsp;<code>s<sub>i</sub></code>&nbsp;，在节点&nbsp;<code>t<sub>i</sub></code>&nbsp;处结束的旅途的最小代价。如果不存在这样的旅途，答案为&nbsp;<code>-1</code>&nbsp;。</p>

<p>返回数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[i]</code><em>&nbsp;</em>表示对于查询 <code>i</code>&nbsp;的&nbsp;<strong>最小</strong>&nbsp;旅途代价。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]</span></p>

<p><span class="example-io"><b>输出：</b>[1,-1]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/01/31/q4_example1-1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 351px; height: 141px;" /></p>

<p>第一个查询想要得到代价为 1 的旅途，我们依次访问：<code>0-&gt;1</code>（边权为 7 ）<code>1-&gt;2</code>&nbsp;（边权为 1 ）<code>2-&gt;1</code>（边权为 1 ）<code>1-&gt;3</code>&nbsp;（边权为 7 ）。</p>

<p>第二个查询中，无法从节点 3 到节点 4 ，所以答案为 -1 。</p>

<p><strong class="example">示例 2：</strong></p>
</div>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]</span></p>

<p><span class="example-io"><b>输出：</b>[0]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/01/31/q4_example2e.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 211px; height: 181px;" /></p>

<p>第一个查询想要得到代价为 0 的旅途，我们依次访问：<code>1-&gt;2</code>（边权为 1 ），<code>2-&gt;1</code>（边权 为 6 ），<code>1-&gt;2</code>（边权为 1 ）。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 3</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= query.length &lt;= 10<sup>5</sup></code></li>
	<li><code>query[i].length == 2</code></li>
	<li><code>0 &lt;= s<sub>i</sub>, t<sub>i</sub> &lt;= n - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 并查集
- 图
- 数组

## 提示

1. The intended solution uses Disjoint Set Union.
2. Notice that, if <code>u</code> and <code>v</code> are not connected then the answer is <code>-1</code>, otherwise we can use all the edges from the connected component where both belong to.

## 示例

```
5
[[0,1,7],[1,3,7],[1,2,1]]
[[0,3],[3,4]]
3
[[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
[[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minimumCost(int n, int** edges, int edgesSize, int* edgesColSize, int** query, int querySize, int* queryColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinimumCost(int n, int[][] edges, int[][] query) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[][]} query
 * @return {number[]}
 */
var minimumCost = function(n, edges, query) {
    
};
```

### TypeScript

```typescript
function minimumCost(n: number, edges: number[][], query: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[][] $query
     * @return Integer[]
     */
    function minimumCost($n, $edges, $query) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ n: Int, _ edges: [[Int]], _ query: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(n: Int, edges: Array<IntArray>, query: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minimumCost(int n, List<List<int>> edges, List<List<int>> query) {
    
  }
}
```

### Go

```golang
func minimumCost(n int, edges [][]int, query [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[][]} query
# @return {Integer[]}
def minimum_cost(n, edges, query)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost n edges query)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec minimum_cost(N :: integer(), Edges :: [[integer()]], Query :: [[integer()]]) -> [integer()].
minimum_cost(N, Edges, Query) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(n :: integer, edges :: [[integer]], query :: [[integer]]) :: [integer]
  def minimum_cost(n, edges, query) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(n: Int64, edges: Array<Array<Int64>>, query: Array<Array<Int64>>): Array<Int64> {

    }
}
```

