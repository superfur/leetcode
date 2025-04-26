# 1818. 绝对差值和

## 题目描述

<p>给你两个正整数数组 <code>nums1</code> 和 <code>nums2</code> ，数组的长度都是 <code>n</code> 。</p>

<p>数组 <code>nums1</code> 和 <code>nums2</code> 的 <strong>绝对差值和</strong> 定义为所有 <code>|nums1[i] - nums2[i]|</code>（<code>0 <= i < n</code>）的 <strong>总和</strong>（<strong>下标从 0 开始</strong>）。</p>

<p>你可以选用 <code>nums1</code> 中的 <strong>任意一个</strong> 元素来替换 <code>nums1</code> 中的 <strong>至多</strong> 一个元素，以 <strong>最小化</strong> 绝对差值和。</p>

<p>在替换数组 <code>nums1</code> 中最多一个元素 <strong>之后</strong> ，返回最小绝对差值和。因为答案可能很大，所以需要对 <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>后返回。</p>

<p><code>|x|</code> 定义为：</p>

<ul>
	<li>如果 <code>x >= 0</code> ，值为 <code>x</code> ，或者</li>
	<li>如果 <code>x <= 0</code> ，值为 <code>-x</code></li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,7,5], nums2 = [2,3,5]
<strong>输出：</strong>3
<strong>解释：</strong>有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,<strong>7</strong>,5] => [1,<strong>1</strong>,5] ，或者
- 将第二个元素替换为第三个元素：[1,<strong>7</strong>,5] => [1,<strong>5</strong>,5]
两种方案的绝对差值和都是 <code>|1-2| + (|1-3| 或者 |5-3|) + |5-5| = </code>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
<strong>输出：</strong>0
<strong>解释：</strong>nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
</pre>

<p><strong>示例 3</strong><strong>：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
<strong>输出：</strong>20
<strong>解释：</strong>将第一个元素替换为第二个元素：[<strong>1</strong>,10,4,4,2,7] => [<strong>10</strong>,10,4,4,2,7]
绝对差值和为 <code>|10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20</code>
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums1[i], nums2[i] <= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 有序集合
- 排序

## 提示

1. Go through each element and test the optimal replacements.
2. There are only 2 possible replacements for each element (higher and lower) that are optimal.

## 示例

```
[1,7,5]
[2,3,5]
[2,4,6,8,10]
[2,4,6,8,10]
[1,10,4,4,2,7]
[9,3,5,1,7,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int minAbsoluteSumDiff(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinAbsoluteSumDiff(int[] nums1, int[] nums2) {
        
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
var minAbsoluteSumDiff = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minAbsoluteSumDiff(nums1: number[], nums2: number[]): number {
    
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
    function minAbsoluteSumDiff($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minAbsoluteSumDiff(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minAbsoluteSumDiff(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minAbsoluteSumDiff(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minAbsoluteSumDiff(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_absolute_sum_diff(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minAbsoluteSumDiff(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_absolute_sum_diff(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-absolute-sum-diff nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_absolute_sum_diff(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_absolute_sum_diff(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_absolute_sum_diff(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_absolute_sum_diff(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minAbsoluteSumDiff(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

