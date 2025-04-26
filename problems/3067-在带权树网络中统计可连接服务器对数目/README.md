# 3067. 在带权树网络中统计可连接服务器对数目

## 题目描述

<p>给你一棵无根带权树，树中总共有 <code>n</code>&nbsp;个节点，分别表示 <code>n</code>&nbsp;个服务器，服务器从 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;编号。同时给你一个数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, weight<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条双向边，边的权值为&nbsp;<code>weight<sub>i</sub></code>&nbsp;。再给你一个整数&nbsp;<code>signalSpeed</code>&nbsp;。</p>

<p>如果两台服务器 <code>a</code>&nbsp;和 <code>b</code>&nbsp;是通过服务器 <code>c</code>&nbsp;<strong>可连接的</strong>，则：</p>

<ul>
	<li><code>a &lt; b</code>&nbsp;，<code>a != c</code> 且&nbsp;<code>b != c</code>&nbsp;。</li>
	<li>从&nbsp;<code>c</code>&nbsp;到&nbsp;<code>a</code>&nbsp;的距离是可以被&nbsp;<code>signalSpeed</code>&nbsp;整除的。</li>
	<li>从&nbsp;<code>c</code>&nbsp;到&nbsp;<code>b</code>&nbsp;的距离是可以被&nbsp;<code>signalSpeed</code>&nbsp;整除的。</li>
	<li>从&nbsp;<code>c</code>&nbsp;到&nbsp;<code>b</code>&nbsp;的路径与从&nbsp;<code>c</code>&nbsp;到&nbsp;<code>a</code>&nbsp;的路径没有任何公共边。</li>
</ul>

<p>请你返回一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>count</code>&nbsp;，其中&nbsp;<code>count[i]</code> 表示通过服务器&nbsp;<code>i</code>&nbsp;<strong>可连接</strong>&nbsp;的服务器对的&nbsp;<strong>数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/01/21/example22.png" style="width: 438px; height: 243px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<pre>
<b>输入：</b>edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1
<b>输出：</b>[0,4,6,6,4,0]
<b>解释：</b>由于 signalSpeed 等于 1 ，count[c] 等于所有从 c 开始且没有公共边的路径对数目。
在输入图中，count[c] 等于服务器 c 左边服务器数目乘以右边服务器数目。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/01/21/example11.png" style="width: 495px; height: 484px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<pre>
<b>输入：</b>edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3
<b>输出：</b>[2,0,0,0,0,0,2]
<b>解释：</b>通过服务器 0 ，有 2 个可连接服务器对(4, 5) 和 (4, 6) 。
通过服务器 6 ，有 2 个可连接服务器对 (4, 5) 和 (0, 5) 。
所有服务器对都必须通过服务器 0 或 6 才可连接，所以其他服务器对应的可连接服务器对数目都为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 3</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, weight<sub>i</sub>]</code><!-- notionvc: a2623897-1bb1-4c07-84b6-917ffdcd83ec --></li>
	<li><code>1 &lt;= weight<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= signalSpeed &lt;= 10<sup>6</sup></code></li>
	<li>输入保证&nbsp;<code>edges</code>&nbsp;构成一棵合法的树。</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 数组

## 提示

1. Take each node as the root of the tree, run DFS, and save for each node <code>i</code>, the number of nodes in the subtree rooted at <code>i</code> whose distance to the root is divisible by <code>signalSpeed</code>.
2. If the root has <code>m</code> children named <code>c<sub>1</sub>, c<sub>2</sub>, …, c<sub>m</sub></code> that respectively have <code>num[c<sub>1</sub>], num[c<sub>2</sub>], …, num[c<sub>m</sub>]</code> nodes in their subtrees whose distance is divisible by signalSpeed. Then, there are <code>((S - num[c<sub>i</sub>]) * num[c<sub>i</sub>]) / 2</code>that are connectable through the root that we have fixed, where <code>S</code> is the sum of <code>num[c<sub>i</sub>]</code>.

## 示例

```
[[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
1
[[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countPairsOfConnectableServers(vector<vector<int>>& edges, int signalSpeed) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPairsOfConnectableServers(int** edges, int edgesSize, int* edgesColSize, int signalSpeed, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} signalSpeed
 * @return {number[]}
 */
var countPairsOfConnectableServers = function(edges, signalSpeed) {
    
};
```

### TypeScript

```typescript
function countPairsOfConnectableServers(edges: number[][], signalSpeed: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $signalSpeed
     * @return Integer[]
     */
    function countPairsOfConnectableServers($edges, $signalSpeed) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairsOfConnectableServers(_ edges: [[Int]], _ signalSpeed: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairsOfConnectableServers(edges: Array<IntArray>, signalSpeed: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countPairsOfConnectableServers(List<List<int>> edges, int signalSpeed) {
    
  }
}
```

### Go

```golang
func countPairsOfConnectableServers(edges [][]int, signalSpeed int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer} signal_speed
# @return {Integer[]}
def count_pairs_of_connectable_servers(edges, signal_speed)
    
end
```

### Scala

```scala
object Solution {
    def countPairsOfConnectableServers(edges: Array[Array[Int]], signalSpeed: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs_of_connectable_servers(edges: Vec<Vec<i32>>, signal_speed: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs-of-connectable-servers edges signalSpeed)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_pairs_of_connectable_servers(Edges :: [[integer()]], SignalSpeed :: integer()) -> [integer()].
count_pairs_of_connectable_servers(Edges, SignalSpeed) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs_of_connectable_servers(edges :: [[integer]], signal_speed :: integer) :: [integer]
  def count_pairs_of_connectable_servers(edges, signal_speed) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairsOfConnectableServers(edges: Array<Array<Int64>>, signalSpeed: Int64): Array<Int64> {

    }
}
```

