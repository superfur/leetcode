# 446. 等差数列划分 II - 子序列

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，返回 <code>nums</code> 中所有 <strong>等差子序列</strong> 的数目。</p>

<p>如果一个序列中 <strong>至少有三个元素</strong> ，并且任意两个相邻元素之差相同，则称该序列为等差序列。</p>

<ul>
	<li>例如，<code>[1, 3, 5, 7, 9]</code>、<code>[7, 7, 7, 7]</code> 和 <code>[3, -1, -5, -9]</code> 都是等差序列。</li>
	<li>再例如，<code>[1, 1, 2, 5, 7]</code> 不是等差序列。</li>
</ul>

<p>数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。</p>

<ul>
	<li>例如，<code>[2,5,10]</code> 是 <code>[1,2,1,<em><strong>2</strong></em>,4,1,<strong><em>5</em></strong>,<em><strong>10</strong></em>]</code> 的一个子序列。</li>
</ul>

<p>题目数据保证答案是一个 <strong>32-bit</strong> 整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,6,8,10]
<strong>输出：</strong>7
<strong>解释：</strong>所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,7,7,7,7]
<strong>输出：</strong>16
<strong>解释：</strong>数组中的任意子序列都是等差子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1&nbsp; &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
[2,4,6,8,10]
[7,7,7,7,7]
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

