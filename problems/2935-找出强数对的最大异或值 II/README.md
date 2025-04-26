# 2935. 找出强数对的最大异或值 II

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。如果一对整数 <code>x</code> 和 <code>y</code> 满足以下条件，则称其为 <strong>强数对</strong> ：</p>

<ul>
	<li><code>|x - y| &lt;= min(x, y)</code></li>
</ul>

<p>你需要从 <code>nums</code> 中选出两个整数，且满足：这两个整数可以形成一个强数对，并且它们的按位异或（<code>XOR</code>）值是在该数组所有强数对中的<strong> 最大值 </strong>。</p>

<p>返回数组 <code>nums</code> 所有可能的强数对中的<strong> 最大 </strong>异或值。</p>

<p><strong>注意</strong>，你可以选择同一个整数两次来形成一个强数对。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5]
<strong>输出：</strong>7
<strong>解释：</strong>数组<code> nums </code>中有 11 个强数对：(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) 和 (5, 5) 。
这些强数对中的最大异或值是 3 XOR 4 = 7 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,100]
<strong>输出：</strong>0
<strong>解释：</strong>数组<code> nums </code>中有 2 个强数对：(10, 10) 和 (100, 100) 。
这些强数对中的最大异或值是 10 XOR 10 = 0 ，数对 (100, 100) 的异或值也是 100 XOR 100 = 0 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [500,520,2500,3000]
<strong>输出：</strong>1020
<strong>解释：</strong>数组<code> nums </code>中有 6 个强数对：(500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) 和 (3000, 3000) 。
这些强数对中的最大异或值是 500 XOR 520 = 1020 ；另一个异或值非零的数对是 (5, 6) ，其异或值是 2500 XOR 3000 = 636 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2<sup>20</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 字典树
- 数组
- 哈希表
- 滑动窗口

## 提示

1. Sort the array, now let <code>x <= y</code> which means <code>|x - y| <= min(x, y)</code> can now be written as <code>y - x <= x</code> or in other words, <code>y <= 2 * x</code>.
2. If <code>x</code> and <code>y</code> have the same number of bits, try making<code>y</code>’s bits different from x if possible for each bit starting from the second most significant bit.
3. If <code>y</code> has 1 more bit than <code>x</code> and <code>y <= 2 * x</code> use the idea about Digit DP to make <code>y</code>’s prefix smaller than <code>2 * x + 1</code> as well as trying to make each bit different from <code>x</code> using a Hashmap.
4. Alternatively, use Trie data structure to find the pair with maximum <code>XOR</code>.

## 示例

```
[1,2,3,4,5]
[10,100]
[500,520,2500,3000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumStrongPairXor(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumStrongPairXor(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumStrongPairXor(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumStrongPairXor(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumStrongPairXor = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumStrongPairXor(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumStrongPairXor($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumStrongPairXor(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumStrongPairXor(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumStrongPairXor(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumStrongPairXor(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_strong_pair_xor(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumStrongPairXor(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-strong-pair-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_strong_pair_xor(Nums :: [integer()]) -> integer().
maximum_strong_pair_xor(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_strong_pair_xor(nums :: [integer]) :: integer
  def maximum_strong_pair_xor(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumStrongPairXor(nums: Array<Int64>): Int64 {

    }
}
```

