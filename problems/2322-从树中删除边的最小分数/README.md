# 2322. 从树中删除边的最小分数

## 题目描述

<p>存在一棵无向连通树，树中有编号从 <code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个节点， 以及 <code>n - 1</code> 条边。</p>

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，长度为 <code>n</code> ，其中 <code>nums[i]</code> 表示第 <code>i</code> 个节点的值。另给你一个二维整数数组 <code>edges</code> ，长度为 <code>n - 1</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中存在一条位于节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间的边。</p>

<p>删除树中两条 <strong>不同</strong> 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：</p>

<ol>
	<li>分别获取三个组件 <strong>每个</strong> 组件中所有节点值的异或值。</li>
	<li><strong>最大</strong> 异或值和 <strong>最小</strong> 异或值的 <strong>差值</strong> 就是这一种删除边方案的分数。</li>
</ol>

<ul>
	<li>例如，三个组件的节点值分别是：<code>[4,5,7]</code>、<code>[1,9]</code> 和 <code>[3,3,3]</code> 。三个异或值分别是 <code>4 ^ 5 ^ 7 = <em><strong>6</strong></em></code>、<code>1 ^ 9 = <em><strong>8</strong></em></code> 和 <code>3 ^ 3 ^ 3 = <em><strong>3</strong></em></code> 。最大异或值是 <code>8</code> ，最小异或值是 <code>3</code> ，分数是 <code>8 - 3 = 5</code> 。</li>
</ul>

<p>返回在给定树上执行任意删除边方案可能的 <strong>最小</strong> 分数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex1drawio.png" style="width: 193px; height: 190px;">
<pre><strong>输入：</strong>nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
<strong>输出：</strong>9
<strong>解释：</strong>上图展示了一种删除边方案。
- 第 1 个组件的节点是 [1,3,4] ，值是 [5,4,11] 。异或值是 5 ^ 4 ^ 11 = 10 。
- 第 2 个组件的节点是 [0] ，值是 [1] 。异或值是 1 = 1 。
- 第 3 个组件的节点是 [2] ，值是 [5] 。异或值是 5 = 5 。
分数是最大异或值和最小异或值的差值，10 - 1 = 9 。
可以证明不存在分数比 9 小的删除边方案。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex2drawio.png" style="width: 287px; height: 150px;">
<pre><strong>输入：</strong>nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
<strong>输出：</strong>0
<strong>解释：</strong>上图展示了一种删除边方案。
- 第 1 个组件的节点是 [3,4] ，值是 [4,4] 。异或值是 4 ^ 4 = 0 。
- 第 2 个组件的节点是 [1,0] ，值是 [5,5] 。异或值是 5 ^ 5 = 0 。
- 第 3 个组件的节点是 [2,5] ，值是 [2,2] 。异或值是 2 ^ 2 = 0 。
分数是最大异或值和最小异或值的差值，0 - 0 = 0 。
无法获得比 0 更小的分数 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code> 表示一棵有效的树</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 树
- 深度优先搜索
- 数组

## 提示

1. Consider iterating over the first edge to remove, and then doing some precalculations on the 2 resulting connected components.
2. Will calculating the XOR of each subtree help?

## 示例

```
[1,5,5,4,11]
[[0,1],[1,2],[1,3],[3,4]]
[5,5,2,4,4,2]
[[0,1],[1,2],[5,2],[4,3],[1,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumScore(int[] nums, int[][] edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        
```

### C

```c
int minimumScore(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumScore(int[] nums, int[][] edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
var minimumScore = function(nums, edges) {
    
};
```

### TypeScript

```typescript
function minimumScore(nums: number[], edges: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $edges
     * @return Integer
     */
    function minimumScore($nums, $edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumScore(_ nums: [Int], _ edges: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumScore(nums: IntArray, edges: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumScore(List<int> nums, List<List<int>> edges) {
    
  }
}
```

### Go

```golang
func minimumScore(nums []int, edges [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def minimum_score(nums, edges)
    
end
```

### Scala

```scala
object Solution {
    def minimumScore(nums: Array[Int], edges: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_score(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-score nums edges)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_score(Nums :: [integer()], Edges :: [[integer()]]) -> integer().
minimum_score(Nums, Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_score(nums :: [integer], edges :: [[integer]]) :: integer
  def minimum_score(nums, edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumScore(nums: Array<Int64>, edges: Array<Array<Int64>>): Int64 {

    }
}
```

