# 1498. 满足条件的子序列数目

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>请你统计并返回 <code>nums</code> 中能满足其最小元素与最大元素的 <strong>和</strong> 小于或等于 <code>target</code> 的 <strong>非空</strong> 子序列的数目。</p>

<p>由于答案可能很大，请将结果对<meta charset="UTF-8" />&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code>&nbsp;取余后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,5,6,7], target = 9
<strong>输出：</strong>4
<strong>解释：</strong>有 4 个子序列满足该条件。
[3] -&gt; 最小元素 + 最大元素 &lt;= target (3 + 3 &lt;= 9)
[3,5] -&gt; (3 + 5 &lt;= 9)
[3,5,6] -&gt; (3 + 6 &lt;= 9)
[3,6] -&gt; (3 + 6 &lt;= 9)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3,6,8], target = 10
<strong>输出：</strong>6
<strong>解释：</strong>有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,3,4,6,7], target = 12
<strong>输出：</strong>61
<strong>解释：</strong>共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Sort the array nums.
2. Use two pointers approach: Given an index i (choose it as the minimum in a subsequence) find the maximum j where j ≥ i and nums[i] +nums[j] ≤ target.
3. Count the number of subsequences.

## 示例

```
[3,5,6,7]
9
[3,3,6,8]
10
[2,3,3,4,6,7]
12
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSubseq(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int numSubseq(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSubseq(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {
    
};
```

### TypeScript

```typescript
function numSubseq(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function numSubseq($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSubseq(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubseq(nums: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSubseq(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func numSubseq(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def num_subseq(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def numSubseq(nums: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_subseq(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-subseq nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_subseq(Nums :: [integer()], Target :: integer()) -> integer().
num_subseq(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_subseq(nums :: [integer], target :: integer) :: integer
  def num_subseq(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSubseq(nums: Array<Int64>, target: Int64): Int64 {

    }
}
```

