# 2862. 完全子集的最大元素和

## 题目描述

<p>给你一个下标从 <strong>1</strong> 开始、由 <code>n</code> 个整数组成的数组。你需要从&nbsp;<code>nums</code>&nbsp;选择一个&nbsp;<strong>完全集</strong>，其中每对元素下标的乘积都是一个 <span data-keyword="perfect-square">完全平方数</span>，例如选择&nbsp;<code>a<sub>i</sub></code>&nbsp;和&nbsp;<code>a<sub>j</sub></code>&nbsp;，<code>i * j</code>&nbsp;一定是完全平方数。</p>

<p>返回&nbsp;<strong>完全子集</strong> 所能取到的 <strong>最大元素和</strong> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [8,7,3,5,7,2,4,9]</span></p>

<p><strong>输出：</strong><span class="example-io">16</span></p>

<p><strong>解释：</strong></p>

<p>我们选择下标为 2 和 8 的元素，并且&nbsp;<code>2 * 8</code>&nbsp;是一个完全平方数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [8,10,3,8,1,13,7,9,4]</span></p>

<p><span class="example-io"><b>输出：</b>20</span></p>

<p><strong>解释：</strong></p>

<p>我们选择下标为 1, 4, 9 的元素。<code>1 * 4</code>, <code>1 * 9</code>, <code>4 * 9</code>&nbsp;是完全平方数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 数论

## 提示

1. Define <strong>P(x)</strong> as the product of primes <strong>p</strong> with odd exponents in <strong>x</strong>'s factorization. Examples: For <code>x = 18</code>, factorization <code>2<sup>1</sup> × 3<sup>2</sup></code>, <strong>P(18) = 2</strong>; for <code>x = 45</code>, factorization <code>3<sup>2</sup> × 5<sup>1</sup></code>, <strong>P(45) = 5</strong>; for <code>x = 50</code>, factorization <code>2<sup>1</sup> × 5<sup>2</sup></code>, <strong>P(50) = 2</strong>; for <code>x = 210</code>, factorization <code>2<sup>1</sup> × 3<sup>1</sup> × 5<sup>1</sup> × 7<sup>1</sup></code>, <strong>P(210) = 210</strong>.
2. If <code>P(i) = P(j)</code>, <code>nums[i]</code> and <code>nums[j]</code> can be grouped together.
3. Pick the group with the largest sum.

## 示例

```
[8,7,3,5,7,2,4,9]
[8,10,3,8,1,13,7,9,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumSum(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
```

### C

```c
long long maximumSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumSum(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSum(nums: List<Int>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumSum(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumSum(nums: List[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum(Nums :: [integer()]) -> integer().
maximum_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(nums :: [integer]) :: integer
  def maximum_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSum(nums: ArrayList<Int64>): Int64 {

    }
}
```

