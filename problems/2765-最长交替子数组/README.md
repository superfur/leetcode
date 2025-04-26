# 2765. 最长交替子数组

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。如果 <code>nums</code>&nbsp;中长度为&nbsp;<code>m</code>&nbsp;的子数组&nbsp;<code>s</code>&nbsp;满足以下条件，我们称它是一个 <strong>交替子数组</strong> ：</p>

<ul>
	<li><code>m</code>&nbsp;大于&nbsp;<code>1</code>&nbsp;。</li>
	<li><code>s<sub>1</sub> = s<sub>0</sub> + 1</code>&nbsp;。</li>
	<li>下标从 <strong>0</strong> 开始的子数组&nbsp;<code>s</code>&nbsp;与数组&nbsp;<code>[s<sub>0</sub>, s<sub>1</sub>, s<sub>0</sub>, s<sub>1</sub>,...,s<sub>(m-1) % 2</sub>]</code>&nbsp;一样。也就是说，<code>s<sub>1</sub> - s<sub>0</sub> = 1</code>&nbsp;，<code>s<sub>2</sub> - s<sub>1</sub> = -1</code>&nbsp;，<code>s<sub>3</sub> - s<sub>2</sub> = 1</code>&nbsp;，<code>s<sub>4</sub> - s<sub>3</sub> = -1</code>&nbsp;，以此类推，直到&nbsp;<code>s[m - 1] - s[m - 2] = (-1)<sup>m</sup></code>&nbsp;。</li>
</ul>

<p>请你返回 <code>nums</code>&nbsp;中所有 <strong>交替</strong>&nbsp;子数组中，最长的长度，如果不存在交替子数组，请你返回 <code>-1</code>&nbsp;。</p>

<p>子数组是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block"><b>输入：</b>nums = [2,3,4,3,4]</div>

<div class="example-block"><b>输出：</b>4</div>

<div class="example-block"><b>解释：</b>交替子数组有 <code>[2,3]</code>，<code>[3,4]</code>，<code>[3,4,3]</code> 和 <code>[3,4,3,4]</code>。最长的子数组为 <code>[3,4,3,4]</code>，长度为 4。</div>

<p>&nbsp;</p>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block"><b>输入：</b>nums = [4,5,6]</div>

<div class="example-block"><b>输出：</b>2</div>

<div class="example-block"><strong>解释：</strong><code>[4,5]</code> 和 <code>[5,6]</code> 是仅有的两个交替子数组。它们长度都为 2 。</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. As the constraints are low, you can check each subarray for the given condition.

## 示例

```
[2,3,4,3,4]
[4,5,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int alternatingSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int alternatingSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int AlternatingSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var alternatingSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function alternatingSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function alternatingSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func alternatingSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun alternatingSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int alternatingSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func alternatingSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def alternating_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def alternatingSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn alternating_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (alternating-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec alternating_subarray(Nums :: [integer()]) -> integer().
alternating_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec alternating_subarray(nums :: [integer]) :: integer
  def alternating_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func alternatingSubarray(nums: Array<Int64>): Int64 {

    }
}
```

