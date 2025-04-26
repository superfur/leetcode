# 1819. 序列中不同最大公约数的数目

## 题目描述

<p>给你一个由正整数组成的数组 <code>nums</code> 。</p>

<p>数字序列的 <strong>最大公约数</strong> 定义为序列中所有整数的共有约数中的最大整数。</p>

<ul>
	<li>例如，序列 <code>[4,6,16]</code> 的最大公约数是 <code>2</code> 。</li>
</ul>

<p>数组的一个 <strong>子序列</strong> 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。</p>

<ul>
	<li>例如，<code>[2,5,10]</code> 是 <code>[1,2,1,<strong>2</strong>,4,1,<strong>5</strong>,<strong>10</strong>]</code> 的一个子序列。</li>
</ul>

<p>计算并返回 <code>nums</code> 的所有 <strong>非空</strong> 子序列中 <strong>不同</strong> 最大公约数的 <strong>数目</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/03/image-1.png" />
<pre>
<strong>输入：</strong>nums = [6,10,3]
<strong>输出：</strong>5
<strong>解释：</strong>上图显示了所有的非空子序列与各自的最大公约数。
不同的最大公约数为 6 、10 、3 、2 和 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,15,40,5,6]
<strong>输出：</strong>7
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 计数
- 数论

## 提示

1. Think of how to check if a number x is a gcd of a subsequence.
2. If there is such subsequence, then all of it will be divisible by x. Moreover, if you divide each number in the subsequence by x , then the gcd of the resulting numbers will be 1.
3. Adding a number to a subsequence cannot increase its gcd. So, if there is a valid subsequence for x , then the subsequence that contains all multiples of x is a valid one too.
4. Iterate on all possiblex from 1 to 10^5, and check if there is a valid subsequence for x.

## 示例

```
[6,10,3]
[5,15,40,5,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDifferentSubsequenceGCDs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        
```

### C

```c
int countDifferentSubsequenceGCDs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDifferentSubsequenceGCDs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countDifferentSubsequenceGCDs = function(nums) {
    
};
```

### TypeScript

```typescript
function countDifferentSubsequenceGCDs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countDifferentSubsequenceGCDs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDifferentSubsequenceGCDs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDifferentSubsequenceGCDs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDifferentSubsequenceGCDs(List<int> nums) {
    
  }
}
```

### Go

```golang
func countDifferentSubsequenceGCDs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_different_subsequence_gc_ds(nums)
    
end
```

### Scala

```scala
object Solution {
    def countDifferentSubsequenceGCDs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_different_subsequence_gc_ds(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-different-subsequence-gc-ds nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_different_subsequence_gc_ds(Nums :: [integer()]) -> integer().
count_different_subsequence_gc_ds(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_different_subsequence_gc_ds(nums :: [integer]) :: integer
  def count_different_subsequence_gc_ds(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDifferentSubsequenceGCDs(nums: Array<Int64>): Int64 {

    }
}
```

