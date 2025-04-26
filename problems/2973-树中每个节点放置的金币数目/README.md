# 2973. 树中每个节点放置的金币数目

## 题目描述

<p>给你一棵&nbsp;<code>n</code>&nbsp;个节点的&nbsp;<strong>无向</strong>&nbsp;树，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，树的根节点在节点&nbsp;<code>0</code>&nbsp;处。同时给你一个长度为 <code>n - 1</code>&nbsp;的二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示树中节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条边。</p>

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>cost</code>&nbsp;，其中&nbsp;<code>cost[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的 <b>开销</b>&nbsp;。</p>

<p>你需要在树中每个节点都放置金币，在节点 <code>i</code>&nbsp;处的金币数目计算方法如下：</p>

<ul>
	<li>如果节点 <code>i</code>&nbsp;对应的子树中的节点数目小于&nbsp;<code>3</code>&nbsp;，那么放&nbsp;<code>1</code>&nbsp;个金币。</li>
	<li>否则，计算节点 <code>i</code> 对应的子树内 <code>3</code> 个不同节点的开销乘积的 <strong>最大值</strong> ，并在节点 <code>i</code> 处放置对应数目的金币。如果最大乘积是 <b>负数</b>&nbsp;，那么放置 <code>0</code>&nbsp;个金币。</li>
</ul>

<p>请你返回一个长度为 <code>n</code>&nbsp;的数组<em>&nbsp;</em><code>coin</code>&nbsp;，<code>coin[i]</code>是节点&nbsp;<code>i</code>&nbsp;处的金币数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012641.png" style="width: 600px; height: 233px;" /></p>

<pre>
<b>输入：</b>edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
<b>输出：</b>[120,1,1,1,1,1]
<b>解释：</b>在节点 0 处放置 6 * 5 * 4 = 120 个金币。所有其他节点都是叶子节点，子树中只有 1 个节点，所以其他每个节点都放 1 个金币。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012614.png" style="width: 800px; height: 374px;" /></p>

<pre>
<b>输入：</b>edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
<b>输出：</b>[280,140,32,1,1,1,1,1,1]
<b>解释：</b>每个节点放置的金币数分别为：
- 节点 0 处放置 8 * 7 * 5 = 280 个金币。
- 节点 1 处放置 7 * 5 * 4 = 140 个金币。
- 节点 2 处放置 8 * 2 * 2 = 32 个金币。
- 其他节点都是叶子节点，子树内节点数目为 1 ，所以其他每个节点都放 1 个金币。
</pre>

<p><strong class="example">示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/09/screenshot-2023-11-10-012513.png" style="width: 300px; height: 277px;" /></p>

<pre>
<b>输入：</b>edges = [[0,1],[0,2]], cost = [1,2,-2]
<b>输出：</b>[0,1,1]
<b>解释：</b>节点 1 和 2 都是叶子节点，子树内节点数目为 1 ，各放置 1 个金币。节点 0 处唯一的开销乘积是 2 * 1 * -2 = -4 。所以在节点 0 处放置 0 个金币。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>cost.length == n</code></li>
	<li><code>1 &lt;= |cost[i]| &lt;= 10<sup>4</sup></code></li>
	<li><code>edges</code>&nbsp;一定是一棵合法的树。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 动态规划
- 排序
- 堆（优先队列）

## 提示

1. Use DFS on the whole tree, for each subtree, save the largest three positive costs and the smallest three non-positive costs. This can be done by using two Heaps with the size of at most three.
2. You need to store at most six values at each subtree.
3. If there are more than three values in total, we can sort them. Let’s call the resultant array <code>A</code>, the maximum product of three is <code>max(A[0] * A[1] * A[n - 1], A[n - 1] * A[n - 2] * A[n - 3])</code>. Don’t forget to set the result to <code>0</code> if the value is negative.
4. If there are less than three values for a subtree, set its result to <code>1</code>.

## 示例

```
[[0,1],[0,2],[0,3],[0,4],[0,5]]
[1,2,3,4,5,6]
[[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]]
[1,4,2,3,5,7,8,-4,2]
[[0,1],[0,2]]
[1,2,-2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> placedCoins(vector<vector<int>>& edges, vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] placedCoins(int[][] edges, int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def placedCoins(self, edges, cost):
        """
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* placedCoins(int** edges, int edgesSize, int* edgesColSize, int* cost, int costSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] PlacedCoins(int[][] edges, int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} cost
 * @return {number[]}
 */
var placedCoins = function(edges, cost) {
    
};
```

### TypeScript

```typescript
function placedCoins(edges: number[][], cost: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[] $cost
     * @return Integer[]
     */
    function placedCoins($edges, $cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func placedCoins(_ edges: [[Int]], _ cost: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun placedCoins(edges: Array<IntArray>, cost: IntArray): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> placedCoins(List<List<int>> edges, List<int> cost) {
    
  }
}
```

### Go

```golang
func placedCoins(edges [][]int, cost []int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer[]} cost
# @return {Integer[]}
def placed_coins(edges, cost)
    
end
```

### Scala

```scala
object Solution {
    def placedCoins(edges: Array[Array[Int]], cost: Array[Int]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn placed_coins(edges: Vec<Vec<i32>>, cost: Vec<i32>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (placed-coins edges cost)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec placed_coins(Edges :: [[integer()]], Cost :: [integer()]) -> [integer()].
placed_coins(Edges, Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec placed_coins(edges :: [[integer]], cost :: [integer]) :: [integer]
  def placed_coins(edges, cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func placedCoins(edges: Array<Array<Int64>>, cost: Array<Int64>): Array<Int64> {

    }
}
```

