# 3080. 执行操作标记数组中的元素

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的正整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>同时给你一个长度为 <code>m</code>&nbsp;的二维操作数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [index<sub>i</sub>, k<sub>i</sub>]</code>&nbsp;。</p>

<p>一开始，数组中的所有元素都 <strong>未标记</strong>&nbsp;。</p>

<p>你需要依次对数组执行 <code>m</code>&nbsp;次操作，第 <code>i</code>&nbsp;次操作中，你需要执行：</p>

<ul>
	<li>如果下标&nbsp;<code>index<sub>i</sub></code>&nbsp;对应的元素还没标记，那么标记这个元素。</li>
	<li>然后标记&nbsp;<code>k<sub>i</sub></code>&nbsp;个数组中还没有标记的&nbsp;<strong>最小</strong>&nbsp;元素。如果有元素的值相等，那么优先标记它们中下标较小的。如果少于&nbsp;<code>k<sub>i</sub></code>&nbsp;个未标记元素存在，那么将它们全部标记。</li>
</ul>

<p>请你返回一个长度为 <code>m</code>&nbsp;的数组 <code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[i]</code>是第&nbsp;<code>i</code>&nbsp;次操作后数组中还没标记元素的&nbsp;<strong>和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">[8,3,0]</span></p>

<p><strong>解释：</strong></p>

<p>我们依次对数组做以下操作：</p>

<ul>
	<li>标记下标为&nbsp;<code>1</code>&nbsp;的元素，同时标记&nbsp;<code>2</code>&nbsp;个未标记的最小元素。标记完后数组为&nbsp;<code>nums = [<em><strong>1</strong></em>,<em><strong>2</strong></em>,2,<em><strong>1</strong></em>,2,3,1]</code>&nbsp;。未标记元素的和为&nbsp;<code>2 + 2 + 3 + 1 = 8</code>&nbsp;。</li>
	<li>标记下标为&nbsp;<code>3</code>&nbsp;的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的&nbsp;<code>3</code>&nbsp;个未标记的最小元素。标记完后数组为&nbsp;<code>nums = [<em><strong>1</strong></em>,<em><strong>2</strong></em>,<em><strong>2</strong></em>,<em><strong>1</strong></em>,<em><strong>2</strong></em>,3,<em><strong>1</strong></em>]</code>&nbsp;。未标记元素的和为&nbsp;<code>3</code>&nbsp;。</li>
	<li>标记下标为 <code>4</code>&nbsp;的元素，由于它已经被标记过了，所以我们忽略这次标记，同时标记最靠前的 <code>2</code>&nbsp;个未标记的最小元素。标记完后数组为&nbsp;<code>nums = [<em><strong>1</strong></em>,<em><strong>2</strong></em>,<em><strong>2</strong></em>,<em><strong>1</strong></em>,<em><strong>2</strong></em>,<em><strong>3</strong></em>,<em><strong>1</strong></em>]</code>&nbsp;。未标记元素的和为&nbsp;<code>0</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [1,4,2,3], queries = [[0,1]]</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">[7]</span></p>

<p><strong>解释：</strong>我们执行一次操作，将下标为&nbsp;<code>0</code>&nbsp;处的元素标记，并且标记最靠前的&nbsp;<code>1</code>&nbsp;个未标记的最小元素。标记完后数组为&nbsp;<code>nums = [<em><strong>1</strong></em>,4,<em><strong>2</strong></em>,3]</code>&nbsp;。未标记元素的和为&nbsp;<code>4 + 3 = 7</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= m &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= index<sub>i</sub>, k<sub>i</sub> &lt;= n - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. Use another array to keep track of marked indices.
2. Sort the array <code>nums</code> to be able to find the smallest unmarked elements quickly in each query.

## 示例

```
[1,2,2,1,2,3,1]
[[1,2],[3,3],[4,2]]
[1,4,2,3]
[[0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> unmarkedSumArray(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] unmarkedSumArray(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* unmarkedSumArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] UnmarkedSumArray(int[] nums, int[][] queries) {
        
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
var unmarkedSumArray = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function unmarkedSumArray(nums: number[], queries: number[][]): number[] {
    
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
    function unmarkedSumArray($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func unmarkedSumArray(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun unmarkedSumArray(nums: IntArray, queries: Array<IntArray>): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> unmarkedSumArray(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func unmarkedSumArray(nums []int, queries [][]int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def unmarked_sum_array(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def unmarkedSumArray(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unmarked_sum_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (unmarked-sum-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec unmarked_sum_array(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
unmarked_sum_array(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unmarked_sum_array(nums :: [integer], queries :: [[integer]]) :: [integer]
  def unmarked_sum_array(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func unmarkedSumArray(nums: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

