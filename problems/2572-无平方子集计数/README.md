# 2572. 无平方子集计数

## 题目描述

<p>给你一个正整数数组 <code>nums</code> 。</p>

<p>如果数组 <code>nums</code> 的子集中的元素乘积是一个 <strong>无平方因子数</strong> ，则认为该子集是一个 <strong>无平方</strong> 子集。</p>

<p><strong>无平方因子数</strong> 是无法被除 <code>1</code> 之外任何平方数整除的数字。</p>

<p>返回数组 <code>nums</code> 中 <strong>无平方</strong> 且 <strong>非空</strong> 的子集数目。因为答案可能很大，返回对 <code>10<sup>9</sup> + 7</code> 取余的结果。</p>

<p><code>nums</code> 的 <strong>非空子集</strong> 是可以由删除 <code>nums</code> 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,4,5]
<strong>输出：</strong>3
<strong>解释：</strong>示例中有 3 个无平方子集：
- 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
- 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
- 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 3 个无平方子集。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>1
<strong>解释：</strong>示例中有 1 个无平方子集：
- 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 1 个无平方子集。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 30</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学
- 动态规划
- 状态压缩

## 提示

1. There are 10 primes before number 30.
2. Label primes from {2, 3, … 29} with {0,1, … 9} and let DP(i, mask) denote the number of subsets before index: i with the subset of taken primes: mask.
3. If the mask and prime factorization of nums[i] have a common prime, then it is impossible to add to the current subset, otherwise, it is possible.

## 示例

```
[3,4,4,5]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int squareFreeSubsets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int squareFreeSubsets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def squareFreeSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        
```

### C

```c
int squareFreeSubsets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SquareFreeSubsets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var squareFreeSubsets = function(nums) {
    
};
```

### TypeScript

```typescript
function squareFreeSubsets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function squareFreeSubsets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func squareFreeSubsets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun squareFreeSubsets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int squareFreeSubsets(List<int> nums) {
    
  }
}
```

### Go

```golang
func squareFreeSubsets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def square_free_subsets(nums)
    
end
```

### Scala

```scala
object Solution {
    def squareFreeSubsets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn square_free_subsets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (square-free-subsets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec square_free_subsets(Nums :: [integer()]) -> integer().
square_free_subsets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec square_free_subsets(nums :: [integer]) :: integer
  def square_free_subsets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func squareFreeSubsets(nums: Array<Int64>): Int64 {

    }
}
```

