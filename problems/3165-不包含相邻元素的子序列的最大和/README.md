# 3165. 不包含相邻元素的子序列的最大和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个二维数组 <code>queries</code>，其中 <code>queries[i] = [pos<sub>i</sub>, x<sub>i</sub>]</code>。</p>

<p>对于每个查询 <code>i</code>，首先将 <code>nums[pos<sub>i</sub>]</code> 设置为 <code>x<sub>i</sub></code>，然后计算查询 <code>i</code> 的答案，该答案为 <code>nums</code> 中 <strong>不包含相邻元素 </strong>的 <span data-keyword="subsequence-array">子序列</span> 的 <strong>最大 </strong>和。</p>

<p>返回所有查询的答案之和。</p>

<p>由于最终答案可能非常大，返回其对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p><strong>子序列</strong> 是指从另一个数组中删除一些或不删除元素而不改变剩余元素顺序得到的数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [3,5,9], queries = [[1,-2],[0,-3]]</span></p>

<p><strong>输出：</strong><span class="example-io">21</span></p>

<p><strong>解释：</strong><br />
执行第 1 个查询后，<code>nums = [3,-2,9]</code>，不包含相邻元素的子序列的最大和为 <code>3 + 9 = 12</code>。<br />
执行第 2 个查询后，<code>nums = [-3,-2,9]</code>，不包含相邻元素的子序列的最大和为 9 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [0,-1], queries = [[0,-5]]</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong><br />
执行第 1 个查询后，<code>nums = [-5,-1]</code>，不包含相邻元素的子序列的最大和为 0（选择空子序列）。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i] == [pos<sub>i</sub>, x<sub>i</sub>]</code></li>
	<li><code>0 &lt;= pos<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>-10<sup>5</sup> &lt;= x<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组
- 分治
- 动态规划

## 提示

1. Can you solve each query in <code>O(nums.length)</code> with dynamic programming?
2. In order to optimize, we will use segment tree where each node contains the maximum value of (front element has been chosen or not, back element has been chosen or not).

## 示例

```
[3,5,9]
[[1,-2],[0,-3]]
[0,-1]
[[0,-5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumSumSubsequence(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSumSubsequence(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        
```

### C

```c
int maximumSumSubsequence(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumSumSubsequence(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var maximumSumSubsequence = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function maximumSumSubsequence(nums: number[], queries: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer
     */
    function maximumSumSubsequence($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSumSubsequence(_ nums: [Int], _ queries: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSumSubsequence(nums: IntArray, queries: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSumSubsequence(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func maximumSumSubsequence(nums []int, queries [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def maximum_sum_subsequence(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def maximumSumSubsequence(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum_subsequence(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum-subsequence nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum_subsequence(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
maximum_sum_subsequence(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_subsequence(nums :: [integer], queries :: [[integer]]) :: integer
  def maximum_sum_subsequence(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSumSubsequence(nums: Array<Int64>, queries: Array<Array<Int64>>): Int64 {

    }
}
```

