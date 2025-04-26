# 413. 等差数列划分

## 题目描述

<p>如果一个数列 <strong>至少有三个元素</strong> ，并且任意两个相邻元素之差相同，则称该数列为等差数列。</p>

<ul>
	<li>例如，<code>[1,3,5,7,9]</code>、<code>[7,7,7,7]</code> 和 <code>[3,-1,-5,-9]</code> 都是等差数列。</li>
</ul>

<div class="original__bRMd">
<div>
<p>给你一个整数数组 <code>nums</code> ，返回数组 <code>nums</code> 中所有为等差数组的 <strong>子数组</strong> 个数。</p>

<p><strong>子数组</strong> 是数组中的一个连续序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>3
<strong>解释：</strong>nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 5000</code></li>
	<li><code>-1000 <= nums[i] <= 1000</code></li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 滑动窗口

## 示例

```
[1,2,3,4]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
```

### C

```c
int numberOfArithmeticSlices(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfArithmeticSlices(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfArithmeticSlices(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfArithmeticSlices($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfArithmeticSlices(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfArithmeticSlices(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfArithmeticSlices(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfArithmeticSlices(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def number_of_arithmetic_slices(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfArithmeticSlices(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-arithmetic-slices nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_arithmetic_slices(Nums :: [integer()]) -> integer().
number_of_arithmetic_slices(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_arithmetic_slices(nums :: [integer]) :: integer
  def number_of_arithmetic_slices(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfArithmeticSlices(nums: Array<Int64>): Int64 {

    }
}
```

