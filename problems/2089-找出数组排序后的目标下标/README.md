# 2089. 找出数组排序后的目标下标

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 以及一个目标元素 <code>target</code> 。</p>

<p><strong>目标下标</strong> 是一个满足&nbsp;<code>nums[i] == target</code> 的下标 <code>i</code> 。</p>

<p>将 <code>nums</code> 按 <strong>非递减</strong> 顺序排序后，返回由 <code>nums</code> 中目标下标组成的列表。如果不存在目标下标，返回一个 <strong>空</strong> 列表。返回的列表必须按 <strong>递增</strong> 顺序排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 2
<strong>输出：</strong>[1,2]
<strong>解释：</strong>排序后，nums 变为 [1,<em><strong>2</strong></em>,<em><strong>2</strong></em>,3,5] 。
满足 nums[i] == 2 的下标是 1 和 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 3
<strong>输出：</strong>[3]
<strong>解释：</strong>排序后，nums 变为 [1,2,2,<em><strong>3</strong></em>,5] 。
满足 nums[i] == 3 的下标是 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 5
<strong>输出：</strong>[4]
<strong>解释：</strong>排序后，nums 变为 [1,2,2,3,<em><strong>5</strong></em>] 。
满足 nums[i] == 5 的下标是 4 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 4
<strong>输出：</strong>[]
<strong>解释：</strong>nums 中不含值为 4 的元素。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 二分查找
- 排序

## 提示

1. Try "sorting" the array first.
2. Now find all indices in the array whose values are equal to target.

## 示例

```
[1,2,5,2,3]
2
[1,2,5,2,3]
3
[1,2,5,2,3]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> TargetIndices(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    
};
```

### TypeScript

```typescript
function targetIndices(nums: number[], target: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function targetIndices($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun targetIndices(nums: IntArray, target: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> targetIndices(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func targetIndices(nums []int, target int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def target_indices(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def targetIndices(nums: Array[Int], target: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (target-indices nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec target_indices(Nums :: [integer()], Target :: integer()) -> [integer()].
target_indices(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec target_indices(nums :: [integer], target :: integer) :: [integer]
  def target_indices(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func targetIndices(nums: Array<Int64>, target: Int64): ArrayList<Int64> {

    }
}
```

