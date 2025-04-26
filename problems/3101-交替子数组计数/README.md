# 3101. 交替子数组计数

## 题目描述

<p>给你一个<span data-keyword="binary-array">二进制数组 </span><code>nums</code> 。</p>

<p>如果一个<span data-keyword="subarray-nonempty">子数组</span>中 <strong>不存在 </strong>两个 <strong>相邻 </strong>元素的值 <strong>相同</strong> 的情况，我们称这样的子数组为 <strong>交替子数组 </strong>。</p>

<p>返回数组 <code>nums</code> 中交替子数组的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>
<!-- 解释示例1的交替子数组 -->

<p>以下子数组是交替子数组：<code>[0]</code> 、<code>[1]</code> 、<code>[1]</code> 、<code>[1]</code> 以及 <code>[0,1]</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,0,1,0]</span></p>

<p><strong>输出：</strong> <span class="example-io">10</span></p>

<p><strong>解释：</strong></p>
<!-- 解释示例2的交替子数组 -->

<p>数组的每个子数组都是交替子数组。可以统计在内的子数组共有 10 个。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 不是 <code>0</code> 就是 <code>1</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. Try using dynamic programming.
2. Let <code>dp[i]</code> be the number of alternating subarrays ending at index <code>i</code>.
3. The final answer is the sum of <code>dp[i]</code> over all  indices <code>i</code> from <code>0</code> to <code>n - 1</code>.

## 示例

```
[0,1,1,1]
[1,0,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
long long countAlternatingSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountAlternatingSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countAlternatingSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function countAlternatingSubarrays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countAlternatingSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countAlternatingSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countAlternatingSubarrays(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countAlternatingSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func countAlternatingSubarrays(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_alternating_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def countAlternatingSubarrays(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-alternating-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_alternating_subarrays(Nums :: [integer()]) -> integer().
count_alternating_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_alternating_subarrays(nums :: [integer]) :: integer
  def count_alternating_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countAlternatingSubarrays(nums: Array<Int64>): Int64 {

    }
}
```

