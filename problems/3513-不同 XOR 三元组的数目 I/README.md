# 3513. 不同 XOR 三元组的数目 I

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>，其中 <code>nums</code> 是范围 <code>[1, n]</code> 内所有数的&nbsp;<strong>排列&nbsp;</strong>。</p>

<p><strong>XOR 三元组</strong> 定义为三个元素的异或值 <code>nums[i] XOR nums[j] XOR nums[k]</code>，其中 <code>i &lt;= j &lt;= k</code>。</p>

<p>返回所有可能三元组 <code>(i, j, k)</code> 中&nbsp;<strong>不同&nbsp;</strong>的 XOR 值的数量。</p>

<p><strong>排列</strong> 是一个集合中所有元素的重新排列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>所有可能的 XOR 三元组值为：</p>

<ul>
	<li><code>(0, 0, 0) → 1 XOR 1 XOR 1 = 1</code></li>
	<li><code>(0, 0, 1) → 1 XOR 1 XOR 2 = 2</code></li>
	<li><code>(0, 1, 1) → 1 XOR 2 XOR 2 = 1</code></li>
	<li><code>(1, 1, 1) → 2 XOR 2 XOR 2 = 2</code></li>
</ul>

<p>不同的 XOR 值为 <code>{1, 2}</code>，因此输出为 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>可能的 XOR 三元组值包括：</p>

<ul>
	<li><code>(0, 0, 0) → 3 XOR 3 XOR 3 = 3</code></li>
	<li><code>(0, 0, 1) → 3 XOR 3 XOR 1 = 1</code></li>
	<li><code>(0, 0, 2) → 3 XOR 3 XOR 2 = 2</code></li>
	<li><code>(0, 1, 2) → 3 XOR 1 XOR 2 = 0</code></li>
</ul>

<p>不同的 XOR 值为 <code>{0, 1, 2, 3}</code>，因此输出为 4。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 是从 <code>1</code> 到 <code>n</code> 的整数的一个排列。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学

## 提示

1. What is the maximum and minimum value we can obtain using the given numbers?
2. Can we generate all numbers within that range?
3. For <code>n >= 3</code> we can obtain all numbers in <code>[0, 2^(msb(n) + 1) - 1]</code>, where <code>msb(n)</code> is the index of the most significant bit in <code>n</code>’s binary representation (i.e., the highest power of 2 less than or equal to <code>n</code>). Handle the case when <code>n <= 2</code> separately.

## 示例

```
[1,2]
[3,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
```

### C

```c
int uniqueXorTriplets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var uniqueXorTriplets = function(nums) {
    
};
```

### TypeScript

```typescript
function uniqueXorTriplets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function uniqueXorTriplets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int uniqueXorTriplets(List<int> nums) {
    
  }
}
```

### Go

```golang
func uniqueXorTriplets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
    
end
```

### Scala

```scala
object Solution {
    def uniqueXorTriplets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unique-xor-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec unique_xor_triplets(Nums :: [integer()]) -> integer().
unique_xor_triplets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_xor_triplets(nums :: [integer]) :: integer
  def unique_xor_triplets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniqueXorTriplets(nums: Array<Int64>): Int64 {

    }
}
```

