# 2321. 拼接数组的最大分数

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，长度都是 <code>n</code> 。</p>

<p>你可以选择两个整数 <code>left</code> 和 <code>right</code> ，其中 <code>0 &lt;= left &lt;= right &lt; n</code> ，接着 <strong>交换</strong> 两个子数组 <code>nums1[left...right]</code> 和 <code>nums2[left...right]</code> 。</p>

<ul>
	<li>例如，设 <code>nums1 = [1,2,3,4,5]</code> 和 <code>nums2 = [11,12,13,14,15]</code> ，整数选择 <code>left = 1</code> 和 <code>right = 2</code>，那么 <code>nums1</code> 会变为 <code>[1,<strong><em>12</em>,<em>13</em></strong>,4,5]</code> 而 <code>nums2</code> 会变为 <code>[11,<em><strong>2,3</strong></em>,14,15]</code> 。</li>
</ul>

<p>你可以选择执行上述操作 <strong>一次</strong> 或不执行任何操作。</p>

<p>数组的 <strong>分数</strong> 取 <code>sum(nums1)</code> 和 <code>sum(nums2)</code> 中的最大值，其中 <code>sum(arr)</code> 是数组 <code>arr</code> 中所有元素之和。</p>

<p>返回 <strong>可能的最大分数</strong> 。</p>

<p><strong>子数组 </strong>是数组中连续的一个元素序列。<code>arr[left...right]</code> 表示子数组包含 <code>nums</code> 中下标 <code>left</code> 和 <code>right</code> 之间的元素<strong>（含</strong> 下标 <code>left</code> 和 <code>right</code> 对应元素<strong>）</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [60,60,60], nums2 = [10,90,10]
<strong>输出：</strong>210
<strong>解释：</strong>选择 left = 1 和 right = 1 ，得到 nums1 = [60,<em><strong>90</strong></em>,60] 和 nums2 = [10,<em><strong>60</strong></em>,10] 。
分数为 max(sum(nums1), sum(nums2)) = max(210, 80) = 210 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]
<strong>输出：</strong>220
<strong>解释：</strong>选择 left = 3 和 right = 4 ，得到 nums1 = [20,40,20,<em><strong>40,20</strong></em>] 和 nums2 = [50,20,50,<em><strong>70,30</strong></em>] 。
分数为 max(sum(nums1), sum(nums2)) = max(140, 220) = 220 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [7,11,13], nums2 = [1,1,1]
<strong>输出：</strong>31
<strong>解释：</strong>选择不交换任何子数组。
分数为 max(sum(nums1), sum(nums2)) = max(31, 3) = 31 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Think on Dynamic Programming.
2. First assume you will be taking the array a and choose some subarray from b
3. Suppose the DP is DP(pos, state). pos is the current position you are in. state is one of {0,1,2}, where 0 means taking the array a, 1 means we are taking the subarray b, and 2 means we are again taking the array a. We need to handle the transitions carefully.

## 示例

```
[60,60,60]
[10,90,10]
[20,40,20,70,30]
[50,20,50,40,20]
[7,11,13]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumsSplicedArray(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int maximumsSplicedArray(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumsSplicedArray(int[] nums1, int[] nums2) {
        
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
var maximumsSplicedArray = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function maximumsSplicedArray(nums1: number[], nums2: number[]): number {
    
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
    function maximumsSplicedArray($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumsSplicedArray(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumsSplicedArray(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumsSplicedArray(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func maximumsSplicedArray(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximums_spliced_array(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def maximumsSplicedArray(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximums_spliced_array(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximums-spliced-array nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximums_spliced_array(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
maximums_spliced_array(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximums_spliced_array(nums1 :: [integer], nums2 :: [integer]) :: integer
  def maximums_spliced_array(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumsSplicedArray(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

