# 2294. 划分数组使最大差为 K

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。你可以将 <code>nums</code> 划分成一个或多个 <strong>子序列</strong> ，使 <code>nums</code> 中的每个元素都 <strong>恰好</strong> 出现在一个子序列中。</p>

<p>在满足每个子序列中最大值和最小值之间的差值最多为 <code>k</code> 的前提下，返回需要划分的 <strong>最少</strong> 子序列数目。</p>

<p><strong>子序列</strong> 本质是一个序列，可以通过删除另一个序列中的某些元素（或者不删除）但不改变剩下元素的顺序得到。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,6,1,2,5], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>
可以将 nums 划分为两个子序列 [3,1,2] 和 [6,5] 。
第一个子序列中最大值和最小值的差值是 3 - 1 = 2 。
第二个子序列中最大值和最小值的差值是 6 - 5 = 1 。
由于创建了两个子序列，返回 2 。可以证明需要划分的最少子序列数目就是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], k = 1
<strong>输出：</strong>2
<strong>解释：</strong>
可以将 nums 划分为两个子序列 [1,2] 和 [3] 。
第一个子序列中最大值和最小值的差值是 2 - 1 = 1 。
第二个子序列中最大值和最小值的差值是 3 - 3 = 0 。
由于创建了两个子序列，返回 2 。注意，另一种最优解法是将 nums 划分成子序列 [1] 和 [2,3] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,4,5], k = 0
<strong>输出：</strong>3
<strong>解释：</strong>
可以将 nums 划分为三个子序列 [2,2]、[4] 和 [5] 。
第一个子序列中最大值和最小值的差值是 2 - 2 = 0 。
第二个子序列中最大值和最小值的差值是 4 - 4 = 0 。
第三个子序列中最大值和最小值的差值是 5 - 5 = 0 。
由于创建了三个子序列，返回 3 。可以证明需要划分的最少子序列数目就是 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Which values in each subsequence matter? The only values that matter are the maximum and minimum values.
2. Let the maximum and minimum values of a subsequence be Max and Min. It is optimal to place all values in between Max and Min in the original array in the same subsequence as Max and Min.
3. Sort the array.

## 示例

```
[3,6,1,2,5]
2
[1,2,3]
1
[2,2,4,5]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int partitionArray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int partitionArray(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int PartitionArray(int[] nums, int k) {
        
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
var partitionArray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function partitionArray(nums: number[], k: number): number {
    
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
    function partitionArray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func partitionArray(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun partitionArray(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int partitionArray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func partitionArray(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def partition_array(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def partitionArray(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (partition-array nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec partition_array(Nums :: [integer()], K :: integer()) -> integer().
partition_array(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec partition_array(nums :: [integer], k :: integer) :: integer
  def partition_array(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func partitionArray(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

