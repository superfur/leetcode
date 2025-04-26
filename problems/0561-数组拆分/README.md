# 561. 数组拆分

## 题目描述

<p>给定长度为&nbsp;<code>2n</code><strong>&nbsp;</strong>的整数数组 <code>nums</code> ，你的任务是将这些数分成&nbsp;<code>n</code><strong> </strong>对, 例如 <code>(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)</code> ，使得从 <code>1</code> 到&nbsp;<code>n</code> 的 <code>min(a<sub>i</sub>, b<sub>i</sub>)</code> 总和最大。</p>

<p>返回该 <strong>最大总和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,4,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -&gt; min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -&gt; min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -&gt; min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,2,6,5,1,2]
<strong>输出：</strong>9
<strong>解释：</strong>最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 计数排序
- 排序

## 提示

1. Obviously, brute force won't help here. Think of something else, take some example like 1,2,3,4.
2. How will you make pairs to get the result? There must be some pattern.
3. Did you observe that- Minimum element gets add into the result in sacrifice of maximum element.
4. Still won't able to find pairs? Sort the array and try to find the pattern.

## 示例

```
[1,4,3,2]
[6,2,6,5,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int arrayPairSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
```

### C

```c
int arrayPairSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ArrayPairSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    
};
```

### TypeScript

```typescript
function arrayPairSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arrayPairSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arrayPairSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arrayPairSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int arrayPairSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func arrayPairSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def arrayPairSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn array_pair_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (array-pair-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec array_pair_sum(Nums :: [integer()]) -> integer().
array_pair_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec array_pair_sum(nums :: [integer]) :: integer
  def array_pair_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arrayPairSum(nums: Array<Int64>): Int64 {

    }
}
```

