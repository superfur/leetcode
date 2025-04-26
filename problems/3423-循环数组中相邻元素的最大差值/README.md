# 3423. 循环数组中相邻元素的最大差值

## 题目描述

<p>给你一个 <strong>循环</strong>&nbsp;数组&nbsp;<code>nums</code>&nbsp;，请你找出相邻元素之间的&nbsp;<strong>最大</strong>&nbsp;绝对差值。</p>

<p><b>注意：</b>一个循环数组中，第一个元素和最后一个元素是相邻的。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,4]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>由于&nbsp;<code>nums</code>&nbsp;是循环的，<code>nums[0]</code> 和&nbsp;<code>nums[2]</code>&nbsp;是相邻的，它们之间的绝对差值是最大值&nbsp;<code>|4 - 1| = 3</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [-5,-10,-5]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<p>相邻元素&nbsp;<code>nums[0]</code> 和&nbsp;<code>nums[1]</code>&nbsp;之间的绝对差值为最大值&nbsp;<code>|-5 - (-10)| = 5</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Traverse from the second element to the last element and check the difference of every adjacent pair.
2. The edge case is to check the difference between the first and last elements.

## 示例

```
[1,2,4]
[-5,-10,-5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxAdjacentDistance(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
```

### C

```c
int maxAdjacentDistance(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxAdjacentDistance(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function(nums) {
    
};
```

### TypeScript

```typescript
function maxAdjacentDistance(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAdjacentDistance($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAdjacentDistance(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAdjacentDistance(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAdjacentDistance(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxAdjacentDistance(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_adjacent_distance(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxAdjacentDistance(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-adjacent-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_adjacent_distance(Nums :: [integer()]) -> integer().
max_adjacent_distance(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_adjacent_distance(nums :: [integer]) :: integer
  def max_adjacent_distance(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAdjacentDistance(nums: Array<Int64>): Int64 {

    }
}
```

