# 2389. 和有限的最长子序列

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组 <code>nums</code> ，和一个长度为 <code>m</code> 的整数数组 <code>queries</code> 。</p>

<p>返回一个长度为 <code>m</code> 的数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer[i]</code><em> </em>是 <code>nums</code> 中<span style=""> </span>元素之和小于等于 <code>queries[i]</code> 的 <strong>子序列</strong> 的 <strong>最大</strong> 长度<span style="">&nbsp;</span><span style=""> </span>。</p>

<p><strong>子序列</strong> 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,2,1], queries = [3,10,21]
<strong>输出：</strong>[2,3,4]
<strong>解释：</strong>queries 对应的 answer 如下：
- 子序列 [2,1] 的和小于或等于 3 。可以证明满足题目要求的子序列的最大长度是 2 ，所以 answer[0] = 2 。
- 子序列 [4,5,1] 的和小于或等于 10 。可以证明满足题目要求的子序列的最大长度是 3 ，所以 answer[1] = 3 。
- 子序列 [4,5,2,1] 的和小于或等于 21 。可以证明满足题目要求的子序列的最大长度是 4 ，所以 answer[2] = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,4,5], queries = [1]
<strong>输出：</strong>[0]
<strong>解释：</strong>空子序列是唯一一个满足元素和小于或等于 1 的子序列，所以 answer[0] = 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 二分查找
- 前缀和
- 排序

## 提示

1. Solve each query independently.
2. When solving a query, which elements of nums should you choose to make the subsequence as long as possible?
3. Choose the smallest elements in nums that add up to a sum less than the query.

## 示例

```
[4,5,2,1]
[3,10,21]
[2,3,4,5]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* answerQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AnswerQueries(int[] nums, int[] queries) {
        
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
var answerQueries = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function answerQueries(nums: number[], queries: number[]): number[] {
    
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
    function answerQueries($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func answerQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun answerQueries(nums: IntArray, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> answerQueries(List<int> nums, List<int> queries) {
    
  }
}
```

### Go

```golang
func answerQueries(nums []int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def answer_queries(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def answerQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn answer_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (answer-queries nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec answer_queries(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
answer_queries(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec answer_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def answer_queries(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func answerQueries(nums: Array<Int64>, queries: Array<Int64>): Array<Int64> {

    }
}
```

