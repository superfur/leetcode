# 2499. 让数组不相等的最小总代价

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，两者长度都为&nbsp;<code>n</code>&nbsp;。</p>

<p>每次操作中，你可以选择交换 <code>nums1</code>&nbsp;中任意两个下标处的值。操作的 <strong>开销</strong>&nbsp;为两个下标的 <strong>和</strong>&nbsp;。</p>

<p>你的目标是对于所有的 <code>0 &lt;= i &lt;= n - 1</code>&nbsp;，都满足&nbsp;<code>nums1[i] != nums2[i]</code>&nbsp;，你可以进行 <strong>任意次</strong>&nbsp;操作，请你返回达到这个目标的 <strong>最小</strong>&nbsp;总代价。</p>

<p>请你返回让<em>&nbsp;</em><code>nums1</code> 和&nbsp;<code>nums2</code><em>&nbsp;</em>满足上述条件的 <strong>最小总代价</strong> ，如果无法达成目标，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]
<b>输出：</b>10
<b>解释：</b>
实现目标的其中一种方法为：
- 交换下标为 0 和 3 的两个值，代价为 0 + 3 = 3 。现在 nums1 = [4,2,3,1,5] 。
- 交换下标为 1 和 2 的两个值，代价为 1 + 2 = 3 。现在 nums1 = [4,3,2,1,5] 。
- 交换下标为 0 和 4 的两个值，代价为 0 + 4 = 4 。现在 nums1 = [5,3,2,1,4] 。
最后，对于每个下标 i ，都有 nums1[i] != nums2[i] 。总代价为 10 。
还有别的交换值的方法，但是无法得到代价和小于 10 的方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]
<b>输出：</b>10
<b>解释：</b>
实现目标的一种方法为：
- 交换下标为 2 和 3 的两个值，代价为 2 + 3 = 5 。现在 nums1 = [2,2,1,2,3] 。
- 交换下标为 1 和 4 的两个值，代价为 1 + 4 = 5 。现在 nums1 = [2,3,1,2,2] 。
总代价为 10 ，是所有方案中的最小代价。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums1 = [1,2,2], nums2 = [1,2,2]
<b>输出：</b>-1
<b>解释：</b>
不管怎么操作，都无法满足题目要求。
所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 哈希表
- 计数

## 提示

1. How can we check which indices of <code>nums1</code> will be considered for swapping? How to minimize the number of such operations?
2. It can be seen that greedily swapping values of indices where <code>nums1[i] == nums2[i]</code> is the most optimal choice. How many values cannot be swapped this way?
3. Find which indices we will swap these remaining values with, and if there are enough such indices.

## 示例

```
[1,2,3,4,5]
[1,2,3,4,5]
[2,2,2,1,3]
[1,2,2,3,3]
[1,2,2]
[1,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumTotalCost(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumTotalCost(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
long long minimumTotalCost(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumTotalCost(int[] nums1, int[] nums2) {
        
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
var minimumTotalCost = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minimumTotalCost(nums1: number[], nums2: number[]): number {
    
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
    function minimumTotalCost($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTotalCost(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTotalCost(nums1: IntArray, nums2: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTotalCost(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minimumTotalCost(nums1 []int, nums2 []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_total_cost(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minimumTotalCost(nums1: Array[Int], nums2: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_total_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-total-cost nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_total_cost(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
minimum_total_cost(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_total_cost(nums1 :: [integer], nums2 :: [integer]) :: integer
  def minimum_total_cost(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTotalCost(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

