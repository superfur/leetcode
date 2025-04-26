# 2541. 使数组中所有元素相等的最小操作数 II

## 题目描述

<p>给你两个整数数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，两个数组长度都是&nbsp;<code>n</code>&nbsp;，再给你一个整数&nbsp;<code>k</code>&nbsp;。你可以对数组&nbsp;<code>nums1</code>&nbsp;进行以下操作：</p>

<ul>
	<li>选择两个下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，将&nbsp;<code>nums1[i]</code>&nbsp;增加&nbsp;<code>k</code>&nbsp;，将&nbsp;<code>nums1[j]</code>&nbsp;减少&nbsp;<code>k</code>&nbsp;。换言之，<code>nums1[i] = nums1[i] + k</code> 且&nbsp;<code>nums1[j] = nums1[j] - k</code>&nbsp;。</li>
</ul>

<p>如果对于所有满足&nbsp;<code>0 &lt;= i &lt; n</code>&nbsp;都有&nbsp;<code>num1[i] == nums2[i]</code>&nbsp;，那么我们称&nbsp;<code>nums1</code> <strong>等于</strong>&nbsp;<code>nums2</code>&nbsp;。</p>

<p>请你返回使<em>&nbsp;</em><code>nums1</code><em> </em>等于<em>&nbsp;</em><code>nums2</code>&nbsp;的&nbsp;<strong>最少</strong>&nbsp;操作数。如果没办法让它们相等，请你返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3
<b>输出：</b>2
<b>解释：</b>我们可以通过 2 个操作将 nums1 变成 nums2 。
第 1 个操作：i = 2 ，j = 0 。操作后得到 nums1 = [1,3,4,4] 。
第 2 个操作：i = 2 ，j = 3 。操作后得到 nums1 = [1,3,7,1] 。
无法用更少操作使两个数组相等。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1
<b>输出：</b>-1
<b>解释：</b>无法使两个数组相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学

## 提示

1. What are the cases for which we cannot make nums1 == nums2?
2. For minimum moves, if nums1[i] < nums2[i], then we should never decrement nums1[i]. 
If nums1[i] > nums2[i], then we should never increment nums1[i].

## 示例

```
[4,3,1,4]
[1,3,7,1]
3
[3,8,5,2]
[2,4,1,6]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long minOperations(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
```

### C

```c
long long minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinOperations(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function minOperations(nums1: number[], nums2: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func minOperations(nums1 []int, nums2 []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def min_operations(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
min_operations(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def min_operations(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Int64 {

    }
}
```

