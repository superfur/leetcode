# 2195. 向数组中追加 K 个整数

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。请你向 <code>nums</code> 中追加 <code>k</code> 个 <strong>未</strong> 出现在 <code>nums</code> 中的、<strong>互不相同</strong> 的 <strong>正</strong> 整数，并使结果数组的元素和 <strong>最小</strong> 。</p>

<p>返回追加到 <code>nums</code> 中的 <code>k</code> 个整数之和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,4,25,10,25], k = 2
<strong>输出：</strong>5
<strong>解释：</strong>在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [5,6], k = 6
<strong>输出：</strong>25
<strong>解释：</strong>在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 排序

## 提示

1. The k smallest numbers that do not appear in nums will result in the minimum sum.
2. Recall that the sum of the first n positive numbers is equal to n * (n+1) / 2.
3. Initialize the answer as the sum of 1 to k. Then, adjust the answer depending on the values in nums.

## 示例

```
[1,4,25,10,25]
2
[5,6]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimalKSum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long minimalKSum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimalKSum(int[] nums, int k) {
        
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
var minimalKSum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minimalKSum(nums: number[], k: number): number {
    
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
    function minimalKSum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimalKSum(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimalKSum(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimalKSum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minimalKSum(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimal_k_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minimalKSum(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimal_k_sum(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimal-k-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimal_k_sum(Nums :: [integer()], K :: integer()) -> integer().
minimal_k_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimal_k_sum(nums :: [integer], k :: integer) :: integer
  def minimal_k_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimalKSum(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

