# 面试题 16.17. 连续数列

## 题目描述

<p>给定一个整数数组，找出总和最大的连续数列，并返回总和。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong> [-2,1,-3,4,-1,2,1,-5,4]
<strong>输出：</strong> 6
<strong>解释：</strong> 连续子数组 [4,-1,2,1] 的和最大，为 6。
</pre>

<p><strong>进阶：</strong></p>

<p>如果你已经实现复杂度为 O(<em>n</em>) 的解法，尝试使用更为精妙的分治法求解。</p>


## 难度

Easy

## 标签

- 数组
- 分治
- 动态规划

## 提示

1. 把数字想象成正负交替的数字序列。注意，我们永远不会只包含一个正序列的一部分或者一个负序列的一部分。
2. 注意，如果你有一个和是负数的数列，那么其一定不是一个数列的开始或结束（如果它们连接了另外两个数列，那么就可以以一个数列的形式出现）。
3. 从数组的开头开始。当这个子数列增长时，它仍然是最佳子数列。然而，一旦变成负数，它就没有意义了。
4. 如果跟踪计算中的和，那就应该在子数列为负时立即重置它。我们永远不会在另一个子数列的开头或结尾添加一个和为负数的数列。
5. 你可以在O(N)时间复杂度和O(1)空间复杂度内解决此问题。

## 示例

```
[-2,1,-3,4,-1,2,1,-5,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSubArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSubArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSubArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSubArray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSubArray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSubArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSubArray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSubArray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sub-array nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sub_array(Nums :: [integer()]) -> integer().
max_sub_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sub_array(nums :: [integer]) :: integer
  def max_sub_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSubArray(nums: Array<Int64>): Int64 {

    }
}
```

