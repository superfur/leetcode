# 2940. 找到 Alice 和 Bob 可以相遇的建筑

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的正整数数组&nbsp;<code>heights</code>&nbsp;，其中&nbsp;<code>heights[i]</code>&nbsp;表示第 <code>i</code>&nbsp;栋建筑的高度。</p>

<p>如果一个人在建筑&nbsp;<code>i</code>&nbsp;，且存在&nbsp;<code>i &lt; j</code>&nbsp;的建筑&nbsp;<code>j</code>&nbsp;满足&nbsp;<code>heights[i] &lt; heights[j]</code>&nbsp;，那么这个人可以移动到建筑&nbsp;<code>j</code>&nbsp;。</p>

<p>给你另外一个数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;。第&nbsp;<code>i</code>&nbsp;个查询中，Alice 在建筑&nbsp;<code>a<sub>i</sub></code> ，Bob 在建筑&nbsp;<code>b<sub>i</sub></code><sub>&nbsp;</sub>。</p>

<p>请你能返回一个数组&nbsp;<code>ans</code>&nbsp;，其中&nbsp;<code>ans[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个查询中，Alice 和 Bob 可以相遇的&nbsp;<strong>最左边的建筑</strong>&nbsp;。如果对于查询&nbsp;<code>i</code>&nbsp;，Alice<em> </em>和<em> </em>Bob 不能相遇，令&nbsp;<code>ans[i]</code> 为&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
<b>输出：</b>[2,5,-1,5,2]
<b>解释：</b>第一个查询中，Alice 和 Bob 可以移动到建筑 2 ，因为 heights[0] &lt; heights[2] 且 heights[1] &lt; heights[2] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[0] &lt; heights[5] 且 heights[3] &lt; heights[5] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Alice 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[3] &lt; heights[5] 且 heights[4] &lt; heights[5] 。
第五个查询中，Alice 和 Bob 已经在同一栋建筑中。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
<b>输出：</b>[7,6,-1,4,6]
<strong>解释：</strong>第一个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[0] &lt; heights[7] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 6 ，因为 heights[3] &lt; heights[6] 且 heights[5] &lt; heights[6] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Bob 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 4 ，因为 heights[3] &lt; heights[4] 且 heights[0] &lt; heights[4] 。
第五个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[1] &lt; heights[6] 。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= heights.length - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 树状数组
- 线段树
- 数组
- 二分查找
- 单调栈
- 堆（优先队列）

## 提示

1. For each query <code>[x, y]</code>, if <code>x > y</code>, swap <code>x</code> and <code>y</code>. Now, we can assume that <code>x <= y</code>.
2. For each query <code>[x, y]</code>, if <code>x == y</code> or <code>heights[x] < heights[y]</code>, then the answer is <code>y</code> since <code>x ≤ y</code>.
3. Otherwise, we need to find the smallest index <code>t</code> such that <code>y < t</code> and <code>heights[x] < heights[t]</code>. Note that <code>heights[y] <= heights[x]</code>, so <code>heights[x] < heights[t]</code> is a sufficient condition.
4. To find index <code>t</code> for each query, sort the queries in descending order of <code>y</code>. Iterate over the queries while maintaining a monotonic stack which we can binary search over to find index <code>t</code>.

## 示例

```
[6,4,8,5,2,7]
[[0,1],[0,3],[2,4],[3,4],[2,2]]
[5,3,8,2,6,1,4,6]
[[0,7],[3,5],[5,2],[3,0],[1,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] leftmostBuildingQueries(int[] heights, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* leftmostBuildingQueries(int* heights, int heightsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] LeftmostBuildingQueries(int[] heights, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} heights
 * @param {number[][]} queries
 * @return {number[]}
 */
var leftmostBuildingQueries = function(heights, queries) {
    
};
```

### TypeScript

```typescript
function leftmostBuildingQueries(heights: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function leftmostBuildingQueries($heights, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func leftmostBuildingQueries(_ heights: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun leftmostBuildingQueries(heights: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> leftmostBuildingQueries(List<int> heights, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func leftmostBuildingQueries(heights []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} heights
# @param {Integer[][]} queries
# @return {Integer[]}
def leftmost_building_queries(heights, queries)
    
end
```

### Scala

```scala
object Solution {
    def leftmostBuildingQueries(heights: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn leftmost_building_queries(heights: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (leftmost-building-queries heights queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec leftmost_building_queries(Heights :: [integer()], Queries :: [[integer()]]) -> [integer()].
leftmost_building_queries(Heights, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec leftmost_building_queries(heights :: [integer], queries :: [[integer]]) :: [integer]
  def leftmost_building_queries(heights, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func leftmostBuildingQueries(heights: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

