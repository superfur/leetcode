# 1800. 最大升序子数组和

## 题目描述

<p>给你一个正整数组成的数组 <code>nums</code> ，返回 <code>nums</code> 中一个 <span data-keyword="strictly-increasing-array">严格递增子数组</span> 的最大可能元素和。</p>

<p>子数组是数组中的一个连续数字序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,20,30,5,10,50]
<strong>输出：</strong>65
<strong>解释：</strong>[5,10,50] 是元素和最大的升序子数组，最大元素和为 65 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,20,30,40,50]
<strong>输出：</strong>150
<strong>解释：</strong>[10,20,30,40,50] 是元素和最大的升序子数组，最大元素和为 150 。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [12,17,15,13,10,11,12]
<strong>输出：</strong>33
<strong>解释：</strong>[10,11,12] 是元素和最大的升序子数组，最大元素和为 33 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. It is fast enough to check all possible subarrays
2. The end of each ascending subarray will be the start of the next

## 示例

```
[10,20,30,5,10,50]
[10,20,30,40,50]
[12,17,15,13,10,11,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxAscendingSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
```

### C

```c
int maxAscendingSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxAscendingSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxAscendingSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAscendingSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAscendingSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAscendingSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAscendingSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxAscendingSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_ascending_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxAscendingSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-ascending-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_ascending_sum(Nums :: [integer()]) -> integer().
max_ascending_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_ascending_sum(nums :: [integer]) :: integer
  def max_ascending_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAscendingSum(nums: Array<Int64>): Int64 {

    }
}
```

