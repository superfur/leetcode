# 3277. 查询子数组最大异或值

## 题目描述

<p>给你一个由 <code>n</code> 个整数组成的数组 <code>nums</code>，以及一个大小为 <code>q</code> 的二维整数数组 <code>queries</code>，其中 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code>。</p>

<p>对于每一个查询，你需要找出 <code>nums[l<sub>i</sub>..r<sub>i</sub>]</code> 中任意 <span data-keyword="subarray">子数组</span> 的 <strong>最大异或值</strong>。</p>

<p><strong>数组的异或值 </strong>需要对数组 <code>a</code> 反复执行以下操作，直到只剩一个元素，剩下的那个元素就是 <strong>异或值</strong>：</p>

<ul>
	<li><span class="text-only" data-eleid="9" style="white-space: pre;">对于除最后一个下标以外的所有下标</span> <code>i</code>，同时将 <code>a[i]</code> 替换为 <code>a[i] XOR a[i + 1]</code> 。</li>
	<li>移除数组的最后一个元素。</li>
</ul>

<p>返回一个大小为 <code>q</code> 的数组 <code>answer</code>，其中 <code>answer[i]</code> 表示查询 <code>i</code> 的答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[12,60,60]</span></p>

<p><strong>解释：</strong></p>

<p>在第一个查询中，<code>nums[0..2]</code> 的子数组分别是 <code>[2]</code>, <code>[8]</code>, <code>[4]</code>, <code>[2, 8]</code>, <code>[8, 4]</code>, 和 <code>[2, 8, 4]</code>，它们的异或值分别为 2, 8, 4, 10, 12, 和 6。查询的答案是 12，所有异或值中的最大值。</p>

<p>在第二个查询中，<code>nums[1..4]</code> 的子数组中最大的异或值是子数组 <code>nums[1..4]</code> 的异或值，为 60。</p>

<p>在第三个查询中，<code>nums[0..5]</code> 的子数组中最大的异或值是子数组 <code>nums[1..4]</code> 的异或值，为 60。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0,7,3,2,8,5,1], queries = [[0,3],[1,5],[2,4],[2,6],[5,6]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[7,14,11,14,5]</span></p>

<p><strong>解释：</strong></p>

<table height="70" width="472">
	<thead>
		<tr>
			<th>下标</th>
			<th>nums[l<sub>i</sub>..r<sub>i</sub>]</th>
			<th>最大异或值子数组</th>
			<th>子数组最大异或值</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>[0, 7, 3, 2]</td>
			<td>[7]</td>
			<td>7</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[7, 3, 2, 8, 5]</td>
			<td>[7, 3, 2, 8]</td>
			<td>14</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[3, 2, 8]</td>
			<td>[3, 2, 8]</td>
			<td>11</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[3, 2, 8, 5, 1]</td>
			<td>[2, 8, 5, 1]</td>
			<td>14</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[5, 1]</td>
			<td>[5]</td>
			<td>5</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= q == queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;= n - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Precompute the XOR score of every subarray.
2. Try to find a relationship between XOR score of <code>nums[i..j], nums[i..j + 1], nums[i..j + 2], …</code>. Do you notice any pattern?
3. If <code>dp[i][j]</code> is the XOR score of subarray <code>nums[i..j]</code>, <code>dp[i][j] = dp[i - 1][j] XOR dp[i - 1][j + 1]</code>.

## 示例

```
[2,8,4,32,16,1]
[[0,2],[1,4],[0,5]]
[0,7,3,2,8,5,1]
[[0,3],[1,5],[2,4],[2,6],[5,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maximumSubarrayXor(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maximumSubarrayXor(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumSubarrayXor(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaximumSubarrayXor(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumSubarrayXor = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function maximumSubarrayXor(nums: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximumSubarrayXor($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSubarrayXor(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSubarrayXor(nums: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumSubarrayXor(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func maximumSubarrayXor(nums []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_subarray_xor(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def maximumSubarrayXor(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_subarray_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-subarray-xor nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_subarray_xor(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
maximum_subarray_xor(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_subarray_xor(nums :: [integer], queries :: [[integer]]) :: [integer]
  def maximum_subarray_xor(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSubarrayXor(nums: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

