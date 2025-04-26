# 3488. 距离最小相等元素查询

## 题目描述

<p>给你一个&nbsp;<strong>循环&nbsp;</strong>数组&nbsp;<code>nums</code>&nbsp;和一个数组&nbsp;<code>queries</code>&nbsp;。</p>

<p>对于每个查询&nbsp;<code>i</code>&nbsp;，你需要找到以下内容：</p>

<ul>
	<li>数组&nbsp;<code>nums</code>&nbsp;中下标&nbsp;<code>queries[i]</code>&nbsp;处的元素与&nbsp;<strong>任意&nbsp;</strong>其他下标&nbsp;<code>j</code>（满足&nbsp;<code>nums[j] == nums[queries[i]]</code>）之间的&nbsp;<strong>最小&nbsp;</strong>距离。如果不存在这样的下标&nbsp;<code>j</code>，则该查询的结果为 <code>-1</code> 。</li>
</ul>

<p>返回一个数组&nbsp;<code>answer</code>，其大小与&nbsp;<code>queries</code>&nbsp;相同，其中&nbsp;<code>answer[i]</code>&nbsp;表示查询<code>i</code>的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3,1,4,1,3,2], queries = [0,3,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,-1,3]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>查询 0：下标&nbsp;<code>queries[0] = 0</code>&nbsp;处的元素为&nbsp;<code>nums[0] = 1</code>&nbsp;。最近的相同值下标为 2，距离为 2。</li>
	<li>查询 1：下标&nbsp;<code>queries[1] = 3</code>&nbsp;处的元素为&nbsp;<code>nums[3] = 4</code>&nbsp;。不存在其他包含值 4 的下标，因此结果为 -1。</li>
	<li>查询 2：下标&nbsp;<code>queries[2] = 5</code>&nbsp;处的元素为&nbsp;<code>nums[5] = 3</code>&nbsp;。最近的相同值下标为 1，距离为 3（沿着循环路径：<code>5 -&gt; 6 -&gt; 0 -&gt; 1</code>）。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4], queries = [0,1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1,-1,-1]</span></p>

<p><strong>解释：</strong></p>

<p>数组&nbsp;<code>nums</code>&nbsp;中的每个值都是唯一的，因此没有下标与查询的元素值相同。所有查询的结果均为 -1。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找

## 提示

1. Use a dictionary that maps each unique value in the array to a sorted list of its indices.
2. For each query, use binary search on the sorted indices list to find the nearest occurrences of the target value.

## 示例

```
[1,3,1,4,1,3,2]
[0,3,5]
[1,2,3,4]
[0,1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solveQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> SolveQueries(int[] nums, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var solveQueries = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function solveQueries(nums: number[], queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function solveQueries($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func solveQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun solveQueries(nums: IntArray, queries: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> solveQueries(List<int> nums, List<int> queries) {
    
  }
}
```

### Go

```golang
func solveQueries(nums []int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def solve_queries(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def solveQueries(nums: Array[Int], queries: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn solve_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (solve-queries nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec solve_queries(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
solve_queries(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec solve_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def solve_queries(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func solveQueries(nums: Array<Int64>, queries: Array<Int64>): ArrayList<Int64> {

    }
}
```

