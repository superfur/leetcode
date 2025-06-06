# 1319. 连通网络的操作次数

## 题目描述

<p>用以太网线缆将&nbsp;<code>n</code>&nbsp;台计算机连接成一个网络，计算机的编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>。线缆用&nbsp;<code>connections</code>&nbsp;表示，其中&nbsp;<code>connections[i] = [a, b]</code>&nbsp;连接了计算机&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>。</p>

<p>网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。</p>

<p>给你这个计算机网络的初始布线&nbsp;<code>connections</code>，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回&nbsp;-1 。&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_1_1677.png" style="height: 167px; width: 570px;"></strong></p>

<pre><strong>输入：</strong>n = 4, connections = [[0,1],[0,2],[1,2]]
<strong>输出：</strong>1
<strong>解释：</strong>拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_2_1677.png" style="height: 175px; width: 660px;"></strong></p>

<pre><strong>输入：</strong>n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
<strong>输出：</strong>-1
<strong>解释：</strong>线缆数量不足。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>1 &lt;= connections.length &lt;= min(n*(n-1)/2, 10^5)</code></li>
	<li><code>connections[i].length == 2</code></li>
	<li><code>0 &lt;= connections[i][0], connections[i][1]&nbsp;&lt; n</code></li>
	<li><code>connections[i][0] != connections[i][1]</code></li>
	<li>没有重复的连接。</li>
	<li>两台计算机不会通过多条线缆连接。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 提示

1. As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.
2. Use DFS to determine the number of isolated computer clusters.

## 示例

```
4
[[0,1],[0,2],[1,2]]
6
[[0,1],[0,2],[0,3],[1,2],[1,3]]
6
[[0,1],[0,2],[0,3],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        
    }
};
```

### Java

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
```

### C

```c
int makeConnected(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MakeConnected(int n, int[][] connections) {
        
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
var makeConnected = function(n, connections) {
    
};
```

### TypeScript

```typescript
function makeConnected(n: number, connections: number[][]): number {
    
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
    function makeConnected($n, $connections) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeConnected(_ n: Int, _ connections: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeConnected(n: Int, connections: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeConnected(int n, List<List<int>> connections) {
    
  }
}
```

### Go

```golang
func makeConnected(n int, connections [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer}
def make_connected(n, connections)
    
end
```

### Scala

```scala
object Solution {
    def makeConnected(n: Int, connections: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (make-connected n connections)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec make_connected(N :: integer(), Connections :: [[integer()]]) -> integer().
make_connected(N, Connections) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_connected(n :: integer, connections :: [[integer]]) :: integer
  def make_connected(n, connections) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeConnected(n: Int64, connections: Array<Array<Int64>>): Int64 {

    }
}
```

