# 3115. 质数的最大距离

## 题目描述

<p>给你一个整数数组 <code>nums</code>。</p>

<p>返回两个（不一定不同的）质数在 <code>nums</code> 中&nbsp;<strong>下标</strong> 的 <strong>最大距离</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,2,9,5,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong> <code>nums[1]</code>、<code>nums[3]</code> 和 <code>nums[4]</code> 是质数。因此答案是 <code>|4 - 1| = 3</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,8,2,8]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong> <code>nums[2]</code> 是质数。因为只有一个质数，所以答案是 <code>|2 - 2| = 0</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li>输入保证 <code>nums</code> 中至少有一个质数。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. Find all prime numbers in the <code>nums</code>.
2. Find the first and the last prime number in the <code>nums</code>.

## 示例

```
[4,2,9,5,3]
[4,8,2,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumPrimeDifference(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumPrimeDifference(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumPrimeDifference(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumPrimeDifference(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumPrimeDifference = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumPrimeDifference(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumPrimeDifference($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumPrimeDifference(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumPrimeDifference(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumPrimeDifference(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumPrimeDifference(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_prime_difference(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumPrimeDifference(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-prime-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_prime_difference(Nums :: [integer()]) -> integer().
maximum_prime_difference(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_prime_difference(nums :: [integer]) :: integer
  def maximum_prime_difference(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumPrimeDifference(nums: Array<Int64>): Int64 {

    }
}
```

