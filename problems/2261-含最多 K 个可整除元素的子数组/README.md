# 2261. 含最多 K 个可整除元素的子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数 <code>k</code> 和 <code>p</code> ，找出并返回满足要求的不同的子数组数，要求子数组中最多 <code>k</code> 个可被 <code>p</code> 整除的元素。</p>

<p>如果满足下述条件之一，则认为数组 <code>nums1</code> 和 <code>nums2</code> 是 <strong>不同</strong> 数组：</p>

<ul>
	<li>两数组长度 <strong>不同</strong> ，或者</li>
	<li>存在 <strong>至少 </strong>一个下标 <code>i</code> 满足 <code>nums1[i] != nums2[i]</code> 。</li>
</ul>

<p><strong>子数组</strong> 定义为：数组中的连续元素组成的一个 <strong>非空</strong> 序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [<em><strong>2</strong></em>,3,3,<em><strong>2</strong></em>,<em><strong>2</strong></em>], k = 2, p = 2
<strong>输出：</strong>11
<strong>解释：</strong>
位于下标 0、3 和 4 的元素都可以被 p = 2 整除。
共计 11 个不同子数组都满足最多含 k = 2 个可以被 2 整除的元素：
[2]、[2,3]、[2,3,3]、[2,3,3,2]、[3]、[3,3]、[3,3,2]、[3,3,2,2]、[3,2]、[3,2,2] 和 [2,2] 。
注意，尽管子数组 [2] 和 [3] 在 nums 中出现不止一次，但统计时只计数一次。
子数组 [2,3,3,2,2] 不满足条件，因为其中有 3 个元素可以被 2 整除。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], k = 4, p = 1
<strong>输出：</strong>10
<strong>解释：</strong>
nums 中的所有元素都可以被 p = 1 整除。
此外，nums 中的每个子数组都满足最多 4 个元素可以被 1 整除。
因为所有子数组互不相同，因此满足所有限制条件的子数组总数为 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i], p &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以设计并实现时间复杂度为 <code>O(n<sup>2</sup>)</code> 的算法解决此问题吗？</p>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 枚举
- 哈希函数
- 滚动哈希

## 提示

1. Enumerate all subarrays and find the ones that satisfy all the conditions.
2. Use any suitable method to hash the subarrays to avoid duplicates.

## 示例

```
[2,3,3,2,2]
2
2
[1,2,3,4]
4
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDistinct(vector<int>& nums, int k, int p) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDistinct(int[] nums, int k, int p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
```

### C

```c
int countDistinct(int* nums, int numsSize, int k, int p) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDistinct(int[] nums, int k, int p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} p
 * @return {number}
 */
var countDistinct = function(nums, k, p) {
    
};
```

### TypeScript

```typescript
function countDistinct(nums: number[], k: number, p: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $p
     * @return Integer
     */
    function countDistinct($nums, $k, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDistinct(_ nums: [Int], _ k: Int, _ p: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDistinct(nums: IntArray, k: Int, p: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDistinct(List<int> nums, int k, int p) {
    
  }
}
```

### Go

```golang
func countDistinct(nums []int, k int, p int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} p
# @return {Integer}
def count_distinct(nums, k, p)
    
end
```

### Scala

```scala
object Solution {
    def countDistinct(nums: Array[Int], k: Int, p: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_distinct(nums: Vec<i32>, k: i32, p: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-distinct nums k p)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_distinct(Nums :: [integer()], K :: integer(), P :: integer()) -> integer().
count_distinct(Nums, K, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_distinct(nums :: [integer], k :: integer, p :: integer) :: integer
  def count_distinct(nums, k, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDistinct(nums: Array<Int64>, k: Int64, p: Int64): Int64 {

    }
}
```

