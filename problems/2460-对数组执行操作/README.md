# 2460. 对数组执行操作

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>nums</code> ，数组大小为 <code>n</code> ，且由 <strong>非负</strong> 整数组成。</p>

<p>你需要对数组执行 <code>n - 1</code> 步操作，其中第 <code>i</code> 步操作（从 <strong>0</strong> 开始计数）要求对 <code>nums</code> 中第 <code>i</code> 个元素执行下述指令：</p>

<ul>
	<li>如果 <code>nums[i] == nums[i + 1]</code> ，则 <code>nums[i]</code> 的值变成原来的 <code>2</code> 倍，<code>nums[i + 1]</code> 的值变成 <code>0</code> 。否则，跳过这步操作。</li>
</ul>

<p>在执行完 <strong>全部</strong> 操作后，将所有 <code>0</code> <strong>移动</strong> 到数组的 <strong>末尾</strong> 。</p>

<ul>
	<li>例如，数组 <code>[1,0,2,0,0,1]</code> 将所有 <code>0</code> 移动到末尾后变为 <code>[1,2,1,0,0,0]</code> 。</li>
</ul>

<p>返回结果数组。</p>

<p><strong>注意</strong> 操作应当 <strong>依次有序</strong> 执行，而不是一次性全部执行。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,1,1,0]
<strong>输出：</strong>[1,4,2,0,0,0]
<strong>解释：</strong>执行以下操作：
- i = 0: nums[0] 和 nums[1] 不相等，跳过这步操作。
- i = 1: nums[1] 和 nums[2] 相等，nums[1] 的值变成原来的 2 倍，nums[2] 的值变成 0 。数组变成 [1,<em><strong>4</strong></em>,<em><strong>0</strong></em>,1,1,0] 。
- i = 2: nums[2] 和 nums[3] 不相等，所以跳过这步操作。
- i = 3: nums[3] 和 nums[4] 相等，nums[3] 的值变成原来的 2 倍，nums[4] 的值变成 0 。数组变成 [1,4,0,<em><strong>2</strong></em>,<em><strong>0</strong></em>,0] 。
- i = 4: nums[4] 和 nums[5] 相等，nums[4] 的值变成原来的 2 倍，nums[5] 的值变成 0 。数组变成 [1,4,0,2,<em><strong>0</strong></em>,<em><strong>0</strong></em>] 。
执行完所有操作后，将 0 全部移动到数组末尾，得到结果数组 [1,4,2,0,0,0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[1,0]
<strong>解释：</strong>无法执行任何操作，只需要将 0 移动到末尾。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 模拟

## 提示

1. Iterate over the array and simulate the described process.

## 示例

```
[1,2,2,1,1,0]
[0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] applyOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* applyOperations(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ApplyOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function applyOperations(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function applyOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func applyOperations(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun applyOperations(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> applyOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func applyOperations(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def apply_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def applyOperations(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn apply_operations(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (apply-operations nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec apply_operations(Nums :: [integer()]) -> [integer()].
apply_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec apply_operations(nums :: [integer]) :: [integer]
  def apply_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func applyOperations(nums: Array<Int64>): Array<Int64> {

    }
}
```

