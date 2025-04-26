# 3177. 求出最长好子序列 II

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>非负</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。如果一个整数序列&nbsp;<code>seq</code>&nbsp;满足在范围下标范围&nbsp;<code>[0, seq.length - 2]</code>&nbsp;中存在 <strong>不超过</strong>&nbsp;<code>k</code>&nbsp;个下标 <code>i</code>&nbsp;满足&nbsp;<code>seq[i] != seq[i + 1]</code>&nbsp;，那么我们称这个整数序列为&nbsp;<strong>好</strong>&nbsp;序列。</p>

<p>请你返回 <code>nums</code>&nbsp;中&nbsp;<strong>好</strong> <span data-keyword="subsequence-array">子序列</span>&nbsp;的最长长度</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,1,1,3], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>最长好子序列为&nbsp;<code>[<em><strong>1</strong></em>,<em><strong>2</strong></em>,<strong><em>1</em></strong>,<em><strong>1</strong></em>,3]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,5,1], k = 0</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>最长好子序列为&nbsp;<code>[<strong><em>1</em></strong>,2,3,4,5,<strong><em>1</em></strong>]</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>3</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= min(50, nums.length)</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 动态规划

## 提示

1. The absolute values in <code>nums</code> don’t really matter. So we can remap the set of values to the range <code>[0, n - 1]</code>.
2. Let <code>dp[i][j]</code> be the length of the longest subsequence till index <code>j</code> with at most <code>i</code> positions such that <code>seq[i] != seq[i + 1]</code>.
3. For each value <code>x</code> from left to right, update <code>dp[i][x] = max(dp[i][x] + 1, dp[i - 1][y] + 1)</code>, where <code>y != x</code>.

## 示例

```
[1,2,1,1,3]
2
[1,2,3,4,5,1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLength(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumLength(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLength(int[] nums, int k) {
        
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
var maximumLength = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumLength(nums: number[], k: number): number {
    
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
    function maximumLength($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLength(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumLength(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length(Nums :: [integer()], K :: integer()) -> integer().
maximum_length(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer], k :: integer) :: integer
  def maximum_length(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLength(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

