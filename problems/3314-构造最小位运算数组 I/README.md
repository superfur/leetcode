# 3314. 构造最小位运算数组 I

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的<span data-keyword="prime">质数</span>数组&nbsp;<code>nums</code>&nbsp;。你的任务是返回一个长度为 <code>n</code>&nbsp;的数组 <code>ans</code>&nbsp;，对于每个下标 <code>i</code>&nbsp;，以下<strong>&nbsp;条件</strong>&nbsp;均成立：</p>

<ul>
	<li><code>ans[i] OR (ans[i] + 1) == nums[i]</code></li>
</ul>

<p>除此以外，你需要 <strong>最小化</strong>&nbsp;结果数组里每一个&nbsp;<code>ans[i]</code>&nbsp;。</p>

<p>如果没法找到符合 <strong>条件</strong>&nbsp;的&nbsp;<code>ans[i]</code>&nbsp;，那么&nbsp;<code>ans[i] = -1</code>&nbsp;。</p>

<p><strong>质数</strong>&nbsp;指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,3,5,7]</span></p>

<p><span class="example-io"><b>输出：</b>[-1,1,4,3]</span></p>

<p><b>解释：</b></p>

<ul>
	<li>对于&nbsp;<code>i = 0</code>&nbsp;，不存在&nbsp;<code>ans[0]</code>&nbsp;满足&nbsp;<code>ans[0] OR (ans[0] + 1) = 2</code>&nbsp;，所以&nbsp;<code>ans[0] = -1</code>&nbsp;。</li>
	<li>对于&nbsp;<code>i = 1</code>&nbsp;，满足 <code>ans[1] OR (ans[1] + 1) = 3</code>&nbsp;的最小&nbsp;<code>ans[1]</code>&nbsp;为&nbsp;<code>1</code>&nbsp;，因为&nbsp;<code>1 OR (1 + 1) = 3</code>&nbsp;。</li>
	<li>对于&nbsp;<code>i = 2</code>&nbsp;，满足 <code>ans[2] OR (ans[2] + 1) = 5</code>&nbsp;的最小 <code>ans[2]</code>&nbsp;为&nbsp;<code>4</code>&nbsp;，因为&nbsp;<code>4 OR (4 + 1) = 5</code>&nbsp;。</li>
	<li>对于&nbsp;<code>i = 3</code>&nbsp;，满足&nbsp;<code>ans[3] OR (ans[3] + 1) = 7</code>&nbsp;的最小&nbsp;<code>ans[3]</code>&nbsp;为&nbsp;<code>3</code>&nbsp;，因为&nbsp;<code>3 OR (3 + 1) = 7</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [11,13,31]</span></p>

<p><span class="example-io"><b>输出：</b>[9,12,15]</span></p>

<p><b>解释：</b></p>

<ul>
	<li>对于&nbsp;<code>i = 0</code>&nbsp;，满足&nbsp;<code>ans[0] OR (ans[0] + 1) = 11</code> 的最小&nbsp;<code>ans[0]</code>&nbsp;为&nbsp;<code>9</code>&nbsp;，因为&nbsp;<code>9 OR (9 + 1) = 11</code>&nbsp;。</li>
	<li>对于&nbsp;<code>i = 1</code>&nbsp;，满足&nbsp;<code>ans[1] OR (ans[1] + 1) = 13</code>&nbsp;的最小&nbsp;<code>ans[1]</code>&nbsp;为&nbsp;<code>12</code>&nbsp;，因为&nbsp;<code>12 OR (12 + 1) = 13</code>&nbsp;。</li>
	<li>对于&nbsp;<code>i = 2</code>&nbsp;，满足&nbsp;<code>ans[2] OR (ans[2] + 1) = 31</code>&nbsp;的最小&nbsp;<code>ans[2]</code>&nbsp;为&nbsp;<code>15</code>&nbsp;，因为&nbsp;<code>15 OR (15 + 1) = 31</code>&nbsp;。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i]</code>&nbsp;是一个质数。</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. The constraints are small, allowing you to iterate over all potential values for <code>ans[i]</code> directly.

## 示例

```
[2,3,5,7]
[11,13,31]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minBitwiseArray = function(nums) {
    
};
```

### TypeScript

```typescript
function minBitwiseArray(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function minBitwiseArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minBitwiseArray(nums: List<Int>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minBitwiseArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func minBitwiseArray(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minBitwiseArray(nums: ArrayList<Int64>): Array<Int64> {

    }
}
```

