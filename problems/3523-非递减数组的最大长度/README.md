# 3523. 非递减数组的最大长度

## 题目描述

<p>给你一个整数数组 <code>nums</code>。在一次操作中，你可以选择一个子数组，并将其替换为一个等于该子数组&nbsp;<strong>最大值&nbsp;</strong>的单个元素。</p>

<p>返回经过零次或多次操作后，数组仍为&nbsp;<strong>非递减&nbsp;</strong>的情况下，数组&nbsp;<strong>可能的最大长度</strong>。</p>

<p><strong>子数组&nbsp;</strong>是数组中一个连续、<b>非空&nbsp;</b>的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,2,5,3,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>实现最大长度的一种方法是：</p>

<ol>
	<li>将子数组 <code>nums[1..2] = [2, 5]</code> 替换为 <code>5</code> → <code>[4, 5, 3, 5]</code>。</li>
	<li>将子数组 <code>nums[2..3] = [3, 5]</code> 替换为 <code>5</code> → <code>[4, 5, 5]</code>。</li>
</ol>

<p>最终数组 <code>[4, 5, 5]</code> 是非递减的，长度为 <font face="monospace">3。</font></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>无需任何操作，因为数组 <code>[1,2,3]</code> 已经是非递减的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 单调栈

## 提示

1. Iterate backwards.
2. Can you remove the largest element in the array? Is that ever helpful?

## 示例

```
[4,2,5,3,5]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumPossibleSize(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumPossibleSize(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumPossibleSize(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumPossibleSize = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumPossibleSize(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumPossibleSize($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumPossibleSize(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumPossibleSize(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumPossibleSize(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumPossibleSize(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_possible_size(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumPossibleSize(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_possible_size(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-possible-size nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_possible_size(Nums :: [integer()]) -> integer().
maximum_possible_size(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_possible_size(nums :: [integer]) :: integer
  def maximum_possible_size(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumPossibleSize(nums: Array<Int64>): Int64 {

    }
}
```

