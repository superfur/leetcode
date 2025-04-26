# 2200. 找出数组中的所有 K 近邻下标

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和两个整数 <code>key</code> 和 <code>k</code> 。<strong>K 近邻下标</strong> 是 <code>nums</code> 中的一个下标 <code>i</code> ，并满足至少存在一个下标 <code>j</code> 使得 <code>|i - j| &lt;= k</code> 且 <code>nums[j] == key</code> 。</p>

<p>以列表形式返回按 <strong>递增顺序</strong> 排序的所有 K 近邻下标。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,9,1,3,9,5], key = 9, k = 1
<strong>输出：</strong>[1,2,3,4,5,6]
<strong>解释：</strong>因此，<code>nums[2] == key</code> 且 <code>nums[5] == key 。
- 对下标 0 ，|0 - 2| &gt; k 且 |0 - 5| &gt; k ，所以不存在 j</code> 使得 <code>|0 - j| &lt;= k</code> 且 <code>nums[j] == key 。所以 0 不是一个 K 近邻下标。
- 对下标 1 ，|1 - 2| &lt;= k 且 nums[2] == key ，所以 1 是一个 K 近邻下标。
- 对下标 2 ，|2 - 2| &lt;= k 且 nums[2] == key ，所以 2 是一个 K 近邻下标。
- 对下标 3 ，|3 - 2| &lt;= k 且 nums[2] == key ，所以 3 是一个 K 近邻下标。
- 对下标 4 ，|4 - 5| &lt;= k 且 nums[5] == key ，所以 4 是一个 K 近邻下标。
- 对下标 5 ，|5 - 5| &lt;= k 且 nums[5] == key ，所以 5 是一个 K 近邻下标。
- 对下标 6 ，|6 - 5| &lt;= k 且 nums[5] == key ，所以 6 是一个 K 近邻下标。
</code>因此，按递增顺序返回 [1,2,3,4,5,6] 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,2,2], key = 2, k = 2
<strong>输出：</strong>[0,1,2,3,4]
<strong>解释：</strong>对 nums 的所有下标 i ，总存在某个下标 j 使得 |i - j| &lt;= k 且 nums[j] == key ，所以每个下标都是一个 <code>K 近邻下标。</code> 
因此，返回 [0,1,2,3,4] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>key</code> 是数组 <code>nums</code> 中的一个整数</li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针

## 提示

1. For every occurrence of key in nums, find all indices within distance k from it.
2. Use a hash table to remove duplicate indices.

## 示例

```
[3,4,9,1,3,9,5]
9
1
[2,2,2,2,2]
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findKDistantIndices(int* nums, int numsSize, int key, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindKDistantIndices(int[] nums, int key, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function(nums, key, k) {
    
};
```

### TypeScript

```typescript
function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $key
     * @param Integer $k
     * @return Integer[]
     */
    function findKDistantIndices($nums, $key, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKDistantIndices(_ nums: [Int], _ key: Int, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKDistantIndices(nums: IntArray, key: Int, k: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findKDistantIndices(List<int> nums, int key, int k) {
    
  }
}
```

### Go

```golang
func findKDistantIndices(nums []int, key int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} key
# @param {Integer} k
# @return {Integer[]}
def find_k_distant_indices(nums, key, k)
    
end
```

### Scala

```scala
object Solution {
    def findKDistantIndices(nums: Array[Int], key: Int, k: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-k-distant-indices nums key k)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_k_distant_indices(Nums :: [integer()], Key :: integer(), K :: integer()) -> [integer()].
find_k_distant_indices(Nums, Key, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_k_distant_indices(nums :: [integer], key :: integer, k :: integer) :: [integer]
  def find_k_distant_indices(nums, key, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKDistantIndices(nums: Array<Int64>, key: Int64, k: Int64): ArrayList<Int64> {

    }
}
```

