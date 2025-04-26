# 3196. 最大化子数组的总成本

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>。</p>

<p>子数组 <code>nums[l..r]</code>（其中 <code>0 &lt;= l &lt;= r &lt; n</code>）的 <strong>成本 </strong>定义为：</p>

<p><code>cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)<sup>r − l</sup></code></p>

<p>你的任务是将 <code>nums</code> 分割成若干子数组，使得所有子数组的成本之和 <strong>最大化</strong>，并确保每个元素 <strong>正好 </strong>属于一个子数组。</p>

<p>具体来说，如果 <code>nums</code> 被分割成 <code>k</code> 个子数组，且分割点为索引 <code>i<sub>1</sub>, i<sub>2</sub>, ..., i<sub>k − 1</sub></code>（其中 <code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>k - 1</sub> &lt; n - 1</code>），则总成本为：</p>

<p><code>cost(0, i<sub>1</sub>) + cost(i<sub>1</sub> + 1, i<sub>2</sub>) + ... + cost(i<sub>k − 1</sub> + 1, n − 1)</code></p>

<p>返回在最优分割方式下的子数组成本之和的最大值。</p>

<p><strong>注意：</strong>如果 <code>nums</code> 没有被分割，即 <code>k = 1</code>，则总成本即为 <code>cost(0, n - 1)</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,-2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">10</span></p>

<p><strong>解释：</strong></p>

<p>一种总成本最大化的方法是将 <code>[1, -2, 3, 4]</code> 分割成子数组 <code>[1, -2, 3]</code> 和 <code>[4]</code>。总成本为 <code>(1 + 2 + 3) + 4 = 10</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,-1,1,-1]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>一种总成本最大化的方法是将 <code>[1, -1, 1, -1]</code> 分割成子数组 <code>[1, -1]</code> 和 <code>[1, -1]</code>。总成本为 <code>(1 + 1) + (1 + 1) = 4</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0]</span></p>

<p><strong>输出：</strong> 0</p>

<p><strong>解释：</strong></p>

<p>无法进一步分割数组，因此答案为 0。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,-1]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>选择整个数组，总成本为 <code>1 + 1 = 2</code>，这是可能的最大成本。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. The problem can be solved using dynamic programming.
2. Since we can always start a new subarray, the problem is the same as selecting some elements in the array and flipping their signs to negative to maximize the sum. However, we cannot flip the signs of 2 consecutive elements, and the first element in the array cannot be negative.
3. Let <code>dp[i][0/1]</code> be the largest sum we can get for prefix <code>nums[0..i]</code>, where <code>dp[i][0]</code> is the maximum if the <code>i<sup>th</sup></code> element wasn't flipped, and <code>dp[i][1]</code> is the maximum if the <code>i<sup>th</sup></code> element was flipped.
4. Based on the restriction:<br />
<code>dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]</code><br />
<code>dp[i][1] = dp[i - 1][0] - nums[i]</code>
5. The initial state is:<br />
<code>dp[1][0] = nums[0] + nums[1]</code><br />
<code>dp[1][1] = nums[0] - nums[1]</code><br />
and the answer is <code>max(dp[n - 1][0], dp[n - 1][1])</code>.
6. Can you optimize the space complexity?

## 示例

```
[1,-2,3,4]
[1,-1,1,-1]
[0]
[1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumTotalCost(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumTotalCost(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        
```

### C

```c
long long maximumTotalCost(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumTotalCost(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTotalCost = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumTotalCost(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumTotalCost($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTotalCost(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTotalCost(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTotalCost(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumTotalCost(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_total_cost(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumTotalCost(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_total_cost(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-total-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_total_cost(Nums :: [integer()]) -> integer().
maximum_total_cost(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_total_cost(nums :: [integer]) :: integer
  def maximum_total_cost(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTotalCost(nums: Array<Int64>): Int64 {

    }
}
```

