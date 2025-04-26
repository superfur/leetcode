# 215. 数组中的第K个最大元素

## 题目描述

<p>给定整数数组 <code>nums</code> 和整数 <code>k</code>，请返回数组中第 <code><strong>k</strong></code> 个最大的元素。</p>

<p>请注意，你需要找的是数组排序后的第 <code>k</code> 个最大的元素，而不是第 <code>k</code> 个不同的元素。</p>

<p>你必须设计并实现时间复杂度为 <code>O(n)</code> 的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,1,5,6,4],</code> k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6], </code>k = 4
<strong>输出:</strong> 4</pre>

<p>&nbsp;</p>

<p><strong>提示： </strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 分治
- 快速选择
- 排序
- 堆（优先队列）

## 示例

```
[3,2,1,5,6,4]
2
[3,2,3,1,2,4,5,5,6]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int findKthLargest(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        
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
var findKthLargest = function(nums, k) {
    
};
```

### TypeScript

```typescript
function findKthLargest(nums: number[], k: number): number {
    
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
    function findKthLargest($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findKthLargest(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func findKthLargest(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def findKthLargest(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-kth-largest nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_kth_largest(Nums :: [integer()], K :: integer()) -> integer().
find_kth_largest(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_kth_largest(nums :: [integer], k :: integer) :: integer
  def find_kth_largest(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKthLargest(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

