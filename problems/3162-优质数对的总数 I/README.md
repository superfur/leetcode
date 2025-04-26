# 3162. 优质数对的总数 I

## 题目描述

<p>给你两个整数数组 <code>nums1</code> 和 <code>nums2</code>，长度分别为 <code>n</code> 和 <code>m</code>。同时给你一个<strong>正整数</strong> <code>k</code>。</p>

<p>如果 <code>nums1[i]</code> 可以除尽&nbsp;<code>nums2[j] * k</code>，则称数对 <code>(i, j)</code> 为 <strong>优质数对</strong>（<code>0 &lt;= i &lt;= n - 1</code>, <code>0 &lt;= j &lt;= m - 1</code>）。</p>

<p>返回<strong> 优质数对 </strong>的总数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [1,3,4], nums2 = [1,3,4], k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>5个优质数对分别是 <code>(0, 0)</code>, <code>(1, 0)</code>, <code>(1, 1)</code>, <code>(2, 0)</code>, 和 <code>(2, 2)</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums1 = [1,2,4,12], nums2 = [2,4], k = 3</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>2个优质数对分别是 <code>(3, 0)</code> 和 <code>(3, 1)</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 50</code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. The constraints are small. Check all pairs.

## 示例

```
[1,3,4]
[1,3,4]
1
[1,2,4,12]
[2,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPairs(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
```

### C

```c
int numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPairs(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, k) {
    
};
```

### TypeScript

```typescript
function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function numberOfPairs($nums1, $nums2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPairs(List<int> nums1, List<int> nums2, int k) {
    
  }
}
```

### Go

```golang
func numberOfPairs(nums1 []int, nums2 []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def number_of_pairs(nums1, nums2, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-pairs nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_pairs(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
number_of_pairs(Nums1, Nums2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def number_of_pairs(nums1, nums2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPairs(nums1: Array<Int64>, nums2: Array<Int64>, k: Int64): Int64 {

    }
}
```

