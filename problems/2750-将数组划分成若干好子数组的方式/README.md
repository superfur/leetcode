# 2750. 将数组划分成若干好子数组的方式

## 题目描述

<p>给你一个二元数组 <code>nums</code> 。</p>

<p>如果数组中的某个子数组 <strong>恰好</strong> 只存在 <strong>一</strong> 个值为 <code>1</code> 的元素，则认为该子数组是一个 <strong>好子数组</strong> 。</p>

<p>请你统计将数组 <code>nums</code> 划分成若干 <strong>好子数组</strong> 的方法数，并以整数形式返回。由于数字可能很大，返回其对 <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>之后的结果。</p>

<p>子数组是数组中的一个连续 <strong>非空</strong> 元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,0,0,1]
<strong>输出：</strong>3
<strong>解释：</strong>存在 3 种可以将 nums 划分成若干好子数组的方式：
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,0]
<strong>输出：</strong>1
<strong>解释：</strong>存在 1 种可以将 nums 划分成若干好子数组的方式：
- [0,1,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划

## 提示

1. If the array consists of only 0s answer is 0.
2. In the final split, exactly one separation point exists between two consecutive 1s.
3. In how many ways can separation points be put?

## 示例

```
[0,1,0,0,1]
[0,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfGoodSubarraySplits(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfGoodSubarraySplits(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
```

### C

```c
int numberOfGoodSubarraySplits(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfGoodSubarraySplits(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubarraySplits = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfGoodSubarraySplits(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodSubarraySplits($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfGoodSubarraySplits(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfGoodSubarraySplits(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfGoodSubarraySplits(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfGoodSubarraySplits(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def number_of_good_subarray_splits(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfGoodSubarraySplits(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_good_subarray_splits(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-good-subarray-splits nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_good_subarray_splits(Nums :: [integer()]) -> integer().
number_of_good_subarray_splits(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_good_subarray_splits(nums :: [integer]) :: integer
  def number_of_good_subarray_splits(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfGoodSubarraySplits(nums: Array<Int64>): Int64 {

    }
}
```

