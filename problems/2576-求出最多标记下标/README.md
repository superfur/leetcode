# 2576. 求出最多标记下标

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>一开始，所有下标都没有被标记。你可以执行以下操作任意次：</p>

<ul>
	<li>选择两个 <strong>互不相同且未标记</strong>&nbsp;的下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，满足&nbsp;<code>2 * nums[i] &lt;= nums[j]</code>&nbsp;，标记下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;。</li>
</ul>

<p>请你执行上述操作任意次，返回<em>&nbsp;</em><code>nums</code>&nbsp;中最多可以标记的下标数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,5,2,4]
<b>输出：</b>2
<strong>解释：</strong>第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] &lt;= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [9,2,5,4]
<b>输出：</b>4
<strong>解释：</strong>第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] &lt;= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] &lt;= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [7,6,8]
<b>输出：</b>0
<strong>解释：</strong>没有任何可以执行的操作，所以答案为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Think about how to check that performing k operations is possible.
2. To perform k operations, it’s optimal to use the smallest k elements and the largest k elements and think about how to match them.
3. It’s optimal to match the ith smallest number with the k-i + 1 largest number.
4. Now we need to binary search on the answer and find the greatest possible valid k.

## 示例

```
[3,5,2,4]
[9,2,5,4]
[7,6,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
```

### C

```c
int maxNumOfMarkedIndices(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNumOfMarkedIndices(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxNumOfMarkedIndices = function(nums) {
    
};
```

### TypeScript

```typescript
function maxNumOfMarkedIndices(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxNumOfMarkedIndices($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumOfMarkedIndices(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumOfMarkedIndices(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNumOfMarkedIndices(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxNumOfMarkedIndices(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_num_of_marked_indices(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxNumOfMarkedIndices(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_num_of_marked_indices(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-num-of-marked-indices nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_num_of_marked_indices(Nums :: [integer()]) -> integer().
max_num_of_marked_indices(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_num_of_marked_indices(nums :: [integer]) :: integer
  def max_num_of_marked_indices(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumOfMarkedIndices(nums: Array<Int64>): Int64 {

    }
}
```

