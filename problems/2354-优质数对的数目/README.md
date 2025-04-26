# 2354. 优质数对的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的正整数数组 <code>nums</code> 和一个正整数 <code>k</code> 。</p>

<p>如果满足下述条件，则数对 <code>(num1, num2)</code> 是 <strong>优质数对</strong> ：</p>

<ul>
	<li><code>num1</code> 和 <code>num2</code> <strong>都</strong> 在数组 <code>nums</code> 中存在。</li>
	<li><code>num1 OR num2</code> 和 <code>num1 AND num2</code> 的二进制表示中值为 <strong>1</strong> 的位数之和大于等于 <code>k</code> ，其中 <code>OR</code> 是按位 <strong>或</strong> 操作，而 <code>AND</code> 是按位 <strong>与</strong> 操作。</li>
</ul>

<p>返回 <strong>不同</strong> 优质数对的数目。</p>

<p>如果&nbsp;<code>a != c</code> 或者 <code>b != d</code> ，则认为 <code>(a, b)</code> 和 <code>(c, d)</code> 是不同的两个数对。例如，<code>(1, 2)</code> 和 <code>(2, 1)</code> 不同。</p>

<p><strong>注意：</strong>如果 <code>num1</code> 在数组中至少出现 <strong>一次</strong> ，则满足 <code>num1 == num2</code> 的数对 <code>(num1, num2)</code> 也可以是优质数对。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], k = 3
<strong>输出：</strong>5
<strong>解释：</strong>有如下几个优质数对：
- (3, 3)：(3 AND 3) 和 (3 OR 3) 的二进制表示都等于 (11) 。值为 1 的位数和等于 2 + 2 = 4 ，大于等于 k = 3 。
- (2, 3) 和 (3, 2)： (2 AND 3) 的二进制表示等于 (10) ，(2 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
- (1, 3) 和 (3, 1)： (1 AND 3) 的二进制表示等于 (01) ，(1 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
所以优质数对的数目是 5 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,1,1], k = 10
<strong>输出：</strong>0
<strong>解释：</strong>该数组中不存在优质数对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 60</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 哈希表
- 二分查找

## 提示

1. Can you find a different way to describe the second condition?
2. The sum of the number of set bits in (num1 OR num2) and (num1 AND num2) is equal to the sum of the number of set bits in num1 and num2.

## 示例

```
[1,2,3,1]
3
[5,1,1]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countExcellentPairs(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countExcellentPairs(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long countExcellentPairs(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountExcellentPairs(int[] nums, int k) {
        
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
var countExcellentPairs = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countExcellentPairs(nums: number[], k: number): number {
    
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
    function countExcellentPairs($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countExcellentPairs(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countExcellentPairs(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countExcellentPairs(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countExcellentPairs(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_excellent_pairs(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countExcellentPairs(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_excellent_pairs(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-excellent-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_excellent_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_excellent_pairs(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_excellent_pairs(nums :: [integer], k :: integer) :: integer
  def count_excellent_pairs(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countExcellentPairs(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

