# 1681. 最小不兼容性

## 题目描述

<p>给你一个整数数组 <code>nums</code>​​​ 和一个整数 <code>k</code> 。你需要将这个数组划分到 <code>k</code> 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。</p>

<p>一个子集的 <strong>不兼容性</strong> 是该子集里面最大值和最小值的差。</p>

<p>请你返回将数组分成 <code>k</code> 个子集后，各子集 <strong>不兼容性 </strong>的<strong> 和</strong> 的 <strong>最小值</strong> ，如果无法分成分成 <code>k</code> 个子集，返回 <code>-1</code> 。</p>

<p>子集的定义是数组中一些数字的集合，对数字顺序没有要求。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,1,4], k = 2
<b>输出：</b>4
<b>解释：</b>最优的分配是 [1,2] 和 [1,4] 。
不兼容性和为 (2-1) + (4-1) = 4 。
注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [6,3,8,1,3,1,2,2], k = 4
<b>输出：</b>6
<b>解释：</b>最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [5,3,3,6,3,3], k = 3
<b>输出：</b>-1
<b>解释：</b>没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= nums.length <= 16</code></li>
	<li><code>nums.length</code> 能被 <code>k</code> 整除。</li>
	<li><code>1 <= nums[i] <= nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. The constraints are small enough for a backtrack solution but not any backtrack solution
2. If we use a naive n^k don't you think it can be optimized

## 示例

```
[1,2,1,4]
2
[6,3,8,1,3,1,2,2]
4
[5,3,3,6,3,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumIncompatibility(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minimumIncompatibility(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumIncompatibility(int[] nums, int k) {
        
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
var minimumIncompatibility = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minimumIncompatibility(nums: number[], k: number): number {
    
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
    function minimumIncompatibility($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumIncompatibility(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumIncompatibility(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumIncompatibility(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minimumIncompatibility(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_incompatibility(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumIncompatibility(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_incompatibility(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-incompatibility nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_incompatibility(Nums :: [integer()], K :: integer()) -> integer().
minimum_incompatibility(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_incompatibility(nums :: [integer], k :: integer) :: integer
  def minimum_incompatibility(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumIncompatibility(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

