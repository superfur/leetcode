# 2538. 最大价值和与最小价值和的差值

## 题目描述

<p>给你一个 <code>n</code>&nbsp;个节点的无向无根图，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。给你一个整数&nbsp;<code>n</code>&nbsp;和一个长度为 <code>n - 1</code>&nbsp;的二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示树中节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边。</p>

<p>每个节点都有一个价值。给你一个整数数组&nbsp;<code>price</code>&nbsp;，其中&nbsp;<code>price[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的价值。</p>

<p>一条路径的 <strong>价值和</strong>&nbsp;是这条路径上所有节点的价值之和。</p>

<p>你可以选择树中任意一个节点作为根节点&nbsp;<code>root</code>&nbsp;。选择 <code>root</code>&nbsp;为根的 <strong>开销</strong>&nbsp;是以 <code>root</code>&nbsp;为起点的所有路径中，<strong>价值和</strong>&nbsp;最大的一条路径与最小的一条路径的差值。</p>

<p>请你返回所有节点作为根节点的选择中，<strong>最大</strong>&nbsp;的 <strong>开销</strong>&nbsp;为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/12/01/example14.png" style="width: 556px; height: 231px;" /></p>

<pre>
<b>输入：</b>n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
<b>输出：</b>24
<b>解释：</b>上图展示了以节点 2 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
- 第一条路径节点为 [2,1,3,4]：价值为 [7,8,6,10] ，价值和为 31 。
- 第二条路径节点为 [2] ，价值为 [7] 。
最大路径和与最小路径和的差值为 24 。24 是所有方案中的最大开销。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p1_example2.png" style="width: 352px; height: 184px;" /></p>

<pre>
<b>输入：</b>n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
<b>输出：</b>2
<b>解释：</b>上图展示了以节点 0 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
- 第一条路径包含节点 [0,1,2]：价值为 [1,1,1] ，价值和为 3 。
- 第二条路径节点为 [0] ，价值为 [1] 。
最大路径和与最小路径和的差值为 2 。2 是所有方案中的最大开销。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>edges</code> 表示一棵符合题面要求的树。</li>
	<li><code>price.length == n</code></li>
	<li><code>1 &lt;= price[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 数组
- 动态规划

## 提示

1. The minimum price sum is always the price of a rooted node.
2. Let’s root the tree at vertex 0 and find the answer from this perspective.
3. In the optimal answer maximum price is the sum of the prices of nodes on the path from “u” to “v” where either “u” or “v” is the parent of the second one or neither is a parent of the second one.
4. The first case is easy to find. For the second case, notice that in the optimal path, “u” and “v” are both leaves. Then we can use dynamic programming to find such a path.
5. Let DP(v,1) denote “the maximum price sum from node v to leaf, where v is a parent of that leaf” and let DP(v,0) denote “the maximum price sum from node v to leaf, where v is a parent of that leaf - price[leaf]”. Then the answer is maximum of DP(u,0) + DP(v,1) + price[parent] where u, v are directly connected to vertex “parent”.

## 示例

```
6
[[0,1],[1,2],[1,3],[3,4],[3,5]]
[9,8,7,6,10,5]
3
[[0,1],[1,2]]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxOutput(int n, int[][] edges, int[] price) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxOutput(self, n, edges, price):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        
```

### C

```c
long long maxOutput(int n, int** edges, int edgesSize, int* edgesColSize, int* price, int priceSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxOutput(int n, int[][] edges, int[] price) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} price
 * @return {number}
 */
var maxOutput = function(n, edges, price) {
    
};
```

### TypeScript

```typescript
function maxOutput(n: number, edges: number[][], price: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $price
     * @return Integer
     */
    function maxOutput($n, $edges, $price) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxOutput(_ n: Int, _ edges: [[Int]], _ price: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxOutput(n: Int, edges: Array<IntArray>, price: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxOutput(int n, List<List<int>> edges, List<int> price) {
    
  }
}
```

### Go

```golang
func maxOutput(n int, edges [][]int, price []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @return {Integer}
def max_output(n, edges, price)
    
end
```

### Scala

```scala
object Solution {
    def maxOutput(n: Int, edges: Array[Array[Int]], price: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_output(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-output n edges price)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_output(N :: integer(), Edges :: [[integer()]], Price :: [integer()]) -> integer().
max_output(N, Edges, Price) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_output(n :: integer, edges :: [[integer]], price :: [integer]) :: integer
  def max_output(n, edges, price) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxOutput(n: Int64, edges: Array<Array<Int64>>, price: Array<Int64>): Int64 {

    }
}
```

