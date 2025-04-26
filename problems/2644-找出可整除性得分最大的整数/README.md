# 2644. 找出可整除性得分最大的整数

## 题目描述

<p>给你两个整数数组 <code>nums</code> 和 <code>divisors</code> 。</p>

<p><code>divisors[i]</code> 的 <strong>可整除性得分</strong> 等于满足 <code>nums[j]</code> 能被 <code>divisors[i]</code> 整除的下标 <code>j</code> 的数量。</p>

<p>返回 <strong>可整除性得分</strong> 最大的整数 <code>divisors[i]</code> 。如果有多个整数具有最大得分，则返回数值最小的一个。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,9,15,50], divisors = [5,3,7,2]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><code>divisors[0]</code>&nbsp;的可整除性分数为 2 因为&nbsp;<code>nums[2]</code> 和&nbsp;<code>nums[3]</code>&nbsp;能被 5 整除。</p>

<p><code>divisors[1]</code> 的可整除性分数为 2 因为&nbsp;<code>nums[1]</code>&nbsp;和&nbsp;<code>nums[2]</code>&nbsp;能被 3 整除。</p>

<p><code>divisors[2]</code> 的可整除性分数为 0 因为&nbsp;<code>nums</code>&nbsp;中没有数字能被 7 整除。</p>

<p><code>divisors[3]</code> 的可整除性分数为 2 因为 <code>nums[0]</code> 和&nbsp;<code>nums[3]</code>&nbsp;能够被 2 整除。</p>

<p>因为&nbsp;<code>divisors[0]</code>&nbsp;、<code>divisor[1]</code> 和&nbsp;<code>divisors[3]</code>&nbsp;有相同的可整除性分数，我们返回更小的那个&nbsp;<code>divisors[3]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [4,7,9,3,9], divisors = [5,2,3]</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p><code>divisors[0]</code> 的可整除性分数为 0&nbsp;因为&nbsp;<code>nums</code>&nbsp;中没有数字能被 5 整除。</p>

<p><code>divisors[1]</code> 的可整除性分数为 1 因为只有 <code>nums[0]</code>&nbsp;能被 2 整除。</p>

<p><code>divisors[2]</code> 的可整除性分数为 3 因为&nbsp;<code>nums[2]</code>&nbsp;，<code>nums[3]</code>&nbsp;和&nbsp;<code>nums[4]</code>&nbsp;能被 3 整除。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [20,14,21,10], divisors = [10,16,20]</span></p>

<p><strong>输出：</strong><span class="example-io">10</span></p>

<p><strong>解释：</strong></p>

<p><code>divisors[0]</code> 的可整除性分数为 2 因为&nbsp;<code>nums[0]</code>&nbsp;和&nbsp;<code>nums[3]</code> 能被 10 整除。</p>

<p><code>divisors[1]</code> 的可整除性分数为 0 因为&nbsp;<code>nums</code>&nbsp;中没有数字能被 16&nbsp;整除。</p>

<p><code>divisors[2]</code> 的可整除性分数为 1 因为&nbsp;<code>nums[0]</code>&nbsp;能被 20&nbsp;整除。</p>

<p>因为&nbsp;<code>divisors[0]</code>&nbsp;的可整除性分数最大，我们返回&nbsp;<code>divisors[0]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, divisors.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], divisors[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Consider counting for each element in divisors the count of elements in nums divisible by it using bruteforce.
2. After counting for each divisor, take the one with the maximum count. In case of a tie, take the minimum one of them.

## 示例

```
[2,9,15,50]
[5,3,7,2]
[4,7,9,3,9]
[5,2,3]
[20,14,21,10]
[10,16,20]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
```

### C

```c
int maxDivScore(int* nums, int numsSize, int* divisors, int divisorsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDivScore(int[] nums, int[] divisors) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} divisors
 * @return {number}
 */
var maxDivScore = function(nums, divisors) {
    
};
```

### TypeScript

```typescript
function maxDivScore(nums: number[], divisors: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $divisors
     * @return Integer
     */
    function maxDivScore($nums, $divisors) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDivScore(_ nums: [Int], _ divisors: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDivScore(nums: IntArray, divisors: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDivScore(List<int> nums, List<int> divisors) {
    
  }
}
```

### Go

```golang
func maxDivScore(nums []int, divisors []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} divisors
# @return {Integer}
def max_div_score(nums, divisors)
    
end
```

### Scala

```scala
object Solution {
    def maxDivScore(nums: Array[Int], divisors: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_div_score(nums: Vec<i32>, divisors: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-div-score nums divisors)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_div_score(Nums :: [integer()], Divisors :: [integer()]) -> integer().
max_div_score(Nums, Divisors) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_div_score(nums :: [integer], divisors :: [integer]) :: integer
  def max_div_score(nums, divisors) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDivScore(nums: Array<Int64>, divisors: Array<Int64>): Int64 {

    }
}
```

