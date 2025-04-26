# 2956. 找到两个数组中的公共元素

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，它们分别含有 <code>n</code>&nbsp;和 <code>m</code>&nbsp;个元素。请你计算以下两个数值：</p>

<ul>
	<li><code>answer1</code>：使得&nbsp;<code>nums1[i]</code>&nbsp;在&nbsp;<code>nums2</code>&nbsp;中出现的下标&nbsp;<code>i</code>&nbsp;的数量。</li>
	<li><code>answer2</code>：使得&nbsp;<code>nums2[i]</code>&nbsp;在&nbsp;<code>nums1</code>&nbsp;中出现的下标&nbsp;<code>i</code>&nbsp;的数量。</li>
</ul>

<p>返回 <code>[answer1, answer2]</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [2,3,2], nums2 = [1,2]</span></p>

<p><strong>输出：</strong><span class="example-io">[2,1]</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/26/3488_find_common_elements_between_two_arrays-t1.gif" style="width: 225px; height: 150px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]</span></p>

<p><strong>输出：</strong><span class="example-io">[3,4]</span></p>

<p><strong>解释：</strong></p>

<p><code>nums1</code>&nbsp;中下标在 1，2，3 的元素在&nbsp;<code>nums2</code>&nbsp;中也存在。所以&nbsp;<code>answer1</code>&nbsp;为&nbsp;3。</p>

<p><code>nums2</code>&nbsp;中下标在 0，1，3，4 的元素在&nbsp;<code>nums1</code>&nbsp;中也存在。所以&nbsp;<code>answer2</code>&nbsp;为 4。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [3,4,2,3], nums2 = [1,5]</span></p>

<p><strong>输出：</strong><span class="example-io">[0,0]</span></p>

<p><strong>解释：</strong></p>

<p><code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;中没有相同的数字，所以答案是 [0,0]。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>m == nums2.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 100</code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Since the constraints are small, you can use brute force to solve the problem.
2. For each element <code>i</code> in <code>nums1</code>, iterate over all elements of <code>nums2</code> to find if it occurs.

## 示例

```
[2,3,2]
[1,2]
[4,3,2,3,1]
[2,2,5,2,3,6]
[3,4,2,3]
[1,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIntersectionValues(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var findIntersectionValues = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function findIntersectionValues($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findIntersectionValues(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findIntersectionValues(nums1: IntArray, nums2: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findIntersectionValues(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func findIntersectionValues(nums1 []int, nums2 []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def find_intersection_values(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def findIntersectionValues(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_intersection_values(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-intersection-values nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_intersection_values(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
find_intersection_values(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_intersection_values(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def find_intersection_values(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findIntersectionValues(nums1: Array<Int64>, nums2: Array<Int64>): Array<Int64> {

    }
}
```

