# 1466. 重新规划路线

## 题目描述

<p><code>n</code> 座城市，从 <code>0</code> 到 <code>n-1</code> 编号，其间共有 <code>n-1</code> 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。</p>

<p>路线用 <code>connections</code> 表示，其中 <code>connections[i] = [a, b]</code> 表示从城市 <code>a</code> 到 <code>b</code> 的一条有向路线。</p>

<p>今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。</p>

<p>请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。</p>

<p>题目数据 <strong>保证</strong> 每个城市在重新规划路线方向后都能到达城市 0 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_1_1819.png" style="height: 150px; width: 240px;"></strong></p>

<pre><strong>输入：</strong>n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
<strong>输出：</strong>3
<strong>解释：</strong>更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_2_1819.png" style="height: 60px; width: 380px;"></strong></p>

<pre><strong>输入：</strong>n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
<strong>输出：</strong>2
<strong>解释：</strong>更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 3, connections = [[1,0],[2,0]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10^4</code></li>
	<li><code>connections.length == n-1</code></li>
	<li><code>connections[i].length == 2</code></li>
	<li><code>0 &lt;= connections[i][0], connections[i][1] &lt;= n-1</code></li>
	<li><code>connections[i][0] != connections[i][1]</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. Treat the graph as undirected. Start a dfs from the root, if you come across an edge in the forward direction, you need to reverse the edge.

## 示例

```
6
[[0,1],[1,3],[2,3],[4,0],[4,5]]
5
[[1,0],[1,2],[3,2],[3,4]]
3
[[1,0],[2,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        
    }
};
```

### Java

```java
class Solution {
    public int minReorder(int n, int[][] connections) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
```

### C

```c
int minReorder(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinReorder(int n, int[][] connections) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    
};
```

### TypeScript

```typescript
function minReorder(n: number, connections: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer
     */
    function minReorder($n, $connections) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minReorder(_ n: Int, _ connections: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minReorder(int n, List<List<int>> connections) {
    
  }
}
```

### Go

```golang
func minReorder(n int, connections [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer}
def min_reorder(n, connections)
    
end
```

### Scala

```scala
object Solution {
    def minReorder(n: Int, connections: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-reorder n connections)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_reorder(N :: integer(), Connections :: [[integer()]]) -> integer().
min_reorder(N, Connections) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_reorder(n :: integer, connections :: [[integer]]) :: integer
  def min_reorder(n, connections) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minReorder(n: Int64, connections: Array<Array<Int64>>): Int64 {

    }
}
```

