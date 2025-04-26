# 2867. 统计树中的合法路径数目

## 题目描述

<p>给你一棵 <code>n</code>&nbsp;个节点的无向树，节点编号为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;。给你一个整数&nbsp;<code>n</code>&nbsp;和一个长度为 <code>n - 1</code>&nbsp;的二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>u<sub>i</sub></code> 和&nbsp;<code>v<sub>i</sub></code>&nbsp;在树中有一条边。</p>

<p>请你返回树中的 <strong>合法路径数目</strong>&nbsp;。</p>

<p>如果在节点 <code>a</code>&nbsp;到节点 <code>b</code>&nbsp;之间 <strong>恰好有一个</strong>&nbsp;节点的编号是质数，那么我们称路径&nbsp;<code>(a, b)</code>&nbsp;是 <strong>合法的</strong>&nbsp;。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>路径&nbsp;<code>(a, b)</code>&nbsp;指的是一条从节点 <code>a</code>&nbsp;开始到节点 <code>b</code>&nbsp;结束的一个节点序列，序列中的节点 <strong>互不相同</strong>&nbsp;，且相邻节点之间在树上有一条边。</li>
	<li>路径&nbsp;<code>(a, b)</code>&nbsp;和路径&nbsp;<code>(b, a)</code>&nbsp;视为 <strong>同一条</strong>&nbsp;路径，且只计入答案 <strong>一次</strong>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/27/example1.png" style="width: 440px; height: 357px;" /></p>

<pre>
<b>输入：</b>n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
<b>输出：</b>4
<b>解释：</b>恰好有一个质数编号的节点路径有：
- (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
- (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
- (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
- (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
只有 4 条合法路径。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/27/example2.png" style="width: 488px; height: 384px;" /></p>

<pre>
<b>输入：</b>n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
<b>输出：</b>6
<b>解释：</b>恰好有一个质数编号的节点路径有：
- (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
- (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
- (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
- (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
- (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
- (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
只有 6 条合法路径。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li>输入保证&nbsp;<code>edges</code>&nbsp;形成一棵合法的树。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 数学
- 动态规划
- 数论

## 提示

1. Use the sieve of Eratosthenes to find all prime numbers in the range <code>[1, n]</code>.****
2. Root the tree at any node.
3. Let <code>dp[i][0] = the number of vertical paths starting from i containing no prime nodes </code>, and <code>dp[i][1] = the number of vertical paths starting from i containing one prime node </code>.
4. If <code>i</code> is not prime, <code>dp[i][0] = sum(dp[child][0]) + 1</code>, and <code>dp[i][1] = sum(dp[child][1])</code> for each <code>child</code> of <code>i</code> in the rooted tree.
5. If <code>i</code> is prime, <code>dp[i][0] = 0</code>, and <code>dp[i][1] = sum(dp[child][0]) + 1</code> for each <code>child</code> of <code>i</code> in the rooted tree.
6. For each node <code>i</code>, and using the computed <code>dp</code> matrix, count the number of unordered pairs <code>(a,b)</code> such that <code>lca(a,b) = i</code>, and there exists exactly one prime number on the path from <code>a</code> to <code>b</code>.

## 示例

```
5
[[1,2],[1,3],[2,4],[2,5]]
6
[[1,2],[1,3],[2,4],[3,5],[3,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countPaths(int n, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public long countPaths(int n, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        
```

### C

```c
long long countPaths(int n, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountPaths(int n, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPaths = function(n, edges) {
    
};
```

### TypeScript

```typescript
function countPaths(n: number, edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countPaths($n, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPaths(n: Int, edges: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPaths(int n, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func countPaths(n int, edges [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_paths(n, edges)
    
end
```

### Scala

```scala
object Solution {
    def countPaths(n: Int, edges: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_paths(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-paths n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_paths(N :: integer(), Edges :: [[integer()]]) -> integer().
count_paths(N, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_paths(n :: integer, edges :: [[integer]]) :: integer
  def count_paths(n, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPaths(n: Int64, edges: Array<Array<Int64>>): Int64 {

    }
}
```

