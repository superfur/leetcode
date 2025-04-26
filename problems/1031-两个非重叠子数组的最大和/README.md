# 1031. 两个非重叠子数组的最大和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和两个整数 <code>firstLen</code> 和 <code>secondLen</code>，请你找出并返回两个非重叠<strong> 子数组 </strong>中元素的最大和<em>，</em>长度分别为 <code>firstLen</code> 和 <code>secondLen</code> 。</p>

<p>长度为 <code>firstLen</code> 的子数组可以出现在长为 <code>secondLen</code> 的子数组之前或之后，但二者必须是不重叠的。</p>

<p>子数组是数组的一个 <strong>连续</strong> 部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
<strong>输出：</strong>20
<strong>解释：</strong>子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
<strong>输出：</strong>29
<strong>解释：</strong>子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
<strong>输出：</strong>31
<strong>解释：</strong>子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= firstLen, secondLen &lt;= 1000</code></li>
	<li><code>2 &lt;= firstLen + secondLen &lt;= 1000</code></li>
	<li><code>firstLen + secondLen &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 滑动窗口

## 提示

1. We can use prefix sums to calculate any subarray sum quickly.
For each L length subarray, find the best possible M length subarray that occurs before and after it.

## 示例

```
[0,6,5,2,2,5,1,9,4]
1
2
[3,8,1,3,2,1,8,9,0]
3
2
[2,1,5,6,0,9,5,0,3,8]
4
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
```

### C

```c
int maxSumTwoNoOverlap(int* nums, int numsSize, int firstLen, int secondLen) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} firstLen
 * @param {number} secondLen
 * @return {number}
 */
var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    
};
```

### TypeScript

```typescript
function maxSumTwoNoOverlap(nums: number[], firstLen: number, secondLen: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $firstLen
     * @param Integer $secondLen
     * @return Integer
     */
    function maxSumTwoNoOverlap($nums, $firstLen, $secondLen) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumTwoNoOverlap(_ nums: [Int], _ firstLen: Int, _ secondLen: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumTwoNoOverlap(nums: IntArray, firstLen: Int, secondLen: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumTwoNoOverlap(List<int> nums, int firstLen, int secondLen) {
    
  }
}
```

### Go

```golang
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} first_len
# @param {Integer} second_len
# @return {Integer}
def max_sum_two_no_overlap(nums, first_len, second_len)
    
end
```

### Scala

```scala
object Solution {
    def maxSumTwoNoOverlap(nums: Array[Int], firstLen: Int, secondLen: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_two_no_overlap(nums: Vec<i32>, first_len: i32, second_len: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-two-no-overlap nums firstLen secondLen)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_two_no_overlap(Nums :: [integer()], FirstLen :: integer(), SecondLen :: integer()) -> integer().
max_sum_two_no_overlap(Nums, FirstLen, SecondLen) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_two_no_overlap(nums :: [integer], first_len :: integer, second_len :: integer) :: integer
  def max_sum_two_no_overlap(nums, first_len, second_len) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumTwoNoOverlap(nums: Array<Int64>, firstLen: Int64, secondLen: Int64): Int64 {

    }
}
```

