# 3123. 最短路径中的边

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的无向带权图，节点编号为 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;。图中总共有 <code>m</code>&nbsp;条边，用二维数组&nbsp;<code>edges</code>&nbsp;表示，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, w<sub>i</sub>]</code>&nbsp;表示节点 <code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边权为&nbsp;<code>w<sub>i</sub></code>&nbsp;的边。</p>

<p>对于节点 <code>0</code>&nbsp;为出发点，节点 <code>n - 1</code>&nbsp;为结束点的所有最短路，你需要返回一个长度为 <code>m</code>&nbsp;的 <strong>boolean</strong>&nbsp;数组&nbsp;<code>answer</code>&nbsp;，如果&nbsp;<code>edges[i]</code>&nbsp;<strong>至少</strong>&nbsp;在其中一条最短路上，那么&nbsp;<code>answer[i]</code>&nbsp;为&nbsp;<code>true</code>&nbsp;，否则&nbsp;<code>answer[i]</code>&nbsp;为&nbsp;<code>false</code>&nbsp;。</p>

<p>请你返回数组&nbsp;<code>answer</code>&nbsp;。</p>

<p><b>注意</b>，图可能不连通。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/05/graph35drawio-1.png" style="height: 129px; width: 250px;" /></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]</span></p>

<p><span class="example-io"><b>输出：</b>[true,true,true,false,true,true,true,false]</span></p>

<p><strong>解释：</strong></p>

<p>以下为节点 0 出发到达节点 5 的 <strong>所有</strong>&nbsp;最短路：</p>

<ul>
	<li>路径&nbsp;<code>0 -&gt; 1 -&gt; 5</code>&nbsp;：边权和为&nbsp;<code>4 + 1 = 5</code>&nbsp;。</li>
	<li>路径&nbsp;<code>0 -&gt; 2 -&gt; 3 -&gt; 5</code>&nbsp;：边权和为&nbsp;<code>1 + 1 + 3 = 5</code>&nbsp;。</li>
	<li>路径&nbsp;<code>0 -&gt; 2 -&gt; 3 -&gt; 1 -&gt; 5</code>&nbsp;：边权和为&nbsp;<code>1 + 1 + 2 + 1 = 5</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/05/graphhhh.png" style="width: 185px; height: 136px;" /></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]</span></p>

<p><span class="example-io"><b>输出：</b>[true,false,false,true]</span></p>

<p><strong>解释：</strong></p>

<p>只有一条从节点 0 出发到达节点 3 的最短路&nbsp;<code>0 -&gt; 2 -&gt; 3</code>&nbsp;，边权和为&nbsp;<code>1 + 2 = 3</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>m == edges.length</code></li>
	<li><code>1 &lt;= m &lt;= min(5 * 10<sup>4</sup>, n * (n - 1) / 2)</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li>图中没有重边。</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 最短路
- 堆（优先队列）

## 提示

1. Find all the shortest paths starting from nodes 0 and <code>n - 1</code> to all other nodes.
2. How to use the above calculated shortest paths to check if an edge is part of at least one shortest path from 0 to <code>n - 1</code>?

## 示例

```
6
[[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
4
[[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> findAnswer(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean[] findAnswer(int n, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* findAnswer(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool[] FindAnswer(int n, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean[]}
 */
var findAnswer = function(n, edges) {
    
};
```

### TypeScript

```typescript
function findAnswer(n: number, edges: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Boolean[]
     */
    function findAnswer($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findAnswer(_ n: Int, _ edges: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findAnswer(n: Int, edges: Array<IntArray>): BooleanArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> findAnswer(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func findAnswer(n int, edges [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean[]}
def find_answer(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def findAnswer(n: Int, edges: Array[Array[Int]]): Array[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_answer(n: i32, edges: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (find-answer n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec find_answer(N :: integer(), Edges :: [[integer()]]) -> [boolean()].
find_answer(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_answer(n :: integer, edges :: [[integer]]) :: [boolean]
  def find_answer(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findAnswer(n: Int64, edges: Array<Array<Int64>>): Array<Bool> {

    }
}
```

