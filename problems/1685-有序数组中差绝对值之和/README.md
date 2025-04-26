# 1685. 有序数组中差绝对值之和

## 题目描述

<p>给你一个 <strong>非递减 </strong>有序整数数组 <code>nums</code> 。</p>

<p>请你建立并返回一个整数数组<em> </em><code>result</code>，它跟<em> </em><code>nums</code> 长度相同，且<code>result[i]</code> 等于<em> </em><code>nums[i]</code> 与数组中所有其他元素差的绝对值之和。</p>

<p>换句话说， <code>result[i]</code> 等于 <code>sum(|nums[i]-nums[j]|)</code> ，其中 <code>0 <= j < nums.length</code> 且 <code>j != i</code> （下标从 0 开始）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,5]
<b>输出：</b>[4,3,5]
<b>解释：</b>假设数组下标从 0 开始，那么
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,6,8,10]
<b>输出：</b>[24,15,13,15,21]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= nums[i + 1] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 前缀和

## 提示

1. Absolute difference is the same as max(a, b) - min(a, b). How can you use this fact with the fact that the array is sorted?
2. For nums[i], the answer is (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i-1]) + (nums[i+1] - nums[i]) + (nums[i+2] - nums[i]) + ... + (nums[n-1] - nums[i]).
3. It can be simplified to (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) + ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1)). One can build prefix and suffix sums to compute  this quickly.

## 示例

```
[2,3,5]
[1,4,6,8,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSumAbsoluteDifferences(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetSumAbsoluteDifferences(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
    
};
```

### TypeScript

```typescript
function getSumAbsoluteDifferences(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSumAbsoluteDifferences($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSumAbsoluteDifferences(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSumAbsoluteDifferences(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getSumAbsoluteDifferences(List<int> nums) {
    
  }
}
```

### Go

```golang
func getSumAbsoluteDifferences(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def get_sum_absolute_differences(nums)
    
end
```

### Scala

```scala
object Solution {
    def getSumAbsoluteDifferences(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-sum-absolute-differences nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_sum_absolute_differences(Nums :: [integer()]) -> [integer()].
get_sum_absolute_differences(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_sum_absolute_differences(nums :: [integer]) :: [integer]
  def get_sum_absolute_differences(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSumAbsoluteDifferences(nums: Array<Int64>): Array<Int64> {

    }
}
```

