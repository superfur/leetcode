# 3171. 找到按位或最接近 K 的子数组

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你需要找到&nbsp;<code>nums</code>&nbsp;的一个&nbsp;<span data-keyword="subarray-nonempty">子数组</span>&nbsp;，满足子数组中所有元素按位或运算 <code>OR</code> 的值与 <code>k</code>&nbsp;的 <strong>绝对差</strong>&nbsp;尽可能 <strong>小</strong>&nbsp;。换言之，你需要选择一个子数组&nbsp;<code>nums[l..r]</code>&nbsp;满足 <code>|k - (nums[l] OR nums[l + 1] ... OR nums[r])|</code>&nbsp;最小。</p>

<p>请你返回 <strong>最小</strong>&nbsp;的绝对差值。</p>

<p><strong>子数组 </strong>是数组中连续的&nbsp;<strong>非空</strong>&nbsp;元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,4,5], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>nums[0..1]</code> 的按位 <code>OR</code> 运算值为 3 ，得到最小差值&nbsp;<code>|3 - 3| = 0</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,1,3], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>nums[1..1]</code> 的按位 <code>OR</code> 运算值为 3 ，得到最小差值&nbsp;<code>|3 - 2| = 1</code> 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1], k = 10</span></p>

<p><span class="example-io"><b>输出：</b>9</span></p>

<p><strong>解释：</strong></p>

<p>只有一个子数组，按位 <code>OR</code> 运算值为 1 ，得到最小差值&nbsp;<code>|10 - 1| = 9</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 线段树
- 数组
- 二分查找

## 提示

1. Let <code>dp[i]</code> be the set of all the bitwise <code>OR</code> of all the subarrays ending at index <code>i</code>.
2. We start from <code>nums[i]</code>, taking the bitwise <code>OR</code> result by including elements one by one from <code>i</code> towards left. Notice that only unset bits can become set on adding an element, and set bits never become unset again.
3. Hence <code>dp[i]</code> can contain at most 30 elements.

## 示例

```
[1,2,4,5]
3
[1,3,1,3]
2
[1]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDifference(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minimumDifference(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        
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
var minimumDifference = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minimumDifference(nums: number[], k: number): number {
    
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
    function minimumDifference($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDifference(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDifference(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minimumDifference(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_difference(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumDifference(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-difference nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_difference(Nums :: [integer()], K :: integer()) -> integer().
minimum_difference(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_difference(nums :: [integer], k :: integer) :: integer
  def minimum_difference(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDifference(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

