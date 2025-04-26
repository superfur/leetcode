# 3346. 执行操作后元素的最高频率 I

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和两个整数&nbsp;<code>k</code> 和&nbsp;<code>numOperations</code>&nbsp;。</p>

<p>你必须对 <code>nums</code>&nbsp;执行 <strong>操作</strong>&nbsp; <code>numOperations</code>&nbsp;次。每次操作中，你可以：</p>

<ul>
	<li>选择一个下标&nbsp;<code>i</code>&nbsp;，它在之前的操作中 <strong>没有</strong>&nbsp;被选择过。</li>
	<li>将 <code>nums[i]</code>&nbsp;增加范围&nbsp;<code>[-k, k]</code>&nbsp;中的一个整数。</li>
</ul>

<p>在执行完所有操作以后，请你返回 <code>nums</code>&nbsp;中出现 <strong>频率最高</strong>&nbsp;元素的出现次数。</p>

<p>一个元素 <code>x</code>&nbsp;的 <strong>频率</strong>&nbsp;指的是它在数组中出现的次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,4,5], k = 1, numOperations = 2</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>通过以下操作得到最高频率 2 ：</p>

<ul>
	<li>将&nbsp;<code>nums[1]</code>&nbsp;增加 0 ，<code>nums</code> 变为&nbsp;<code>[1, 4, 5]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[2]</code>&nbsp;增加 -1 ，<code>nums</code> 变为&nbsp;<code>[1, 4, 4]</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [5,11,20,20], k = 5, numOperations = 1</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>通过以下操作得到最高频率 2 ：</p>

<ul>
	<li>将 <code>nums[1]</code> 增加 0 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= numOperations &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和
- 排序
- 滑动窗口

## 提示

1. Sort the array and try each value in range as a candidate.

## 示例

```
[1,4,5]
1
2
[5,11,20,20]
5
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
```

### C

```c
int maxFrequency(int* nums, int numsSize, int k, int numOperations) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxFrequency(int[] nums, int k, int numOperations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} numOperations
 * @return {number}
 */
var maxFrequency = function(nums, k, numOperations) {
    
};
```

### TypeScript

```typescript
function maxFrequency(nums: number[], k: number, numOperations: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $numOperations
     * @return Integer
     */
    function maxFrequency($nums, $k, $numOperations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxFrequency(List<int> nums, int k, int numOperations) {
    
  }
}
```

### Go

```golang
func maxFrequency(nums []int, k int, numOperations int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} num_operations
# @return {Integer}
def max_frequency(nums, k, num_operations)
    
end
```

### Scala

```scala
object Solution {
    def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-frequency nums k numOperations)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_frequency(Nums :: [integer()], K :: integer(), NumOperations :: integer()) -> integer().
max_frequency(Nums, K, NumOperations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_frequency(nums :: [integer], k :: integer, num_operations :: integer) :: integer
  def max_frequency(nums, k, num_operations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxFrequency(nums: Array<Int64>, k: Int64, numOperations: Int64): Int64 {

    }
}
```

