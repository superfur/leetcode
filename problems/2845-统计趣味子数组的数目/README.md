# 2845. 统计趣味子数组的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，以及整数 <code>modulo</code> 和整数 <code>k</code> 。</p>

<p>请你找出并统计数组中 <strong>趣味子数组</strong> 的数目。</p>

<p>如果 <strong>子数组</strong> <code>nums[l..r]</code> 满足下述条件，则称其为 <strong>趣味子数组</strong> ：</p>

<ul>
	<li>在范围 <code>[l, r]</code> 内，设 <code>cnt</code> 为满足 <code>nums[i] % modulo == k</code> 的索引 <code>i</code> 的数量。并且 <code>cnt % modulo == k</code> 。</li>
</ul>

<p>以整数形式表示并返回趣味子数组的数目。<em> </em></p>

<p><span><strong>注意：</strong>子数组是数组中的一个连续非空的元素序列。</span></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,4], modulo = 2, k = 1
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，趣味子数组分别是： 
子数组 nums[0..0] ，也就是 [3] 。 
- 在范围 [0, 0] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
子数组 nums[0..1] ，也就是 [3,2] 。
- 在范围 [0, 1] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
子数组 nums[0..2] ，也就是 [3,2,4] 。
- 在范围 [0, 2] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
- 因此 cnt = 1 ，且 cnt % modulo == k 。
可以证明不存在其他趣味子数组。因此，答案为 3 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,9,6], modulo = 3, k = 0
<strong>输出：</strong>2
<strong>解释：</strong>在这个示例中，趣味子数组分别是： 
子数组 nums[0..3] ，也就是 [3,1,9,6] 。
- 在范围 [0, 3] 内，只存在 3 个下标 i = 0, 2, 3 满足 nums[i] % modulo == k 。
- 因此 cnt = 3 ，且 cnt % modulo == k 。
子数组 nums[1..1] ，也就是 [1] 。
- 在范围 [1, 1] 内，不存在下标满足 nums[i] % modulo == k 。
- 因此 cnt = 0 ，且 cnt % modulo == k 。
可以证明不存在其他趣味子数组，因此答案为 2 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5 </sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= modulo &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt; modulo</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. The problem can be solved using prefix sums.
2. Let <code>count[i]</code> be the number of indices where <code>nums[i] % modulo == k</code> among the first <code>i</code> indices.
3. <code>count[0] = 0</code> and <code>count[i] = count[i - 1] + (nums[i - 1] % modulo == k ? 1 : 0)</code> for <code>i = 1, 2, ..., n</code>.
4. Now we want to calculate for each <code>i = 1, 2, ..., n</code>, how many indices <code>j < i</code> such that <code>(count[i] - count[j]) % modulo == k</code>.
5. Rewriting <code>(count[i] - count[j]) % modulo == k</code> becomes <code>count[j] = (count[i] + modulo - k) % modulo</code>.
6. Using a map data structure, for each <code>i = 0, 1, 2, ..., n</code>, we just sum up all <code>map[(count[i] + modulo - k) % modulo]</code> before increasing <code>map[count[i] % modulo]</code>, and the total sum is the final answer.

## 示例

```
[3,2,4]
2
1
[3,1,9,6]
3
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countInterestingSubarrays(List<Integer> nums, int modulo, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
```

### C

```c
long long countInterestingSubarrays(int* nums, int numsSize, int modulo, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountInterestingSubarrays(IList<int> nums, int modulo, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} modulo
 * @param {number} k
 * @return {number}
 */
var countInterestingSubarrays = function(nums, modulo, k) {
    
};
```

### TypeScript

```typescript
function countInterestingSubarrays(nums: number[], modulo: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $modulo
     * @param Integer $k
     * @return Integer
     */
    function countInterestingSubarrays($nums, $modulo, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countInterestingSubarrays(_ nums: [Int], _ modulo: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countInterestingSubarrays(nums: List<Int>, modulo: Int, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countInterestingSubarrays(List<int> nums, int modulo, int k) {
    
  }
}
```

### Go

```golang
func countInterestingSubarrays(nums []int, modulo int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} modulo
# @param {Integer} k
# @return {Integer}
def count_interesting_subarrays(nums, modulo, k)
    
end
```

### Scala

```scala
object Solution {
    def countInterestingSubarrays(nums: List[Int], modulo: Int, k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-interesting-subarrays nums modulo k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_interesting_subarrays(Nums :: [integer()], Modulo :: integer(), K :: integer()) -> integer().
count_interesting_subarrays(Nums, Modulo, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_interesting_subarrays(nums :: [integer], modulo :: integer, k :: integer) :: integer
  def count_interesting_subarrays(nums, modulo, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countInterestingSubarrays(nums: ArrayList<Int64>, modulo: Int64, k: Int64): Int64 {

    }
}
```

