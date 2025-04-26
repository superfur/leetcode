# 321. 拼接最大数

## 题目描述

<p>给你两个整数数组 <code>nums1</code> 和 <code>nums2</code>，它们的长度分别为 <code>m</code> 和 <code>n</code>。数组 <code>nums1</code> 和 <code>nums2</code> 分别代表两个数各位上的数字。同时你也会得到一个整数 <code>k</code>。</p>

<p>请你利用这两个数组中的数字创建一个长度为 <code>k &lt;= m + n</code> 的最大数。同一数组中数字的相对顺序必须保持不变。</p>

<p>返回代表答案的长度为 <code>k</code> 的数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
<strong>输出：</strong>[9,8,6,5,3]
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [6,7], nums2 = [6,0,4], k = 5
<strong>输出：</strong>[6,7,6,0,4]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [3,9], nums2 = [8,9], k = 3
<strong>输出：</strong>[9,8,9]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 9</code></li>
	<li><code>1 &lt;= k &lt;= m + n</code></li>
	<li><code>nums1</code>&nbsp;和&nbsp;<code>nums2</code> 没有前导 0。</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 双指针
- 单调栈

## 示例

```
[3,4,6,5]
[9,1,2,5,8,3]
5
[6,7]
[6,0,4]
5
[3,9]
[8,9]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxNumber(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaxNumber(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[]}
 */
var maxNumber = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function maxNumber(nums1: number[], nums2: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[]
     */
    function maxNumber($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumber(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumber(nums1: IntArray, nums2: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxNumber(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func maxNumber(nums1 []int, nums2 []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[]}
def max_number(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def maxNumber(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_number(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-number nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_number(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> [integer()].
max_number(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_number(nums1 :: [integer], nums2 :: [integer], k :: integer) :: [integer]
  def max_number(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumber(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

