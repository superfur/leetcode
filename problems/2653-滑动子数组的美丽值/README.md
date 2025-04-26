# 2653. 滑动子数组的美丽值

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;，请你求出每个长度为&nbsp;<code>k</code>&nbsp;的子数组的 <b>美丽值</b>&nbsp;。</p>

<p>一个子数组的 <strong>美丽值</strong>&nbsp;定义为：如果子数组中第 <code>x</code>&nbsp;<strong>小整数</strong>&nbsp;是 <strong>负数</strong>&nbsp;，那么美丽值为第 <code>x</code>&nbsp;小的数，否则美丽值为 <code>0</code>&nbsp;。</p>

<p>请你返回一个包含<em>&nbsp;</em><code>n - k + 1</code>&nbsp;个整数的数组，<strong>依次</strong>&nbsp;表示数组中从第一个下标开始，每个长度为&nbsp;<code>k</code>&nbsp;的子数组的<strong>&nbsp;美丽值</strong>&nbsp;。</p>

<ul>
	<li>
	<p>子数组指的是数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,-1,-3,-2,3], k = 3, x = 2
<b>输出：</b>[-1,-2,-2]
<b>解释：</b>总共有 3 个 k = 3 的子数组。
第一个子数组是 <code>[1, -1, -3]</code> ，第二小的数是负数 -1 。
第二个子数组是 <code>[-1, -3, -2]</code> ，第二小的数是负数 -2 。
第三个子数组是 <code>[-3, -2, 3]&nbsp;，第二小的数是负数 -2 。</code></pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [-1,-2,-3,-4,-5], k = 2, x = 2
<b>输出：</b>[-1,-2,-3,-4]
<b>解释：</b>总共有 4 个 k = 2 的子数组。
<code>[-1, -2] 中第二小的数是负数 -1 。</code>
<code>[-2, -3] 中第二小的数是负数 -2 。</code>
<code>[-3, -4] 中第二小的数是负数 -3 。</code>
<code>[-4, -5] 中第二小的数是负数 -4 。</code></pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [-3,1,2,-3,0,-3], k = 2, x = 1
<b>输出：</b>[-3,0,-3,-3,-3]
<b>解释：</b>总共有 5 个 k = 2 的子数组。
<code>[-3, 1] 中最小的数是负数 -3 。</code>
<code>[1, 2] 中最小的数不是负数，所以美丽值为 0 。</code>
<code>[2, -3] 中最小的数是负数 -3 。</code>
<code>[-3, 0] 中最小的数是负数 -3 。</code>
<code>[0, -3] 中最小的数是负数 -3 。</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length&nbsp;</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li><code>1 &lt;= x &lt;= k&nbsp;</code></li>
	<li><code>-50&nbsp;&lt;= nums[i] &lt;= 50&nbsp;</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. Try to maintain the frequency of negative numbers in the current window of size k.
2. The x^th smallest negative integer can be gotten by iterating through the frequencies of the numbers in order.

## 示例

```
[1,-1,-3,-2,3]
3
2
[-1,-2,-3,-4,-5]
2
2
[-3,1,2,-3,0,-3]
2
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSubarrayBeauty(int* nums, int numsSize, int k, int x, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetSubarrayBeauty(int[] nums, int k, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var getSubarrayBeauty = function(nums, k, x) {
    
};
```

### TypeScript

```typescript
function getSubarrayBeauty(nums: number[], k: number, x: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function getSubarrayBeauty($nums, $k, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSubarrayBeauty(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSubarrayBeauty(nums: IntArray, k: Int, x: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getSubarrayBeauty(List<int> nums, int k, int x) {
    
  }
}
```

### Go

```golang
func getSubarrayBeauty(nums []int, k int, x int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def get_subarray_beauty(nums, k, x)
    
end
```

### Scala

```scala
object Solution {
    def getSubarrayBeauty(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_subarray_beauty(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-subarray-beauty nums k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_subarray_beauty(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
get_subarray_beauty(Nums, K, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_subarray_beauty(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def get_subarray_beauty(nums, k, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSubarrayBeauty(nums: Array<Int64>, k: Int64, x: Int64): Array<Int64> {

    }
}
```

