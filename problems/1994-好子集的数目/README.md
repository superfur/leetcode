# 1994. 好子集的数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。如果&nbsp;<code>nums</code>&nbsp;的一个子集中，所有元素的乘积可以表示为一个或多个 <strong>互不相同的质数</strong> 的乘积，那么我们称它为&nbsp;<strong>好子集</strong>&nbsp;。</p>

<ul>
	<li>比方说，如果&nbsp;<code>nums = [1, 2, 3, 4]</code>&nbsp;：

	<ul>
		<li><code>[2, 3]</code>&nbsp;，<code>[1, 2, 3]</code>&nbsp;和&nbsp;<code>[1, 3]</code>&nbsp;是 <strong>好</strong>&nbsp;子集，乘积分别为&nbsp;<code>6 = 2*3</code>&nbsp;，<code>6 = 2*3</code>&nbsp;和&nbsp;<code>3 = 3</code>&nbsp;。</li>
		<li><code>[1, 4]</code> 和&nbsp;<code>[4]</code>&nbsp;不是 <strong>好</strong>&nbsp;子集，因为乘积分别为&nbsp;<code>4 = 2*2</code> 和&nbsp;<code>4 = 2*2</code>&nbsp;。</li>
	</ul>
	</li>
</ul>

<p>请你返回 <code>nums</code>&nbsp;中不同的&nbsp;<strong>好</strong>&nbsp;子集的数目对<em>&nbsp;</em><code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;的结果。</p>

<p><code>nums</code>&nbsp;中的 <strong>子集</strong>&nbsp;是通过删除 <code>nums</code>&nbsp;中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>6
<b>解释：</b>好子集为：
- [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [4,2,3,15]
<b>输出：</b>5
<b>解释：</b>好子集为：
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
- [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 30</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学
- 动态规划
- 状态压缩

## 提示

1. Consider only the numbers which have a good prime factorization.
2. Use brute force to find all possible good subsets and then calculate its frequency in nums.

## 示例

```
[1,2,3,4]
[4,2,3,15]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfGoodSubsets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfGoodSubsets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        
```

### C

```c
int numberOfGoodSubsets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfGoodSubsets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubsets = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfGoodSubsets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodSubsets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfGoodSubsets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfGoodSubsets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfGoodSubsets(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfGoodSubsets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def number_of_good_subsets(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfGoodSubsets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_good_subsets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-good-subsets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_good_subsets(Nums :: [integer()]) -> integer().
number_of_good_subsets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_good_subsets(nums :: [integer]) :: integer
  def number_of_good_subsets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfGoodSubsets(nums: Array<Int64>): Int64 {

    }
}
```

