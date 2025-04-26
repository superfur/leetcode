# 1976. 到达目的地的方案数

## 题目描述

<p>你在一个城市里，城市由 <code>n</code>&nbsp;个路口组成，路口编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，某些路口之间有 <strong>双向</strong>&nbsp;道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。</p>

<p>给你一个整数&nbsp;<code>n</code>&nbsp;和二维整数数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [u<sub>i</sub>, v<sub>i</sub>, time<sub>i</sub>]</code>&nbsp;表示在路口&nbsp;<code>u<sub>i</sub></code>&nbsp;和&nbsp;<code>v<sub>i</sub></code>&nbsp;之间有一条需要花费&nbsp;<code>time<sub>i</sub></code>&nbsp;时间才能通过的道路。你想知道花费 <strong>最少时间</strong>&nbsp;从路口&nbsp;<code>0</code>&nbsp;出发到达路口&nbsp;<code>n - 1</code>&nbsp;的方案数。</p>

<p>请返回花费 <strong>最少时间</strong>&nbsp;到达目的地的 <strong>路径数目</strong>&nbsp;。由于答案可能很大，将结果对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/02/14/1976_corrected.png" style="width: 255px; height: 400px;" />
<pre>
<b>输入：</b>n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
<b>输出：</b>4
<b>解释：</b>从路口 0 出发到路口 6 花费的最少时间是 7 分钟。
四条花费 7 分钟的路径分别为：
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 2, roads = [[1,0,10]]
<b>输出：</b>1
<b>解释：</b>只有一条从路口 0 到路口 1 的路，花费 10 分钟。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>n - 1 &lt;= roads.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>roads[i].length == 3</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>1 &lt;= time<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>u<sub>i </sub>!= v<sub>i</sub></code></li>
	<li>任意两个路口之间至多有一条路。</li>
	<li>从任意路口出发，你能够到达其他任意路口。</li>
</ul>


## 难度

Medium

## 标签

- 图
- 拓扑排序
- 动态规划
- 最短路

## 提示

1. First use any shortest path algorithm to get edges where dist[u] + weight = dist[v], here dist[x] is the shortest distance between node 0 and x
2. Using those edges only the graph turns into a dag now we just need to know the number of ways to get from node 0 to node n - 1 on a dag using dp

## 示例

```
7
[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
2
[[1,0,10]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPaths(int n, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
```

### C

```c
int countPaths(int n, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPaths(int n, int[][] roads) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    
};
```

### TypeScript

```typescript
function countPaths(n: number, roads: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function countPaths($n, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPaths(_ n: Int, _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPaths(n: Int, roads: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPaths(int n, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func countPaths(n int, roads [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def count_paths(n, roads)
    
end
```

### Scala

```scala
object Solution {
    def countPaths(n: Int, roads: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_paths(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-paths n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_paths(N :: integer(), Roads :: [[integer()]]) -> integer().
count_paths(N, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_paths(n :: integer, roads :: [[integer]]) :: integer
  def count_paths(n, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPaths(n: Int64, roads: Array<Array<Int64>>): Int64 {

    }
}
```

