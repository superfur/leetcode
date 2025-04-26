# 2444. 统计定界子数组的数目

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数 <code>minK</code> 以及 <code>maxK</code> 。</p>

<p><code>nums</code> 的定界子数组是满足下述条件的一个子数组：</p>

<ul>
	<li>子数组中的 <strong>最小值</strong> 等于 <code>minK</code> 。</li>
	<li>子数组中的 <strong>最大值</strong> 等于 <code>maxK</code> 。</li>
</ul>

<p>返回定界子数组的数目。</p>

<p>子数组是数组中的一个连续部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,5,2,7,5], minK = 1, maxK = 5
<strong>输出：</strong>2
<strong>解释：</strong>定界子数组是 [1,3,5] 和 [1,3,5,2] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,1], minK = 1, maxK = 1
<strong>输出：</strong>10
<strong>解释：</strong>nums 的每个子数组都是一个定界子数组。共有 10 个子数组。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], minK, maxK &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 队列
- 数组
- 滑动窗口
- 单调队列

## 提示

1. Can you solve the problem if all the numbers in the array were between minK and maxK inclusive?
2. Think of the inclusion-exclusion principle.
3. Divide the array into multiple subarrays such that each number in each subarray is between minK and maxK inclusive, solve the previous problem for each subarray, and sum all the answers.

## 示例

```
[1,3,5,2,7,5]
1
5
[1,1,1,1]
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        
    }
};
```

### Java

```java
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
```

### C

```c
long long countSubarrays(int* nums, int numsSize, int minK, int maxK) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, int minK, int maxK) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    
};
```

### TypeScript

```typescript
function countSubarrays(nums: number[], minK: number, maxK: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $minK
     * @param Integer $maxK
     * @return Integer
     */
    function countSubarrays($nums, $minK, $maxK) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int], _ minK: Int, _ maxK: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray, minK: Int, maxK: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubarrays(List<int> nums, int minK, int maxK) {
    
  }
}
```

### Go

```golang
func countSubarrays(nums []int, minK int, maxK int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} min_k
# @param {Integer} max_k
# @return {Integer}
def count_subarrays(nums, min_k, max_k)
    
end
```

### Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int], minK: Int, maxK: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-subarrays nums minK maxK)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_subarrays(Nums :: [integer()], MinK :: integer(), MaxK :: integer()) -> integer().
count_subarrays(Nums, MinK, MaxK) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer], min_k :: integer, max_k :: integer) :: integer
  def count_subarrays(nums, min_k, max_k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubarrays(nums: Array<Int64>, minK: Int64, maxK: Int64): Int64 {

    }
}
```

