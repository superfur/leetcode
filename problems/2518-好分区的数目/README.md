# 2518. 好分区的数目

## 题目描述

<p>给你一个正整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p><strong>分区</strong> 的定义是：将数组划分成两个有序的 <strong>组</strong> ，并满足每个元素 <strong>恰好</strong> 存在于 <strong>某一个</strong> 组中。如果分区中每个组的元素和都大于等于 <code>k</code> ，则认为分区是一个好分区。</p>

<p>返回 <strong>不同</strong> 的好分区的数目。由于答案可能很大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后的结果。</p>

<p>如果在两个分区中，存在某个元素 <code>nums[i]</code> 被分在不同的组中，则认为这两个分区不同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], k = 4
<strong>输出：</strong>6
<strong>解释：</strong>好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) 和 ([4], [1,2,3]) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3,3], k = 4
<strong>输出：</strong>0
<strong>解释：</strong>数组中不存在好分区。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,6], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>可以将 nums[0] 放入第一个分区或第二个分区中。
好分区的情况是 ([6], [6]) 和 ([6], [6]) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, k &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. If the sum of the array is smaller than 2*k, then it is impossible to find a great partition.
2. Solve the reverse problem, that is, find the number of partitions where the sum of elements of at least one of the two groups is smaller than k.

## 示例

```
[1,2,3,4]
4
[3,3,3]
4
[6,6]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPartitions(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int countPartitions(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPartitions(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPartitions = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countPartitions(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countPartitions($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPartitions(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countPartitions(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_partitions(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countPartitions(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-partitions nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_partitions(Nums :: [integer()], K :: integer()) -> integer().
count_partitions(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_partitions(nums :: [integer], k :: integer) :: integer
  def count_partitions(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPartitions(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

