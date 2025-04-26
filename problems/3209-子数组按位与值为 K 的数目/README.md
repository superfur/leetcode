# 3209. 子数组按位与值为 K 的数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，请你返回&nbsp;<code>nums</code>&nbsp;中有多少个<span data-keyword="subarray-nonempty">子数组</span>满足：子数组中所有元素按位&nbsp;<code>AND</code>&nbsp;的结果为 <code>k</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,1], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><strong>解释：</strong></p>

<p>所有子数组都只含有元素 1 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,2], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<p>按位&nbsp;<code>AND</code>&nbsp;值为 1 的子数组包括：<code>[<u><strong>1</strong></u>,1,2]</code>, <code>[1,<u><strong>1</strong></u>,2]</code>, <code>[<u><strong>1,1</strong></u>,2]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>按位&nbsp;<code>AND</code>&nbsp;值为 2 的子数组包括：<code>[1,<b><u>2</u></b>,3]</code>, <code>[1,<u><strong>2,3</strong></u>]</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 线段树
- 数组
- 二分查找

## 提示

1. Let’s say we want to count the number of pairs <code>(l, r)</code> such that <code>nums[l] & nums[l + 1] & … & nums[r] == k</code>.
2. Fix the left index <code>l</code>.
3. Note that if you increase <code>r</code> for a fixed <code>l</code>, then the AND value of the subarray either decreases or remains unchanged.
4. Therefore, consider using binary search.
5. To calculate the AND value of a subarray, use sparse tables.

## 示例

```
[1,1,1]
1
[1,1,2]
1
[1,2,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        
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
long long countSubarrays(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        
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
    fun countSubarrays(nums: IntArray, k: Int): Long {
        
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
func countSubarrays(nums []int, k int) int64 {
    
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
    def countSubarrays(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        
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

