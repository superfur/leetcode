# 3350. 检测相邻递增子数组 II

## 题目描述

<p>给你一个由 <code>n</code> 个整数组成的数组 <code>nums</code> ，请你找出 <code>k</code> 的 <strong>最大值</strong>，使得存在 <strong>两个</strong> <strong>相邻</strong> 且长度为 <code>k</code> 的 <strong>严格递增</strong> <span data-keyword="subarray-nonempty">子数组</span>。具体来说，需要检查是否存在从下标 <code>a</code> 和 <code>b</code> (<code>a &lt; b</code>) 开始的 <strong>两个</strong> 子数组，并满足下述全部条件：</p>

<ul>
	<li>这两个子数组 <code>nums[a..a + k - 1]</code> 和 <code>nums[b..b + k - 1]</code> 都是 <strong>严格递增</strong> 的。</li>
	<li>这两个子数组必须是 <strong>相邻的</strong>，即 <code>b = a + k</code>。</li>
</ul>

<p>返回 <code>k</code> 的 <strong>最大可能 </strong>值。</p>

<p><strong>子数组</strong> 是数组中的一个连续<b> 非空</b> 的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,5,7,8,9,2,3,4,3,1]</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从下标 2 开始的子数组是 <code>[7, 8, 9]</code>，它是严格递增的。</li>
	<li>从下标 5 开始的子数组是 <code>[2, 3, 4]</code>，它也是严格递增的。</li>
	<li>这两个子数组是相邻的，因此 3 是满足题目条件的 <strong>最大</strong> <code>k</code> 值。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,2,3,4,4,4,4,5,6,7]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从下标 0 开始的子数组是 <code>[1, 2]</code>，它是严格递增的。</li>
	<li>从下标 2 开始的子数组是 <code>[3, 4]</code>，它也是严格递增的。</li>
	<li>这两个子数组是相邻的，因此 2 是满足题目条件的 <strong>最大</strong> <code>k</code> 值。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Find the boundaries between strictly increasing subarrays.
2. Can we use binary search?

## 示例

```
[2,5,7,8,9,2,3,4,3,1]
[1,2,3,4,4,4,4,5,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
int maxIncreasingSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxIncreasingSubarrays(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxIncreasingSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function maxIncreasingSubarrays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxIncreasingSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxIncreasingSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxIncreasingSubarrays(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxIncreasingSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxIncreasingSubarrays(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_increasing_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxIncreasingSubarrays(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-increasing-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_increasing_subarrays(Nums :: [integer()]) -> integer().
max_increasing_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_increasing_subarrays(nums :: [integer]) :: integer
  def max_increasing_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxIncreasingSubarrays(nums: ArrayList<Int64>): Int64 {

    }
}
```

