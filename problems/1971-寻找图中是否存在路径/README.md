# 1971. 寻找图中是否存在路径

## 题目描述

<p>有一个具有 <code>n</code> 个顶点的 <strong>双向</strong> 图，其中每个顶点标记从 <code>0</code> 到 <code>n - 1</code>（包含 <code>0</code> 和 <code>n - 1</code>）。图中的边用一个二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示顶点 <code>ui</code> 和顶点 <code>vi</code> 之间的双向边。 每个顶点对由 <strong>最多一条</strong> 边连接，并且没有顶点存在与自身相连的边。</p>

<p>请你确定是否存在从顶点 <code>source</code> 开始，到顶点 <code>destination</code> 结束的 <strong>有效路径</strong> 。</p>

<p>给你数组 <code>edges</code> 和整数 <code>n</code>、<code>source</code> 和 <code>destination</code>，如果从 <code>source</code> 到 <code>destination</code> 存在 <strong>有效路径</strong> ，则返回 <code>true</code>，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png" style="width: 141px; height: 121px;" />
<pre>
<strong>输入：</strong>n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
<strong>输出：</strong>true
<strong>解释：</strong>存在由顶点 0 到顶点 2 的路径:
- 0 → 1 → 2 
- 0 → 2
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png" style="width: 281px; height: 141px;" />
<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
<strong>输出：</strong>false
<strong>解释：</strong>不存在由顶点 0 到顶点 5 的路径.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= source, destination &lt;= n - 1</code></li>
	<li>不存在重复边</li>
	<li>不存在指向顶点自身的边</li>
</ul>


## 难度

Easy

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 示例

```
3
[[0,1],[1,2],[2,0]]
0
2
6
[[0,1],[0,2],[3,5],[5,4],[4,3]]
0
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
```

### C

```c
bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidPath(int n, int[][] edges, int source, int destination) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    
};
```

### TypeScript

```typescript
function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @return Boolean
     */
    function validPath($n, $edges, $source, $destination) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validPath(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validPath(int n, List<List<int>> edges, int source, int destination) {
    
  }
}
```

### Go

```golang
func validPath(n int, edges [][]int, source int, destination int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @return {Boolean}
def valid_path(n, edges, source, destination)
    
end
```

### Scala

```scala
object Solution {
    def validPath(n: Int, edges: Array[Array[Int]], source: Int, destination: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (valid-path n edges source destination)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec valid_path(N :: integer(), Edges :: [[integer()]], Source :: integer(), Destination :: integer()) -> boolean().
valid_path(N, Edges, Source, Destination) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_path(n :: integer, edges :: [[integer]], source :: integer, destination :: integer) :: boolean
  def valid_path(n, edges, source, destination) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validPath(n: Int64, edges: Array<Array<Int64>>, source: Int64, destination: Int64): Bool {

    }
}
```

