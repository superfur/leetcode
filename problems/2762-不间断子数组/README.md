# 2762. 不间断子数组

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。<code>nums</code>&nbsp;的一个子数组如果满足以下条件，那么它是 <strong>不间断</strong> 的：</p>

<ul>
	<li><code>i</code>，<code>i + 1</code>&nbsp;，...，<code>j</code><sub> </sub>&nbsp;表示子数组中的下标。对于所有满足&nbsp;<code>i &lt;= i<sub>1</sub>, i<sub>2</sub> &lt;= j</code>&nbsp;的下标对，都有 <code>0 &lt;= |nums[i<sub>1</sub>] - nums[i<sub>2</sub>]| &lt;= 2</code>&nbsp;。</li>
</ul>

<p>请你返回 <strong>不间断</strong> 子数组的总数目。</p>

<p>子数组是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [5,4,2,4]
<strong>输出：</strong>8
<b>解释：</b>
大小为 1 的不间断子数组：[5], [4], [2], [4] 。
大小为 2 的不间断子数组：[5,4], [4,2], [2,4] 。
大小为 3 的不间断子数组：[4,2,4] 。
没有大小为 4 的不间断子数组。
不间断子数组的总数目为 4 + 3 + 1 = 8 。
除了这些以外，没有别的不间断子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3]
<b>输出：</b>6
<b>解释：</b>
大小为 1 的不间断子数组：[1], [2], [3] 。
大小为 2 的不间断子数组：[1,2], [2,3] 。
大小为 3 的不间断子数组：[1,2,3] 。
不间断子数组的总数目为 3 + 2 + 1 = 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 队列
- 数组
- 有序集合
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 提示

1. Try using the sliding window technique.
2. Use a set or map to keep track of the maximum and minimum of subarrays.

## 示例

```
[5,4,2,4]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long continuousSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
long long continuousSubarrays(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public long ContinuousSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function continuousSubarrays(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function continuousSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func continuousSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun continuousSubarrays(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int continuousSubarrays(List<int> nums) {

  }
}
```

### Go

```golang
func continuousSubarrays(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def continuous_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def continuousSubarrays(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn continuous_subarrays(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (continuous-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec continuous_subarrays(Nums :: [integer()]) -> integer().
continuous_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec continuous_subarrays(nums :: [integer]) :: integer
  def continuous_subarrays(nums) do

  end
end
```

### Cangjie

```cangjie
class Solution {
    func continuousSubarrays(nums: Array<Int64>): Int64 {

    }
}
```

