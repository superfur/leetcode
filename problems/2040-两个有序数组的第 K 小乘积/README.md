# 2040. 两个有序数组的第 K 小乘积

## 题目描述

给你两个 <strong>从小到大排好序</strong>&nbsp;且下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;以及一个整数&nbsp;<code>k</code>&nbsp;，请你返回第<em>&nbsp;</em><code>k</code>&nbsp;（从 <strong>1</strong>&nbsp;开始编号）小的&nbsp;<code>nums1[i] * nums2[j]</code><em>&nbsp;</em>的乘积，其中<em>&nbsp;</em><code>0 &lt;= i &lt; nums1.length</code><em> </em>且<em> </em><code>0 &lt;= j &lt; nums2.length</code>&nbsp;。
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [2,5], nums2 = [3,4], k = 2
<b>输出：</b>8
<b>解释：</b>第 2 小的乘积计算如下：
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
第 2 小的乘积为 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
<b>输出：</b>0
<strong>解释：</strong>第 6 小的乘积计算如下：
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
第 6 小的乘积为 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
<b>输出：</b>-6
<b>解释：</b>第 3 小的乘积计算如下：
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
第 3 小的乘积为 -6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums1.length * nums2.length</code></li>
	<li><code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;都是从小到大排好序的。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找

## 提示

1. Can we split this problem into four cases depending on the sign of the numbers?
2. Can we binary search the value?

## 示例

```
[2,5]
[3,4]
2
[-4,-2,0,3]
[2,4]
6
[-2,-1,0,1,2]
[-3,-1,2,4,5]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
```

### C

```c
long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public long KthSmallestProduct(int[] nums1, int[] nums2, long k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function kthSmallestProduct(nums1: number[], nums2: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function kthSmallestProduct($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthSmallestProduct(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthSmallestProduct(nums1: IntArray, nums2: IntArray, k: Long): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthSmallestProduct(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def kth_smallest_product(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def kthSmallestProduct(nums1: Array[Int], nums2: Array[Int], k: Long): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_smallest_product(nums1: Vec<i32>, nums2: Vec<i32>, k: i64) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-smallest-product nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_smallest_product(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
kth_smallest_product(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_smallest_product(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def kth_smallest_product(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthSmallestProduct(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Int64 {

    }
}
```

