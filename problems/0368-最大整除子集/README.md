# 368. 最大整除子集

## 题目描述

给你一个由 <strong>无重复</strong> 正整数组成的集合 <code>nums</code> ，请你找出并返回其中最大的整除子集 <code>answer</code> ，子集中每一元素对 <code>(answer[i], answer[j])</code> 都应当满足：
<ul>
	<li><code>answer[i] % answer[j] == 0</code> ，或</li>
	<li><code>answer[j] % answer[i] == 0</code></li>
</ul>

<p>如果存在多个有效解子集，返回其中任何一个均可。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>[1,3] 也会被视为正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,8]
<strong>输出：</strong>[1,2,4,8]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 2 * 10<sup>9</sup></code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划
- 排序

## 示例

```
[1,2,3]
[1,2,4,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> LargestDivisibleSubset(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var largestDivisibleSubset = function(nums) {
    
};
```

### TypeScript

```typescript
function largestDivisibleSubset(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function largestDivisibleSubset($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestDivisibleSubset(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestDivisibleSubset(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> largestDivisibleSubset(List<int> nums) {
    
  }
}
```

### Go

```golang
func largestDivisibleSubset(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def largest_divisible_subset(nums)
    
end
```

### Scala

```scala
object Solution {
    def largestDivisibleSubset(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (largest-divisible-subset nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec largest_divisible_subset(Nums :: [integer()]) -> [integer()].
largest_divisible_subset(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_divisible_subset(nums :: [integer]) :: [integer]
  def largest_divisible_subset(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestDivisibleSubset(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

