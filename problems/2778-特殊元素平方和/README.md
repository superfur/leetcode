# 2778. 特殊元素平方和

## 题目描述

<p>给你一个下标从 <strong>1</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> 。</p>

<p>对 <code>nums</code> 中的元素 <code>nums[i]</code> 而言，如果 <code>n</code> 能够被 <code>i</code> 整除，即 <code>n % i == 0</code> ，则认为 <code>num[i]</code> 是一个 <strong>特殊元素</strong> 。</p>

<p>返回 <code>nums</code> 中所有 <strong>特殊元素</strong> 的 <strong>平方和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>21
<strong>解释：</strong>nums 中共有 3 个特殊元素：nums[1]，因为 4 被 1 整除；nums[2]，因为 4 被 2 整除；以及 nums[4]，因为 4 被 4 整除。 
因此，nums 中所有特殊元素的平方和等于 nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21 。  
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,1,19,18,3]
<strong>输出：</strong>63
<strong>解释：</strong>nums 中共有 4 个特殊元素：nums[1]，因为 6 被 1 整除；nums[2] ，因为 6 被 2 整除；nums[3]，因为 6 被 3 整除；以及 nums[6]，因为 6 被 6 整除。 
因此，nums 中所有特殊元素的平方和等于 nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63 。 </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. Iterate over all the elements of the array. For each index i, check if it is special using the modulo operator.
2. if n%i == 0, index i is special and you should add nums[i] to the answer.

## 示例

```
[1,2,3,4]
[2,7,1,19,18,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfSquares(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
```

### C

```c
int sumOfSquares(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfSquares(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {
    
};
```

### TypeScript

```typescript
function sumOfSquares(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfSquares($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfSquares(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfSquares(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfSquares(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumOfSquares(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_of_squares(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumOfSquares(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-squares nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_squares(Nums :: [integer()]) -> integer().
sum_of_squares(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_squares(nums :: [integer]) :: integer
  def sum_of_squares(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfSquares(nums: Array<Int64>): Int64 {

    }
}
```

