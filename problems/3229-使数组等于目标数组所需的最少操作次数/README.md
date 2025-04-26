# 3229. 使数组等于目标数组所需的最少操作次数

## 题目描述

<p>给你两个长度相同的正整数数组 <code>nums</code> 和 <code>target</code>。</p>

<p>在一次操作中，你可以选择 <code>nums</code> 的任何子数组，并将该子数组内的每个元素的值增加或减少 1。</p>

<p>返回使 <code>nums</code> 数组变为 <code>target</code> 数组所需的 <strong>最少 </strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,5,1,2], target = [4,6,2,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>执行以下操作可以使 <code>nums</code> 等于 <code>target</code>：<br />
- <code>nums[0..3]</code> 增加 1，<code>nums = [4,6,2,3]</code>。<br />
- <code>nums[3..3]</code> 增加 1，<code>nums = [4,6,2,4]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3,2], target = [2,1,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>执行以下操作可以使 <code>nums</code> 等于 <code>target</code>：<br />
- <code>nums[0..0]</code> 增加 1，<code>nums = [2,3,2]</code>。<br />
- <code>nums[1..1]</code> 减少 1，<code>nums = [2,2,2]</code>。<br />
- <code>nums[1..1]</code> 减少 1，<code>nums = [2,1,2]</code>。<br />
- <code>nums[2..2]</code> 增加 1，<code>nums = [2,1,3]</code>。<br />
- <code>nums[2..2]</code> 增加 1，<code>nums = [2,1,4]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], target[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 动态规划
- 单调栈

## 提示

1. Change <code>nums'[i] = nums[i] - target[i]</code>, so our goal is to make <code>nums'</code> into all 0s.
2. Divide and conquer.

## 示例

```
[3,5,1,2]
[4,6,2,4]
[1,3,2]
[2,1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumOperations(int[] nums, int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        
```

### C

```c
long long minimumOperations(int* nums, int numsSize, int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumOperations(int[] nums, int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var minimumOperations = function(nums, target) {
    
};
```

### TypeScript

```typescript
function minimumOperations(nums: number[], target: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $target
     * @return Integer
     */
    function minimumOperations($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int], _ target: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray, target: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<int> nums, List<int> target) {
    
  }
}
```

### Go

```golang
func minimumOperations(nums []int, target []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def minimum_operations(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int], target: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations nums target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Nums :: [integer()], Target :: [integer()]) -> integer().
minimum_operations(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer], target :: [integer]) :: integer
  def minimum_operations(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(nums: Array<Int64>, target: Array<Int64>): Int64 {

    }
}
```

