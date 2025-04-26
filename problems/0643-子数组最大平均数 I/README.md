# 643. 子数组最大平均数 I

## 题目描述

<p>给你一个由 <code>n</code> 个元素组成的整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p>请你找出平均数最大且 <strong>长度为 <code>k</code></strong> 的连续子数组，并输出该最大平均数。</p>

<p>任何误差小于 <code>10<sup>-5</sup></code> 的答案都将被视为正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,12,-5,-6,50,3], k = 4
<strong>输出：</strong>12.75
<strong>解释：</strong>最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5], k = 1
<strong>输出：</strong>5.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 滑动窗口

## 示例

```
[1,12,-5,-6,50,3]
4
[5]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
```

### C

```c
double findMaxAverage(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        
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
var findMaxAverage = function(nums, k) {
    
};
```

### TypeScript

```typescript
function findMaxAverage(nums: number[], k: number): number {
    
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
    function findMaxAverage($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxAverage(_ nums: [Int], _ k: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxAverage(nums: IntArray, k: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double findMaxAverage(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func findMaxAverage(nums []int, k int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def find_max_average(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def findMaxAverage(nums: Array[Int], k: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-average nums k)
  (-> (listof exact-integer?) exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec find_max_average(Nums :: [integer()], K :: integer()) -> float().
find_max_average(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_average(nums :: [integer], k :: integer) :: float
  def find_max_average(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxAverage(nums: Array<Int64>, k: Int64): Float64 {

    }
}
```

