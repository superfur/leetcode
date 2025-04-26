# 2386. 找出数组的第 K 大和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个 <strong>正</strong> 整数 <code>k</code> 。你可以选择数组的任一 <strong>子序列</strong> 并且对其全部元素求和。</p>

<p>数组的 <strong>第 k 大和</strong> 定义为：可以获得的第 <code>k</code> 个 <strong>最大</strong> 子序列和（子序列和允许出现重复）</p>

<p>返回数组的 <strong>第 k 大和</strong> 。</p>

<p>子序列是一个可以由其他数组删除某些或不删除元素派生而来的数组，且派生过程不改变剩余元素的顺序。</p>

<p><strong>注意：</strong>空子序列的和视作 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,-2], k = 5
<strong>输出：</strong>2
<strong>解释：</strong>所有可能获得的子序列和列出如下，按递减顺序排列：
6、4、4、2、<strong><em>2</em></strong>、0、0、-2
数组的第 5 大和是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-2,3,4,-10,12], k = 16
<strong>输出：</strong>10
<strong>解释：</strong>数组的第 16 大和是 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(2000, 2<sup>n</sup>)</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 排序
- 堆（优先队列）

## 提示

1. Start from the largest sum possible, and keep finding the next largest sum until you reach the kth sum.
2. Starting from a sum, what are the two next largest sums that you can obtain from it?

## 示例

```
[2,4,-2]
5
[1,-2,3,4,-10,12]
16
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long kSum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long kSum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long kSum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long KSum(int[] nums, int k) {
        
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
var kSum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function kSum(nums: number[], k: number): number {
    
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
    function kSum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kSum(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kSum(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int kSum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func kSum(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def kSum(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_sum(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (k-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_sum(Nums :: [integer()], K :: integer()) -> integer().
k_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_sum(nums :: [integer], k :: integer) :: integer
  def k_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kSum(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

