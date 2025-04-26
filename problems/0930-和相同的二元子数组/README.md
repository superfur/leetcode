# 930. 和相同的二元子数组

## 题目描述

<p>给你一个二元数组 <code>nums</code> ，和一个整数 <code>goal</code> ，请你统计并返回有多少个和为 <code>goal</code> 的<strong> 非空</strong> 子数组。</p>

<p><strong>子数组</strong> 是数组的一段连续部分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,0,1], goal = 2
<strong>输出：</strong>4
<strong>解释：</strong>
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0,0,0], goal = 0
<strong>输出：</strong>15
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>nums[i]</code> 不是 <code>0</code> 就是 <code>1</code></li>
	<li><code>0 <= goal <= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和
- 滑动窗口

## 示例

```
[1,0,1,0,1]
2
[0,0,0,0,0]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
```

### C

```c
int numSubarraysWithSum(int* nums, int numsSize, int goal) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSubarraysWithSum(int[] nums, int goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function(nums, goal) {
    
};
```

### TypeScript

```typescript
function numSubarraysWithSum(nums: number[], goal: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $goal
     * @return Integer
     */
    function numSubarraysWithSum($nums, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSubarraysWithSum(_ nums: [Int], _ goal: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSubarraysWithSum(nums: IntArray, goal: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSubarraysWithSum(List<int> nums, int goal) {
    
  }
}
```

### Go

```golang
func numSubarraysWithSum(nums []int, goal int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} goal
# @return {Integer}
def num_subarrays_with_sum(nums, goal)
    
end
```

### Scala

```scala
object Solution {
    def numSubarraysWithSum(nums: Array[Int], goal: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-subarrays-with-sum nums goal)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_subarrays_with_sum(Nums :: [integer()], Goal :: integer()) -> integer().
num_subarrays_with_sum(Nums, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_subarrays_with_sum(nums :: [integer], goal :: integer) :: integer
  def num_subarrays_with_sum(nums, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSubarraysWithSum(nums: Array<Int64>, goal: Int64): Int64 {

    }
}
```

