# 2488. 统计中位数为 K 的子数组

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>nums</code> ，该数组由从 <code>1</code> 到 <code>n</code> 的 <strong>不同</strong> 整数组成。另给你一个正整数 <code>k</code> 。</p>

<p>统计并返回 <code>nums</code> 中的 <strong>中位数</strong> 等于 <code>k</code> 的非空子数组的数目。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>数组的中位数是按 <strong>递增</strong> 顺序排列后位于 <strong>中间</strong> 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 <strong>左</strong> 的那个元素。

	<ul>
		<li>例如，<code>[2,3,1,4]</code> 的中位数是 <code>2</code> ，<code>[8,4,3,5,1]</code> 的中位数是 <code>4</code> 。</li>
	</ul>
	</li>
	<li>子数组是数组中的一个连续部分。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1,4,5], k = 4
<strong>输出：</strong>3
<strong>解释：</strong>中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,1], k = 3
<strong>输出：</strong>1
<strong>解释：</strong>[3] 是唯一一个中位数等于 3 的子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= n</code></li>
	<li><code>nums</code> 中的整数互不相同</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Consider changing the numbers that are strictly greater than k in the array to 1, the numbers that are strictly smaller than k to -1, and k to 0.
2. After the change, what property does a subarray with median k have in the new array?
3. An array with median k should have a sum equal to either 0 or 1 in the new array and should contain the element k. How do you count such subarrays?

## 示例

```
[3,2,1,4,5]
4
[2,3,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubarrays(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int countSubarrays(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubarrays(int[] nums, int k) {
        
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
var countSubarrays = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countSubarrays(nums: number[], k: number): number {
    
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
    function countSubarrays($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countSubarrays(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_subarrays(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], k :: integer) :: integer
  def count_subarrays(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubarrays(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

