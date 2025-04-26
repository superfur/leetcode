# LCR 009. 乘积小于 K 的子数组

## 题目描述

<p>给定一个正整数数组&nbsp;<code>nums</code>和整数 <code>k</code>&nbsp;，请找出该数组内乘积小于&nbsp;<code>k</code>&nbsp;的连续的子数组的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> nums = [10,5,2,6], k = 100
<strong>输出:</strong> 8
<strong>解释:</strong> 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], k = 0
<strong>输出:</strong> 0</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 713&nbsp;题相同：<a href="https://leetcode-cn.com/problems/subarray-product-less-than-k/">https://leetcode-cn.com/problems/subarray-product-less-than-k/</a>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 示例

```
[10,5,2,6]
100
[1,2,3]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {

    }
};
```

### Java

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {

    }
}
```

### Python

```python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
```

### C

```c


int numSubarrayProductLessThanK(int* nums, int numsSize, int k){

}
```

### C#

```csharp
public class Solution {
    public int NumSubarrayProductLessThanK(int[] nums, int k) {

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
var numSubarrayProductLessThanK = function(nums, k) {

};
```

### TypeScript

```typescript
function numSubarrayProductLessThanK(nums: number[], k: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function numSubarrayProductLessThanK($nums, $k) {

    }
}
```

### Swift

```swift
class Solution {
    func numSubarrayProductLessThanK(_ nums: [Int], _ k: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubarrayProductLessThanK(nums: IntArray, k: Int): Int {

    }
}
```

### Go

```golang
func numSubarrayProductLessThanK(nums []int, k int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def num_subarray_product_less_than_k(nums, k)

end
```

### Scala

```scala
object Solution {
    def numSubarrayProductLessThanK(nums: Array[Int], k: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (num-subarray-product-less-than-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec num_subarray_product_less_than_k(Nums :: [integer()], K :: integer()) -> integer().
num_subarray_product_less_than_k(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_subarray_product_less_than_k(nums :: [integer], k :: integer) :: integer
  def num_subarray_product_less_than_k(nums, k) do

  end
end
```

