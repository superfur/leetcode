# 2920. 收集所有金币可获得的最大积分

## 题目描述

<p>有一棵由 <code>n</code> 个节点组成的无向树，以&nbsp;<code>0</code>&nbsp; 为根节点，节点编号从 <code>0</code> 到 <code>n - 1</code> 。给你一个长度为 <code>n - 1</code> 的二维 <strong>整数</strong> 数组 <code>edges</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示在树上的节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条边。另给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的数组 <code>coins</code> 和一个整数 <code>k</code> ，其中 <code>coins[i]</code> 表示节点 <code>i</code> 处的金币数量。</p>

<p>从根节点开始，你必须收集所有金币。要想收集节点上的金币，必须先收集该节点的祖先节点上的金币。</p>

<p>节点 <code>i</code> 上的金币可以用下述方法之一进行收集：</p>

<ul>
	<li>收集所有金币，得到共计 <code>coins[i] - k</code> 点积分。如果 <code>coins[i] - k</code> 是负数，你将会失去 <code>abs(coins[i] - k)</code> 点积分。</li>
	<li>收集所有金币，得到共计 <code>floor(coins[i] / 2)</code> 点积分。如果采用这种方法，节点 <code>i</code> 子树中所有节点 <code>j</code> 的金币数 <code>coins[j]</code> 将会减少至 <code>floor(coins[j] / 2)</code> 。</li>
</ul>

<p>返回收集 <strong>所有</strong> 树节点的金币之后可以获得的最大积分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/09/18/ex1-copy.png" style="width: 60px; height: 316px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<pre>
<strong>输入：</strong>edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5
<strong>输出：</strong>11                        
<strong>解释：</strong>
使用第一种方法收集节点 0 上的所有金币。总积分 = 10 - 5 = 5 。
使用第一种方法收集节点 1 上的所有金币。总积分 = 5 + (10 - 5) = 10 。
使用第二种方法收集节点 2 上的所有金币。所以节点 3 上的金币将会变为 floor(3 / 2) = 1 ，总积分 = 10 + floor(3 / 2) = 11 。
使用第二种方法收集节点 3 上的所有金币。总积分 =  11 + floor(1 / 2) = 11.
可以证明收集所有节点上的金币能获得的最大积分是 11 。 
</pre>

<p><strong class="example">示例 2：</strong></p>
<strong class="example"> <img alt="" src="https://assets.leetcode.com/uploads/2023/09/18/ex2.png" style="width: 140px; height: 147px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong>

<pre>
<strong>输入：</strong>edges = [[0,1],[0,2]], coins = [8,4,4], k = 0
<strong>输出：</strong>16
<strong>解释：</strong>
使用第一种方法收集所有节点上的金币，因此，总积分 = (8 - 0) + (4 - 0) + (4 - 0) = 16 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == coins.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code><font face="monospace">0 &lt;= coins[i] &lt;= 10<sup>4</sup></font></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code><font face="monospace">0 &lt;= edges[i][0], edges[i][1] &lt; n</font></code></li>
	<li><code><font face="monospace">0 &lt;= k &lt;= 10<sup>4</sup></font></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 树
- 深度优先搜索
- 记忆化搜索
- 数组
- 动态规划

## 提示

1. Let <code>dp[x][t]</code> be the maximum points we can get from the subtree rooted at node <code>x</code> and the second operation has been used <code>t</code> times in its ancestors.
2. Note that the value of each <code>node <= 10<sup>4</sup></code>, so when <code>t >= 14</code> <code>dp[x][t]</code> is always <code>0</code>.
3. General equation will be: <code>dp[x][t] = max((coins[x] >> t) - k + sigma(dp[y][t]), (coins[x] >> (t + 1)) + sigma(dp[y][t + 1]))</code> where nodes denoted by <code>y</code> in the sigma, are the direct children of node <code>x</code>.

## 示例

```
[[0,1],[1,2],[2,3]]
[10,10,3,3]
5
[[0,1],[0,2]]
[8,4,4]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumPoints(vector<vector<int>>& edges, vector<int>& coins, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumPoints(int[][] edges, int[] coins, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumPoints(self, edges, coins, k):
        """
        :type edges: List[List[int]]
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
```

### C

```c
int maximumPoints(int** edges, int edgesSize, int* edgesColSize, int* coins, int coinsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumPoints(int[][] edges, int[] coins, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var maximumPoints = function(edges, coins, k) {
    
};
```

### TypeScript

```typescript
function maximumPoints(edges: number[][], coins: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[] $coins
     * @param Integer $k
     * @return Integer
     */
    function maximumPoints($edges, $coins, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumPoints(_ edges: [[Int]], _ coins: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumPoints(edges: Array<IntArray>, coins: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumPoints(List<List<int>> edges, List<int> coins, int k) {
    
  }
}
```

### Go

```golang
func maximumPoints(edges [][]int, coins []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def maximum_points(edges, coins, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumPoints(edges: Array[Array[Int]], coins: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_points(edges: Vec<Vec<i32>>, coins: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-points edges coins k)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_points(Edges :: [[integer()]], Coins :: [integer()], K :: integer()) -> integer().
maximum_points(Edges, Coins, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_points(edges :: [[integer]], coins :: [integer], k :: integer) :: integer
  def maximum_points(edges, coins, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumPoints(edges: Array<Array<Int64>>, coins: Array<Int64>, k: Int64): Int64 {

    }
}
```

