# 2962. 统计最大元素出现至少 K 次的子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个 <strong>正整数</strong> <code>k</code> 。</p>

<p>请你统计有多少满足 「&nbsp;<code>nums</code> 中的 <strong>最大</strong> 元素」至少出现 <code>k</code> 次的子数组，并返回满足这一条件的子数组的数目。</p>

<p>子数组是数组中的一个连续元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,2,3,3], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,4,2,1], k = 3
<strong>输出：</strong>0
<strong>解释：</strong>没有子数组包含元素 4 至少 3 次。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 示例

```
[1,3,2,3,3]
2
[1,4,2,1]
3
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

