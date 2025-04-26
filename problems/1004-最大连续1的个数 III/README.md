# 1004. 最大连续1的个数 III

## 题目描述

<p>给定一个二进制数组&nbsp;<code>nums</code>&nbsp;和一个整数 <code>k</code>，假设最多可以翻转 <code>k</code> 个 <code>0</code> ，则返回执行操作后 <em>数组中连续 <code>1</code> 的最大个数</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
<strong>输出：</strong>6
<strong>解释：</strong>[1,1,1,0,0,<strong>1</strong>,1,1,1,1,<strong>1</strong>]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
<strong>输出：</strong>10
<strong>解释：</strong>[0,0,1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
2. Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
3. We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
4. The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.

## 示例

```
[1,1,1,0,0,0,1,1,1,1,0]
2
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int longestOnes(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestOnes(int[] nums, int k) {
        
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
var longestOnes = function(nums, k) {
    
};
```

### TypeScript

```typescript
function longestOnes(nums: number[], k: number): number {
    
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
    function longestOnes($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestOnes(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestOnes(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestOnes(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func longestOnes(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_ones(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def longestOnes(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-ones nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_ones(Nums :: [integer()], K :: integer()) -> integer().
longest_ones(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_ones(nums :: [integer], k :: integer) :: integer
  def longest_ones(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestOnes(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

