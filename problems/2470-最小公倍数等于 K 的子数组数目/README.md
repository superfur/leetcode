# 2470. 最小公倍数等于 K 的子数组数目

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，请你统计并返回 <code>nums</code> 的 <strong>子数组</strong> 中满足 <em>元素最小公倍数为 <code>k</code> </em>的子数组数目。</p>

<p><strong>子数组</strong> 是数组中一个连续非空的元素序列。</p>

<p><strong>数组的最小公倍数</strong> 是可被所有数组元素整除的最小正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre><strong>输入：</strong>nums = [3,6,2,7,1], k = 6
<strong>输出：</strong>4
<strong>解释：</strong>以 6 为最小公倍数的子数组是：
- [<em><strong>3</strong></em>,<em><strong>6</strong></em>,2,7,1]
- [<em><strong>3</strong></em>,<em><strong>6</strong></em>,<em><strong>2</strong></em>,7,1]
- [3,<em><strong>6</strong></em>,2,7,1]
- [3,<em><strong>6</strong></em>,<em><strong>2</strong></em>,7,1]
</pre>

<p><strong>示例 2 ：</strong></p>

<pre><strong>输入：</strong>nums = [3], k = 2
<strong>输出：</strong>0
<strong>解释：</strong>不存在以 2 为最小公倍数的子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. The constraints on nums.length are small. It is possible to check every subarray.
2. To calculate LCM, you can use a built-in function or the formula lcm(a, b) = a * b / gcd(a, b).
3. As you calculate the LCM of more numbers, it can only become greater. Once it becomes greater than k, you know that any larger subarrays containing all the current elements will not work.

## 示例

```
[3,6,2,7,1]
6
[3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarrayLCM(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int subarrayLCM(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarrayLCM(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarrayLCM = function(nums, k) {
    
};
```

### TypeScript

```typescript
function subarrayLCM(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarrayLCM($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarrayLCM(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarrayLCM(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarrayLCM(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func subarrayLCM(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_lcm(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def subarrayLCM(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarray_lcm(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarray-lcm nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec subarray_lcm(Nums :: [integer()], K :: integer()) -> integer().
subarray_lcm(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarray_lcm(nums :: [integer], k :: integer) :: integer
  def subarray_lcm(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarrayLCM(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

