# 2569. 更新数组后处理求和查询

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，和一个二维数组&nbsp;<code>queries</code>&nbsp;表示一些操作。总共有 3 种类型的操作：</p>

<ol>
	<li>操作类型 1 为&nbsp;<code>queries[i]&nbsp;= [1, l, r]</code>&nbsp;。你需要将 <code>nums1</code>&nbsp;从下标&nbsp;<code>l</code>&nbsp;到下标 <code>r</code>&nbsp;的所有 <code>0</code>&nbsp;反转成 <code>1</code> 并且所有&nbsp;<code>1</code>&nbsp;反转成 <code>0</code>&nbsp;。<code>l</code>&nbsp;和 <code>r</code>&nbsp;下标都从 <strong>0</strong>&nbsp;开始。</li>
	<li>操作类型 2 为&nbsp;<code>queries[i]&nbsp;= [2, p, 0]</code>&nbsp;。对于&nbsp;<code>0 &lt;= i &lt; n</code>&nbsp;中的所有下标，令&nbsp;<code>nums2[i] =&nbsp;nums2[i]&nbsp;+ nums1[i]&nbsp;* p</code>&nbsp;。</li>
	<li>操作类型 3 为&nbsp;<code>queries[i]&nbsp;= [3, 0, 0]</code>&nbsp;。求&nbsp;<code>nums2</code>&nbsp;中所有元素的和。</li>
</ol>

<p>请你返回一个&nbsp;<em>数组</em>，包含&nbsp;<em>所有第三种操作类型&nbsp;</em>的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
<b>输出：</b>[3]
<strong>解释：</strong>第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
<b>输出：</b>[5]
<b>解释：</b>第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length,nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums1.length = nums2.length</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length = 3</code></li>
	<li><code>0 &lt;= l &lt;= r &lt;= nums1.length - 1</code></li>
	<li><code>0 &lt;= p &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= nums1[i] &lt;= 1</code></li>
	<li><code>0 &lt;= nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组

## 提示

1. Use the Lazy Segment Tree to process the queries quickly.

## 示例

```
[1,0,1]
[0,0,0]
[[1,1,1],[2,1,0],[3,0,0]]
[1]
[5]
[[2,0,0],[3,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def handleQuery(self, nums1, nums2, queries):
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
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* handleQuery(int* nums1, int nums1Size, int* nums2, int nums2Size, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] HandleQuery(int[] nums1, int[] nums2, int[][] queries) {
        
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
var handleQuery = function(nums1, nums2, queries) {
    
};
```

### TypeScript

```typescript
function handleQuery(nums1: number[], nums2: number[], queries: number[][]): number[] {
    
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
    function handleQuery($nums1, $nums2, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func handleQuery(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun handleQuery(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> handleQuery(List<int> nums1, List<int> nums2, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func handleQuery(nums1 []int, nums2 []int, queries [][]int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def handle_query(nums1, nums2, queries)
    
end
```

### Scala

```scala
object Solution {
    def handleQuery(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn handle_query(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (handle-query nums1 nums2 queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec handle_query(Nums1 :: [integer()], Nums2 :: [integer()], Queries :: [[integer()]]) -> [integer()].
handle_query(Nums1, Nums2, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec handle_query(nums1 :: [integer], nums2 :: [integer], queries :: [[integer]]) :: [integer]
  def handle_query(nums1, nums2, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func handleQuery(nums1: Array<Int64>, nums2: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

