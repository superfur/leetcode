# 2455. 可被三整除的偶数的平均值

## 题目描述

<p>给你一个由正整数组成的整数数组 <code>nums</code> ，返回其中可被 <code>3</code> 整除的所有偶数的平均值。</p>

<p>注意：<code>n</code> 个元素的平均值等于 <code>n</code> 个元素 <strong>求和</strong> 再除以 <code>n</code> ，结果 <strong>向下取整</strong> 到最接近的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,6,10,12,15]
<strong>输出：</strong>9
<strong>解释：</strong>6 和 12 是可以被 3 整除的偶数。(6 + 12) / 2 = 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,7,10]
<strong>输出：</strong>0
<strong>解释：</strong>不存在满足题目要求的整数，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. What is the property of a number if it is divisible by both 2 and 3 at the same time?
2. It is equivalent to finding all the numbers that are divisible by 6.

## 示例

```
[1,3,6,10,12,15]
[1,2,4,7,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int averageValue(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int averageValue(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
```

### C

```c
int averageValue(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int AverageValue(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    
};
```

### TypeScript

```typescript
function averageValue(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function averageValue($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func averageValue(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun averageValue(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int averageValue(List<int> nums) {
    
  }
}
```

### Go

```golang
func averageValue(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def average_value(nums)
    
end
```

### Scala

```scala
object Solution {
    def averageValue(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn average_value(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (average-value nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec average_value(Nums :: [integer()]) -> integer().
average_value(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec average_value(nums :: [integer]) :: integer
  def average_value(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func averageValue(nums: Array<Int64>): Int64 {

    }
}
```

