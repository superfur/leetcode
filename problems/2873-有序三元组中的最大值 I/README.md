# 2873. 有序三元组中的最大值 I

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。</p>

<p>请你从所有满足&nbsp;<code>i &lt; j &lt; k</code> 的下标三元组 <code>(i, j, k)</code> 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 <code>0</code> 。</p>

<p><strong>下标三元组</strong> <code>(i, j, k)</code> 的值等于 <code>(nums[i] - nums[j]) * nums[k]</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [12,6,1,2,7]
<strong>输出：</strong>77
<strong>解释：</strong>下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。
可以证明不存在值大于 77 的有序下标三元组。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,10,3,4,19]
<strong>输出：</strong>133
<strong>解释：</strong>下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。
可以证明不存在值大于 133 的有序下标三元组。 
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>0
<strong>解释：</strong>唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Use three nested loops to find all the triplets.

## 示例

```
[12,6,1,2,7]
[1,10,3,4,19]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumTripletValue(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
```

### C

```c
long long maximumTripletValue(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumTripletValue(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumTripletValue(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumTripletValue($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTripletValue(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTripletValue(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumTripletValue(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumTripletValue(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-triplet-value nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_triplet_value(Nums :: [integer()]) -> integer().
maximum_triplet_value(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_triplet_value(nums :: [integer]) :: integer
  def maximum_triplet_value(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTripletValue(nums: Array<Int64>): Int64 {

    }
}
```

