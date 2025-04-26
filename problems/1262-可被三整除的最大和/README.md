# 1262. 可被三整除的最大和

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，请你找出并返回能被三整除的元素 <strong>最大和</strong>。</p>

<ol>
</ol>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,6,5,1,8]
<strong>输出：</strong>18
<strong>解释：</strong>选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4]
<strong>输出：</strong>0
<strong>解释：</strong>4 不能被 3 整除，所以无法选出数字，返回 0。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,4]
<strong>输出：</strong>12
<strong>解释：</strong>选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划
- 排序

## 提示

1. Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.

## 示例

```
[3,6,5,1,8]
[4]
[1,2,3,4,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumDivThree(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSumDivThree(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumDivThree(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumDivThree = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSumDivThree(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumDivThree(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSumDivThree(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_sum_div_three(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSumDivThree(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-div-three nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_div_three(Nums :: [integer()]) -> integer().
max_sum_div_three(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_div_three(nums :: [integer]) :: integer
  def max_sum_div_three(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumDivThree(nums: Array<Int64>): Int64 {

    }
}
```

