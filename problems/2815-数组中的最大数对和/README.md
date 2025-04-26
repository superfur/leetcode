# 2815. 数组中的最大数对和

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。请你从 <code>nums</code> 中找出和 <strong>最大</strong> 的一对数，且这两个数数位上最大的数字相等。</p>

<p>返回最大和，如果不存在满足题意的数字对，返回 <code>-1</code><em> 。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [51,71,17,24,42]
<strong>输出：</strong>88
<strong>解释：</strong>
i = 1 和 j = 2 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 71 + 17 = 88 。 
i = 3 和 j = 4 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 24 + 42 = 66 。
可以证明不存在其他数对满足数位上最大的数字相等，所以答案是 88 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>-1
<strong>解释：</strong>不存在数对满足数位上最大的数字相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Find the largest and second largest element with maximum digits equal to x where 1<=x<=9.

## 示例

```
[112,131,411]
[2536,1613,3366,162]
[51,71,17,24,42]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum(Nums :: [integer()]) -> integer().
max_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer]) :: integer
  def max_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSum(nums: Array<Int64>): Int64 {

    }
}
```

