# 801. 使序列递增的最小交换次数

## 题目描述

<p>我们有两个长度相等且不为空的整型数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;。在一次操作中，我们可以交换&nbsp;<code>nums1[i]</code>&nbsp;和&nbsp;<code>nums2[i]</code>的元素。</p>

<ul>
	<li>例如，如果 <code>nums1 = [1,2,3,<u>8</u>]</code> ， <code>nums2 =[5,6,7,<u>4</u>]</code> ，你可以交换 <code>i = 3</code> 处的元素，得到 <code>nums1 =[1,2,3,4]</code> 和 <code>nums2 =[5,6,7,8]</code> 。</li>
</ul>

<p>返回 <em>使 <code>nums1</code> 和 <code>nums2</code> <strong>严格递增&nbsp;</strong>所需操作的最小次数</em> 。</p>

<p>数组&nbsp;<code>arr</code>&nbsp;<strong>严格递增</strong> 且&nbsp;&nbsp;<code>arr[0] &lt; arr[1] &lt; arr[2] &lt; ... &lt; arr[arr.length - 1]</code>&nbsp;。</p>

<p><b>注意：</b></p>

<ul>
	<li>用例保证可以实现操作。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [1,3,5,4], nums2 = [1,2,3,7]
<strong>输出:</strong> 1
<strong>解释: </strong>
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= nums1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums2.length == nums1.length</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 2 * 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
[1,3,5,4]
[1,2,3,7]
[0,3,5,8,9]
[2,1,4,6,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int minSwap(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSwap(int[] nums1, int[] nums2) {
        
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
var minSwap = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minSwap(nums1: number[], nums2: number[]): number {
    
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
    function minSwap($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSwap(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSwap(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSwap(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minSwap(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_swap(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minSwap(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_swap(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-swap nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_swap(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_swap(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_swap(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_swap(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSwap(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

