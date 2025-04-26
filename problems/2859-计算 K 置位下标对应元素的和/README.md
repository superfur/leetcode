# 2859. 计算 K 置位下标对应元素的和

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p>请你用整数形式返回 <code>nums</code> 中的特定元素之 <strong>和</strong> ，这些特定元素满足：其对应下标的二进制表示中恰存在 <code>k</code> 个置位。</p>

<p>整数的二进制表示中的 1 就是这个整数的 <strong>置位</strong> 。</p>

<p>例如，<code>21</code> 的二进制表示为 <code>10101</code> ，其中有 <code>3</code> 个置位。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,10,1,5,2], k = 1
<strong>输出：</strong>13
<strong>解释：</strong>下标的二进制表示是： 
0 = 000<sub>2</sub>
1 = 001<sub>2</sub>
2 = 010<sub>2</sub>
3 = 011<sub>2</sub>
4 = 100<sub>2 
</sub>下标 1、2 和 4 在其二进制表示中都存在 k = 1 个置位。
因此，答案为 nums[1] + nums[2] + nums[4] = 13 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,3,2,1], k = 2
<strong>输出：</strong>1
<strong>解释：</strong>下标的二进制表示是： 
0 = 00<sub>2</sub>
1 = 01<sub>2</sub>
2 = 10<sub>2</sub>
3 = 11<sub>2
</sub>只有下标 3 的二进制表示中存在 k = 2 个置位。
因此，答案为 nums[3] = 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. Iterate through the indices <code>i</code> in the range <code>[0, n - 1]</code>, for each index <code>i</code> count the number of bits in its binary representation. If it is <code>k</code>, add <code>nums[i]</code> to the result.

## 示例

```
[5,10,1,5,2]
1
[4,3,2,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int sumIndicesWithKSetBits(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumIndicesWithKSetBits(IList<int> nums, int k) {
        
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
var sumIndicesWithKSetBits = function(nums, k) {
    
};
```

### TypeScript

```typescript
function sumIndicesWithKSetBits(nums: number[], k: number): number {
    
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
    function sumIndicesWithKSetBits($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumIndicesWithKSetBits(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumIndicesWithKSetBits(nums: List<Int>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumIndicesWithKSetBits(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func sumIndicesWithKSetBits(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_indices_with_k_set_bits(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def sumIndicesWithKSetBits(nums: List[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_indices_with_k_set_bits(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-indices-with-k-set-bits nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_indices_with_k_set_bits(Nums :: [integer()], K :: integer()) -> integer().
sum_indices_with_k_set_bits(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_indices_with_k_set_bits(nums :: [integer], k :: integer) :: integer
  def sum_indices_with_k_set_bits(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumIndicesWithKSetBits(nums: ArrayList<Int64>, k: Int64): Int64 {

    }
}
```

