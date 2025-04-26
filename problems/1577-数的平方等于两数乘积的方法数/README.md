# 1577. 数的平方等于两数乘积的方法数

## 题目描述

<p>给你两个整数数组 <code>nums1</code> 和 <code>nums2</code> ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：</p>

<ul>
	<li>类型 1：三元组 <code>(i, j, k)</code> ，如果 <code>nums1[i]<sup>2</sup>&nbsp;== nums2[j] * nums2[k]</code> 其中 <code>0 &lt;= i &lt; nums1.length</code> 且 <code>0 &lt;= j &lt; k &lt; nums2.length</code></li>
	<li>类型 2：三元组 <code>(i, j, k)</code> ，如果 <code>nums2[i]<sup>2</sup>&nbsp;== nums1[j] * nums1[k]</code> 其中 <code>0 &lt;= i &lt; nums2.length</code> 且 <code>0 &lt;= j &lt; k &lt; nums1.length</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums1 = [7,4], nums2 = [5,2,8,9]
<strong>输出：</strong>1
<strong>解释：</strong>类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums1 = [1,1], nums2 = [1,1,1]
<strong>输出：</strong>9
<strong>解释：</strong>所有三元组都符合题目要求，因为 1^2 = 1 * 1
类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k]
类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums1 = [7,7,8,3], nums2 = [1,2,9,7]
<strong>输出：</strong>2
<strong>解释：</strong>有两个符合题目要求的三元组
类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
<strong>输出：</strong>0
<strong>解释：</strong>不存在符合题目要求的三元组
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 双指针

## 提示

1. Precalculate the frequencies of all nums1[i]^2 and nums2[i]^2

## 示例

```
[7,4]
[5,2,8,9]
[1,1]
[1,1,1]
[7,7,8,3]
[1,2,9,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int numTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumTriplets(int[] nums1, int[] nums2) {
        
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
var numTriplets = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function numTriplets(nums1: number[], nums2: number[]): number {
    
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
    function numTriplets($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numTriplets(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numTriplets(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func numTriplets(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def num_triplets(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def numTriplets(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-triplets nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_triplets(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
num_triplets(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_triplets(nums1 :: [integer], nums2 :: [integer]) :: integer
  def num_triplets(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numTriplets(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

