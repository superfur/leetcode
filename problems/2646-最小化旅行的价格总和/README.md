# 2646. 最小化旅行的价格总和

## 题目描述

<p>现有一棵无向、无根的树，树中有 <code>n</code> 个节点，按从 <code>0</code> 到 <code>n - 1</code> 编号。给你一个整数 <code>n</code> 和一个长度为 <code>n - 1</code> 的二维整数数组 <code>edges</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条边。</p>

<p>每个节点都关联一个价格。给你一个整数数组 <code>price</code> ，其中 <code>price[i]</code> 是第 <code>i</code> 个节点的价格。</p>

<p>给定路径的 <strong>价格总和</strong> 是该路径上所有节点的价格之和。</p>

<p>另给你一个二维整数数组 <code>trips</code> ，其中 <code>trips[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示您从节点 <code>start<sub>i</sub></code> 开始第 <code>i</code> 次旅行，并通过任何你喜欢的路径前往节点 <code>end<sub>i</sub></code> 。</p>

<p>在执行第一次旅行之前，你可以选择一些 <strong>非相邻节点</strong> 并将价格减半。</p>

<p>返回执行所有旅行的最小价格总和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/03/16/diagram2.png" style="width: 541px; height: 181px;">
<pre><strong>输入：</strong>n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
<strong>输出：</strong>23
<strong>解释：
</strong>上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/03/16/diagram3.png" style="width: 456px; height: 111px;">
<pre><strong>输入：</strong>n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
<strong>输出：</strong>1
<strong>解释：</strong>
上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>edges</code> 表示一棵有效的树</li>
	<li><code>price.length == n</code></li>
	<li><code>price[i]</code> 是一个偶数</li>
	<li><code>1 &lt;= price[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= trips.length &lt;= 100</code></li>
	<li><code>0 &lt;= start<sub>i</sub>, end<sub>i</sub>&nbsp;&lt;= n - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 图
- 数组
- 动态规划

## 提示

1. The final answer is the price[i] * freq[i], where freq[i] is the number of times node i was visited during the trip, and price[i] is the final price.
2. To find freq[i] we will use dfs or bfs for each trip and update every node on the path start and end.
3. Finally, to find the final price[i] we will use dynamic programming on the tree. Let dp(v, 0/1) denote the minimum total price with the node v’s price being halved or not.

## 示例

```
4
[[0,1],[1,2],[1,3]]
[2,2,10,6]
[[0,3],[2,1],[2,3]]
2
[[0,1]]
[2,2]
[[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTotalPrice(int n, vector<vector<int>>& edges, vector<int>& price, vector<vector<int>>& trips) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
```

### C

```c
int minimumTotalPrice(int n, int** edges, int edgesSize, int* edgesColSize, int* price, int priceSize, int** trips, int tripsSize, int* tripsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} price
 * @param {number[][]} trips
 * @return {number}
 */
var minimumTotalPrice = function(n, edges, price, trips) {
    
};
```

### TypeScript

```typescript
function minimumTotalPrice(n: number, edges: number[][], price: number[], trips: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $price
     * @param Integer[][] $trips
     * @return Integer
     */
    function minimumTotalPrice($n, $edges, $price, $trips) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTotalPrice(_ n: Int, _ edges: [[Int]], _ price: [Int], _ trips: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTotalPrice(n: Int, edges: Array<IntArray>, price: IntArray, trips: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTotalPrice(int n, List<List<int>> edges, List<int> price, List<List<int>> trips) {
    
  }
}
```

### Go

```golang
func minimumTotalPrice(n int, edges [][]int, price []int, trips [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @param {Integer[][]} trips
# @return {Integer}
def minimum_total_price(n, edges, price, trips)
    
end
```

### Scala

```scala
object Solution {
    def minimumTotalPrice(n: Int, edges: Array[Array[Int]], price: Array[Int], trips: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_total_price(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>, trips: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-total-price n edges price trips)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_total_price(N :: integer(), Edges :: [[integer()]], Price :: [integer()], Trips :: [[integer()]]) -> integer().
minimum_total_price(N, Edges, Price, Trips) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_total_price(n :: integer, edges :: [[integer]], price :: [integer], trips :: [[integer]]) :: integer
  def minimum_total_price(n, edges, price, trips) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTotalPrice(n: Int64, edges: Array<Array<Int64>>, price: Array<Int64>, trips: Array<Array<Int64>>): Int64 {

    }
}
```

