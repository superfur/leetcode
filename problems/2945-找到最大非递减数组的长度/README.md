# 2945. 找到最大非递减数组的长度

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以执行任意次操作。每次操作中，你需要选择一个 <strong>子数组</strong>&nbsp;，并将这个子数组用它所包含元素的 <strong>和</strong>&nbsp;替换。比方说，给定数组是&nbsp;<code>[1,3,5,6]</code>&nbsp;，你可以选择子数组&nbsp;<code>[3,5]</code>&nbsp;，用子数组的和 <code>8</code>&nbsp;替换掉子数组，然后数组会变为&nbsp;<code>[1,8,6]</code>&nbsp;。</p>

<p>请你返回执行任意次操作以后，可以得到的 <strong>最长非递减</strong>&nbsp;数组的长度。</p>

<p><strong>子数组</strong>&nbsp;指的是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [5,2,2]
<b>输出：</b>1
<strong>解释：</strong>这个长度为 3 的数组不是非递减的。
我们有 2 种方案使数组长度为 2 。
第一种，选择子数组 [2,2] ，对数组执行操作后得到 [5,4] 。
第二种，选择子数组 [5,2] ，对数组执行操作后得到 [7,2] 。
这两种方案中，数组最后都不是 <strong>非递减</strong>&nbsp;的，所以不是可行的答案。
如果我们选择子数组 [5,2,2] ，并将它替换为 [9] ，数组变成非递减的。
所以答案为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>4
<b>解释：</b>数组已经是非递减的。所以答案为 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [4,3,2,6]
<b>输出：</b>3
<b>解释：</b>将 [3,2] 替换为 [5] ，得到数组 [4,5,6] ，它是非递减的。
最大可能的答案为 3 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 队列
- 数组
- 二分查找
- 动态规划
- 单调队列
- 单调栈

## 提示

1. Let <code>dp[i]</code> be the maximum number of elements in the increasing sequence after processing the first <code>i</code> elements of the original array.
2. We have <code>dp[0] = 0</code>. <code>dp[i + 1] >= dp[i]</code> (since if we have the solution for the first <code>i</code> elements, we can always merge the last one of the first <code>i + 1</code> elements which is <code>nums[i]</code> into the solution of the first <code>i</code> elements.
3. For <code>i > 0</code>, we want to <code>dp[i] = max(dp[j] + 1)</code> where <code>sum(nums[i - 1] + nums[i - 2] +… + nums[j]) >= v[j]</code> and <code>v[j]</code> is the last element of the solution ending with <code>nums[j - 1]</code>.

## 示例

```
[5,2,2]
[1,2,3,4]
[4,3,2,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaximumLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaximumLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        
```

### C

```c
int findMaximumLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaximumLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumLength = function(nums) {
    
};
```

### TypeScript

```typescript
function findMaximumLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaximumLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximumLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaximumLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMaximumLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_maximum_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMaximumLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximum_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_maximum_length(Nums :: [integer()]) -> integer().
find_maximum_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximum_length(nums :: [integer]) :: integer
  def find_maximum_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaximumLength(nums: Array<Int64>): Int64 {

    }
}
```

