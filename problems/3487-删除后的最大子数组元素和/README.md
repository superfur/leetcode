# 3487. 删除后的最大子数组元素和

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以从数组 <code>nums</code> 中删除任意数量的元素，但不能将其变为 <strong>空</strong> 数组。执行删除操作后，选出&nbsp;<code>nums</code>&nbsp;中满足下述条件的一个子数组：</p>

<ol>
	<li>子数组中的所有元素 <strong>互不相同</strong> 。</li>
	<li><strong>最大化</strong> 子数组的元素和。</li>
</ol>

<p>返回子数组的 <strong>最大元素和</strong> 。</p>
<strong>子数组</strong> 是数组的一个连续、<strong>非空</strong> 的元素序列。

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,5]</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><b>解释：</b></p>

<p>不删除任何元素，选中整个数组得到最大元素和。</p>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [1,1,0,1,1]</span></p>

<p><span class="example-io"><b>输出：</b></span>1</p>

<p><b>解释：</b></p>

<p>删除元素&nbsp;<code>nums[0] == 1</code>、<code>nums[1] == 1</code>、<code>nums[2] == 0</code>&nbsp;和&nbsp;<code>nums[3] == 1</code>&nbsp;。选中整个数组&nbsp;<code>[1]</code>&nbsp;得到最大元素和。</p>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [1,2,-1,-2,1,0,-1]</span></p>

<p><span class="example-io"><b>输出：</b></span>3</p>

<p><b>解释：</b></p>

<p>删除元素&nbsp;<code>nums[2] == -1</code>&nbsp;和&nbsp;<code>nums[3] == -2</code>&nbsp;，从&nbsp;<code>[1, 2, 1, 0, -1]</code>&nbsp;中选中子数组&nbsp;<code>[2, 1]</code>&nbsp;以获得最大元素和。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. If the maximum element in the array is less than zero, the answer is the maximum element.
2. Otherwise, the answer is the sum of all unique values that are greater than or equal to zero.

## 示例

```
[1,2,3,4,5]
[1,1,0,1,1]
[1,2,-1,-2,1,0,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum(Nums :: [integer()]) -> integer().
max_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer]) :: integer
  def max_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSum(nums: Array<Int64>): Int64 {

    }
}
```

