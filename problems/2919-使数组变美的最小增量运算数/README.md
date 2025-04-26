# 2919. 使数组变美的最小增量运算数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> ，和一个整数 <code>k</code> 。</p>

<p>你可以执行下述 <strong>递增</strong> 运算 <strong>任意</strong> 次（可以是 <strong>0</strong> 次）：</p>

<ul>
	<li>从范围&nbsp;<code>[0, n - 1]</code> 中选择一个下标 <code>i</code> ，并将 <code>nums[i]</code> 的值加 <code>1</code> 。</li>
</ul>

<p>如果数组中任何长度 <strong>大于或等于 3</strong> 的子数组，其 <strong>最大</strong> 元素都大于或等于 <code>k</code> ，则认为数组是一个 <strong>美丽数组</strong> 。</p>

<p>以整数形式返回使数组变为 <strong>美丽数组</strong> 需要执行的 <strong>最小</strong> 递增运算数。</p>

<p>子数组是数组中的一个连续 <strong>非空</strong> 元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,0,0,2], k = 4
<strong>输出：</strong>3
<strong>解释：</strong>可以执行下述递增运算，使 nums 变为美丽数组：
选择下标 i = 1 ，并且将 nums[1] 的值加 1 -&gt; [2,4,0,0,2] 。
选择下标 i = 4 ，并且将 nums[4] 的值加 1 -&gt; [2,4,0,0,3] 。
选择下标 i = 4 ，并且将 nums[4] 的值加 1 -&gt; [2,4,0,0,4] 。
长度大于或等于 3 的子数组为 [2,4,0], [4,0,0], [0,0,4], [2,4,0,0], [4,0,0,4], [2,4,0,0,4] 。
在所有子数组中，最大元素都等于 k = 4 ，所以 nums 现在是美丽数组。
可以证明无法用少于 3 次递增运算使 nums 变为美丽数组。
因此，答案为 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,3,3], k = 5
<strong>输出：</strong>2
<strong>解释：</strong>可以执行下述递增运算，使 nums 变为美丽数组：
选择下标 i = 2 ，并且将 nums[2] 的值加 1 -&gt; [0,1,4,3] 。
选择下标 i = 2 ，并且将 nums[2] 的值加 1 -&gt; [0,1,5,3] 。
长度大于或等于 3 的子数组为 [0,1,5]、[1,5,3]、[0,1,5,3] 。
在所有子数组中，最大元素都等于 k = 5 ，所以 nums 现在是美丽数组。
可以证明无法用少于 2 次递增运算使 nums 变为美丽数组。 
因此，答案为 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2], k = 1
<strong>输出：</strong>0
<strong>解释：</strong>在这个示例中，只有一个长度大于或等于 3 的子数组 [1,1,2] 。
其最大元素 2 已经大于 k = 1 ，所以无需执行任何增量运算。
因此，答案为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. There needs to be at least one value among <code>3</code> consecutive values in the array that is greater than or equal to <code>k</code>.
2. The problem can be solved using dynamic programming.
3. Let <code>dp[i]</code> be the minimum number of increment operations required to make the subarray consisting of the first <code>i</code> values beautiful, while also having the value at <code>nums[i] >= k</code>.
4. <code>dp[0] = max(0, k - nums[0])</code>, <code>dp[1] = max(0, k - nums[1])</code>, and <code>dp[2] = max(0, k - nums[2])</code>.
5. <code>dp[i] = max(0, k - nums[i]) + min(dp[i - 1], dp[i - 2], dp[i - 3])</code> for <code>i</code> in the range <code>[3, n - 1]</code>.
6. The answer to the problem is <code>min(dp[n - 1], dp[n - 2], dp[n - 3])</code>.

## 示例

```
[2,3,0,0,2]
4
[0,1,3,3]
5
[1,1,2]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minIncrementOperations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long minIncrementOperations(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minIncrementOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long minIncrementOperations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinIncrementOperations(int[] nums, int k) {
        
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
var minIncrementOperations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minIncrementOperations(nums: number[], k: number): number {
    
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
    function minIncrementOperations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minIncrementOperations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minIncrementOperations(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minIncrementOperations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minIncrementOperations(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_increment_operations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minIncrementOperations(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_increment_operations(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-increment-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_increment_operations(Nums :: [integer()], K :: integer()) -> integer().
min_increment_operations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_increment_operations(nums :: [integer], k :: integer) :: integer
  def min_increment_operations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minIncrementOperations(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

