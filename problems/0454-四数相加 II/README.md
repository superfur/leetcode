# 454. 四数相加 II

## 题目描述

<p>给你四个整数数组 <code>nums1</code>、<code>nums2</code>、<code>nums3</code> 和 <code>nums4</code> ，数组长度都是 <code>n</code> ，请你计算有多少个元组 <code>(i, j, k, l)</code> 能满足：</p>

<ul>
	<li><code>0 &lt;= i, j, k, l &lt; n</code></li>
	<li><code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
<strong>输出：</strong>2
<strong>解释：</strong>
两个元组如下：
1. (0, 0, 0, 1) -&gt; nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p>&nbsp; <strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>n == nums3.length</code></li>
	<li><code>n == nums4.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-2<sup>28</sup> &lt;= nums1[i], nums2[i], nums3[i], nums4[i] &lt;= 2<sup>28</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 示例

```
[1,2]
[-2,-1]
[-1,2]
[0,2]
[0]
[0]
[0]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        
    }
};
```

### Java

```java
class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
```

### C

```c
int fourSumCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* nums4, int nums4Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int FourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function(nums1, nums2, nums3, nums4) {
    
};
```

### TypeScript

```typescript
function fourSumCount(nums1: number[], nums2: number[], nums3: number[], nums4: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[] $nums3
     * @param Integer[] $nums4
     * @return Integer
     */
    function fourSumCount($nums1, $nums2, $nums3, $nums4) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fourSumCount(_ nums1: [Int], _ nums2: [Int], _ nums3: [Int], _ nums4: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fourSumCount(nums1: IntArray, nums2: IntArray, nums3: IntArray, nums4: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int fourSumCount(List<int> nums1, List<int> nums2, List<int> nums3, List<int> nums4) {
    
  }
}
```

### Go

```golang
func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[]} nums3
# @param {Integer[]} nums4
# @return {Integer}
def four_sum_count(nums1, nums2, nums3, nums4)
    
end
```

### Scala

```scala
object Solution {
    def fourSumCount(nums1: Array[Int], nums2: Array[Int], nums3: Array[Int], nums4: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn four_sum_count(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>, nums4: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (four-sum-count nums1 nums2 nums3 nums4)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec four_sum_count(Nums1 :: [integer()], Nums2 :: [integer()], Nums3 :: [integer()], Nums4 :: [integer()]) -> integer().
four_sum_count(Nums1, Nums2, Nums3, Nums4) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec four_sum_count(nums1 :: [integer], nums2 :: [integer], nums3 :: [integer], nums4 :: [integer]) :: integer
  def four_sum_count(nums1, nums2, nums3, nums4) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fourSumCount(nums1: Array<Int64>, nums2: Array<Int64>, nums3: Array<Int64>, nums4: Array<Int64>): Int64 {

    }
}
```

