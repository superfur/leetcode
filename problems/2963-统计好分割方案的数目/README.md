# 2963. 统计好分割方案的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、由 <strong>正整数</strong> 组成的数组 <code>nums</code>。</p>

<p>将数组分割成一个或多个<strong> 连续</strong> 子数组，如果不存在包含了相同数字的两个子数组，则认为是一种 <strong>好分割方案</strong> 。</p>

<p>返回 <code>nums</code> 的 <strong>好分割方案</strong> 的 <strong>数目</strong>。</p>

<p>由于答案可能很大，请返回答案对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>8
<strong>解释：</strong>有 8 种 <strong>好分割方案 </strong>：([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]) 和 ([1,2,3,4]) 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1]
<strong>输出：</strong>1
<strong>解释：</strong>唯一的 <strong>好分割方案</strong> 是：([1,1,1,1]) 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,3]
<strong>输出：</strong>2
<strong>解释：</strong>有 2 种<strong> 好分割方案 </strong>：([1,2,1], [3]) 和 ([1,2,1,3]) 。
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

- 数组
- 哈希表
- 数学
- 组合数学

## 提示

1. If a segment contains a value, it must contain all occurrences of the same value.
2. Partition the array into segments making each one as short as possible. This can be achieved by two-pointers or using a Set.
3. If we have <code>m</code> segments, we can arbitrarily group the neighboring segments. How many ways are there to group these <code>m</code> segments?

## 示例

```
[1,2,3,4]
[1,1,1,1]
[1,2,1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfGoodPartitions(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfGoodPartitions(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        
```

### C

```c
int numberOfGoodPartitions(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfGoodPartitions(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodPartitions = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfGoodPartitions(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodPartitions($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfGoodPartitions(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfGoodPartitions(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfGoodPartitions(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfGoodPartitions(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def number_of_good_partitions(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfGoodPartitions(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_good_partitions(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-good-partitions nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_good_partitions(Nums :: [integer()]) -> integer().
number_of_good_partitions(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_good_partitions(nums :: [integer]) :: integer
  def number_of_good_partitions(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfGoodPartitions(nums: Array<Int64>): Int64 {

    }
}
```

