# 2421. 好路径的数目

## 题目描述

<p>给你一棵 <code>n</code>&nbsp;个节点的树（连通无向无环的图），节点编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;且恰好有&nbsp;<code>n - 1</code>&nbsp;条边。</p>

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>vals</code>&nbsp;，分别表示每个节点的值。同时给你一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code><sub>&nbsp;</sub>之间有一条&nbsp;<strong>无向</strong>&nbsp;边。</p>

<p>一条 <strong>好路径</strong>&nbsp;需要满足以下条件：</p>

<ol>
	<li>开始节点和结束节点的值 <strong>相同</strong>&nbsp;。</li>
	<li>开始节点和结束节点中间的所有节点值都 <strong>小于等于</strong>&nbsp;开始节点的值（也就是说开始节点的值应该是路径上所有节点的最大值）。</li>
</ol>

<p>请你返回不同好路径的数目。</p>

<p>注意，一条路径和它反向的路径算作 <strong>同一</strong>&nbsp;路径。比方说，&nbsp;<code>0 -&gt; 1</code>&nbsp;与&nbsp;<code>1 -&gt; 0</code>&nbsp;视为同一条路径。单个节点也视为一条合法路径。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/f9caaac15b383af9115c5586779dec5.png" style="width: 400px; height: 333px;"></p>

<pre><b>输入：</b>vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
<b>输出：</b>6
<b>解释：</b>总共有 5 条单个节点的好路径。
还有 1 条好路径：1 -&gt; 0 -&gt; 2 -&gt; 4 。
（反方向的路径 4 -&gt; 2 -&gt; 0 -&gt; 1 视为跟 1 -&gt; 0 -&gt; 2 -&gt; 4 一样的路径）
注意 0 -&gt; 2 -&gt; 3 不是一条好路径，因为 vals[2] &gt; vals[0] 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/149d3065ec165a71a1b9aec890776ff.png" style="width: 273px; height: 350px;"></p>

<pre><b>输入：</b>vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
<b>输出：</b>7
<strong>解释：</strong>总共有 5 条单个节点的好路径。
还有 2 条好路径：0 -&gt; 1 和 2 -&gt; 3 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/31705e22af3d9c0a557459bc7d1b62d.png" style="width: 100px; height: 88px;"></p>

<pre><b>输入：</b>vals = [1], edges = []
<b>输出：</b>1
<b>解释：</b>这棵树只有一个节点，所以只有一条好路径。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == vals.length</code></li>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= vals[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code>&nbsp;表示一棵合法的树。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 并查集
- 图
- 数组
- 哈希表
- 排序

## 提示

1. Can you process nodes from smallest to largest value?
2. Try to build the graph from nodes with the smallest value to the largest value.
3. May union find help?

## 示例

```
[1,3,2,1,3]
[[0,1],[0,2],[2,3],[2,4]]
[1,1,2,2,3]
[[0,1],[1,2],[2,3],[2,4]]
[1]
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfGoodPaths(int[] vals, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
```

### C

```c
int numberOfGoodPaths(int* vals, int valsSize, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfGoodPaths(int[] vals, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @return {number}
 */
var numberOfGoodPaths = function(vals, edges) {
    
};
```

### TypeScript

```typescript
function numberOfGoodPaths(vals: number[], edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $vals
     * @param Integer[][] $edges
     * @return Integer
     */
    function numberOfGoodPaths($vals, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfGoodPaths(_ vals: [Int], _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfGoodPaths(vals: IntArray, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfGoodPaths(List<int> vals, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func numberOfGoodPaths(vals []int, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} vals
# @param {Integer[][]} edges
# @return {Integer}
def number_of_good_paths(vals, edges)
    
end
```

### Scala

```scala
object Solution {
    def numberOfGoodPaths(vals: Array[Int], edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_good_paths(vals: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-good-paths vals edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_good_paths(Vals :: [integer()], Edges :: [[integer()]]) -> integer().
number_of_good_paths(Vals, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_good_paths(vals :: [integer], edges :: [[integer]]) :: integer
  def number_of_good_paths(vals, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfGoodPaths(vals: Array<Int64>, edges: Array<Array<Int64>>): Int64 {

    }
}
```

