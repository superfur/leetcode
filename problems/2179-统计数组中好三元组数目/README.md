# 2179. 统计数组中好三元组数目

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始且长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，两者都是&nbsp;<code>[0, 1, ..., n - 1]</code>&nbsp;的&nbsp;<strong>排列</strong>&nbsp;。</p>

<p><strong>好三元组&nbsp;</strong>指的是&nbsp;<code>3</code>&nbsp;个&nbsp;<strong>互不相同</strong>&nbsp;的值，且它们在数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;中出现顺序保持一致。换句话说，如果我们将&nbsp;<code>pos1<sub>v</sub></code> 记为值&nbsp;<code>v</code>&nbsp;在&nbsp;<code>nums1</code>&nbsp;中出现的位置，<code>pos2<sub>v</sub></code>&nbsp;为值&nbsp;<code>v</code>&nbsp;在&nbsp;<code>nums2</code>&nbsp;中的位置，那么一个好三元组定义为&nbsp;<code>0 &lt;= x, y, z &lt;= n - 1</code>&nbsp;，且&nbsp;<code>pos1<sub>x</sub> &lt; pos1<sub>y</sub> &lt; pos1<sub>z</sub></code> 和&nbsp;<code>pos2<sub>x</sub> &lt; pos2<sub>y</sub> &lt; pos2<sub>z</sub></code>&nbsp;都成立的&nbsp;<code>(x, y, z)</code>&nbsp;。</p>

<p>请你返回好三元组的 <strong>总数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [2,0,1,3], nums2 = [0,1,2,3]
<b>输出：</b>1
<b>解释：</b>
总共有 4 个三元组 (x,y,z) 满足 pos1<sub>x</sub> &lt; pos1<sub>y</sub> &lt; pos1<sub>z&nbsp;</sub>，分别是 (2,0,1) ，(2,0,3) ，(2,1,3) 和 (0,1,3) 。
这些三元组中，只有 (0,1,3) 满足 pos2<sub>x</sub> &lt; pos2<sub>y</sub> &lt; pos2<sub>z</sub>&nbsp;。所以只有 1 个好三元组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
<b>输出：</b>4
<b>解释：</b>总共有 4 个好三元组 (4,0,3) ，(4,0,2) ，(4,1,3) 和 (4,1,2) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= n - 1</code></li>
	<li><code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;是&nbsp;<code>[0, 1, ..., n - 1]</code> 的排列。</li>
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

1. For every value y, how can you find the number of values x  (0 ≤ x, y ≤ n - 1) such that x appears before y in both of the arrays?
2. Similarly, for every value y, try finding the number of values z (0 ≤ y, z ≤ n - 1) such that z appears after y in both of the arrays.
3. Now, for every value y, count the number of good triplets that can be formed if y is considered as the middle element.

## 示例

```
[2,0,1,3]
[0,1,2,3]
[4,0,1,3,2]
[4,1,0,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public long goodTriplets(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
long long goodTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public long GoodTriplets(int[] nums1, int[] nums2) {
        
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
var goodTriplets = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function goodTriplets(nums1: number[], nums2: number[]): number {
    
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
    function goodTriplets($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func goodTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun goodTriplets(nums1: IntArray, nums2: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int goodTriplets(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func goodTriplets(nums1 []int, nums2 []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def good_triplets(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def goodTriplets(nums1: Array[Int], nums2: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn good_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (good-triplets nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec good_triplets(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
good_triplets(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec good_triplets(nums1 :: [integer], nums2 :: [integer]) :: integer
  def good_triplets(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func goodTriplets(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

