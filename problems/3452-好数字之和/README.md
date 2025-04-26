# 3452. 好数字之和

## 题目描述

<p>给定一个整数数组 <code>nums</code> 和一个整数 <code>k</code>，如果元素 <code>nums[i]</code> <strong>严格</strong> 大于下标&nbsp;<code>i - k</code> 和 <code>i + k</code> 处的元素（如果这些元素存在），则该元素 <code>nums[i]</code> 被认为是 <strong>好</strong> 的。如果这两个下标至少一个不存在，那么 <code>nums[i]</code> 仍然被认为是 <strong>好</strong> 的。</p>

<p>返回数组中所有 <strong>好</strong> 元素的 <strong>和</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3,2,1,5,4], k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p>好的数字包括&nbsp;<code>nums[1] = 3</code>，<code>nums[4] = 5</code> 和 <code>nums[5] = 4</code>，因为它们严格大于下标&nbsp;<code>i - k</code> 和 <code>i + k</code> 处的数字。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,1], k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>唯一的好数字是 <code>nums[0] = 2</code>，因为它严格大于 <code>nums[1]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= floor(nums.length / 2)</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. For each index, check if <code>nums[i]</code> is strictly greater than <code>nums[i - k]</code> and <code>nums[i + k]</code>.

## 示例

```
[1,3,2,1,5,4]
2
[2,1]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int sumOfGoodNumbers(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfGoodNumbers(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var sumOfGoodNumbers = function(nums, k) {
    
};
```

### TypeScript

```typescript
function sumOfGoodNumbers(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function sumOfGoodNumbers($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfGoodNumbers(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfGoodNumbers(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfGoodNumbers(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func sumOfGoodNumbers(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_good_numbers(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def sumOfGoodNumbers(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_good_numbers(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-good-numbers nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_good_numbers(Nums :: [integer()], K :: integer()) -> integer().
sum_of_good_numbers(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_good_numbers(nums :: [integer], k :: integer) :: integer
  def sum_of_good_numbers(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfGoodNumbers(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

