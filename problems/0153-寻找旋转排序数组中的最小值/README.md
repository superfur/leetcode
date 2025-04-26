# 153. 寻找旋转排序数组中的最小值

## 题目描述

已知一个长度为 <code>n</code> 的数组，预先按照升序排列，经由 <code>1</code> 到 <code>n</code> 次 <strong>旋转</strong> 后，得到输入数组。例如，原数组 <code>nums = [0,1,2,4,5,6,7]</code> 在变化后可能得到：
<ul>
	<li>若旋转 <code>4</code> 次，则可以得到 <code>[4,5,6,7,0,1,2]</code></li>
	<li>若旋转 <code>7</code> 次，则可以得到 <code>[0,1,2,4,5,6,7]</code></li>
</ul>

<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> <strong>旋转一次</strong> 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。</p>

<p>给你一个元素值 <strong>互不相同</strong> 的数组 <code>nums</code> ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 <strong>最小元素</strong> 。</p>

<p>你必须设计一个时间复杂度为&nbsp;<code>O(log n)</code> 的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,5,1,2]
<strong>输出：</strong>1
<strong>解释：</strong>原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2]
<strong>输出：</strong>0
<strong>解释：</strong>原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [11,13,15,17]
<strong>输出：</strong>11
<strong>解释：</strong>原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
	<li><code>nums</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
2. You can divide the search space into two and see which direction to go.
Can you think of an algorithm which has O(logN) search complexity?
3. <ol>
<li>All the elements to the left of inflection point > first element of the array.</li>
<li>All the elements to the right of inflection point < first element of the array.</li>
<ol>

## 示例

```
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMin(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
```

### C

```c
int findMin(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMin(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    
};
```

### TypeScript

```typescript
function findMin(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMin($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMin(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMin(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMin(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMin(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-min nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_min(Nums :: [integer()]) -> integer().
find_min(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_min(nums :: [integer]) :: integer
  def find_min(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMin(nums: Array<Int64>): Int64 {

    }
}
```

