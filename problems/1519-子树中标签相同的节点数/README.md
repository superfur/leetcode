# 1519. 子树中标签相同的节点数

## 题目描述

<p>给你一棵树（即，一个连通的无环无向图），这棵树由编号从 <code>0</code>&nbsp; 到 <code>n - 1</code> 的 n 个节点组成，且恰好有 <code>n - 1</code> 条 <code>edges</code> 。树的根节点为节点 <code>0</code> ，树上的每一个节点都有一个标签，也就是字符串 <code>labels</code> 中的一个小写字符（编号为 <code>i</code> 的 节点的标签就是 <code>labels[i]</code> ）</p>

<p>边数组 <code>edges</code> 以 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 的形式给出，该格式表示节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条边。</p>

<p>返回一个大小为 <em><code>n</code></em> 的数组，其中 <code>ans[i]</code> 表示第 <code>i</code> 个节点的子树中与节点 <code>i</code> 标签相同的节点数。</p>

<p>树 <code>T</code> 中的子树是由 <code>T</code> 中的某个节点及其所有后代节点组成的树。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e1.jpg" style="height: 321px; width: 441px;" /></p>

<pre>
<strong>输入：</strong>n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
<strong>输出：</strong>[2,1,1,1,1,1,1]
<strong>解释：</strong>节点 0 的标签为 'a' ，以 'a' 为根节点的子树中，节点 2 的标签也是 'a' ，因此答案为 2 。注意树中的每个节点都是这棵子树的一部分。
节点 1 的标签为 'b' ，节点 1 的子树包含节点 1、4 和 5，但是节点 4、5 的标签与节点 1 不同，故而答案为 1（即，该节点本身）。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e2.jpg" style="height: 321px; width: 381px;" /></p>

<pre>
<strong>输入：</strong>n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
<strong>输出：</strong>[4,2,1,1]
<strong>解释：</strong>节点 2 的子树中只有节点 2 ，所以答案为 1 。
节点 3 的子树中只有节点 3 ，所以答案为 1 。
节点 1 的子树中包含节点 1 和 2 ，标签都是 'b' ，因此答案为 2 。
节点 0 的子树中包含节点 0、1、2 和 3，标签都是 'b'，因此答案为 4 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e3.jpg" style="height: 321px; width: 381px;" /></p>

<pre>
<strong>输入：</strong>n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
<strong>输出：</strong>[3,2,1,1,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>,&nbsp;b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> !=&nbsp;b<sub>i</sub></code></li>
	<li><code>labels.length == n</code></li>
	<li><code>labels</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 哈希表
- 计数

## 提示

1. Start traversing the tree and each node should return a vector to its parent node.
2. The vector should be of length 26 and have the count of all the labels in the sub-tree of this node.

## 示例

```
7
[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
"abaedcd"
4
[[0,1],[1,2],[0,3]]
"bbbb"
5
[[0,1],[0,2],[1,3],[0,4]]
"aabab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSubTrees(int n, int** edges, int edgesSize, int* edgesColSize, char* labels, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountSubTrees(int n, int[][] edges, string labels) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    
};
```

### TypeScript

```typescript
function countSubTrees(n: number, edges: number[][], labels: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $labels
     * @return Integer[]
     */
    function countSubTrees($n, $edges, $labels) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubTrees(_ n: Int, _ edges: [[Int]], _ labels: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubTrees(n: Int, edges: Array<IntArray>, labels: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countSubTrees(int n, List<List<int>> edges, String labels) {
    
  }
}
```

### Go

```golang
func countSubTrees(n int, edges [][]int, labels string) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} labels
# @return {Integer[]}
def count_sub_trees(n, edges, labels)
    
end
```

### Scala

```scala
object Solution {
    def countSubTrees(n: Int, edges: Array[Array[Int]], labels: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_sub_trees(n: i32, edges: Vec<Vec<i32>>, labels: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-sub-trees n edges labels)
  (-> exact-integer? (listof (listof exact-integer?)) string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_sub_trees(N :: integer(), Edges :: [[integer()]], Labels :: unicode:unicode_binary()) -> [integer()].
count_sub_trees(N, Edges, Labels) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_sub_trees(n :: integer, edges :: [[integer]], labels :: String.t) :: [integer]
  def count_sub_trees(n, edges, labels) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubTrees(n: Int64, edges: Array<Array<Int64>>, labels: String): Array<Int64> {

    }
}
```

