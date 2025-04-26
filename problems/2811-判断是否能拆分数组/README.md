# 2811. 判断是否能拆分数组

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>nums</code> 和一个整数 <code>m</code> 。请你判断能否执行一系列操作，将数组拆分成 <code>n</code> 个 <strong>非空 </strong>数组。</p>

<p>一个数组被称为 <strong>好</strong> 的，如果：</p>

<ul>
	<li>子数组的长度为 1 ，或者</li>
	<li>子数组元素之和 <strong>大于或等于</strong>&nbsp; <code>m</code> 。</li>
</ul>

<p>在每一步操作中，你可以选择一个 <strong>长度至少为 2</strong> 的现有数组（之前步骤的结果） 并将其拆分成 <strong>2</strong> 个子数组，而得到的 <strong>每个</strong> 子数组都需要是好的。</p>

<p>如果你可以将给定数组拆分成 <code>n</code> 个满足要求的数组，返回 <code>true</code><em> </em>；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2, 2, 1], m = 4</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将 <code>[2, 2, 1]</code> <span class="example-io">切分为</span> <code>[2, 2]</code> 和&nbsp;<code>[1]</code>。数组 <code>[1]</code> 的长度为 1，数组 <code>[2, 2]</code> 的元素之和等于 <code>4 &gt;= m</code>，所以两者都是好的数组。</li>
	<li>将 <code>[2, 2]</code> <span class="example-io">切分为</span> <code>[2]</code> 和&nbsp;<code>[2]</code>。两个数组的长度都是 1，所以都是好的数组。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [2, 1, 3], m = 5</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>第一步必须是以下之一：</p>

<ul>
	<li>将&nbsp;<code>[2, 1, 3]</code> <span class="example-io">切分为</span> <code>[2, 1]</code> 和&nbsp;<code>[3]</code>。数组&nbsp;<code>[2, 1]</code> 既不是长度为 1，也没有大于或等于 <code>m</code> 的元素和。</li>
	<li>将 <code>[2, 1, 3]</code> <span class="example-io">切分为</span> <code>[2]</code> 和 <code>[1, 3]</code>。数组&nbsp;<code>[1, 3]</code> 既不是长度为 1，也没有大于或等于 <code>m</code> 的元素和。</li>
</ul>

<p>因此，由于这两个操作都无效（它们没有将数组分成两个好的数组），因此我们无法将 <code>nums</code> 分成 <code>n</code> 个大小为 1 的数组。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [2, 3, 3, 2, 3], m = 6</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><span class="example-io">将&nbsp;<code>[2, 3, 3, 2, 3]</code>&nbsp;切分为&nbsp;<code>[2]</code> 和&nbsp;<code>[3, 3, 2, 3]</code>。</span></li>
	<li><span class="example-io">将 <code>[3, 3, 2, 3]</code> 切分为 <code>[3, 3, 2]</code> 和 <code>[3]</code>。</span></li>
	<li><span class="example-io">将 <code>[3, 3, 2]</code> 切分为 <code>[3, 3]</code> 和 <code>[2]</code>。</span></li>
	<li><span class="example-io">将 <code>[3, 3]</code> 切分为 <code>[3]</code> 和 <code>[3]</code>。</span></li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= m &lt;= 200</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. It can be proven that if you can split more than one element as a subarray, then you can split exactly one element.

## 示例

```
[2, 2, 1]
4
[2, 1, 3]
5
[2, 3, 3, 2, 3]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canSplitArray(vector<int>& nums, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canSplitArray(List<Integer> nums, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        
```

### C

```c
bool canSplitArray(int* nums, int numsSize, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanSplitArray(IList<int> nums, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {boolean}
 */
var canSplitArray = function(nums, m) {
    
};
```

### TypeScript

```typescript
function canSplitArray(nums: number[], m: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $m
     * @return Boolean
     */
    function canSplitArray($nums, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canSplitArray(_ nums: [Int], _ m: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canSplitArray(nums: List<Int>, m: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canSplitArray(List<int> nums, int m) {
    
  }
}
```

### Go

```golang
func canSplitArray(nums []int, m int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} m
# @return {Boolean}
def can_split_array(nums, m)
    
end
```

### Scala

```scala
object Solution {
    def canSplitArray(nums: List[Int], m: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_split_array(nums: Vec<i32>, m: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-split-array nums m)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_split_array(Nums :: [integer()], M :: integer()) -> boolean().
can_split_array(Nums, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_split_array(nums :: [integer], m :: integer) :: boolean
  def can_split_array(nums, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canSplitArray(nums: ArrayList<Int64>, m: Int64): Bool {

    }
}
```

