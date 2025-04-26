# 2426. 满足不等式的数对数目

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，两个数组的大小都为&nbsp;<code>n</code>&nbsp;，同时给你一个整数&nbsp;<code>diff</code>&nbsp;，统计满足以下条件的&nbsp;<strong>数对&nbsp;</strong><code>(i, j)</code>&nbsp;：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt;= n - 1</code>&nbsp;<b>且</b></li>
	<li><code>nums1[i] - nums1[j] &lt;= nums2[i] - nums2[j] + diff</code>.</li>
</ul>

<p>请你返回满足条件的 <strong>数对数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
<b>输出：</b>3
<strong>解释：</strong>
总共有 3 个满足条件的数对：
1. i = 0, j = 1：3 - 2 &lt;= 2 - 2 + 1 。因为 i &lt; j 且 1 &lt;= 1 ，这个数对满足条件。
2. i = 0, j = 2：3 - 5 &lt;= 2 - 1 + 1 。因为 i &lt; j 且 -2 &lt;= 2 ，这个数对满足条件。
3. i = 1, j = 2：2 - 5 &lt;= 2 - 1 + 1 。因为 i &lt; j 且 -3 &lt;= 2 ，这个数对满足条件。
所以，我们返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [3,-1], nums2 = [-2,2], diff = -1
<b>输出：</b>0
<strong>解释：</strong>
没有满足条件的任何数对，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= diff &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 提示

1. Try rearranging the equation.
2. Once the equation is rearranged properly, think how a segment tree or a Fenwick tree can be used to solve the rearranged equation.
3. Iterate through the array backwards.

## 示例

```
[3,2,5]
[2,2,1]
1
[3,-1]
[-2,2]
-1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int diff) {
        
    }
};
```

### Java

```java
class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int diff) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
```

### C

```c
long long numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int diff) {
    
}
```

### C#

```csharp
public class Solution {
    public long NumberOfPairs(int[] nums1, int[] nums2, int diff) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} diff
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, diff) {
    
};
```

### TypeScript

```typescript
function numberOfPairs(nums1: number[], nums2: number[], diff: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $diff
     * @return Integer
     */
    function numberOfPairs($nums1, $nums2, $diff) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ diff: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, diff: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPairs(List<int> nums1, List<int> nums2, int diff) {
    
  }
}
```

### Go

```golang
func numberOfPairs(nums1 []int, nums2 []int, diff int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} diff
# @return {Integer}
def number_of_pairs(nums1, nums2, diff)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPairs(nums1: Array[Int], nums2: Array[Int], diff: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, diff: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-pairs nums1 nums2 diff)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_pairs(Nums1 :: [integer()], Nums2 :: [integer()], Diff :: integer()) -> integer().
number_of_pairs(Nums1, Nums2, Diff) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], diff :: integer) :: integer
  def number_of_pairs(nums1, nums2, diff) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPairs(nums1: Array<Int64>, nums2: Array<Int64>, diff: Int64): Int64 {

    }
}
```

