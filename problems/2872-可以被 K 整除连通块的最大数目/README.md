# 2872. 可以被 K 整除连通块的最大数目

## 题目描述

<p>给你一棵 <code>n</code>&nbsp;个节点的无向树，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。给你整数&nbsp;<code>n</code>&nbsp;和一个长度为 <code>n - 1</code>&nbsp;的二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示树中节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;有一条边。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>values</code>&nbsp;，其中&nbsp;<code>values[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的 <strong>值</strong>&nbsp;。再给你一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你可以从树中删除一些边，也可以一条边也不删，得到若干连通块。一个 <strong>连通块的值</strong> 定义为连通块中所有节点值之和。如果所有连通块的值都可以被 <code>k</code>&nbsp;整除，那么我们说这是一个 <strong>合法分割</strong>&nbsp;。</p>

<p>请你返回所有合法分割中，<b>连通块数目的最大值</b>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg" style="width: 1024px; height: 453px;" /></p>

<pre>
<b>输入：</b>n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
<b>输出：</b>2
<b>解释：</b>我们删除节点 1 和 2 之间的边。这是一个合法分割，因为：
- 节点 1 和 3 所在连通块的值为 values[1] + values[3] = 12 。
- 节点 0 ，2 和 4 所在连通块的值为 values[0] + values[2] + values[4] = 6 。
最多可以得到 2 个连通块的合法分割。</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg" style="width: 999px; height: 338px;" /></p>

<pre>
<b>输入：</b>n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
<b>输出：</b>3
<b>解释：</b>我们删除节点 0 和 2 ，以及节点 0 和 1 之间的边。这是一个合法分割，因为：
- 节点 0 的连通块的值为 values[0] = 3 。
- 节点 2 ，5 和 6 所在连通块的值为 values[2] + values[5] + values[6] = 9 。
- 节点 1 ，3 和 4 的连通块的值为 values[1] + values[3] + values[4] = 6 。
最多可以得到 3 个连通块的合法分割。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>values.length == n</code></li>
	<li><code>0 &lt;= values[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li><code>values</code>&nbsp;之和可以被 <code>k</code>&nbsp;整除。</li>
	<li>输入保证&nbsp;<code>edges</code>&nbsp;是一棵无向树。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索

## 提示

1. Root the tree at node <code>0</code>.
2. If a leaf node is not divisible by <code>k</code>, it must be in the same component as its parent node so we merge it with its parent node.
3. If a leaf node is divisible by <code>k</code>, it will be in its own components so we separate it from its parent node.
4. In each step, we either cut a leaf node down or merge a leaf node. The number of nodes on the tree reduces by one. Repeat this process until only one node is left.

## 示例

```
5
[[0,2],[1,2],[1,3],[2,4]]
[1,8,1,4,4]
6
7
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
[3,0,6,1,5,2,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
```

### C

```c
int maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    
};
```

### TypeScript

```typescript
function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $values
     * @param Integer $k
     * @return Integer
     */
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>, values: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxKDivisibleComponents(int n, List<List<int>> edges, List<int> values, int k) {
    
  }
}
```

### Go

```golang
func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} values
# @param {Integer} k
# @return {Integer}
def max_k_divisible_components(n, edges, values, k)
    
end
```

### Scala

```scala
object Solution {
    def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-k-divisible-components n edges values k)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_k_divisible_components(N :: integer(), Edges :: [[integer()]], Values :: [integer()], K :: integer()) -> integer().
max_k_divisible_components(N, Edges, Values, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_k_divisible_components(n :: integer, edges :: [[integer]], values :: [integer], k :: integer) :: integer
  def max_k_divisible_components(n, edges, values, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxKDivisibleComponents(n: Int64, edges: Array<Array<Int64>>, values: Array<Int64>, k: Int64): Int64 {

    }
}
```

