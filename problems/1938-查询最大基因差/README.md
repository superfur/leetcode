# 1938. 查询最大基因差

## 题目描述

<p>给你一棵 <code>n</code> 个节点的有根树，节点编号从 <code>0</code> 到 <code>n - 1</code> 。每个节点的编号表示这个节点的 <strong>独一无二的基因值</strong> （也就是说节点 <code>x</code> 的基因值为 <code>x</code>）。两个基因值的 <strong>基因差</strong> 是两者的 <strong>异或和</strong> 。给你整数数组 <code>parents</code> ，其中 <code>parents[i]</code> 是节点 <code>i</code> 的父节点。如果节点 <code>x</code> 是树的 <strong>根</strong> ，那么 <code>parents[x] == -1</code> 。</p>

<p>给你查询数组 <code>queries</code> ，其中 <code>queries[i] = [node<sub>i</sub>, val<sub>i</sub>]</code> 。对于查询 <code>i</code> ，请你找到 <code>val<sub>i</sub></code> 和 <code>p<sub>i</sub></code> 的 <strong>最大基因差</strong> ，其中 <code>p<sub>i</sub></code> 是节点 <code>node<sub>i</sub></code> 到根之间的任意节点（包含 <code>node<sub>i</sub></code> 和根节点）。更正式的，你想要最大化 <code>val<sub>i</sub> XOR p<sub>i</sub></code><sub> </sub>。</p>

<p>请你返回数组<em> </em><code>ans</code> ，其中 <code>ans[i]</code> 是第 <code>i</code> 个查询的答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/c1.png" style="width: 118px; height: 163px;">
<pre><b>输入：</b>parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
<b>输出：</b>[2,3,7]
<strong>解释：</strong>查询数组处理如下：
- [0,2]：最大基因差的对应节点为 0 ，基因差为 2 XOR 0 = 2 。
- [3,2]：最大基因差的对应节点为 1 ，基因差为 2 XOR 1 = 3 。
- [2,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/c2.png" style="width: 256px; height: 221px;">
<pre><b>输入：</b>parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
<b>输出：</b>[6,14,7]
<strong>解释：</strong>查询数组处理如下：
- [4,6]：最大基因差的对应节点为 0 ，基因差为 6 XOR 0 = 6 。
- [1,15]：最大基因差的对应节点为 1 ，基因差为 15 XOR 1 = 14 。
- [0,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= parents.length &lt;= 10<sup>5</sup></code></li>
	<li>对于每个 <strong>不是</strong> 根节点的 <code>i</code> ，有 <code>0 &lt;= parents[i] &lt;= parents.length - 1</code> 。</li>
	<li><code>parents[root] == -1</code></li>
	<li><code>1 &lt;= queries.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= node<sub>i</sub> &lt;= parents.length - 1</code></li>
	<li><code>0 &lt;= val<sub>i</sub> &lt;= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 深度优先搜索
- 字典树
- 数组
- 哈希表

## 提示

1. How can we use a trie to store all the XOR values in the path from a node to the root?
2. How can we dynamically add the XOR values with a DFS search?

## 示例

```
[-1,0,1,1]
[[0,2],[3,2],[2,5]]
[3,7,-1,2,0,7,0,2]
[[4,6],[1,15],[0,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maxGeneticDifference(int[] parents, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxGeneticDifference(int* parents, int parentsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaxGeneticDifference(int[] parents, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} parents
 * @param {number[][]} queries
 * @return {number[]}
 */
var maxGeneticDifference = function(parents, queries) {
    
};
```

### TypeScript

```typescript
function maxGeneticDifference(parents: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maxGeneticDifference($parents, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxGeneticDifference(_ parents: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxGeneticDifference(parents: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxGeneticDifference(List<int> parents, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func maxGeneticDifference(parents []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} parents
# @param {Integer[][]} queries
# @return {Integer[]}
def max_genetic_difference(parents, queries)
    
end
```

### Scala

```scala
object Solution {
    def maxGeneticDifference(parents: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_genetic_difference(parents: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-genetic-difference parents queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_genetic_difference(Parents :: [integer()], Queries :: [[integer()]]) -> [integer()].
max_genetic_difference(Parents, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_genetic_difference(parents :: [integer], queries :: [[integer]]) :: [integer]
  def max_genetic_difference(parents, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxGeneticDifference(parents: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

