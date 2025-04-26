# 1877. 数组中最大数对和的最小值

## 题目描述

<p>一个数对 <code>(a,b)</code> 的 <strong>数对和</strong> 等于 <code>a + b</code> 。<strong>最大数对和</strong> 是一个数对数组中最大的 <strong>数对和</strong> 。</p>

<ul>
	<li>比方说，如果我们有数对 <code>(1,5)</code> ，<code>(2,3)</code> 和 <code>(4,4)</code>，<strong>最大数对和</strong> 为 <code>max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8</code> 。</li>
</ul>

<p>给你一个长度为 <strong>偶数</strong> <code>n</code> 的数组 <code>nums</code> ，请你将 <code>nums</code> 中的元素分成 <code>n / 2</code> 个数对，使得：</p>

<ul>
	<li><code>nums</code> 中每个元素 <strong>恰好</strong> 在 <strong>一个</strong> 数对中，且</li>
	<li><strong>最大数对和</strong> 的值 <strong>最小</strong> 。</li>
</ul>

<p>请你在最优数对划分的方案下，返回最小的 <strong>最大数对和</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,5,2,3]
<b>输出：</b>7
<b>解释：</b>数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [3,5,4,2,4,6]
<b>输出：</b>8
<b>解释：</b>数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 是 <strong>偶数</strong> 。</li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 提示

1. Would sorting help find the optimal order?
2. Given a specific element, how would you minimize its specific pairwise sum?

## 示例

```
[3,5,2,3]
[3,5,4,2,4,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minPairSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
```

### C

```c
int minPairSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinPairSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    
};
```

### TypeScript

```typescript
function minPairSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minPairSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minPairSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minPairSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func minPairSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_pair_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def minPairSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_pair_sum(Nums :: [integer()]) -> integer().
min_pair_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_pair_sum(nums :: [integer]) :: integer
  def min_pair_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minPairSum(nums: Array<Int64>): Int64 {

    }
}
```

