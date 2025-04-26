# 1224. 最大相等频率

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>，请你帮忙从该数组中找出能满足下面要求的 <strong>最长</strong> 前缀，并返回该前缀的长度：</p>

<ul>
	<li>从前缀中 <strong>恰好删除一个</strong> 元素后，剩下每个数字的出现次数都相同。</li>
</ul>

<p>如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,1,1,5,3,3,5]
<strong>输出：</strong>7
<strong>解释：</strong>对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
<strong>输出：</strong>13
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表

## 提示

1. Keep track of the min and max frequencies.
2. The number to be eliminated must have a frequency of 1, same as the others or the same +1.

## 示例

```
[2,2,1,1,5,3,3,5]
[1,1,1,2,2,2,3,3,3,4,4,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxEqualFreq(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxEqualFreq(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        
```

### C

```c
int maxEqualFreq(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxEqualFreq(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxEqualFreq = function(nums) {
    
};
```

### TypeScript

```typescript
function maxEqualFreq(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxEqualFreq($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxEqualFreq(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxEqualFreq(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxEqualFreq(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxEqualFreq(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_equal_freq(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxEqualFreq(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_equal_freq(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-equal-freq nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_equal_freq(Nums :: [integer()]) -> integer().
max_equal_freq(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_equal_freq(nums :: [integer]) :: integer
  def max_equal_freq(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxEqualFreq(nums: Array<Int64>): Int64 {

    }
}
```

