# 3349. 检测相邻递增子数组 I

## 题目描述

<p>给你一个由 <code>n</code> 个整数组成的数组 <code>nums</code> 和一个整数 <code>k</code>，请你确定是否存在 <strong>两个</strong> <strong>相邻</strong> 且长度为 <code>k</code> 的 <strong>严格递增</strong> 子数组。具体来说，需要检查是否存在从下标 <code>a</code> 和 <code>b</code> (<code>a &lt; b</code>) 开始的 <strong>两个</strong> 子数组，并满足下述全部条件：</p>

<ul>
	<li>这两个子数组 <code>nums[a..a + k - 1]</code> 和 <code>nums[b..b + k - 1]</code> 都是 <strong>严格递增</strong> 的。</li>
	<li>这两个子数组必须是 <strong>相邻的</strong>，即 <code>b = a + k</code>。</li>
</ul>

<p>如果可以找到这样的 <strong>两个</strong> 子数组，请返回 <code>true</code>；否则返回 <code>false</code>。</p>

<p><strong>子数组</strong> 是数组中的一个连续<b> 非空</b> 的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,5,7,8,9,2,3,4,3,1], k = 3</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从下标 <code>2</code> 开始的子数组为 <code>[7, 8, 9]</code>，它是严格递增的。</li>
	<li>从下标 <code>5</code> 开始的子数组为 <code>[2, 3, 4]</code>，它也是严格递增的。</li>
	<li>两个子数组是相邻的，因此结果为 <code>true</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,2,3,4,4,4,4,5,6,7], k = 5</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= 2 * k &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Store the longest decreasing subarray starting and ending at an index.

## 示例

```
[2,5,7,8,9,2,3,4,3,1]
3
[1,2,3,4,4,4,4,5,6,7]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool hasIncreasingSubarrays(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasIncreasingSubarrays(IList<int> nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function(nums, k) {
    
};
```

### TypeScript

```typescript
function hasIncreasingSubarrays(nums: number[], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function hasIncreasingSubarrays($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasIncreasingSubarrays(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasIncreasingSubarrays(nums: List<Int>, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasIncreasingSubarrays(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func hasIncreasingSubarrays(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def has_increasing_subarrays(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def hasIncreasingSubarrays(nums: List[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-increasing-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec has_increasing_subarrays(Nums :: [integer()], K :: integer()) -> boolean().
has_increasing_subarrays(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_increasing_subarrays(nums :: [integer], k :: integer) :: boolean
  def has_increasing_subarrays(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasIncreasingSubarrays(nums: ArrayList<Int64>, k: Int64): Bool {

    }
}
```

