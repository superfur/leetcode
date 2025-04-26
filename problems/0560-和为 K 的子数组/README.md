# 560. 和为 K 的子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数&nbsp;<code>k</code> ，请你统计并返回 <em>该数组中和为&nbsp;<code>k</code><strong>&nbsp;</strong>的子数组的个数&nbsp;</em>。</p>

<p>子数组是数组中元素的连续非空序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1], k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], k = 3
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Will Brute force work here? Try to optimize it.
2. Can we optimize it by using some extra space?
3. What about storing sum frequencies in a hash table? Will it be useful?
4. sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1.

Can we use this property to optimize it.

## 示例

```
[1,1,1]
2
[1,2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int subarraySum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarraySum(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function subarraySum(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraySum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarraySum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func subarraySum(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
subarray_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarray_sum(nums :: [integer], k :: integer) :: integer
  def subarray_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarraySum(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

