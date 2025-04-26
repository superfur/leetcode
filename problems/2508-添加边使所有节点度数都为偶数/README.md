# 2508. 添加边使所有节点度数都为偶数

## 题目描述

<p>给你一个有 <code>n</code>&nbsp;个节点的 <strong>无向</strong>&nbsp;图，节点编号为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;。再给你整数&nbsp;<code>n</code>&nbsp;和一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边。图不一定连通。</p>

<p>你可以给图中添加 <strong>至多</strong>&nbsp;两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。</p>

<p>如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>点的度数是连接一个点的边的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/26/agraphdrawio.png" style="width: 500px; height: 190px;" /></p>

<pre>
<b>输入：</b>n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
<b>输出：</b>true
<b>解释：</b>上图展示了添加一条边的合法方案。
最终图中每个节点都连接偶数条边。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/26/aagraphdrawio.png" style="width: 400px; height: 120px;" /></p>

<pre>
<b>输入：</b>n = 4, edges = [[1,2],[3,4]]
<b>输出：</b>true
<b>解释：</b>上图展示了添加两条边的合法方案。</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/26/aaagraphdrawio.png" style="width: 150px; height: 158px;" /></p>

<pre>
<b>输入：</b>n = 4, edges = [[1,2],[1,3],[1,4]]
<b>输出：</b>false
<b>解释：</b>无法添加至多 2 条边得到一个符合要求的图。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>图中不会有重边</li>
</ul>


## 难度

Hard

## 标签

- 图
- 哈希表

## 提示

1. Notice that each edge that we add changes the degree of exactly 2 nodes.
2. The number of nodes with an odd degree in the original graph should be either 0, 2, or 4. Try to work on each of these cases.

## 示例

```
5
[[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
4
[[1,2],[3,4]]
4
[[1,2],[1,3],[1,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPossible(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPossible(int n, List<List<Integer>> edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
```

### C

```c
bool isPossible(int n, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPossible(int n, IList<IList<int>> edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var isPossible = function(n, edges) {
    
};
```

### TypeScript

```typescript
function isPossible(n: number, edges: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Boolean
     */
    function isPossible($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPossible(_ n: Int, _ edges: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPossible(n: Int, edges: List<List<Int>>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPossible(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func isPossible(n int, edges [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean}
def is_possible(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def isPossible(n: Int, edges: List[List[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_possible(n: i32, edges: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-possible n edges)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_possible(N :: integer(), Edges :: [[integer()]]) -> boolean().
is_possible(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_possible(n :: integer, edges :: [[integer]]) :: boolean
  def is_possible(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPossible(n: Int64, edges: ArrayList<ArrayList<Int64>>): Bool {

    }
}
```

