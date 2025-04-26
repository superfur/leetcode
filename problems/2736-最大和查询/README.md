# 2736. 最大和查询

## 题目描述

<p>给你两个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，另给你一个下标从 <strong>1</strong> 开始的二维数组 <code>queries</code> ，其中 <code>queries[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 。</p>

<p>对于第 <code>i</code> 个查询，在所有满足 <code>nums1[j] &gt;= x<sub>i</sub></code> 且 <code>nums2[j] &gt;= y<sub>i</sub></code> 的下标 <code>j</code> <code>(0 &lt;= j &lt; n)</code> 中，找出 <code>nums1[j] + nums2[j]</code> 的 <strong>最大值</strong> ，如果不存在满足条件的 <code>j</code> 则返回 <strong>-1</strong> 。</p>

<p>返回数组<em> </em><code>answer</code><em> ，</em>其中<em> </em><code>answer[i]</code><em> </em>是第 <code>i</code> 个查询的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
<strong>输出：</strong>[6,10,7]
<strong>解释：</strong>
对于第 1 个查询：<code>x<sub>i</sub> = 4</code>&nbsp;且&nbsp;<code>y<sub>i</sub> = 1</code> ，可以选择下标&nbsp;<code>j = 0</code>&nbsp;，此时 <code>nums1[j] &gt;= 4</code>&nbsp;且&nbsp;<code>nums2[j] &gt;= 1</code> 。<code>nums1[j] + nums2[j]</code>&nbsp;等于 6 ，可以证明 6 是可以获得的最大值。
对于第 2 个查询：<code>x<sub>i</sub> = 1</code>&nbsp;且&nbsp;<code>y<sub>i</sub> = 3</code> ，可以选择下标&nbsp;<code>j = 2</code>&nbsp;，此时 <code>nums1[j] &gt;= 1</code>&nbsp;且&nbsp;<code>nums2[j] &gt;= 3</code> 。<code>nums1[j] + nums2[j]</code>&nbsp;等于 10 ，可以证明 10 是可以获得的最大值。
对于第 3 个查询：<code>x<sub>i</sub> = 2</code>&nbsp;且&nbsp;<code>y<sub>i</sub> = 5</code> ，可以选择下标&nbsp;<code>j = 3</code>&nbsp;，此时 <code>nums1[j] &gt;= 2</code>&nbsp;且&nbsp;<code>nums2[j] &gt;= 5</code> 。<code>nums1[j] + nums2[j]</code>&nbsp;等于 7 ，可以证明 7 是可以获得的最大值。
因此，我们返回&nbsp;<code>[6,10,7]</code> 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
<strong>输出：</strong>[9,9,9]
<strong>解释：</strong>对于这个示例，我们可以选择下标&nbsp;<code>j = 2</code>&nbsp;，该下标可以满足每个查询的限制。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
<strong>输出：</strong>[-1]
<strong>解释：</strong>示例中的查询 <code>x<sub>i</sub></code> = 3 且 <code>y<sub>i</sub></code> = 3 。对于每个下标 j ，都只满足 nums1[j] &lt; <code>x<sub>i</sub></code> 或者 nums2[j] &lt; <code>y<sub>i</sub></code> 。因此，不存在答案。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums1.length == nums2.length</code>&nbsp;</li>
	<li><code>n ==&nbsp;nums1.length&nbsp;</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup>&nbsp;</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length ==&nbsp;2</code></li>
	<li><code>x<sub>i</sub>&nbsp;== queries[i][1]</code></li>
	<li><code>y<sub>i</sub> == queries[i][2]</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 树状数组
- 线段树
- 数组
- 二分查找
- 排序
- 单调栈

## 提示

1. Sort (x, y) tuples and queries by x-coordinate descending. Don’t forget to index queries before sorting so that you can answer them in the correct order.
2. Before answering a query (min_x, min_y), add all (x, y) pairs with x >= min_x to some data structure.
3. Use a monotone descending map to store (y, x + y) pairs. A monotone map has ascending keys and descending values. When inserting a pair (y, x + y), remove all pairs (y', x' + y') with y' < y and x' + y' <= x + y.
4. To find the insertion position use binary search (built-in in many languages).
5. When querying for max (x + y) over y >= y', use binary search to find the first pair (y, x + y) with y >= y'. It will have the maximum value of x + y because the map has monotone descending values.

## 示例

```
[4,3,1,2]
[2,4,9,5]
[[4,1],[1,3],[2,5]]
[3,2,5]
[2,3,4]
[[4,4],[3,2],[1,1]]
[2,1]
[2,3]
[[3,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maximumSumQueries(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maximumSumQueries(int[] nums1, int[] nums2, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSumQueries(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumSumQueries(int* nums1, int nums1Size, int* nums2, int nums2Size, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaximumSumQueries(int[] nums1, int[] nums2, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumSumQueries = function(nums1, nums2, queries) {
    
};
```

### TypeScript

```typescript
function maximumSumQueries(nums1: number[], nums2: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximumSumQueries($nums1, $nums2, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSumQueries(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSumQueries(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumSumQueries(List<int> nums1, List<int> nums2, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func maximumSumQueries(nums1 []int, nums2 []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_sum_queries(nums1, nums2, queries)
    
end
```

### Scala

```scala
object Solution {
    def maximumSumQueries(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum_queries(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum-queries nums1 nums2 queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_sum_queries(Nums1 :: [integer()], Nums2 :: [integer()], Queries :: [[integer()]]) -> [integer()].
maximum_sum_queries(Nums1, Nums2, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_queries(nums1 :: [integer], nums2 :: [integer], queries :: [[integer]]) :: [integer]
  def maximum_sum_queries(nums1, nums2, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSumQueries(nums1: Array<Int64>, nums2: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

