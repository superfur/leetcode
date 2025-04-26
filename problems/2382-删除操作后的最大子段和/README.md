# 2382. 删除操作后的最大子段和

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code> 和&nbsp;<code>removeQueries</code>&nbsp;，两者长度都为&nbsp;<code>n</code>&nbsp;。对于第&nbsp;<code>i</code>&nbsp;个查询，<code>nums</code>&nbsp;中位于下标&nbsp;<code>removeQueries[i]</code>&nbsp;处的元素被删除，将 <code>nums</code>&nbsp;分割成更小的子段。</p>

<p>一个 <strong>子段</strong>&nbsp;是 <code>nums</code>&nbsp;中连续 <strong>正</strong>&nbsp;整数形成的序列。<strong>子段和</strong>&nbsp;是子段中所有元素的和。</p>

<p>请你返回一个长度为 <code>n</code>&nbsp;的整数数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[i]</code>是第&nbsp;<code>i</code>&nbsp;次删除操作以后的&nbsp;<strong>最大</strong>&nbsp;子段和。</p>

<p><strong>注意：</strong>一个下标至多只会被删除一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
<b>输出：</b>[14,7,2,2,0]
<b>解释：</b>用 0 表示被删除的元素，答案如下所示：
查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。
查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。
查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。
查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。
查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
所以，我们返回 [14,7,2,2,0] 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [3,2,11,1], removeQueries = [3,2,1,0]
<b>输出：</b>[16,5,3,0]
<b>解释：</b>用 0 表示被删除的元素，答案如下所示：
查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。
查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。
查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。
查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
所以，我们返回 [16,5,3,0] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length == removeQueries.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= removeQueries[i] &lt; n</code></li>
	<li><code>removeQueries</code>&nbsp;中所有数字 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 数组
- 有序集合
- 前缀和

## 提示

1. Use a sorted data structure to collect removal points and store the segments.
2. Use a heap or priority queue to store segment sums and their corresponding boundaries.
3. Make sure to remove invalid segments from the heap.

## 示例

```
[1,2,5,6,1]
[0,3,2,4,1]
[3,2,11,1]
[3,2,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] maximumSegmentSum(int[] nums, int[] removeQueries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* maximumSegmentSum(int* nums, int numsSize, int* removeQueries, int removeQueriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] MaximumSegmentSum(int[] nums, int[] removeQueries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} removeQueries
 * @return {number[]}
 */
var maximumSegmentSum = function(nums, removeQueries) {
    
};
```

### TypeScript

```typescript
function maximumSegmentSum(nums: number[], removeQueries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $removeQueries
     * @return Integer[]
     */
    function maximumSegmentSum($nums, $removeQueries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSegmentSum(_ nums: [Int], _ removeQueries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSegmentSum(nums: IntArray, removeQueries: IntArray): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumSegmentSum(List<int> nums, List<int> removeQueries) {
    
  }
}
```

### Go

```golang
func maximumSegmentSum(nums []int, removeQueries []int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} remove_queries
# @return {Integer[]}
def maximum_segment_sum(nums, remove_queries)
    
end
```

### Scala

```scala
object Solution {
    def maximumSegmentSum(nums: Array[Int], removeQueries: Array[Int]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_segment_sum(nums: Vec<i32>, remove_queries: Vec<i32>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-segment-sum nums removeQueries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_segment_sum(Nums :: [integer()], RemoveQueries :: [integer()]) -> [integer()].
maximum_segment_sum(Nums, RemoveQueries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_segment_sum(nums :: [integer], remove_queries :: [integer]) :: [integer]
  def maximum_segment_sum(nums, remove_queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSegmentSum(nums: Array<Int64>, removeQueries: Array<Int64>): Array<Int64> {

    }
}
```

