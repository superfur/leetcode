# 2826. 将三个组排序

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。<code>nums</code>&nbsp;的每个元素是 1，2 或 3。在每次操作中，你可以删除&nbsp;<code>nums</code>&nbsp;中的一个元素。返回使 nums 成为 <strong>非递减</strong>&nbsp;顺序所需操作数的 <strong>最小值</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,3,2,1]
<b>输出：</b>3
<b>解释：</b>
其中一个最优方案是删除 nums[0]，nums[2] 和 nums[3]。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,2,1,3,3]
<b>输出：</b>2
<b>解释：</b>
其中一个最优方案是删除 nums[1] 和 nums[2]。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [2,2,2,2,3,3]
<b>输出：</b>0
<b>解释：</b>
nums 已是非递减顺序的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 3</code></li>
</ul>

<p><strong>进阶：</strong>你可以使用&nbsp;<code>O(n)</code>&nbsp;时间复杂度以内的算法解决吗？</p>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 动态规划

## 提示

1. The problem asks to change the array nums to make it sorted (i.e., all the 1s are on the left of 2s, and all the 2s are on the left of 3s.).
2. We can try all the possibilities to make nums indices range in [0, i) to 0 and [i, j) to 1 and [j, n) to 2. Note the ranges are left-close and right-open; each might be empty. Namely, 0 <= i <= j <= n.
3. Count the changes we need for each possibility by comparing the expected and original values at each index position.

## 示例

```
[2,1,3,2,1]
[1,3,2,1,3,3]
[2,2,2,2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(nums: ArrayList<Int64>): Int64 {

    }
}
```

