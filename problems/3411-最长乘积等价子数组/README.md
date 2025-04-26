# 3411. 最长乘积等价子数组

## 题目描述

<p>给你一个由&nbsp;<strong>正整数&nbsp;</strong>组成的数组 <code>nums</code>。</p>

<p>如果一个数组 <code>arr</code> 满足 <code>prod(arr) == lcm(arr) * gcd(arr)</code>，则称其为&nbsp;<strong>乘积等价数组&nbsp;</strong>，其中：</p>

<ul>
	<li><code>prod(arr)</code> 表示 <code>arr</code> 中所有元素的乘积。</li>
	<li><code>gcd(arr)</code> 表示 <code>arr</code> 中所有元素的最大公因数 (<span data-keyword="gcd-function">GCD</span>)。</li>
	<li><code>lcm(arr)</code> 表示 <code>arr</code> 中所有元素的最小公倍数 (<span data-keyword="lcm-function">LCM</span>)。</li>
</ul>

<p>返回数组 <code>nums</code> 的&nbsp;<strong>最长</strong> <strong>乘积等价 <span data-keyword="subarray-nonempty">子数组</span>&nbsp;</strong>的长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,2,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[1, 2, 1, 1, 1]</code>，其中&nbsp;<code>prod([1, 2, 1, 1, 1]) = 2</code>，&nbsp;<code>gcd([1, 2, 1, 1, 1]) = 1</code>，以及&nbsp;<code>lcm([1, 2, 1, 1, 1]) = 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,4,5,6]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong>&nbsp;</p>

<p>最长的乘积等价子数组是 <code>[3, 4, 5]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,1,4,5,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 枚举
- 数论
- 滑动窗口

## 提示

1. What is the maximum possible lcm?

## 示例

```
[1,2,1,2,1,1,1]
[2,3,4,5,6]
[1,2,3,1,4,5,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
```

### C

```c
int maxLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    
};
```

### TypeScript

```typescript
function maxLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_length(Nums :: [integer()]) -> integer().
max_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_length(nums :: [integer]) :: integer
  def max_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxLength(nums: Array<Int64>): Int64 {

    }
}
```

