# 813. 最大平均值和的分组

## 题目描述

<p>给定数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。我们将给定的数组&nbsp;<code>nums</code>&nbsp;分成 <strong>最多</strong>&nbsp;<code>k</code>&nbsp;个非空子数组，且数组内部是连续的&nbsp;。&nbsp;<strong>分数</strong> 由每个子数组内的平均值的总和构成。</p>

<p>注意我们必须使用 <code>nums</code> 数组中的每一个数进行分组，并且分数不一定需要是整数。</p>

<p>返回我们所能得到的最大 <strong>分数</strong> 是多少。答案误差在&nbsp;<code>10<sup>-6</sup></code>&nbsp;内被视为是正确的。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [9,1,2,3,9], k = 3
<strong>输出:</strong> 20.00000
<strong>解释:</strong> 
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3,4,5,6,7], k = 4
<strong>输出:</strong> 20.50000
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 前缀和

## 示例

```
[9,1,2,3,9]
3
[1,2,3,4,5,6,7]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public double largestSumOfAverages(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
```

### C

```c
double largestSumOfAverages(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public double LargestSumOfAverages(int[] nums, int k) {
        
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
var largestSumOfAverages = function(nums, k) {
    
};
```

### TypeScript

```typescript
function largestSumOfAverages(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function largestSumOfAverages($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestSumOfAverages(_ nums: [Int], _ k: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestSumOfAverages(nums: IntArray, k: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double largestSumOfAverages(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func largestSumOfAverages(nums []int, k int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def largest_sum_of_averages(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def largestSumOfAverages(nums: Array[Int], k: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_sum_of_averages(nums: Vec<i32>, k: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-sum-of-averages nums k)
  (-> (listof exact-integer?) exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec largest_sum_of_averages(Nums :: [integer()], K :: integer()) -> float().
largest_sum_of_averages(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_sum_of_averages(nums :: [integer], k :: integer) :: float
  def largest_sum_of_averages(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestSumOfAverages(nums: Array<Int64>, k: Int64): Float64 {

    }
}
```

