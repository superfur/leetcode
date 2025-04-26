# 2875. 无限数组的最短子数组

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>下标从 <strong>0</strong> 开始的数组 <code>infinite_nums</code> 是通过无限地将 nums 的元素追加到自己之后生成的。</p>

<p>请你从 <code>infinite_nums</code> 中找出满足 <strong>元素和</strong> 等于&nbsp;<code>target</code> 的 <strong>最短</strong> 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], target = 5
<strong>输出：</strong>2
<strong>解释：</strong>在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。
区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,2,3], target = 4
<strong>输出：</strong>2
<strong>解释：</strong>在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...].
区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,6,8], target = 3
<strong>输出：</strong>-1
<strong>解释：</strong>在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。
可以证明，不存在元素和等于目标值 target = 3 的子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和
- 滑动窗口

## 提示

1. Notice that, <code>target</code> is either: A subarray of <code>nums</code>, or <code>prefix_sum[i]</code> + <code> k * sum(nums) </code> + <code>suffix_sum[j]</code> for some <code>i, j, k</code>.
2. You can solve the problem for those two separate cases using hash map and prefix sums.

## 示例

```
[1,2,3]
5
[1,1,1,2,3]
4
[2,4,6,8]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSizeSubarray(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int minSizeSubarray(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSizeSubarray(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minSizeSubarray = function(nums, target) {
    
};
```

### TypeScript

```typescript
function minSizeSubarray(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function minSizeSubarray($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSizeSubarray(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSizeSubarray(nums: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSizeSubarray(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func minSizeSubarray(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_size_subarray(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def minSizeSubarray(nums: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_size_subarray(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-size-subarray nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_size_subarray(Nums :: [integer()], Target :: integer()) -> integer().
min_size_subarray(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_size_subarray(nums :: [integer], target :: integer) :: integer
  def min_size_subarray(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSizeSubarray(nums: Array<Int64>, target: Int64): Int64 {

    }
}
```

