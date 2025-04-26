# 480. 滑动窗口中位数

## 题目描述

<p>中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。</p>

<p>例如：</p>

<ul>
	<li><code>[2,3,4]</code>，中位数是 <code>3</code></li>
	<li><code>[2,3]</code>，中位数是 <code>(2 + 3) / 2 = 2.5</code></li>
</ul>

<p>给你一个数组 <em>nums</em>，有一个长度为 <em>k</em> 的窗口从最左端滑动到最右端。窗口中有 <em>k</em> 个数，每次窗口向右移动 <em>1</em> 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。</p>

<p> </p>

<p><strong>示例：</strong></p>

<p>给出 <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>，以及 <em>k</em> = 3。</p>

<pre>
窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
</pre>

<p> 因此，返回该滑动窗口的中位数数组 <code>[1,-1,-1,3,5,6]</code>。</p>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>你可以假设 <code>k</code> 始终有效，即：<code>k</code> 始终小于等于输入的非空数组的元素个数。</li>
	<li>与真实值误差在 <code>10 ^ -5</code> 以内的答案将被视作正确答案。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 滑动窗口
- 堆（优先队列）

## 提示

1. The simplest of solutions comes from the basic idea of finding the median given a set of numbers. We know that by definition, a median is the center element (or an average of the two center elements). Given an unsorted list of numbers, how do we find the median element? If you know the answer to this question, can we extend this idea to every sliding window that we come across in the array?
2. Is there a better way to do what we are doing in the above hint? Don't you think there is duplication of calculation being done there? Is there some sort of optimization that we can do to achieve the same result? This approach is merely a modification of the basic approach except that it simply reduces duplication of calculations once done.
3. The third line of thought is also based on this same idea but achieving the result in a different way. We obviously need the window to be sorted for us to be able to find the median. Is there a data-structure out there that we can use (in one or more quantities) to obtain the median element extremely fast, say O(1) time while having the ability to perform the other operations fairly efficiently as well?

## 示例

```
[1,3,-1,-3,5,3,6,7]
3
[1,2,3,4,2,3,1,4,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* medianSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] MedianSlidingWindow(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function(nums, k) {
    
};
```

### TypeScript

```typescript
function medianSlidingWindow(nums: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float[]
     */
    function medianSlidingWindow($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func medianSlidingWindow(_ nums: [Int], _ k: Int) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> medianSlidingWindow(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func medianSlidingWindow(nums []int, k int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Float[]}
def median_sliding_window(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def medianSlidingWindow(nums: Array[Int], k: Int): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (median-sliding-window nums k)
  (-> (listof exact-integer?) exact-integer? (listof flonum?))
  )
```

### Erlang

```erlang
-spec median_sliding_window(Nums :: [integer()], K :: integer()) -> [float()].
median_sliding_window(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec median_sliding_window(nums :: [integer], k :: integer) :: [float]
  def median_sliding_window(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func medianSlidingWindow(nums: Array<Int64>, k: Int64): Array<Float64> {

    }
}
```

