# 1589. 所有排列中的最大和

## 题目描述

<p>有一个整数数组&nbsp;<code>nums</code>&nbsp;，和一个查询数组&nbsp;<code>requests</code>&nbsp;，其中&nbsp;<code>requests[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;。第&nbsp;<code>i</code>&nbsp;个查询求&nbsp;<code>nums[start<sub>i</sub>] + nums[start<sub>i</sub> + 1] + ... + nums[end<sub>i</sub> - 1] + nums[end<sub>i</sub>]</code>&nbsp;的结果&nbsp;，<code>start<sub>i</sub></code> 和&nbsp;<code>end<sub>i</sub></code>&nbsp;数组索引都是 <strong>从 0 开始</strong> 的。</p>

<p>你可以任意排列 <code>nums</code>&nbsp;中的数字，请你返回所有查询结果之和的最大值。</p>

<p>由于答案可能会很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
<strong>输出：</strong>19
<strong>解释：</strong>一个可行的 nums 排列为 [2,1,3,4,5]，并有如下结果：
requests[0] -&gt; nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -&gt; nums[0] + nums[1] = 2 + 1 = 3
总和为：8 + 3 = 11。
一个总和更大的排列为 [3,5,4,2,1]，并有如下结果：
requests[0] -&gt; nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -&gt; nums[0] + nums[1] = 3 + 5  = 8
总和为： 11 + 8 = 19，这个方案是所有排列中查询之和最大的结果。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,5,6], requests = [[0,1]]
<strong>输出：</strong>11
<strong>解释：</strong>一个总和最大的排列为 [6,5,4,3,2,1] ，查询和为 [11]。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
<strong>输出：</strong>47
<strong>解释：</strong>一个和最大的排列为 [4,10,5,3,2,1] ，查询结果分别为 [19,18,10]。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= requests.length &lt;=&nbsp;10<sup>5</sup></code></li>
	<li><code>requests[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub>&nbsp;&lt;= end<sub>i</sub>&nbsp;&lt;&nbsp;n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 前缀和
- 排序

## 提示

1. Indexes with higher frequencies should be bound with larger values

## 示例

```
[1,2,3,4,5]
[[1,3],[0,1]]
[1,2,3,4,5,6]
[[0,1]]
[1,2,3,4,5,10]
[[0,2],[1,3],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
```

### C

```c
int maxSumRangeQuery(int* nums, int numsSize, int** requests, int requestsSize, int* requestsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumRangeQuery(int[] nums, int[][] requests) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} requests
 * @return {number}
 */
var maxSumRangeQuery = function(nums, requests) {
    
};
```

### TypeScript

```typescript
function maxSumRangeQuery(nums: number[], requests: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $requests
     * @return Integer
     */
    function maxSumRangeQuery($nums, $requests) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumRangeQuery(_ nums: [Int], _ requests: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumRangeQuery(nums: IntArray, requests: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumRangeQuery(List<int> nums, List<List<int>> requests) {
    
  }
}
```

### Go

```golang
func maxSumRangeQuery(nums []int, requests [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} requests
# @return {Integer}
def max_sum_range_query(nums, requests)
    
end
```

### Scala

```scala
object Solution {
    def maxSumRangeQuery(nums: Array[Int], requests: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_range_query(nums: Vec<i32>, requests: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-range-query nums requests)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_range_query(Nums :: [integer()], Requests :: [[integer()]]) -> integer().
max_sum_range_query(Nums, Requests) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_range_query(nums :: [integer], requests :: [[integer]]) :: integer
  def max_sum_range_query(nums, requests) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumRangeQuery(nums: Array<Int64>, requests: Array<Array<Int64>>): Int64 {

    }
}
```

