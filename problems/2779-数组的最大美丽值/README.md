# 2779. 数组的最大美丽值

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个 <strong>非负</strong> 整数 <code>k</code> 。</p>

<p>在一步操作中，你可以执行下述指令：</p>

<ul>
	<li>在范围&nbsp;<code>[0, nums.length - 1]</code> 中选择一个 <strong>此前没有选过</strong> 的下标 <code>i</code> 。</li>
	<li>将 <code>nums[i]</code> 替换为范围 <code>[nums[i] - k, nums[i] + k]</code> 内的任一整数。</li>
</ul>

<p>数组的 <strong>美丽值</strong> 定义为数组中由相等元素组成的最长子序列的长度。</p>

<p>对数组 <code>nums</code> 执行上述操作任意次后，返回数组可能取得的 <strong>最大</strong> 美丽值。</p>

<p><strong>注意：</strong>你 <strong>只</strong> 能对每个下标执行 <strong>一次</strong> 此操作。</p>

<p>数组的 <strong>子序列</strong> 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,6,1,2], k = 2
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，我们执行下述操作：
- 选择下标 1 ，将其替换为 4（从范围 [4,8] 中选出），此时 nums = [4,4,1,2] 。
- 选择下标 3 ，将其替换为 4（从范围 [0,4] 中选出），此时 nums = [4,4,1,4] 。
执行上述操作后，数组的美丽值是 3（子序列由下标 0 、1 、3 对应的元素组成）。
可以证明 3 是我们可以得到的由相等元素组成的最长子序列长度。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1], k = 10
<strong>输出：</strong>4
<strong>解释：</strong>在这个示例中，我们无需执行任何操作。
数组 nums 的美丽值是 4（整个数组）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 排序
- 滑动窗口

## 提示

1. Sort the array.
2. The problem becomes the following: find maximum subarray A[i … j] such that A[j] - A[i] ≤ 2 * k.

## 示例

```
[4,6,1,2]
2
[1,1,1,1]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumBeauty(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumBeauty(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumBeauty(int[] nums, int k) {
        
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
var maximumBeauty = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumBeauty(nums: number[], k: number): number {
    
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
    function maximumBeauty($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBeauty(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBeauty(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumBeauty(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumBeauty(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_beauty(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumBeauty(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_beauty(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-beauty nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_beauty(Nums :: [integer()], K :: integer()) -> integer().
maximum_beauty(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(nums :: [integer], k :: integer) :: integer
  def maximum_beauty(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBeauty(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

