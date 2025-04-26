# 2799. 统计完全子数组的数目

## 题目描述

<p>给你一个由 <strong>正</strong> 整数组成的数组 <code>nums</code> 。</p>

<p>如果数组中的某个子数组满足下述条件，则称之为 <strong>完全子数组</strong> ：</p>

<ul>
	<li>子数组中 <strong>不同</strong> 元素的数目等于整个数组不同元素的数目。</li>
</ul>

<p>返回数组中 <strong>完全子数组</strong> 的数目。</p>

<p><strong>子数组</strong> 是数组中的一个连续非空序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,1,2,2]
<strong>输出：</strong>4
<strong>解释：</strong>完全子数组有：[1,3,1,2]、[1,3,1,2,2]、[3,1,2] 和 [3,1,2,2] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [5,5,5,5]
<strong>输出：</strong>10
<strong>解释：</strong>数组仅由整数 5 组成，所以任意子数组都满足完全子数组的条件。子数组的总数为 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. Let’s say k is the number of distinct elements in the array. Our goal is to find the number of subarrays with k distinct elements.
2. Since the constraints are small, you can check every subarray.

## 示例

```
[1,3,1,2,2]
[5,5,5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCompleteSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
int countCompleteSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCompleteSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function countCompleteSubarrays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countCompleteSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCompleteSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCompleteSubarrays(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCompleteSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func countCompleteSubarrays(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_complete_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def countCompleteSubarrays(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-complete-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_complete_subarrays(Nums :: [integer()]) -> integer().
count_complete_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_complete_subarrays(nums :: [integer]) :: integer
  def count_complete_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCompleteSubarrays(nums: Array<Int64>): Int64 {

    }
}
```

