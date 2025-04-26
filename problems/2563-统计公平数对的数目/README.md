# 2563. 统计公平数对的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组&nbsp;<code>nums</code>&nbsp;，和两个整数&nbsp;<code>lower</code> 和&nbsp;<code>upper</code> ，返回 <strong>公平数对的数目</strong> 。</p>

<p>如果&nbsp;<code>(i, j)</code>&nbsp;数对满足以下情况，则认为它是一个 <strong>公平数对</strong>&nbsp;：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code>，且</li>
	<li><code>lower &lt;= nums[i] + nums[j] &lt;= upper</code></li>
</ul>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<b>输入：</b>nums = [0,1,7,4,4,5], lower = 3, upper = 6
<b>输出：</b>6
<b>解释：</b>共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
</pre>

<p><b>示例 2：</b></p>

<pre>
<b>输入：</b>nums = [1,7,9,2,5], lower = 11, upper = 11
<b>输出：</b>1
<b>解释：</b>只有单个公平数对：(2,3) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= lower &lt;= upper &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Sort the array in ascending order.
2. For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.
3. As you move to larger number, both boundaries move down.

## 示例

```
[0,1,7,4,4,5]
3
6
[1,7,9,2,5]
11
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        
    }
};
```

### Java

```java
class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
```

### C

```c
long long countFairPairs(int* nums, int numsSize, int lower, int upper) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountFairPairs(int[] nums, int lower, int upper) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countFairPairs = function(nums, lower, upper) {
    
};
```

### TypeScript

```typescript
function countFairPairs(nums: number[], lower: number, upper: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function countFairPairs($nums, $lower, $upper) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countFairPairs(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countFairPairs(nums: IntArray, lower: Int, upper: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countFairPairs(List<int> nums, int lower, int upper) {
    
  }
}
```

### Go

```golang
func countFairPairs(nums []int, lower int, upper int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def count_fair_pairs(nums, lower, upper)
    
end
```

### Scala

```scala
object Solution {
    def countFairPairs(nums: Array[Int], lower: Int, upper: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_fair_pairs(nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-fair-pairs nums lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_fair_pairs(Nums :: [integer()], Lower :: integer(), Upper :: integer()) -> integer().
count_fair_pairs(Nums, Lower, Upper) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_fair_pairs(nums :: [integer], lower :: integer, upper :: integer) :: integer
  def count_fair_pairs(nums, lower, upper) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countFairPairs(nums: Array<Int64>, lower: Int64, upper: Int64): Int64 {

    }
}
```

