# 3105. 最长的严格递增或递减子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。</p>

<p>返回数组 <code>nums</code> 中 <strong><span data-keyword="strictly-increasing-array">严格递增</span></strong> 或 <strong><span data-keyword="strictly-decreasing-array">严格递减</span> </strong>的最长非空子数组的长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,4,3,3,2]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code> 中严格递增的子数组有<code>[1]</code>、<code>[2]</code>、<code>[3]</code>、<code>[3]</code>、<code>[4]</code> 以及 <code>[1,4]</code> 。</p>

<p><code>nums</code> 中严格递减的子数组有<code>[1]</code>、<code>[2]</code>、<code>[3]</code>、<code>[3]</code>、<code>[4]</code>、<code>[3,2]</code> 以及 <code>[4,3]</code> 。</p>

<p>因此，返回 <code>2</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [3,3,3,3]</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code> 中严格递增的子数组有 <code>[3]</code>、<code>[3]</code>、<code>[3]</code> 以及 <code>[3]</code> 。</p>

<p><code>nums</code> 中严格递减的子数组有 <code>[3]</code>、<code>[3]</code>、<code>[3]</code> 以及 <code>[3]</code> 。</p>

<p>因此，返回 <code>1</code> 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [3,2,1]</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code> 中严格递增的子数组有 <code>[3]</code>、<code>[2]</code> 以及 <code>[1]</code> 。</p>

<p><code>nums</code> 中严格递减的子数组有 <code>[3]</code>、<code>[2]</code>、<code>[1]</code>、<code>[3,2]</code>、<code>[2,1]</code> 以及 <code>[3,2,1]</code> 。</p>

<p>因此，返回 <code>3</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 示例

```
[1,4,3,3,2]
[3,3,3,3]
[3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int longestMonotonicSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestMonotonicSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function longestMonotonicSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestMonotonicSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestMonotonicSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestMonotonicSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestMonotonicSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_monotonic_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestMonotonicSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-monotonic-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_monotonic_subarray(Nums :: [integer()]) -> integer().
longest_monotonic_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_monotonic_subarray(nums :: [integer]) :: integer
  def longest_monotonic_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestMonotonicSubarray(nums: Array<Int64>): Int64 {

    }
}
```

