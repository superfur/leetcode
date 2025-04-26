# 1879. 两个数组最小的异或值之和

## 题目描述

<p>给你两个整数数组 <code>nums1</code> 和 <code>nums2</code> ，它们长度都为 <code>n</code> 。</p>

<p>两个数组的 <strong>异或值之和</strong> 为 <code>(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1])</code> （<strong>下标从 0 开始</strong>）。</p>

<ul>
	<li>比方说，<code>[1,2,3]</code> 和 <code>[3,2,1]</code> 的 <strong>异或值之和</strong> 等于 <code>(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4</code> 。</li>
</ul>

<p>请你将 <code>nums2</code> 中的元素重新排列，使得 <strong>异或值之和</strong> <strong>最小</strong> 。</p>

<p>请你返回重新排列之后的 <strong>异或值之和</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [1,2], nums2 = [2,3]
<b>输出：</b>2
<b>解释：</b>将 <code>nums2</code> 重新排列得到 <code>[3,2] 。</code>
异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [1,0,3], nums2 = [5,3,4]
<b>输出：</b>8
<b>解释：</b>将 <code>nums2 重新排列得到</code> <code>[5,4,3] 。</code>
异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 14</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. Since n <= 14, we can consider every subset of nums2.
2. We can represent every subset of nums2 using bitmasks.

## 示例

```
[1,2]
[2,3]
[1,0,3]
[5,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumXORSum(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int minimumXORSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumXORSum(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumXORSum = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minimumXORSum(nums1: number[], nums2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minimumXORSum($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumXORSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumXORSum(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumXORSum(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minimumXORSum(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_xor_sum(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minimumXORSum(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_xor_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-xor-sum nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_xor_sum(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
minimum_xor_sum(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_xor_sum(nums1 :: [integer], nums2 :: [integer]) :: integer
  def minimum_xor_sum(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumXORSum(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

