# 1192. 查找集群内的关键连接

## 题目描述

<p>力扣数据中心有&nbsp;<code>n</code>&nbsp;台服务器，分别按从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的方式进行了编号。它们之间以 <strong>服务器到服务器</strong> 的形式相互连接组成了一个内部集群，连接是无向的。用 &nbsp;<code>connections</code> 表示集群网络，<code>connections[i] = [a, b]</code>&nbsp;表示服务器 <code>a</code>&nbsp;和 <code>b</code>&nbsp;之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。</p>

<p><strong>关键连接</strong><em> </em>是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。</p>

<p>请你以任意顺序返回该集群内的所有 <strong>关键连接</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/critical-connections-in-a-network.png" style="height: 205px; width: 200px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>输出：</strong>[[1,3]]
<strong>解释：</strong>[[3,1]] 也是正确的。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>n = 2, connections = [[0,1]]
<b>输出：</b>[[0,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n - 1 &lt;= connections.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>不存在重复的连接</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 图
- 双连通分量

## 提示

1. Use Tarjan's algorithm.

## 示例

```
4
[[0,1],[1,2],[2,0],[1,3]]
2
[[0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        
    }
}
```

### Python

```python
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** criticalConnections(int n, int** connections, int connectionsSize, int* connectionsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> CriticalConnections(int n, IList<IList<int>> connections) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function(n, connections) {
    
};
```

### TypeScript

```typescript
function criticalConnections(n: number, connections: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer[][]
     */
    function criticalConnections($n, $connections) {
        
    }
}
```

### Swift

```swift
class Solution {
    func criticalConnections(_ n: Int, _ connections: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> criticalConnections(int n, List<List<int>> connections) {
    
  }
}
```

### Go

```golang
func criticalConnections(n int, connections [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer[][]}
def critical_connections(n, connections)
    
end
```

### Scala

```scala
object Solution {
    def criticalConnections(n: Int, connections: List[List[Int]]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (critical-connections n connections)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec critical_connections(N :: integer(), Connections :: [[integer()]]) -> [[integer()]].
critical_connections(N, Connections) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec critical_connections(n :: integer, connections :: [[integer]]) :: [[integer]]
  def critical_connections(n, connections) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func criticalConnections(n: Int64, connections: ArrayList<ArrayList<Int64>>): ArrayList<ArrayList<Int64>> {

    }
}
```

