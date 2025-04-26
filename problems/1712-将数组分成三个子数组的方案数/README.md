# 1712. 将数组分成三个子数组的方案数

## 题目描述

<p>我们称一个分割整数数组的方案是 <strong>好的</strong> ，当它满足：</p>

<ul>
	<li>数组被分成三个 <strong>非空</strong> 连续子数组，从左至右分别命名为 <code>left</code> ， <code>mid</code> ， <code>right</code> 。</li>
	<li><code>left</code> 中元素和小于等于 <code>mid</code> 中元素和，<code>mid</code> 中元素和小于等于 <code>right</code> 中元素和。</li>
</ul>

<p>给你一个 <strong>非负</strong> 整数数组 <code>nums</code> ，请你返回 <strong>好的</strong> 分割 <code>nums</code> 方案数目。由于答案可能会很大，请你将结果对 <code>10<sup>9 </sup>+ 7</code> 取余后返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,1]
<b>输出：</b>1
<b>解释：</b>唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,2,2,5,0]
<b>输出：</b>3
<b>解释：</b>nums 总共有 3 种好的分割方案：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,1]
<b>输出：</b>0
<b>解释：</b>没有好的分割方案。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 前缀和

## 提示

1. Create a prefix array to efficiently find the sum of subarrays.
2. As we are dividing the array into three subarrays, there are two "walls". Iterate over the right wall positions and find where the left wall could be for each right wall position.
3. Use binary search to find the left-most position and right-most position the left wall could be.

## 示例

```
[1,1,1]
[1,2,2,2,5,0]
[3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToSplit(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
```

### C

```c
int waysToSplit(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToSplit(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplit = function(nums) {
    
};
```

### TypeScript

```typescript
function waysToSplit(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function waysToSplit($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToSplit(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToSplit(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToSplit(List<int> nums) {
    
  }
}
```

### Go

```golang
func waysToSplit(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def ways_to_split(nums)
    
end
```

### Scala

```scala
object Solution {
    def waysToSplit(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_split(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-split nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_split(Nums :: [integer()]) -> integer().
ways_to_split(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_split(nums :: [integer]) :: integer
  def ways_to_split(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToSplit(nums: Array<Int64>): Int64 {

    }
}
```

