# 1590. 使数组和能被 P 整除

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>，请你移除 <strong>最短</strong>&nbsp;子数组（可以为 <strong>空</strong>），使得剩余元素的 <strong>和</strong>&nbsp;能被 <code>p</code>&nbsp;整除。 <strong>不允许</strong>&nbsp;将整个数组都移除。</p>

<p>请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 <code>-1</code>&nbsp;。</p>

<p><strong>子数组</strong>&nbsp;定义为原数组中连续的一组元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,1,4,2], p = 6
<strong>输出：</strong>1
<strong>解释：</strong>nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [6,3,5,2], p = 9
<strong>输出：</strong>2
<strong>解释：</strong>我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3], p = 3
<strong>输出：</strong>0
<strong>解释：</strong>和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
</pre>

<p><strong>示例&nbsp; 4：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3], p = 7
<strong>输出：</strong>-1
<strong>解释：</strong>没有任何方案使得移除子数组后剩余元素的和被 7 整除。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>nums = [1000000000,1000000000,1000000000], p = 3
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= p &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Use prefix sums to calculate the subarray sums.
2. Suppose you know the remainder for the sum of the entire array. How does removing a subarray affect that remainder? What remainder does the subarray need to have in order to make the rest of the array sum up to be divisible by k?
3. Use a map to keep track of the rightmost index for every prefix sum % p.

## 示例

```
[3,1,4,2]
6
[6,3,5,2]
9
[1,2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSubarray(int[] nums, int p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
```

### C

```c
int minSubarray(int* nums, int numsSize, int p) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSubarray(int[] nums, int p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    
};
```

### TypeScript

```typescript
function minSubarray(nums: number[], p: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minSubarray($nums, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSubarray(nums: IntArray, p: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSubarray(List<int> nums, int p) {
    
  }
}
```

### Go

```golang
func minSubarray(nums []int, p int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} p
# @return {Integer}
def min_subarray(nums, p)
    
end
```

### Scala

```scala
object Solution {
    def minSubarray(nums: Array[Int], p: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-subarray nums p)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_subarray(Nums :: [integer()], P :: integer()) -> integer().
min_subarray(Nums, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_subarray(nums :: [integer], p :: integer) :: integer
  def min_subarray(nums, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSubarray(nums: Array<Int64>, p: Int64): Int64 {

    }
}
```

