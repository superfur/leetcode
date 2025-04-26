# 995. K 连续位的最小翻转次数

## 题目描述

<p>给定一个二进制数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p><strong>k位翻转</strong> 就是从 <code>nums</code> 中选择一个长度为 <code>k</code> 的 <strong>子数组</strong> ，同时把子数组中的每一个 <code>0</code> 都改成 <code>1</code> ，把子数组中的每一个 <code>1</code> 都改成 <code>0</code> 。</p>

<p>返回数组中不存在 <code>0</code> 所需的最小 <strong>k位翻转</strong> 次数。如果不可能，则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p><strong>子数组</strong> 是数组的 <strong>连续</strong> 部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0], K = 1
<strong>输出：</strong>2
<strong>解释：</strong>先翻转 A[0]，然后翻转 A[2]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,0], K = 2
<strong>输出：</strong>-1
<strong>解释：</strong>无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0,1,0,1,1,0], K = 3
<strong>输出：</strong>3
<strong>解释：</strong>
翻转 A[0],A[1],A[2]:&nbsp;A变成 [1,1,1,1,0,1,1,0]
翻转 A[4],A[5],A[6]:&nbsp;A变成 [1,1,1,1,1,0,0,0]
翻转 A[5],A[6],A[7]:&nbsp;A变成 [1,1,1,1,1,1,1,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 队列
- 数组
- 前缀和
- 滑动窗口

## 示例

```
[0,1,0]
1
[1,1,0]
2
[0,0,0,1,0,1,1,0]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minKBitFlips(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minKBitFlips(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinKBitFlips(int[] nums, int k) {
        
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
var minKBitFlips = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minKBitFlips(nums: number[], k: number): number {
    
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
    function minKBitFlips($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minKBitFlips(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minKBitFlips(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minKBitFlips(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minKBitFlips(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_k_bit_flips(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minKBitFlips(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_k_bit_flips(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-k-bit-flips nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_k_bit_flips(Nums :: [integer()], K :: integer()) -> integer().
min_k_bit_flips(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_k_bit_flips(nums :: [integer], k :: integer) :: integer
  def min_k_bit_flips(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minKBitFlips(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

