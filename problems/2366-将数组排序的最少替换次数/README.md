# 2366. 将数组排序的最少替换次数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。每次操作中，你可以将数组中任何一个元素替换为&nbsp;<strong>任意两个</strong>&nbsp;和为该元素的数字。</p>

<ul>
	<li>比方说，<code>nums = [5,6,7]</code>&nbsp;。一次操作中，我们可以将&nbsp;<code>nums[1]</code> 替换成&nbsp;<code>2</code> 和&nbsp;<code>4</code>&nbsp;，将&nbsp;<code>nums</code>&nbsp;转变成&nbsp;<code>[5,2,4,7]</code>&nbsp;。</li>
</ul>

<p>请你执行上述操作，将数组变成元素按 <strong>非递减</strong> 顺序排列的数组，并返回所需的最少操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,9,3]
<b>输出：</b>2
<b>解释：</b>以下是将数组变成非递减顺序的步骤：
- [3,9,3] ，将9 变成 3 和 6 ，得到数组 [3,3,6,3] 
- [3,3,6,3] ，将 6 变成 3 和 3 ，得到数组 [3,3,3,3,3] 
总共需要 2 步将数组变成非递减有序，所以我们返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5]
<b>输出：</b>0
<b>解释：</b>数组已经是非递减顺序，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 数学

## 提示

1. It is optimal to never make an operation to the last element of the array.
2. You can iterate from the second last element to the first. If the current value is greater than the previous bound, we want to break it into pieces so that the smaller one is as large as possible but not larger than the previous one.

## 示例

```
[3,9,3]
[1,2,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumReplacement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
```

### C

```c
long long minimumReplacement(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumReplacement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumReplacement = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumReplacement(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumReplacement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumReplacement(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumReplacement(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumReplacement(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumReplacement(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_replacement(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumReplacement(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-replacement nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_replacement(Nums :: [integer()]) -> integer().
minimum_replacement(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_replacement(nums :: [integer]) :: integer
  def minimum_replacement(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumReplacement(nums: Array<Int64>): Int64 {

    }
}
```

