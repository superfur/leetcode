# 2509. 查询树中环的长度

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示你有一棵含有&nbsp;<code>2<sup>n</sup> - 1</code>&nbsp;个节点的 <strong>完全二叉树</strong>&nbsp;。根节点的编号是&nbsp;<code>1</code>&nbsp;，树中编号在<code>[1, 2<sup>n - 1</sup> - 1]</code>&nbsp;之间，编号为&nbsp;<code>val</code>&nbsp;的节点都有两个子节点，满足：</p>

<ul>
	<li>左子节点的编号为&nbsp;<code>2 * val</code></li>
	<li>右子节点的编号为&nbsp;<code>2 * val + 1</code></li>
</ul>

<p>给你一个长度为 <code>m</code>&nbsp;的查询数组 <code>queries</code>&nbsp;，它是一个二维整数数组，其中&nbsp;<code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;。对于每个查询，求出以下问题的解：</p>

<ol>
	<li>在节点编号为&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间添加一条边。</li>
	<li>求出图中环的长度。</li>
	<li>删除节点编号为&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间新添加的边。</li>
</ol>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>环</strong> 是开始和结束于同一节点的一条路径，路径中每条边都只会被访问一次。</li>
	<li>环的长度是环中边的数目。</li>
	<li>在树中添加额外的边后，两个点之间可能会有多条边。</li>
</ul>

<p>请你返回一个长度为 <code>m</code>&nbsp;的数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个查询的结果<i>。</i></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/25/bexample1.png" style="width: 647px; height: 128px;" /></p>

<pre>
<b>输入：</b>n = 3, queries = [[5,3],[4,7],[2,3]]
<b>输出：</b>[4,5,3]
<b>解释：</b>上图是一棵有 2<sup>3</sup> - 1 个节点的树。红色节点表示添加额外边后形成环的节点。
- 在节点 3 和节点 5 之间添加边后，环为 [5,2,1,3] ，所以第一个查询的结果是 4 。删掉添加的边后处理下一个查询。
- 在节点 4 和节点 7 之间添加边后，环为 [4,2,1,3,7] ，所以第二个查询的结果是 5 。删掉添加的边后处理下一个查询。
- 在节点 2 和节点 3 之间添加边后，环为 [2,1,3] ，所以第三个查询的结果是 3 。删掉添加的边。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/25/aexample2.png" style="width: 146px; height: 71px;" /></p>

<pre>
<b>输入：</b>n = 2, queries = [[1,2]]
<b>输出：</b>[2]
<b>解释：</b>上图是一棵有 2<sup>2</sup> - 1 个节点的树。红色节点表示添加额外边后形成环的节点。
- 在节点 1 和节点 2 之间添加边后，环为 [2,1] ，所以第一个查询的结果是 2 。删掉添加的边。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 30</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= 2<sup>n</sup> - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


## 难度

Hard

## 标签

- 树
- 数组
- 二叉树

## 提示

1. Find the distance between nodes “a” and “b”.
2. distance(a, b) = depth(a) + depth(b) - 2 * depth(LCA(a, b)). Where depth(a) denotes depth from root to node “a” and LCA(a, b) denotes the lowest common ancestor of nodes “a” and “b”.
3. To find LCA(a, b), iterate over all ancestors of node “a” and check if it is the ancestor of node “b” too. If so, take the one with maximum depth.

## 示例

```
3
[[5,3],[4,7],[2,3]]
2
[[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] cycleLengthQueries(int n, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def cycleLengthQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* cycleLengthQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CycleLengthQueries(int n, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var cycleLengthQueries = function(n, queries) {
    
};
```

### TypeScript

```typescript
function cycleLengthQueries(n: number, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function cycleLengthQueries($n, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func cycleLengthQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun cycleLengthQueries(n: Int, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> cycleLengthQueries(int n, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func cycleLengthQueries(n int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def cycle_length_queries(n, queries)
    
end
```

### Scala

```scala
object Solution {
    def cycleLengthQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn cycle_length_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (cycle-length-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec cycle_length_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
cycle_length_queries(N, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec cycle_length_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def cycle_length_queries(n, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func cycleLengthQueries(n: Int64, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

