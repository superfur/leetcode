# 1782. 统计点对的数目

## 题目描述

<p>给你一个无向图，无向图由整数&nbsp;<code>n</code>&nbsp;&nbsp;，表示图中节点的数目，和&nbsp;<code>edges</code>&nbsp;组成，其中&nbsp;<code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>&nbsp;表示&nbsp;<code>u<sub>i</sub></code> 和&nbsp;<code>v<sub>i</sub></code><sub>&nbsp;</sub>之间有一条无向边。同时给你一个代表查询的整数数组&nbsp;<code>queries</code>&nbsp;。</p>

<p>第 <code>j</code> 个查询的答案是满足如下条件的点对 <code>(a, b)</code> 的数目：</p>

<ul>
	<li><code>a &lt; b</code></li>
	<li><code>cnt</code>&nbsp;是与 <code>a</code>&nbsp;<strong>或者&nbsp;</strong><code>b</code>&nbsp;相连的边的数目，且 <code>cnt</code>&nbsp;<strong>严格大于&nbsp;</strong><code>queries[j]</code>&nbsp;。</li>
</ul>

<p>请你返回一个数组&nbsp;<code>answers</code>&nbsp;，其中&nbsp;<code>answers.length == queries.length</code> 且&nbsp;<code>answers[j]</code>&nbsp;是第 <code>j</code>&nbsp;个查询的答案。</p>

<p>请注意，图中可能会有 <strong>多重边</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1692844033-Kvxjvr-image.png" style="width: 600px; height: 338px;" /></p>

<pre>
<b>输入：</b>n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
<b>输出：</b>[6,5]
<b>解释：</b>每个点对中，与至少一个点相连的边的数目如上图所示。
answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个；
answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
<b>输出：</b>[10,10,9,8,6]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i </sub>!= v<sub>i</sub></code></li>
	<li><code>1 &lt;= queries.length &lt;= 20</code></li>
	<li><code>0 &lt;= queries[j] &lt; edges.length</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. We want to count pairs (x,y) such that degree[x] + degree[y] - occurrences(x,y) > k
2. Think about iterating on x, and counting the number of valid y to pair with x.
3. You can consider at first that the (- occurrences(x,y)) isn't there, or it is 0 at first for all y. Count the valid y this way.
4. Then you can iterate on the neighbors of x, let that neighbor be y, and update occurrences(x,y).
5. When you update occurrences(x,y), the left-hand side decreases. Once it reaches k, then y is not valid for x anymore, so you should decrease the answer by 1.

## 示例

```
4
[[1,2],[2,4],[1,3],[2,3],[2,1]]
[2,3]
5
[[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]]
[1,2,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countPairs(int n, int[][] edges, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPairs(int n, int** edges, int edgesSize, int* edgesColSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountPairs(int n, int[][] edges, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} queries
 * @return {number[]}
 */
var countPairs = function(n, edges, queries) {
    
};
```

### TypeScript

```typescript
function countPairs(n: number, edges: number[][], queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countPairs($n, $edges, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ n: Int, _ edges: [[Int]], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(n: Int, edges: Array<IntArray>, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countPairs(int n, List<List<int>> edges, List<int> queries) {
    
  }
}
```

### Go

```golang
func countPairs(n int, edges [][]int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} queries
# @return {Integer[]}
def count_pairs(n, edges, queries)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(n: Int, edges: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs n edges queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_pairs(N :: integer(), Edges :: [[integer()]], Queries :: [integer()]) -> [integer()].
count_pairs(N, Edges, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(n :: integer, edges :: [[integer]], queries :: [integer]) :: [integer]
  def count_pairs(n, edges, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(n: Int64, edges: Array<Array<Int64>>, queries: Array<Int64>): Array<Int64> {

    }
}
```

