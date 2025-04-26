# 1514. 概率最大的路径

## 题目描述

<p>给你一个由 <code>n</code> 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 <code>edges[i] = [a, b]</code> 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 <code>succProb[i]</code> 。</p>

<p>指定两个节点分别作为起点 <code>start</code> 和终点 <code>end</code> ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。</p>

<p>如果不存在从 <code>start</code> 到 <code>end</code> 的路径，请 <strong>返回 0</strong> 。只要答案与标准答案的误差不超过 <strong>1e-5 </strong>，就会被视作正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex1.png" style="height: 186px; width: 187px;"></strong></p>

<pre><strong>输入：</strong>n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
<strong>输出：</strong>0.25000
<strong>解释：</strong>从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex2.png" style="height: 186px; width: 189px;"></strong></p>

<pre><strong>输入：</strong>n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
<strong>输出：</strong>0.30000
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex3.png" style="height: 191px; width: 215px;"></strong></p>

<pre><strong>输入：</strong>n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
<strong>输出：</strong>0.00000
<strong>解释：</strong>节点 0 和 节点 2 之间不存在路径
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10^4</code></li>
	<li><code>0 &lt;= start, end &lt; n</code></li>
	<li><code>start != end</code></li>
	<li><code>0 &lt;= a, b &lt; n</code></li>
	<li><code>a != b</code></li>
	<li><code>0 &lt;= succProb.length == edges.length &lt;= 2*10^4</code></li>
	<li><code>0 &lt;= succProb[i] &lt;= 1</code></li>
	<li>每两个节点之间最多有一条边</li>
</ul>


## 难度

Medium

## 标签

- 图
- 数组
- 最短路
- 堆（优先队列）

## 提示

1. Multiplying probabilities will result in precision errors.
2. Take log probabilities to sum up numbers instead of multiplying them.
3. Use Dijkstra's algorithm to find the minimum path between the two nodes after negating all costs.

## 示例

```
3
[[0,1],[1,2],[0,2]]
[0.5,0.5,0.2]
0
2
3
[[0,1],[1,2],[0,2]]
[0.5,0.5,0.3]
0
2
3
[[0,1]]
[0.5]
0
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        
    }
};
```

### Java

```java
class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
```

### C

```c
double maxProbability(int n, int** edges, int edgesSize, int* edgesColSize, double* succProb, int succProbSize, int start_node, int end_node) {
    
}
```

### C#

```csharp
public class Solution {
    public double MaxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} succProb
 * @param {number} start_node
 * @param {number} end_node
 * @return {number}
 */
var maxProbability = function(n, edges, succProb, start_node, end_node) {
    
};
```

### TypeScript

```typescript
function maxProbability(n: number, edges: number[][], succProb: number[], start_node: number, end_node: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Float[] $succProb
     * @param Integer $start_node
     * @param Integer $end_node
     * @return Float
     */
    function maxProbability($n, $edges, $succProb, $start_node, $end_node) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProbability(_ n: Int, _ edges: [[Int]], _ succProb: [Double], _ start_node: Int, _ end_node: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProbability(n: Int, edges: Array<IntArray>, succProb: DoubleArray, start_node: Int, end_node: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double maxProbability(int n, List<List<int>> edges, List<double> succProb, int start_node, int end_node) {
    
  }
}
```

### Go

```golang
func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Float[]} succ_prob
# @param {Integer} start_node
# @param {Integer} end_node
# @return {Float}
def max_probability(n, edges, succ_prob, start_node, end_node)
    
end
```

### Scala

```scala
object Solution {
    def maxProbability(n: Int, edges: Array[Array[Int]], succProb: Array[Double], start_node: Int, end_node: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_probability(n: i32, edges: Vec<Vec<i32>>, succ_prob: Vec<f64>, start_node: i32, end_node: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-probability n edges succProb start_node end_node)
  (-> exact-integer? (listof (listof exact-integer?)) (listof flonum?) exact-integer? exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec max_probability(N :: integer(), Edges :: [[integer()]], SuccProb :: [float()], Start_node :: integer(), End_node :: integer()) -> float().
max_probability(N, Edges, SuccProb, Start_node, End_node) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_probability(n :: integer, edges :: [[integer]], succ_prob :: [float], start_node :: integer, end_node :: integer) :: float
  def max_probability(n, edges, succ_prob, start_node, end_node) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProbability(n: Int64, edges: Array<Array<Int64>>, succProb: Array<Float64>, start_node: Int64, end_node: Int64): Float64 {

    }
}
```

