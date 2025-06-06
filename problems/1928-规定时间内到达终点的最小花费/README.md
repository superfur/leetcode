# 1928. 规定时间内到达终点的最小花费

## 题目描述

<p>一个国家有 <code>n</code> 个城市，城市编号为 <code>0</code> 到 <code>n - 1</code> ，题目保证 <strong>所有城市</strong> 都由双向道路 <b>连接在一起</b> 。道路由二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [x<sub>i</sub>, y<sub>i</sub>, time<sub>i</sub>]</code> 表示城市 <code>x<sub>i</sub></code> 和 <code>y<sub>i</sub></code> 之间有一条双向道路，耗费时间为 <code>time<sub>i</sub></code> 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。</p>

<p>每次经过一个城市时，你需要付通行费。通行费用一个长度为 <code>n</code> 且下标从 <strong>0</strong> 开始的整数数组 <code>passingFees</code> 表示，其中 <code>passingFees[j]</code> 是你经过城市 <code>j</code> 需要支付的费用。</p>

<p>一开始，你在城市 <code>0</code> ，你想要在 <code>maxTime</code> <strong>分钟以内</strong> （包含 <code>maxTime</code> 分钟）到达城市 <code>n - 1</code> 。旅行的 <strong>费用</strong> 为你经过的所有城市 <strong>通行费之和</strong> （<strong>包括</strong> 起点和终点城市的通行费）。</p>

<p>给你 <code>maxTime</code>，<code>edges</code> 和 <code>passingFees</code> ，请你返回完成旅行的 <strong>最小费用</strong> ，如果无法在 <code>maxTime</code> 分钟以内完成旅行，请你返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png" style="width: 371px; height: 171px;" /></p>

<pre>
<b>输入：</b>maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
<b>输出：</b>11
<b>解释：</b>最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/copy-of-leetgraph1-1.png" style="width: 371px; height: 171px;" /></strong></p>

<pre>
<b>输入：</b>maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
<b>输出：</b>48
<b>解释：</b>最优路径为 0 -> 3 -> 4 -> 5 ，总共需要耗费 26 分钟，需要支付 48 的通行费。
你不能选择路径 0 -> 1 -> 2 -> 5 ，因为这条路径耗费的时间太长。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
<b>输出：</b>-1
<b>解释：</b>无法在 25 分钟以内从城市 0 到达城市 5 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= maxTime <= 1000</code></li>
	<li><code>n == passingFees.length</code></li>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>n - 1 <= edges.length <= 1000</code></li>
	<li><code>0 <= x<sub>i</sub>, y<sub>i</sub> <= n - 1</code></li>
	<li><code>1 <= time<sub>i</sub> <= 1000</code></li>
	<li><code>1 <= passingFees[j] <= 1000</code> </li>
	<li>图中两个节点之间可能有多条路径。</li>
	<li>图中不含有自环。</li>
</ul>


## 难度

Hard

## 标签

- 图
- 数组
- 动态规划

## 提示

1. Consider a new graph where each node is one of the old nodes at a specific time. For example, node 0 at time 5.
2. You need to find the shortest path in the new graph.

## 示例

```
30
[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
[5,1,2,20,20,3]
29
[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
[5,1,2,20,20,3]
25
[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
[5,1,2,20,20,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFees) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int maxTime, int[][] edges, int[] passingFees) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
```

### C

```c
int minCost(int maxTime, int** edges, int edgesSize, int* edgesColSize, int* passingFees, int passingFeesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int maxTime, int[][] edges, int[] passingFees) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} maxTime
 * @param {number[][]} edges
 * @param {number[]} passingFees
 * @return {number}
 */
var minCost = function(maxTime, edges, passingFees) {
    
};
```

### TypeScript

```typescript
function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $maxTime
     * @param Integer[][] $edges
     * @param Integer[] $passingFees
     * @return Integer
     */
    function minCost($maxTime, $edges, $passingFees) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ maxTime: Int, _ edges: [[Int]], _ passingFees: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(maxTime: Int, edges: Array<IntArray>, passingFees: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(int maxTime, List<List<int>> edges, List<int> passingFees) {
    
  }
}
```

### Go

```golang
func minCost(maxTime int, edges [][]int, passingFees []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} max_time
# @param {Integer[][]} edges
# @param {Integer[]} passing_fees
# @return {Integer}
def min_cost(max_time, edges, passing_fees)
    
end
```

### Scala

```scala
object Solution {
    def minCost(maxTime: Int, edges: Array[Array[Int]], passingFees: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fees: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost maxTime edges passingFees)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(MaxTime :: integer(), Edges :: [[integer()]], PassingFees :: [integer()]) -> integer().
min_cost(MaxTime, Edges, PassingFees) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(max_time :: integer, edges :: [[integer]], passing_fees :: [integer]) :: integer
  def min_cost(max_time, edges, passing_fees) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(maxTime: Int64, edges: Array<Array<Int64>>, passingFees: Array<Int64>): Int64 {

    }
}
```

