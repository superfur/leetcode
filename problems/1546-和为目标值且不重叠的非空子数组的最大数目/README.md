# 1546. 和为目标值且不重叠的非空子数组的最大数目

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>target</code>&nbsp;。</p>

<p>请你返回&nbsp;<strong>非空不重叠</strong>&nbsp;子数组的最大数目，且每个子数组中数字和都为 <code>target</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,1,1], target = 2
<strong>输出：</strong>2
<strong>解释：</strong>总共有 2 个不重叠子数组（加粗数字表示） [<strong>1,1</strong>,1,<strong>1,1</strong>] ，它们的和为目标值 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [-1,3,5,1,4,2,-9], target = 6
<strong>输出：</strong>2
<strong>解释：</strong>总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [-2,6,6,3,5,4,1,2,8], target = 10
<strong>输出：</strong>3
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums = [0,0,0], target = 0
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;=&nbsp;10^5</code></li>
	<li><code>-10^4 &lt;= nums[i] &lt;=&nbsp;10^4</code></li>
	<li><code>0 &lt;= target &lt;= 10^6</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 前缀和

## 提示

1. Keep track of prefix sums to quickly look up what subarray that sums "target" can be formed at each step of scanning the input array.
2. It can be proved that greedily forming valid subarrays as soon as one is found is optimal.

## 示例

```
[1,1,1,1,1]
2
[-1,3,5,1,4,2,-9]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNonOverlapping(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNonOverlapping(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int maxNonOverlapping(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNonOverlapping(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var maxNonOverlapping = function(nums, target) {
    
};
```

### TypeScript

```typescript
function maxNonOverlapping(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function maxNonOverlapping($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNonOverlapping(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNonOverlapping(nums: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNonOverlapping(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func maxNonOverlapping(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def max_non_overlapping(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def maxNonOverlapping(nums: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_non_overlapping(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-non-overlapping nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_non_overlapping(Nums :: [integer()], Target :: integer()) -> integer().
max_non_overlapping(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_non_overlapping(nums :: [integer], target :: integer) :: integer
  def max_non_overlapping(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNonOverlapping(nums: Array<Int64>, target: Int64): Int64 {

    }
}
```

