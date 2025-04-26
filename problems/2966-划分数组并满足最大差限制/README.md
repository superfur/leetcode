# 2966. 划分数组并满足最大差限制

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>，以及一个正整数 <code>k</code> 。</p>

<p>将这个数组划分为&nbsp;<code>n / 3</code>&nbsp;个长度为 <code>3</code> 的子数组，并满足以下条件：</p>

<ul>
	<li>子数组中<strong> 任意 </strong>两个元素的差必须 <strong>小于或等于</strong> <code>k</code> 。</li>
</ul>

<p>返回一个<em> </em><strong>二维数组 </strong>，包含所有的子数组。如果不可能满足条件，就返回一个空数组。如果有多个答案，返回 <strong>任意一个</strong> 即可。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,4,8,7,9,3,5,1], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>[[1,1,3],[3,4,5],[7,8,9]]</span></p>

<p><strong>解释：</strong></p>

<p>每个数组中任何两个元素之间的差小于或等于 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [2,4,2,2,5,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">[]</span></p>

<p><strong>解释：</strong></p>

<p>将&nbsp;<code>nums</code>&nbsp;划分为 2 个长度为 3 的数组的不同方式有：</p>

<ul>
	<li>[[2,2,2],[2,4,5]] （及其排列）</li>
	<li>[[2,2,4],[2,2,5]] （及其排列）</li>
</ul>

<p>因为有四个 2，所以无论我们如何划分，都会有一个包含元素 2 和 5 的数组。因为&nbsp;<code>5 - 2 = 3 &gt; k</code>，条件无法被满足，所以没有合法的划分。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">[[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]</span></p>

<p><strong>解释：</strong></p>

<p>每个数组中任何两个元素之间的差小于或等于 14。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 是 <code>3</code> 的倍数</li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Try to use a greedy approach.
2. Sort the array and try to group each <code>3</code> consecutive elements.

## 示例

```
[1,3,4,8,7,9,3,5,1]
2
[2,4,2,2,5,2]
2
[4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
14
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] divideArray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** divideArray(int* nums, int numsSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
var divideArray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function divideArray(nums: number[], k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[][]
     */
    function divideArray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divideArray(_ nums: [Int], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divideArray(nums: IntArray, k: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> divideArray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func divideArray(nums []int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[][]}
def divide_array(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def divideArray(nums: Array[Int], k: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (divide-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec divide_array(Nums :: [integer()], K :: integer()) -> [[integer()]].
divide_array(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide_array(nums :: [integer], k :: integer) :: [[integer]]
  def divide_array(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divideArray(nums: Array<Int64>, k: Int64): Array<Array<Int64>> {

    }
}
```

