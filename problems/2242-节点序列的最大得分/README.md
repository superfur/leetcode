# 2242. 节点序列的最大得分

## 题目描述

<p>给你一个&nbsp;<code>n</code>&nbsp;个节点的&nbsp;<strong>无向图</strong>&nbsp;，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>scores</code>&nbsp;，其中&nbsp;<code>scores[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的分数。同时给你一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;，表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条&nbsp;<strong>无向</strong>&nbsp;边。</p>

<p>一个合法的节点序列如果满足以下条件，我们称它是 <strong>合法的</strong>&nbsp;：</p>

<ul>
	<li>序列中每&nbsp;<b>相邻</b>&nbsp;节点之间有边相连。</li>
	<li>序列中没有节点出现超过一次。</li>
</ul>

<p>节点序列的分数定义为序列中节点分数之 <strong>和</strong> 。</p>

<p>请你返回一个长度为 <code>4</code>&nbsp;的合法节点序列的最大分数。如果不存在这样的序列，请你返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/04/15/ex1new3.png" style="width: 290px; height: 215px;" /></p>

<pre>
<b>输入：</b>scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
<b>输出：</b>24
<b>解释：</b>上图为输入的图，节点序列为 [0,1,2,3] 。
节点序列的分数为 5 + 2 + 9 + 8 = 24 。
观察可知，没有其他节点序列得分和超过 24 。
注意节点序列 [3,1,2,0] 和 [1,0,2,3] 也是合法的，且分数为 24 。
序列 [0,3,2,4] 不是合法的，因为没有边连接节点 0 和 3 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/17/ex2.png" style="width: 333px; height: 151px;" /></p>

<pre>
<b>输入：</b>scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
<b>输出：</b>-1
<b>解释：</b>上图为输入的图。
没有长度为 4 的合法序列，所以我们返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == scores.length</code></li>
	<li><code>4 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= scores[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>不会有重边。</li>
</ul>


## 难度

Hard

## 标签

- 图
- 数组
- 枚举
- 排序

## 提示

1. For every node sequence of length 4, there are 3 relevant edges. How can we consider valid triplets of edges?
2. Fix the middle 2 nodes connected by an edge in the node sequence. Can you determine the other 2 nodes that will give the highest possible score?
3. The other 2 nodes must each be connected to one of the middle nodes. If we only consider nodes with the highest scores, how many should we store to ensure we don’t choose duplicate nodes?
4. For each node, we should store the 3 adjacent nodes with the highest scores to ensure we can find a sequence with no duplicate nodes via the method above.

## 示例

```
[5,2,9,8,4]
[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
[9,20,6,4,11,12]
[[0,3],[5,3],[2,4],[1,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumScore(int[] scores, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
```

### C

```c
int maximumScore(int* scores, int scoresSize, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(int[] scores, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} scores
 * @param {number[][]} edges
 * @return {number}
 */
var maximumScore = function(scores, edges) {
    
};
```

### TypeScript

```typescript
function maximumScore(scores: number[], edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @param Integer[][] $edges
     * @return Integer
     */
    function maximumScore($scores, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ scores: [Int], _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(scores: IntArray, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(List<int> scores, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func maximumScore(scores []int, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} scores
# @param {Integer[][]} edges
# @return {Integer}
def maximum_score(scores, edges)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(scores: Array[Int], edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(scores: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score scores edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(Scores :: [integer()], Edges :: [[integer()]]) -> integer().
maximum_score(Scores, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(scores :: [integer], edges :: [[integer]]) :: integer
  def maximum_score(scores, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(scores: Array<Int64>, edges: Array<Array<Int64>>): Int64 {

    }
}
```

