# 2918. 数组的最小相等和

## 题目描述

<p>给你两个由正整数和 <code>0</code> 组成的数组 <code>nums1</code> 和 <code>nums2</code> 。</p>

<p>你必须将两个数组中的<strong> 所有</strong> <code>0</code> 替换为 <strong>严格</strong> 正整数，并且满足两个数组中所有元素的和 <strong>相等</strong> 。</p>

<p>返回 <strong>最小</strong> 相等和 ，如果无法使两数组相等，则返回 <code>-1</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [3,2,0,1,0], nums2 = [6,5,0]
<strong>输出：</strong>12
<strong>解释：</strong>可以按下述方式替换数组中的 0 ：
- 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。
- 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。
两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,0,2,0], nums2 = [1,4]
<strong>输出：</strong>-1
<strong>解释：</strong>无法使两个数组的和相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Consider we replace all the 0’s with 1’s on both arrays, the answer will be <code>-1</code> if there was no <code>0</code> in the array with the smaller sum of elements.
2. Otherwise, how can you update the value of exactly one of these <code>1</code>’s to make the sum of the two arrays equal?

## 示例

```
[3,2,0,1,0]
[6,5,0]
[2,0,2,0]
[1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public long minSum(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
long long minSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinSum(int[] nums1, int[] nums2) {
        
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
var minSum = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minSum(nums1: number[], nums2: number[]): number {
    
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
    function minSum($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSum(nums1: IntArray, nums2: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSum(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minSum(nums1 []int, nums2 []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_sum(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minSum(nums1: Array[Int], nums2: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-sum nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_sum(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_sum(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_sum(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_sum(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSum(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

