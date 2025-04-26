# 3002. 移除后集合的最多元素数

## 题目描述

<p>给你两个下标从 <code>0</code> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，它们的长度都是偶数<code> n</code> 。</p>

<p>你必须从 <code>nums1</code> 中移除 <code>n / 2</code> 个元素，同时从 <code>nums2</code> 中也移除 <code>n / 2</code> 个元素。移除之后，你将 <code>nums1</code> 和 <code>nums2</code> 中剩下的元素插入到集合 <code>s</code> 中。</p>

<p>返回集合 <code>s</code>可能的<strong> 最多 </strong>包含多少元素。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,1,2], nums2 = [1,1,1,1]
<strong>输出：</strong>2
<strong>解释：</strong>从 nums1 和 nums2 中移除两个 1 。移除后，数组变为 nums1 = [2,2] 和 nums2 = [1,1] 。因此，s = {1,2} 。
可以证明，在移除之后，集合 s 最多可以包含 2 个元素。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]
<strong>输出：</strong>5
<strong>解释：</strong>从 nums1 中移除 2、3 和 6 ，同时从 nums2 中移除两个 3 和一个 2 。移除后，数组变为 nums1 = [1,4,5] 和 nums2 = [2,3,2] 。因此，s = {1,2,3,4,5} 。
可以证明，在移除之后，集合 s 最多可以包含 5 个元素。 
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]
<strong>输出：</strong>6
<strong>解释：</strong>从 nums1 中移除 1、2 和 3 ，同时从 nums2 中移除 4、5 和 6 。移除后，数组变为 nums1 = [1,2,3] 和 nums2 = [4,5,6] 。因此，s = {1,2,3,4,5,6} 。
可以证明，在移除之后，集合 s 最多可以包含 6 个元素。 </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>n</code>是偶数。</li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. Removing <code>n / 2</code> elements from each array is the same as keeping <code>n / 2<code> elements in each array.
2. Think of a greedy algorithm.
3. For each array, we will greedily keep the elements that are only in that array. Once we run out of such elements, we will keep the elements that are common to both arrays.

## 示例

```
[1,2,1,2]
[1,1,1,1]
[1,2,3,4,5,6]
[2,3,2,3,2,3]
[1,1,2,2,3,3]
[4,4,5,5,6,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumSetSize(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumSetSize(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int maximumSetSize(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumSetSize(int[] nums1, int[] nums2) {
        
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
var maximumSetSize = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function maximumSetSize(nums1: number[], nums2: number[]): number {
    
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
    function maximumSetSize($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSetSize(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSetSize(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSetSize(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func maximumSetSize(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximum_set_size(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def maximumSetSize(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_set_size(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-set-size nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_set_size(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
maximum_set_size(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_set_size(nums1 :: [integer], nums2 :: [integer]) :: integer
  def maximum_set_size(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSetSize(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

