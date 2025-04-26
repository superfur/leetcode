# 2537. 统计好子数组的数目

## 题目描述

<p>给你一个整数数组 <code>nums</code>&nbsp;和一个整数 <code>k</code>&nbsp;，请你返回 <code>nums</code>&nbsp;中 <strong>好</strong>&nbsp;子数组的数目。</p>

<p>一个子数组 <code>arr</code>&nbsp;如果有 <strong>至少</strong>&nbsp;<code>k</code>&nbsp;对下标 <code>(i, j)</code>&nbsp;满足 <code>i &lt; j</code>&nbsp;且 <code>arr[i] == arr[j]</code>&nbsp;，那么称它是一个 <strong>好</strong>&nbsp;子数组。</p>

<p><strong>子数组</strong>&nbsp;是原数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,1,1,1,1], k = 10
<b>输出：</b>1
<b>解释：</b>唯一的好子数组是这个数组本身。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [3,1,4,3,2,2,4], k = 2
<b>输出：</b>4
<b>解释：</b>总共有 4 个不同的好子数组：
- [3,1,4,3,2,2] 有 2 对。
- [3,1,4,3,2,2,4] 有 3 对。
- [1,4,3,2,2,4] 有 2 对。
- [4,3,2,2,4] 有 2 对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. For a fixed index l, try to find the minimum value of index r, such that the subarray is not good
2. When a number is added to a subarray, it increases the number of pairs by its previous appearances.
3. When a number is removed from the subarray, it decreases the number of pairs by its remaining appearances.
4. Maintain 2-pointers l and r such that we can keep in account the number of equal pairs.

## 示例

```
[1,1,1,1,1]
10
[3,1,4,3,2,2,4]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countGood(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long countGood(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountGood(int[] nums, int k) {
        
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
var countGood = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countGood(nums: number[], k: number): number {
    
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
    function countGood($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGood(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGood(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGood(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countGood(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_good(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countGood(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good(Nums :: [integer()], K :: integer()) -> integer().
count_good(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good(nums :: [integer], k :: integer) :: integer
  def count_good(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGood(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

