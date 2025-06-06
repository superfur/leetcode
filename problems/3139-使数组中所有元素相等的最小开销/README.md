# 3139. 使数组中所有元素相等的最小开销

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和两个整数&nbsp;<code>cost1</code> 和&nbsp;<code>cost2</code>&nbsp;。你可以执行以下&nbsp;<strong>任一</strong>&nbsp;操作&nbsp;<strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>从 <code>nums</code>&nbsp;中选择下标 <code>i</code>&nbsp;并且将 <code>nums[i]</code>&nbsp;<strong>增加</strong> <code>1</code>&nbsp;，开销为 <code>cost1</code>。</li>
	<li>选择 <code>nums</code>&nbsp;中两个 <strong>不同</strong>&nbsp;下标 <code>i</code>&nbsp;和 <code>j</code>&nbsp;，并且将 <code>nums[i]</code>&nbsp;和 <code>nums[j]</code>&nbsp;都&nbsp;<strong>增加</strong> <code>1</code>&nbsp;，开销为 <code>cost2</code>&nbsp;。</li>
</ul>

<p>你的目标是使数组中所有元素都 <strong>相等</strong>&nbsp;，请你返回需要的 <strong>最小开销</strong>&nbsp;之和。</p>

<p>由于答案可能会很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [4,1], cost1 = 5, cost2 = 2</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><strong>解释：</strong></p>

<p>执行以下操作可以使数组中所有元素相等：</p>

<ul>
	<li>将&nbsp;<code>nums[1]</code>&nbsp;增加 1 ，开销为 5 ，<code>nums</code> 变为&nbsp;<code>[4,2]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[1]</code>&nbsp;增加 1 ，开销为 5 ，<code>nums</code> 变为&nbsp;<code>[4,3]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[1]</code>&nbsp;增加 1 ，开销为 5 ，<code>nums</code> 变为&nbsp;<code>[4,4]</code>&nbsp;。</li>
</ul>

<p>总开销为 15 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,3,3,3,5], cost1 = 2, cost2 = 1</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><b>解释：</b></p>

<p>执行以下操作可以使数组中所有元素相等：</p>

<ul>
	<li>将&nbsp;<code>nums[0]</code> 和&nbsp;<code>nums[1]</code>&nbsp;同时增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[3,4,3,3,5]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[0]</code> 和&nbsp;<code>nums[2]</code>&nbsp;同时增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[4,4,4,3,5]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[0]</code> 和&nbsp;<code>nums[3]</code>&nbsp;同时增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[5,4,4,4,5]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[1]</code> 和&nbsp;<code>nums[2]</code>&nbsp;同时增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[5,5,5,4,5]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[3]</code>&nbsp;增加 1 ，开销为 2 ，<code>nums</code> 变为&nbsp;<code>[5,5,5,5,5]</code>&nbsp;。</li>
</ul>

<p>总开销为 6 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,5,3], cost1 = 1, cost2 = 3</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>执行以下操作可以使数组中所有元素相等：</p>

<ul>
	<li>将&nbsp;<code>nums[0]</code>&nbsp;增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[4,5,3]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[0]</code>&nbsp;增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[5,5,3]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[2]</code>&nbsp;增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[5,5,4]</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[2]</code>&nbsp;增加 1 ，开销为 1 ，<code>nums</code> 变为&nbsp;<code>[5,5,5]</code>&nbsp;。</li>
</ul>

<p>总开销为 4 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= cost1 &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= cost2 &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 枚举

## 提示

1. How can you determine the minimum cost if you know the maximum value in the array once all values are made equal?
2. If <code>cost2 > cost1 * 2</code>, we should just use <code>cost1</code> to change all the values to the maximum one.
3. Otherwise, it's optimal to choose the smallest two values and use <code>cost2</code> to increase both of them.
4. Since the maximum value is known, calculate the required increases to equalize all values, instead of naively simulating the operations.
5. There are not a lot of candidates for the maximum; we can try all of them and choose which uses the minimum number of operations.

## 示例

```
[4,1]
5
2
[2,3,3,3,5]
2
1
[3,5,3]
1
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCostToEqualizeArray(vector<int>& nums, int cost1, int cost2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        """
        :type nums: List[int]
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        
```

### C

```c
int minCostToEqualizeArray(int* nums, int numsSize, int cost1, int cost2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var minCostToEqualizeArray = function(nums, cost1, cost2) {
    
};
```

### TypeScript

```typescript
function minCostToEqualizeArray(nums: number[], cost1: number, cost2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $cost1
     * @param Integer $cost2
     * @return Integer
     */
    function minCostToEqualizeArray($nums, $cost1, $cost2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCostToEqualizeArray(_ nums: [Int], _ cost1: Int, _ cost2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCostToEqualizeArray(nums: IntArray, cost1: Int, cost2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCostToEqualizeArray(List<int> nums, int cost1, int cost2) {
    
  }
}
```

### Go

```golang
func minCostToEqualizeArray(nums []int, cost1 int, cost2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} cost1
# @param {Integer} cost2
# @return {Integer}
def min_cost_to_equalize_array(nums, cost1, cost2)
    
end
```

### Scala

```scala
object Solution {
    def minCostToEqualizeArray(nums: Array[Int], cost1: Int, cost2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost_to_equalize_array(nums: Vec<i32>, cost1: i32, cost2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost-to-equalize-array nums cost1 cost2)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost_to_equalize_array(Nums :: [integer()], Cost1 :: integer(), Cost2 :: integer()) -> integer().
min_cost_to_equalize_array(Nums, Cost1, Cost2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost_to_equalize_array(nums :: [integer], cost1 :: integer, cost2 :: integer) :: integer
  def min_cost_to_equalize_array(nums, cost1, cost2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCostToEqualizeArray(nums: Array<Int64>, cost1: Int64, cost2: Int64): Int64 {

    }
}
```

