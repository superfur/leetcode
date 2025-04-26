# 1822. 数组元素积的符号

## 题目描述

<p>已知函数 <code>signFunc(x)</code> 将会根据 <code>x</code> 的正负返回特定值：</p>

<ul>
	<li>如果 <code>x</code> 是正数，返回 <code>1</code> 。</li>
	<li>如果 <code>x</code> 是负数，返回 <code>-1</code> 。</li>
	<li>如果 <code>x</code> 是等于 <code>0</code> ，返回 <code>0</code> 。</li>
</ul>

<p>给你一个整数数组 <code>nums</code> 。令 <code>product</code> 为数组 <code>nums</code> 中所有元素值的乘积。</p>

<p>返回 <code>signFunc(product)</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,-2,-3,-4,3,2,1]
<strong>输出：</strong>1
<strong>解释：</strong>数组中所有值的乘积是 144 ，且 signFunc(144) = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,0,2,-3]
<strong>输出：</strong>0
<strong>解释：</strong>数组中所有值的乘积是 0 ，且 signFunc(0) = 0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,1,-1,1,-1]
<strong>输出：</strong>-1
<strong>解释：</strong>数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>-100 <= nums[i] <= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. If there is a 0 in the array the answer is 0
2. To avoid overflow make all the negative numbers -1 and all positive numbers 1 and calculate the prod

## 示例

```
[-1,-2,-3,-4,3,2,1]
[1,5,0,2,-3]
[-1,1,-1,1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int arraySign(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int arraySign(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
```

### C

```c
int arraySign(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ArraySign(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    
};
```

### TypeScript

```typescript
function arraySign(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arraySign($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arraySign(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arraySign(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int arraySign(List<int> nums) {
    
  }
}
```

### Go

```golang
func arraySign(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def array_sign(nums)
    
end
```

### Scala

```scala
object Solution {
    def arraySign(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (array-sign nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec array_sign(Nums :: [integer()]) -> integer().
array_sign(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec array_sign(nums :: [integer]) :: integer
  def array_sign(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arraySign(nums: Array<Int64>): Int64 {

    }
}
```

