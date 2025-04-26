# 2348. 全 0 子数组的数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，返回全部为&nbsp;<code>0</code>&nbsp;的&nbsp;<strong>子数组</strong>&nbsp;数目。</p>

<p><strong>子数组</strong>&nbsp;是一个数组中一段连续非空元素组成的序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,3,0,0,2,0,0,4]
<b>输出：</b>6
<b>解释：</b>
子数组 [0] 出现了 4 次。
子数组 [0,0] 出现了 2 次。
不存在长度大于 2 的全 0 子数组，所以我们返回 6 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [0,0,0,2,0,0]
<b>输出：</b>9
<strong>解释：
</strong>子数组 [0] 出现了 5 次。
子数组 [0,0] 出现了 3 次。
子数组 [0,0,0] 出现了 1 次。
不存在长度大于 3 的全 0 子数组，所以我们返回 9 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [2,10,2019]
<b>输出：</b>0
<b>解释：</b>没有全 0 子数组，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. For each zero, you can calculate the number of zero-filled subarrays that end on that index, which is the number of consecutive zeros behind the current element + 1.
2. Maintain the number of consecutive zeros behind the current element, count the number of zero-filled subarrays that end on each index, sum it up to get the answer.

## 示例

```
[1,3,0,0,2,0,0,4]
[0,0,0,2,0,0]
[2,10,2019]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long zeroFilledSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
long long zeroFilledSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long ZeroFilledSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function zeroFilledSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function zeroFilledSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func zeroFilledSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun zeroFilledSubarray(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int zeroFilledSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func zeroFilledSubarray(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def zero_filled_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def zeroFilledSubarray(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (zero-filled-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec zero_filled_subarray(Nums :: [integer()]) -> integer().
zero_filled_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec zero_filled_subarray(nums :: [integer]) :: integer
  def zero_filled_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func zeroFilledSubarray(nums: Array<Int64>): Int64 {

    }
}
```

