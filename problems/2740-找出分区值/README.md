# 2740. 找出分区值

## 题目描述

<p>给你一个 <strong>正</strong> 整数数组 <code>nums</code> 。</p>

<p>将 <code>nums</code> 分成两个数组：<code>nums1</code> 和 <code>nums2</code> ，并满足下述条件：</p>

<ul>
	<li>数组 <code>nums</code> 中的每个元素都属于数组 <code>nums1</code> 或数组 <code>nums2</code> 。</li>
	<li>两个数组都 <strong>非空</strong> 。</li>
	<li>分区值 <strong>最小</strong> 。</li>
</ul>

<p>分区值的计算方法是 <code>|max(nums1) - min(nums2)|</code> 。</p>

<p>其中，<code>max(nums1)</code> 表示数组 <code>nums1</code> 中的最大元素，<code>min(nums2)</code> 表示数组 <code>nums2</code> 中的最小元素。</p>

<p>返回表示分区值的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,2,4]
<strong>输出：</strong>1
<strong>解释：</strong>可以将数组 nums 分成 nums1 = [1,2] 和 nums2 = [3,4] 。
- 数组 nums1 的最大值等于 2 。
- 数组 nums2 的最小值等于 3 。
分区值等于 |2 - 3| = 1 。
可以证明 1 是所有分区方案的最小值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [100,1,10]
<strong>输出：</strong>9
<strong>解释：</strong>可以将数组 nums 分成 nums1 = [10] 和 nums2 = [100,1] 。 
- 数组 nums1 的最大值等于 10 。 
- 数组 nums2 的最小值等于 1 。 
分区值等于 |10 - 1| = 9 。 
可以证明 9 是所有分区方案的最小值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 提示

1. Sort the array.
2. The answer is min(nums[i+1] - nums[i]) for all i in the range [0, n-2].

## 示例

```
[1,3,2,4]
[100,1,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findValueOfPartition(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findValueOfPartition(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        
```

### C

```c
int findValueOfPartition(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindValueOfPartition(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findValueOfPartition = function(nums) {
    
};
```

### TypeScript

```typescript
function findValueOfPartition(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findValueOfPartition($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findValueOfPartition(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findValueOfPartition(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findValueOfPartition(List<int> nums) {
    
  }
}
```

### Go

```golang
func findValueOfPartition(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_value_of_partition(nums)
    
end
```

### Scala

```scala
object Solution {
    def findValueOfPartition(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_value_of_partition(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-value-of-partition nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_value_of_partition(Nums :: [integer()]) -> integer().
find_value_of_partition(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_value_of_partition(nums :: [integer]) :: integer
  def find_value_of_partition(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findValueOfPartition(nums: Array<Int64>): Int64 {

    }
}
```

