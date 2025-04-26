# 698. 划分为k个相等的子集

## 题目描述

<p>给定一个整数数组&nbsp;&nbsp;<code>nums</code> 和一个正整数 <code>k</code>，找出是否有可能把这个数组分成 <code>k</code> 个非空子集，其总和都相等。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong> nums = [4, 3, 2, 3, 5, 2, 1], k = 4
<strong>输出：</strong> True
<strong>说明：</strong> 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3,4], k = 3
<strong>输出:</strong> false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= len(nums) &lt;= 16</code></li>
	<li><code>0 &lt; nums[i] &lt; 10000</code></li>
	<li>每个元素的频率在 <code>[1,4]</code> 范围内</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 记忆化搜索
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. We can figure out what target each subset must sum to.  Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.

## 示例

```
[4,3,2,3,5,2,1]
4
[1,2,3,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool canPartitionKSubsets(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanPartitionKSubsets(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function(nums, k) {
    
};
```

### TypeScript

```typescript
function canPartitionKSubsets(nums: number[], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function canPartitionKSubsets($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canPartitionKSubsets(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canPartitionKSubsets(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func canPartitionKSubsets(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_partition_k_subsets(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def canPartitionKSubsets(nums: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_partition_k_subsets(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-partition-k-subsets nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_partition_k_subsets(Nums :: [integer()], K :: integer()) -> boolean().
can_partition_k_subsets(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_partition_k_subsets(nums :: [integer], k :: integer) :: boolean
  def can_partition_k_subsets(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canPartitionKSubsets(nums: Array<Int64>, k: Int64): Bool {

    }
}
```

