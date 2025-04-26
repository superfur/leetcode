# 2602. 使数组元素全部相等的最少操作次数

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>同时给你一个长度为 <code>m</code>&nbsp;的整数数组&nbsp;<code>queries</code>&nbsp;。第 <code>i</code>&nbsp;个查询中，你需要将 <code>nums</code>&nbsp;中所有元素变成&nbsp;<code>queries[i]</code>&nbsp;。你可以执行以下操作&nbsp;<strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>将数组里一个元素&nbsp;<strong>增大</strong>&nbsp;或者&nbsp;<strong>减小</strong>&nbsp;<code>1</code>&nbsp;。</li>
</ul>

<p>请你返回一个长度为 <code>m</code>&nbsp;的数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[i]</code>是将&nbsp;<code>nums</code>&nbsp;中所有元素变成&nbsp;<code>queries[i]</code>&nbsp;的&nbsp;<strong>最少</strong>&nbsp;操作次数。</p>

<p><strong>注意</strong>，每次查询后，数组变回最开始的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,1,6,8], queries = [1,5]
<b>输出：</b>[14,10]
<b>解释：</b>第一个查询，我们可以执行以下操作：
- 将 nums[0] 减小 2 次，nums = [1,1,6,8] 。
- 将 nums[2] 减小 5 次，nums = [1,1,1,8] 。
- 将 nums[3] 减小 7 次，nums = [1,1,1,1] 。
第一个查询的总操作次数为 2 + 5 + 7 = 14 。
第二个查询，我们可以执行以下操作：
- 将 nums[0] 增大 2 次，nums = [5,1,6,8] 。
- 将 nums[1] 增大 4 次，nums = [5,5,6,8] 。
- 将 nums[2] 减小 1 次，nums = [5,5,5,8] 。
- 将 nums[3] 减小 3 次，nums = [5,5,5,5] 。
第二个查询的总操作次数为 2 + 4 + 1 + 3 = 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,9,6,3], queries = [10]
<b>输出：</b>[20]
<b>解释：</b>我们可以将数组中所有元素都增大到 10 ，总操作次数为 8 + 1 + 4 + 7 = 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和
- 排序

## 提示

1. For each query, you should decrease all elements greater than queries[i] and increase all elements less than queries[i].
2. The answer is the sum of absolute differences between queries[i] and every element of the array. How do you calculate that optimally?

## 示例

```
[3,1,6,8]
[1,5]
[2,9,6,3]
[10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Long> minOperations(int[] nums, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* minOperations(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<long> MinOperations(int[] nums, int[] queries) {
        
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
var minOperations = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[], queries: number[]): number[] {
    
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
    function minOperations($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, queries: IntArray): List<Long> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minOperations(List<int> nums, List<int> queries) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int, queries []int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def min_operations(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], queries: Array[Int]): List[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
min_operations(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], queries :: [integer]) :: [integer]
  def min_operations(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: Array<Int64>, queries: Array<Int64>): ArrayList<Int64> {

    }
}
```

