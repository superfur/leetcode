# 2183. 统计可以被 K 整除的下标对数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> 和一个整数 <code>k</code> ，返回满足下述条件的下标对 <code>(i, j)</code> 的数目：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt;= n - 1</code> 且</li>
	<li><code>nums[i] * nums[j]</code> 能被 <code>k</code> 整除。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,5], k = 2
<strong>输出：</strong>7
<strong>解释：</strong>
共有 7 对下标的对应积可以被 2 整除：
(0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
它们的积分别是 2、4、6、8、10、12 和 20 。
其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。    
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4], k = 5
<strong>输出：</strong>0
<strong>解释：</strong>不存在对应积可以被 5 整除的下标对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 数论

## 提示

1. For any element in the array, what is the smallest number it should be multiplied with such that the product is divisible by k?
2. The smallest number which should be multiplied with nums[i] so that the product is divisible by k is k / gcd(k, nums[i]). Now think about how you can store and update the count of such numbers present in the array efficiently.

## 示例

```
[1,2,3,4,5]
2
[1,2,3,4]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countPairs(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countPairs(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long countPairs(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountPairs(int[] nums, int k) {
        
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
var countPairs = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countPairs(nums: number[], k: number): number {
    
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
    function countPairs($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countPairs(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_pairs(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], k :: integer) :: integer
  def count_pairs(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

