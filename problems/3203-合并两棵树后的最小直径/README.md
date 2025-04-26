# 3203. 合并两棵树后的最小直径

## 题目描述

<p>给你两棵 <strong>无向</strong>&nbsp;树，分别有&nbsp;<code>n</code> 和&nbsp;<code>m</code>&nbsp;个节点，节点编号分别为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;和&nbsp;<code>0</code>&nbsp;到&nbsp;<code>m - 1</code>&nbsp;。给你两个二维整数数组&nbsp;<code>edges1</code> 和&nbsp;<code>edges2</code>&nbsp;，长度分别为&nbsp;<code>n - 1</code> 和&nbsp;<code>m - 1</code>&nbsp;，其中&nbsp;<code>edges1[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示在第一棵树中节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边，<code>edges2[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>&nbsp;表示在第二棵树中节点&nbsp;<code>u<sub>i</sub></code> 和&nbsp;<code>v<sub>i</sub></code>&nbsp;之间有一条边。</p>

<p>你必须在第一棵树和第二棵树中分别选一个节点，并用一条边连接它们。</p>

<p>请你返回添加边后得到的树中，<strong>最小直径</strong>&nbsp;为多少。</p>

<p>一棵树的 <strong>直径</strong>&nbsp;指的是树中任意两个节点之间的最长路径长度。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b><img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example11-transformed.png" style="width: 1000px; height: 494px;" /></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>将第一棵树中的节点 0 与第二棵树中的任意节点连接，得到一棵直径为 3 的树。</p>
</div>

<p><strong class="example">示例 2：<img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example211.png" style="width: 1000px; height: 492px;" /></strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>将第一棵树中的节点 0 和第二棵树中的节点 0 连接，可以得到一棵直径为 5 的树。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>edges1.length == n - 1</code></li>
	<li><code>edges2.length == m - 1</code></li>
	<li><code>edges1[i].length == edges2[i].length == 2</code></li>
	<li><code>edges1[i] = [a<sub>i</sub>, b<sub>i</sub>]</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>edges2[i] = [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; m</code></li>
	<li>输入保证&nbsp;<code>edges1</code> 和&nbsp;<code>edges2</code>&nbsp;分别表示一棵合法的树。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. Suppose that we connected node <code>a</code> in tree1 with node <code>b</code> in tree2. The diameter length of the resulting tree will be the largest of the following 3 values: 
<ol>
<li>The diameter of tree 1.</li>
<li>The diameter of tree 2.</li>
<li>The length of the longest path that starts at node <code>a</code> and that is completely within Tree 1 + The length of the longest path that starts at node <code>b</code> and that is completely within Tree 2 + 1.</li>
</ol> 
The added one in the third value is due to the additional edge that we have added between trees 1 and 2.
2. Values 1 and 2 are constant regardless of our choice of <code>a</code> and <code>b</code>. Therefore, we need to pick <code>a</code> and <code>b</code> in such a way that minimizes value 3.
3. If we pick <code>a</code> and <code>b</code> optimally, they will be in the diameters of Tree 1 and Tree 2, respectively. Exactly which nodes of the diameter should we pick?
4. <code>a</code> is the center of the diameter of tree 1, and <code>b</code> is the center of the diameter of tree 2.

## 示例

```
[[0,1],[0,2],[0,3]]
[[0,1]]
[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
```

### C

```c
int minimumDiameterAfterMerge(int** edges1, int edges1Size, int* edges1ColSize, int** edges2, int edges2Size, int* edges2ColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @return {number}
 */
var minimumDiameterAfterMerge = function(edges1, edges2) {
    
};
```

### TypeScript

```typescript
function minimumDiameterAfterMerge(edges1: number[][], edges2: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges1
     * @param Integer[][] $edges2
     * @return Integer
     */
    function minimumDiameterAfterMerge($edges1, $edges2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDiameterAfterMerge(_ edges1: [[Int]], _ edges2: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDiameterAfterMerge(edges1: Array<IntArray>, edges2: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDiameterAfterMerge(List<List<int>> edges1, List<List<int>> edges2) {
    
  }
}
```

### Go

```golang
func minimumDiameterAfterMerge(edges1 [][]int, edges2 [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @return {Integer}
def minimum_diameter_after_merge(edges1, edges2)
    
end
```

### Scala

```scala
object Solution {
    def minimumDiameterAfterMerge(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_diameter_after_merge(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-diameter-after-merge edges1 edges2)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_diameter_after_merge(Edges1 :: [[integer()]], Edges2 :: [[integer()]]) -> integer().
minimum_diameter_after_merge(Edges1, Edges2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_diameter_after_merge(edges1 :: [[integer]], edges2 :: [[integer]]) :: integer
  def minimum_diameter_after_merge(edges1, edges2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDiameterAfterMerge(edges1: Array<Array<Int64>>, edges2: Array<Array<Int64>>): Int64 {

    }
}
```

