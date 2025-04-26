# 2717. 半有序排列

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数排列 <code>nums</code> 。</p>

<p>如果排列的第一个数字等于 <code>1</code> 且最后一个数字等于 <code>n</code> ，则称其为 <strong>半有序排列</strong> 。你可以执行多次下述操作，直到将 <code>nums</code> 变成一个 <strong>半有序排列</strong> ：</p>

<ul>
	<li>选择 <code>nums</code> 中相邻的两个元素，然后交换它们。</li>
</ul>

<p>返回使 <code>nums</code> 变成 <strong>半有序排列</strong> 所需的最小操作次数。</p>

<p><strong>排列</strong> 是一个长度为 <code>n</code> 的整数序列，其中包含从 <code>1</code> 到 <code>n</code> 的每个数字恰好一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,4,3]
<strong>输出：</strong>2
<strong>解释：</strong>可以依次执行下述操作得到半有序排列：
1 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
2 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
可以证明，要让 nums 成为半有序排列，不存在执行操作少于 2 次的方案。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,1,3]
<strong>输出：</strong>3
<strong>解释：
</strong>可以依次执行下述操作得到半有序排列：
1 - 交换下标 1 和下标 2 对应元素。排列变为 [2,1,4,3] 。
2 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
3 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
可以证明，要让 nums 成为半有序排列，不存在执行操作少于 3 次的方案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,5]
<strong>输出：</strong>0
<strong>解释：</strong>这个排列已经是一个半有序排列，无需执行任何操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i]&nbsp;&lt;= 50</code></li>
	<li><code>nums</code> 是一个 <strong>排列</strong></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Find the index of elements 1 and n.
2. Let x be the position of 1 and y be the position of n. the answer is x + (n-y-1) if x < y and x + (n-y-1) - 1 if x > y.

## 示例

```
[2,1,4,3]
[2,4,1,3]
[1,3,4,2,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int semiOrderedPermutation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int semiOrderedPermutation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
```

### C

```c
int semiOrderedPermutation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SemiOrderedPermutation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var semiOrderedPermutation = function(nums) {
    
};
```

### TypeScript

```typescript
function semiOrderedPermutation(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function semiOrderedPermutation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func semiOrderedPermutation(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun semiOrderedPermutation(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int semiOrderedPermutation(List<int> nums) {
    
  }
}
```

### Go

```golang
func semiOrderedPermutation(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def semi_ordered_permutation(nums)
    
end
```

### Scala

```scala
object Solution {
    def semiOrderedPermutation(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn semi_ordered_permutation(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (semi-ordered-permutation nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec semi_ordered_permutation(Nums :: [integer()]) -> integer().
semi_ordered_permutation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec semi_ordered_permutation(nums :: [integer]) :: integer
  def semi_ordered_permutation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func semiOrderedPermutation(nums: Array<Int64>): Int64 {

    }
}
```

