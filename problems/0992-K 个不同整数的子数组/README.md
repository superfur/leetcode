# 992. K 个不同整数的子数组

## 题目描述

<p>给定一个正整数数组 <code>nums</code>和一个整数 <code>k</code>，返回 <code>nums</code> 中 「<strong>好子数组」</strong><em>&nbsp;</em>的数目。</p>

<p>如果 <code>nums</code>&nbsp;的某个子数组中不同整数的个数恰好为 <code>k</code>，则称 <code>nums</code>&nbsp;的这个连续、不一定不同的子数组为 <strong>「</strong><strong>好子数组 」</strong>。</p>

<ul>
	<li>例如，<code>[1,2,3,1,2]</code> 中有&nbsp;<code>3</code>&nbsp;个不同的整数：<code>1</code>，<code>2</code>，以及&nbsp;<code>3</code>。</li>
</ul>

<p><strong>子数组</strong> 是数组的 <strong>连续</strong> 部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,3], k = 2
<strong>输出：</strong>7
<strong>解释：</strong>恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,3,4], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 计数
- 滑动窗口

## 提示

1. Try generating all possible subarrays and check for the number of unique integers. Increment the count accordingly.
2. How about using a map to store the count of integers?
3. Think about the Sliding Window and 2-pointer approach.

## 示例

```
[1,2,1,2,3]
2
[1,2,1,3,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarraysWithKDistinct(int[] nums, int k) {
        
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
var subarraysWithKDistinct = function(nums, k) {
    
};
```

### TypeScript

```typescript
function subarraysWithKDistinct(nums: number[], k: number): number {
    
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
    function subarraysWithKDistinct($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarraysWithKDistinct(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarraysWithKDistinct(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarraysWithKDistinct(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func subarraysWithKDistinct(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_with_k_distinct(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def subarraysWithKDistinct(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarrays-with-k-distinct nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec subarrays_with_k_distinct(Nums :: [integer()], K :: integer()) -> integer().
subarrays_with_k_distinct(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarrays_with_k_distinct(nums :: [integer], k :: integer) :: integer
  def subarrays_with_k_distinct(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarraysWithKDistinct(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

