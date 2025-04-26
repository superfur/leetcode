# 1814. 统计一个数组中好对子的数目

## 题目描述

<p>给你一个数组 <code>nums</code> ，数组中只包含非负整数。定义 <code>rev(x)</code> 的值为将整数 <code>x</code> 各个数字位反转得到的结果。比方说 <code>rev(123) = 321</code> ， <code>rev(120) = 21</code> 。我们称满足下面条件的下标对 <code>(i, j)</code> 是 <strong>好的</strong> ：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; nums.length</code></li>
	<li><code>nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])</code></li>
</ul>

<p>请你返回好下标对的数目。由于结果可能会很大，请将结果对 <code>10<sup>9</sup> + 7</code> <b>取余</b> 后返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [42,11,1,97]
<b>输出：</b>2
<b>解释：</b>两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [13,10,35,24,76]
<b>输出：</b>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 计数

## 提示

1. The condition can be rearranged to (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])).
2. Transform each nums[i] into (nums[i] - rev(nums[i])). Then, count the number of (i, j) pairs that have equal values.
3. Keep a map storing the frequencies of values that you have seen so far. For each i, check if nums[i] is in the map. If it is, then add that count to the overall count. Then, increment the frequency of nums[i].

## 示例

```
[42,11,1,97]
[13,10,35,24,76]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countNicePairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
```

### C

```c
int countNicePairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountNicePairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {
    
};
```

### TypeScript

```typescript
function countNicePairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countNicePairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countNicePairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countNicePairs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countNicePairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func countNicePairs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_nice_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def countNicePairs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-nice-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_nice_pairs(Nums :: [integer()]) -> integer().
count_nice_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_nice_pairs(nums :: [integer]) :: integer
  def count_nice_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countNicePairs(nums: Array<Int64>): Int64 {

    }
}
```

