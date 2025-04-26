# 1695. 删除子数组的最大得分

## 题目描述

<p>给你一个正整数数组 <code>nums</code> ，请你从中删除一个含有 <strong>若干不同元素</strong> 的子数组<strong>。</strong>删除子数组的 <strong>得分</strong> 就是子数组各元素之 <strong>和</strong> 。</p>

<p>返回 <strong>只删除一个</strong> 子数组可获得的 <strong>最大得分</strong><em> 。</em></p>

<p>如果数组 <code>b</code> 是数组 <code>a</code> 的一个连续子序列，即如果它等于 <code>a[l],a[l+1],...,a[r]</code> ，那么它就是 <code>a</code> 的一个子数组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,4,5,6]
<strong>输出：</strong>17
<strong>解释：</strong>最优子数组是 [2,4,5,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,2,1,2,5,2,1,2,5]
<strong>输出：</strong>8
<strong>解释：</strong>最优子数组是 [5,2,1] 或 [1,2,5]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. The main point here is for the subarray to contain unique elements for each index. Only the first subarrays starting from that index have unique elements.
2. This can be solved using the two pointers technique

## 示例

```
[4,2,4,5,6]
[5,2,1,2,5,2,1,2,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumUniqueSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumUniqueSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumUniqueSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumUniqueSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumUniqueSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumUniqueSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumUniqueSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumUniqueSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_unique_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumUniqueSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-unique-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_unique_subarray(Nums :: [integer()]) -> integer().
maximum_unique_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_unique_subarray(nums :: [integer]) :: integer
  def maximum_unique_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumUniqueSubarray(nums: Array<Int64>): Int64 {

    }
}
```

